"""GitTrends relaunch: 3-year revenue-vs-cost model (monthly cohorts, expected values).
Month 1 = Dec 2026. Y1 = months 1-12, Y2 = 13-24, Y3 = 25-36. USD, before income tax.
Run: python3 forecast_model.py  -> prints JSON for every scenario and sensitivity.
Edit DEFAULTS / SCENARIOS to try other prices, conversion rates or MAU paths.
"""
import json, copy, sys

DEFAULTS = {
  "timeline": {"months": 36, "month1": "2026-12", "relaunch_month": 3, "premium_month": 5,
               "pro_month": 13, "build_months_claude": 4},
  "store": {"store_fee": 0.15, "tax_drag": 0.06, "refund_rate": 0.03},
  "ladder": {
     "premium_monthly": 4.99, "premium_annual": 39.99, "founder_first_year": 19.99,
     "pro_monthly": 9.99, "pro_annual": 99.99,
     "annual_share_new_payers": 0.60, "pro_share_new_payers": 0.10, "pro_annual_share": 0.50,
     "trial_to_paid": 0.33},
  "single_tier": {"monthly": 9.99, "annual": 99.99, "annual_share_new_payers": 0.35,
                  "relative_conversion": 0.50},
  "retention": {"monthly_paid_months_y1": 4.5, "annual_renewal_first": 0.30, "annual_renewal_later": 0.50},
  "funnel": {"paid_share_annual_of_mau": 0.025, "founder_share_of_mau_at_premium": 0.01},
  "mau": {"launch": 250, "end_y1": 600, "end_y2": 900, "end_y3": 1200},
  "costs": {
     "cloud_curve_high": [[0, 0.50], [500, 1.50], [2000, 3.50], [10000, 31.0]],
     "cloud_curve_low":  [[0, 0.20], [500, 0.40], [2000, 0.80], [10000, 5.0]],
     "cloud_curve_stress": [[0, 1.0], [500, 2.0], [2000, 9.0], [10000, 52.0]],
     "cloud_curve_used": "high",
     "phase1_daily_uplift_curve": [[0, 0.0], [500, 0.20], [2000, 0.50], [10000, 5.0]],
     "pre_relaunch_cloud_per_month": 0.50,
     "apple_developer_per_year": 99.0, "google_play_one_time": 25.0,
     "domain_per_year": 20.0, "dns_per_month": 0.0,
     "sentry_free_until_mau": 4000, "sentry_team_per_month": 29.0,
     "ci_public_repo": True, "ci_private_build_month": 60.0, "ci_private_steady_month": 31.0,
     "staging_per_month_without_credit": 6.0, "mvp_credit_covers_staging": True,
     "eu_art27_rep_per_year": 0.0, "legal_review_one_time": 0.0,
     "claude_ultra_per_month": 200.0},
}

SCENARIOS = {
  "bear": {"mau": {"launch": 150, "end_y1": 300, "end_y2": 375, "end_y3": 400},
           "funnel": {"paid_share_annual_of_mau": 0.010, "founder_share_of_mau_at_premium": 0.005},
           "retention": {"monthly_paid_months_y1": 4.0, "annual_renewal_first": 0.25, "annual_renewal_later": 0.40},
           "timeline": {"pro_month": 999}},
  "base": {},
  "bull": {"mau": {"launch": 400, "end_y1": 1500, "end_y2": 3000, "end_y3": 5000},
           "funnel": {"paid_share_annual_of_mau": 0.050, "founder_share_of_mau_at_premium": 0.02},
           "retention": {"monthly_paid_months_y1": 5.0, "annual_renewal_first": 0.35, "annual_renewal_later": 0.60},
           "timeline": {"pro_month": 11}},
}

def deep_merge(a, b):
    r = copy.deepcopy(a)
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(r.get(k), dict):
            r[k] = deep_merge(r[k], v)
        else:
            r[k] = v
    return r

def solve_r(paid_months):
    lo, hi = 0.0, 0.999999
    for _ in range(200):
        mid = (lo + hi) / 2
        s = sum(mid ** k for k in range(12))
        if s < paid_months: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def interp(curve, x):
    if x <= curve[0][0]: return curve[0][1]
    for (x0, y0), (x1, y1) in zip(curve, curve[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    (x0, y0), (x1, y1) = curve[-2], curve[-1]
    return y1 + (y1 - y0) * (x - x1) / (x1 - x0)

def mau_at(p, m):
    t = p["timeline"]; mu = p["mau"]
    if m < t["relaunch_month"]: return 0.0
    pts = [(t["relaunch_month"], mu["launch"]), (12, mu["end_y1"]), (24, mu["end_y2"]), (36, mu["end_y3"])]
    for (m0, v0), (m1, v1) in zip(pts, pts[1:]):
        if m <= m1:
            return v0 + (v1 - v0) * (m - m0) / (m1 - m0)
    return pts[-1][1]

def run(p, pricing="ladder", cost_mode=None):
    t = p["timeline"]; s = p["store"]; c = p["costs"]; ret = p["retention"]; f = p["funnel"]
    M = t["months"]
    net_factor = (1 - s["tax_drag"]) * (1 - s["refund_rate"]) * (1 - s["store_fee"])
    r = solve_r(ret["monthly_paid_months_y1"])
    rev = [0.0] * (M + 2); gross = [0.0] * (M + 2)
    # active stock trackers
    monthly_active = [0.0] * (M + 2)
    annual_active = [0.0] * (M + 2)
    acq_total = [0.0] * (M + 2)
    trial_starts = [0.0] * (M + 2)
    def add_monthly(start, n, price):
        for m in range(start, M + 1):
            surv = n * r ** (m - start)
            gross[m] += surv * price
            monthly_active[m] += surv
    def add_annual(start, n, first_price, renew_price):
        alive = n
        k = 0
        while start + 12 * k <= M:
            pay_m = start + 12 * k
            price = first_price if k == 0 else renew_price
            gross[pay_m] += alive * price
            for m in range(pay_m, min(pay_m + 12, M + 1)):
                annual_active[m] += alive
            k += 1
            alive *= ret["annual_renewal_first"] if k == 1 else ret["annual_renewal_later"]
    if pricing == "ladder":
        L = p["ladder"]
        paid_share = f["paid_share_annual_of_mau"]
        founder = f["founder_share_of_mau_at_premium"] * mau_at(p, t["premium_month"])
        if founder > 0:
            add_annual(t["premium_month"], founder, L["founder_first_year"], L["premium_annual"])
            acq_total[t["premium_month"]] += founder
        for m in range(t["premium_month"], M + 1):
            n = paid_share / 12.0 * mau_at(p, m)
            acq_total[m] += n
            pro_sh = L["pro_share_new_payers"] if m >= t["pro_month"] else 0.0
            n_pro, n_prem = n * pro_sh, n * (1 - pro_sh)
            a = L["annual_share_new_payers"]
            add_annual(m, n_prem * a, L["premium_annual"], L["premium_annual"])
            add_monthly(m, n_prem * (1 - a), L["premium_monthly"])
            pa = L["pro_annual_share"]
            add_annual(m, n_pro * pa, L["pro_annual"], L["pro_annual"])
            add_monthly(m, n_pro * (1 - pa), L["pro_monthly"])
            trial_starts[m] += n_prem * a / L["trial_to_paid"]
    else:
        S = p["single_tier"]
        k = S["relative_conversion"]
        paid_share = f["paid_share_annual_of_mau"] * k
        founder = f["founder_share_of_mau_at_premium"] * k * mau_at(p, t["premium_month"])
        if founder > 0:
            add_annual(t["premium_month"], founder, S["annual"], S["annual"])
            acq_total[t["premium_month"]] += founder
        for m in range(t["premium_month"], M + 1):
            n = paid_share / 12.0 * mau_at(p, m)
            acq_total[m] += n
            a = S["annual_share_new_payers"]
            add_annual(m, n * a, S["annual"], S["annual"])
            add_monthly(m, n * (1 - a), S["monthly"])
    for m in range(1, M + 1):
        rev[m] = gross[m] * net_factor
    # costs
    curve_name = cost_mode or c["cloud_curve_used"]
    curve = c["cloud_curve_" + curve_name]
    cost = [0.0] * (M + 2); cloud = [0.0] * (M + 2); fixed = [0.0] * (M + 2)
    for m in range(1, M + 1):
        mau = mau_at(p, m)
        if m < t["relaunch_month"]:
            cl = c["pre_relaunch_cloud_per_month"]
        else:
            cl = interp(curve, mau)
            if m < t["premium_month"] + 1:  # daily-for-everyone until 3.1 switches free users to weekly
                cl += interp(c["phase1_daily_uplift_curve"], mau)
        cloud[m] = cl
        fx = 0.0
        if (m - 1) % 12 == 0:
            fx += c["apple_developer_per_year"] + c["domain_per_year"] + c["eu_art27_rep_per_year"]
        if m == 1:
            fx += c["google_play_one_time"] + c["legal_review_one_time"]
        fx += c["dns_per_month"]
        if mau > c["sentry_free_until_mau"]:
            fx += c["sentry_team_per_month"]
        if not c["ci_public_repo"]:
            fx += c["ci_private_build_month"] if m < t["premium_month"] + 1 else c["ci_private_steady_month"]
        if not c["mvp_credit_covers_staging"]:
            fx += c["staging_per_month_without_credit"]
        fixed[m] = fx
        cost[m] = cl + fx
    def yr(arr, y): return sum(arr[12 * (y - 1) + 1: 12 * y + 1])
    out = {"r_monthly": r, "net_factor": net_factor}
    for y in (1, 2, 3):
        out[f"net_revenue_y{y}"] = yr(rev, y)
        out[f"gross_y{y}"] = yr(gross, y)
        out[f"cost_y{y}"] = yr(cost, y)
        out[f"cloud_y{y}"] = yr(cloud, y)
        out[f"fixed_y{y}"] = yr(fixed, y)
        out[f"profit_y{y}"] = yr(rev, y) - yr(cost, y)
        out[f"mau_end_y{y}"] = mau_at(p, 12 * y)
        out[f"paying_end_y{y}"] = monthly_active[12 * y] + annual_active[12 * y]
        out[f"acq_y{y}"] = yr(acq_total, y)
        out[f"trial_starts_y{y}"] = yr(trial_starts, y)
    out["one_time_build_claude"] = p["costs"]["claude_ultra_per_month"] * t["build_months_claude"]
    out["cum_profit_3y"] = sum(out[f"profit_y{y}"] for y in (1, 2, 3))
    out["cum_profit_3y_after_build"] = out["cum_profit_3y"] - out["one_time_build_claude"]
    out["series"] = {"rev": rev[1:M+1], "cost": cost[1:M+1], "mau": [mau_at(p, m) for m in range(1, M+1)], "paying": [monthly_active[m] + annual_active[m] for m in range(1, M+1)]}
    out["monthly_cost_last"] = cost[M]
    out["monthly_rev_last"] = rev[M]
    return out

def params_for(name):
    return deep_merge(DEFAULTS, SCENARIOS[name])

if __name__ == "__main__":
    res = {}
    for sc in ("bear", "base", "bull"):
        p = params_for(sc)
        res[sc + "_ladder"] = run(p, "ladder")
        res[sc + "_single"] = run(p, "single")
    # stress: base ladder with stress costs
    p = params_for("base")
    p["costs"]["ci_public_repo"] = False
    p["costs"]["eu_art27_rep_per_year"] = 250.0
    p["costs"]["mvp_credit_covers_staging"] = False
    p["costs"]["sentry_free_until_mau"] = 0
    res["base_ladder_stress_costs"] = run(p, "ladder", "stress")
    # elasticity sweep for single tier (base MAU)
    sweep = {}
    for k in (0.35, 0.40, 0.45, 0.50, 0.70, 1.00):
        p = params_for("base"); p["single_tier"]["relative_conversion"] = k
        o = run(p, "single")
        sweep[str(k)] = {y: round(o[f"net_revenue_y{y}"], 0) for y in (1, 2, 3)}
        sweep[str(k)]["3y"] = round(sum(o[f"net_revenue_y{y}"] for y in (1, 2, 3)), 0)
    res["single_elasticity_sweep_base"] = sweep
    # breakeven relative conversion (3y net revenue parity) for each scenario
    be = {}
    for sc in ("bear", "base", "bull"):
        lad = run(params_for(sc), "ladder")
        lad3 = sum(lad[f"net_revenue_y{y}"] for y in (1, 2, 3))
        lo, hi = 0.0, 3.0
        for _ in range(60):
            mid = (lo + hi) / 2
            p = params_for(sc); p["single_tier"]["relative_conversion"] = mid
            o = run(p, "single"); s3 = sum(o[f"net_revenue_y{y}"] for y in (1, 2, 3))
            if s3 < lad3: lo = mid
            else: hi = mid
        be[sc] = round((lo + hi) / 2, 3)
    res["single_vs_ladder_parity_relative_conversion"] = be
    # sensitivity: no collect-for-everyone (paid share 1.75%, no founder burst)
    p = params_for("base"); p["funnel"]["paid_share_annual_of_mau"] = 0.0175; p["funnel"]["founder_share_of_mau_at_premium"] = 0.0
    res["base_ladder_subscriber_only_collection"] = run(p, "ladder")
    # sensitivity: on-time schedule (judge target)
    p = params_for("base"); p["timeline"]["relaunch_month"] = 2; p["timeline"]["premium_month"] = 4
    res["base_ladder_on_time"] = run(p, "ladder")
    # MVP credit effect: base ladder without credit
    for sc in ("bear", "base", "bull"):
        p = params_for(sc); p["costs"]["mvp_credit_covers_staging"] = False
        res[sc + "_ladder_no_mvp_credit"] = run(p, "ladder")
    # private repo CI effect
    p = params_for("base"); p["costs"]["ci_public_repo"] = False
    res["base_ladder_private_ci"] = run(p, "ladder")
    # 10k stretch
    p = params_for("bull"); p["mau"] = {"launch": 500, "end_y1": 2500, "end_y2": 6000, "end_y3": 10000}
    res["stretch_10k_ladder"] = run(p, "ladder")
    for v in res.values():
        if isinstance(v, dict): v.pop("series", None)
    def rnd(o):
        if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
        if isinstance(o, float): return round(o, 3)
        return o
    print(json.dumps(rnd(res), indent=1))
