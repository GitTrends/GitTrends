# GitTrends relaunch: 3-year revenue vs cost model

Part of the [relaunch plan](README.md).

As of 2026-11-15. Figures are in USD, before income tax, and round to whole dollars. Subscriber counts are expected values, so fractions appear.

## 1. Bottom line

- **The cash risk is small and capped.** Recurring costs are about $137–161 a year at 500–2,000 MAU. Of that, 74–87% is the Apple $99/yr fee plus the domain. Azure production is $18–42 a year.
  - Worst modelled 3-year cash loss: about $156, or about $956 if the optional $800 Claude Ultra build subscription is counted.
  - A free-only relaunch would cost almost the same cash, because the Apple fee is paid either way.
- **Revenue is also small unless the audience grows well past 2020.** 3-year net revenue on the recommended ladder:
  - Bear: $267.
  - Base: $1,735.
  - Bull: $11,587.
- **3-year profit:**

| Scenario | Before build cost | After $800 build cost |
|---|---|---|
| Bear | −$156 | −$956 |
| Base | +$1,289 | +$489 |
| Bull | +$10,824 | +$10,024 |

- **Cash break-even needs about 5 annual Premium subscribers** at the old 500-user scale (1% of MAU), or about 13 to also recover the $800 build cost within 3 years.
  - Paying the owner $50/h for about 160 hands-on hours (the reconciled estimate with Claude doing the coding; see [estimates.md](estimates.md)) is $8,000. Only the bull path earns that back within 3 years.
- **Owner's $9.99/$99.99 single tier vs the ladder.** The two earn about the same: the single tier wins only if it converts at 55% or more of the ladder's rate (bear 0.49, bull 0.57).
  - At the assumed 0.5, the ladder earns 10% more over 3 years and has 2.6× as many paying users.
  - That 10% comes from Pro sales from year 2. Comparing Premium alone with the single tier, 3-year net revenue is within about 1% ($1,590 vs $1,570 at base), and parity is about 0.51 (bear 0.49, bull 0.51).
  - The single tier earns more in year 1 ($284 vs $227).
- **What would actually lose money is fixed-fee creep, not Azure.** Private-repo CI, Sentry Team from day 1, an EU representative and paid staging together turn base into −$1,975 over 3 years.
- **Collecting history for everyone matters most.** Collecting only for subscribers cuts base 3-year profit from $1,289 to $701.

**Decision framing.** Financially this is a hobby project with a capped downside and a real but unlikely upside. Proceed if the non-financial reasons count:
- a .NET 11, Aspire and MAUI showcase;
- community value;
- the MVP portfolio.

Keep every fixed fee at $0 until subscribers cover it. Set the decision gates in section 11.

## 2. Scenario results: recommended ladder

The ladder is Free; Premium at $4.99/mo or $39.99/yr with a 14-day annual trial and a $19.99 Founding Member first year; and Pro at $9.99/$99.99 from month 13 in base (month 11 in bull, never in bear).

| | Bear | Base | Bull |
|---|---|---|---|
| MAU end Y1 / Y2 / Y3 | 300 / 375 / 400 | 600 / 900 / 1,200 | 1,500 / 3,000 / 5,000 |
| New payers per year as % of MAU (plus founder burst) | 1.0% (+0.5%) | 2.5% (+1%) | 5.0% (+2%) |
| Monthly paid months in Y1 / first annual renewal / later renewals | 4.0 / 25% / 40% | 4.5 / 30% / 50% | 5.0 / 35% / 60% |
| New payers acquired Y1 / Y2 / Y3 | 2.5 / 3.4 / 3.9 | 11.0 / 19.1 / 26.6 | 48.6 / 115.6 / 204.2 |
| Paying subscribers at end of Y1 / Y2 / Y3 | 2.2 / 3.0 / 3.6 | 9.6 / 16.9 / 24.8 | 43.1 / 103.1 / 191.6 |
| Gross sales Y1 / Y2 / Y3 | $65 / $126 / $153 | $292 / $775 / $1,171 | $1,347 / $4,661 / $8,943 |
| **Net revenue** Y1 / Y2 / Y3 | $51 / $98 / $118 | $227 / $600 / $908 | $1,044 / $3,612 / $6,931 |
| **Total cost** Y1 / Y2 / Y3 | $155 / $133 / $134 | $159 / $141 / $146 | $167 / $175 / $421 |
| of which cloud | $11 / $14 / $15 | $15 / $22 / $27 | $23 / $57 / $128 |
| **Profit** Y1 / Y2 / Y3 | −$104 / −$35 / −$16 | +$68 / +$459 / +$762 | +$877 / +$3,437 / +$6,510 |
| 3-year profit (after $800 build cost) | −$156 (−$956) | +$1,289 (+$489) | +$10,824 (+$10,024) |
| Monthly net revenue vs cost at month 36 | $10 vs $1.30 | $86 vs $2.40 | $720 vs $43 |

**Owner's single tier** ($9.99/mo or $99.99/yr, converting at 0.5× the ladder's rate, 35% choosing annual, no Pro):

| | Bear | Base | Bull |
|---|---|---|---|
| Paying subscribers at end of Y1 / Y2 / Y3 | 1.0 / 1.2 / 1.3 | 4.4 / 6.8 / 9.7 | 19.8 / 42.8 / 77.2 |
| Net revenue Y1 / Y2 / Y3 | $68 / $93 / $109 | $284 / $523 / $764 | $1,231 / $3,127 / $5,873 |
| Profit Y1 / Y2 / Y3 | −$87 / −$40 / −$25 | +$125 / +$381 / +$618 | +$1,064 / +$2,951 / +$5,452 |
| 3-year profit (after build cost) | −$152 (−$952) | +$1,124 (+$324) | +$9,468 (+$8,668) |

**Why these MAU paths.**
- **Anchor:** about 500 users at the 2020–22 peak, all free.
- **Bear:** returning users must install the new version. Users drop off at the GitHub App "Administration: read" consent, and org repos need an org owner. Free self-hosted archivers and Repohistory ($90/yr; free for 1 repo) take the technical buyers.
- **Base:** the landing page, the owner's MVP and .NET community reach, and the history-vault hook regain and pass the peak.
- **Bull:** needs a launch moment and word of mouth, reaching 10× the 2020 peak by year 3.

## 3. Break-even

Net revenue per subscriber-year is the list price × 0.775 (6% VAT drag, 3% refunds, 15% store fee):
- Premium annual: $30.99.
- Premium monthly, active all year: $46.41.
- Founding Member, first year: $15.49.
- $99.99/yr (Pro or single tier): $77.50.
- $9.99/mo for 12 months: $92.91.

| MAU | Recurring opex per year | Annual Premium subs | Monthly Premium subs | $99.99/yr subs | Plus $800 build cost over 3 years | Without MVP credit | Private-repo CI |
|---|---|---|---|---|---|---|---|
| 500 | $137 | 5 (1.0% of MAU) | 3 | 2 | 13 | 7 | 17 |
| 1,000 | $145 | 5 | 4 | 2 | 14 | 7 | 17 |
| 2,000 | $161 | 6 | 4 | 3 | 14 | 8 | 18 |
| 5,000 | $633 (Sentry Team) | 21 | 14 | 9 | 29 | 23 | 33 |
| 10,000 | $839 | 28 | 19 | 11 | 36 | 30 | 40 |

**Timing:**

| Scenario | Cumulative opex covered from | $800 build cost paid back |
|---|---|---|
| Base ladder | Month 10 (Sep 2027) | Month 30 (May 2029) |
| Base single tier | Month 6 | Month 32 |
| Bull ladder | Month 5 | Month 12 |
| Bear | Never within 36 months | Never |

**Owner time is not costed in the table.** With Claude writing the code, the reconciled estimate is about 160 owner hands-on hours (range 130–210), plus about 1–3 hours a week of maintenance. Done without Claude, the same work is about 525–1,030 engineer-hours. The 3-year return per owner hour, after the $800 and ignoring maintenance:

| Scenario | Per owner hour (160 h, with Claude) | Per hour if done by hand (about 440 h, the judge's figure) |
|---|---|---|
| Bear | Negative | Negative |
| Base | About $3/h | About $1/h |
| Bull | About $63/h | About $23/h |
| Stretch (10,000 MAU) | About $124/h | About $45/h |

## 4. Owner's $9.99/$99.99 vs the recommended ladder

**Revenue per payer** (net):

| Measure | Ladder | Single tier | Ratio |
|---|---|---|---|
| First 12 months | $25.56 | $49.77 | 0.51 |
| 36-month value | $34.37 | $63.41 | 0.54 |

The plan-mix assumptions behind those figures:
- **Ladder:** 60% annual at $39.99, 40% monthly at $4.99 for 4.5 paid months.
- **Single tier:** 35% annual at $99.99, 65% monthly at $9.99.

The single tier sells mostly monthly because its annual discount is shallow: annual costs 10× monthly, against an app-store norm of about 3.5–4×.

**Parity conversion factor** (single-tier conversion as a fraction of the ladder's, at which 3-year net revenue is equal):

| Case | Parity factor |
|---|---|
| Bear | 0.49 |
| Base | 0.55 |
| Bull | 0.57 |

These correct the judge's "about 40%", which compared annual prices only.

**Sweep at base MAU** (3-year net revenue; the ladder earns $1,735 in every row):

| Single-tier conversion factor | Matching price elasticity | Single tier | Ladder ($1,735) vs single tier |
|---|---|---|---|
| 0.35 | about 1.3 | $1,099 | Ladder +58% |
| 0.40 | | $1,256 | Ladder +38% |
| 0.45 | | $1,413 | Ladder +23% |
| **0.50 (assumed)** | about 0.85 | $1,570 | Ladder +10.5% |
| 0.70 | about 0.44 | $2,198 | Single tier +27% |
| 1.00 | 0 | $3,141 | Single tier +81% |

The matching elasticity uses factor = (price ratio)^−elasticity, with a blended price ratio of about 2.25×.

**Without Pro.** With Pro switched off, the ladder's 3-year net revenue at base is $1,590 against $1,570 for the single tier, and 3-year profit is +$1,144 against +$1,124. Parity drops to about 0.51 in every scenario.

At base user numbers, the single tier's revenue relative to Premium alone depends on its conversion factor:

| Single-tier conversion factor | Premium alone vs single tier |
|---|---|
| 0.35 | Premium alone +45% |
| 0.45 | Premium alone +13% |
| 0.50 | Premium alone +1% |
| 0.70 | Single tier +38% |

Pro's build cost isn't modelled: 50–75 Claude hours and 20–30 owner hours.

**Recommendation: keep the ladder.**
- Technical buyers have free self-hosted alternatives and a $90/yr web competitor, so the market is probably elastic.
- The ladder gives 2.5× more paying users, which means more banked-history advocates and a less noisy revenue base.
- It keeps $9.99/$99.99 as the Pro anchor.
- The dollar stakes are small either way: under $200 over 3 years at base and about $1.4k at bull.

If the owner wants to test price-insensitivity, test $99.99 as the Pro tier rather than as the only tier.

## 5. Cost lines

| Line | Amount | In the model |
|---|---|---|
| Production cloud (pay-as-you-go, Flex + Table) | $0.35–1.20/mo at 500 MAU ($1.50 used in the model for headroom); $0.80–3.50 at 2k; about $14 at 5k; $5–31 at 10k | High end, interpolated by MAU. $0.50/mo before relaunch. Daily-for-everyone uplift until Premium |
| Cloud stress curve (research, before optimisation) | $2 / $9 / $52 per month | Stress case only |
| Staging / dev | $2–10/mo | $0, paid by the MVP credit ($6/mo if not) |
| Apple Developer Program | $99/yr | Months 1, 13, 25 |
| Apple Small Business Program | $0 (enrollment) | 15% fee assumed |
| Google Play registration | $25 one-time | Year 1. $0 if the 2020 account is active |
| Store commission | 15% (Apple SBP; Play 10% service + 5% billing) | Revenue deduction |
| VAT/GST (remitted by the stores) | About 6% of gross outside the US | Revenue deduction |
| Refunds | About 3% (Productivity median 4.7%) | Revenue deduction |
| Domain | $12–20/yr; DNS at registrar $0 (Azure DNS optional $6/yr) | $20/yr |
| GitHub Pages (landing, policies, config.json) | $0 | $0 |
| Sentry | Developer plan free (1 user, about 5k errors/mo); Team $26/mo annual or $29/mo monthly | $29/mo above 4,000 MAU |
| CI (GitHub Actions) | Public repo $0. Private: $12/mo included; macOS $0.062/min, Linux $0.006/min, so about $60/mo during build and $31/mo after | $0, repo stays public |
| Google Cloud Pub/Sub (Play notifications) | Free tier | $0 |
| RevenueCat (fallback only) | $0 under $2.5k monthly tracked revenue, then 1% | Not used |
| Avoided by design | Notification Hubs Basic $120/yr; ACR Basic about $61/yr; Postgres about $190/yr | $0 |
| Claude Ultra, build period | $200/mo × 4 months = $800 (range $600–1,200; $180/mo more than Pro) | One-time, shown separately |
| EU/UK Art. 27 representative | About €100–300/yr | Stress case only ($250) |
| Owner time, hardware, income tax | n/a | Not costed |

**Year-1 base cost:** Apple $99 + Google $25 + domain $20 + cloud $15 = **$159**. Years 2–3 are $141–146.

## 6. Effect of the MVP $150/month credit

**Terms:**
- Visual Studio Enterprise NFR credit, for dev/test only. Production use breaks the terms.
- Not for App Insights. No Functions free grant on this subscription.
- Usage stops when the credit runs out, and it renews only while the MVP award lasts.

**Use:** staging, load tests and spikes, about $2–10/month (about 4% of the nominal $1,800/yr).

**Effect on 3-year profit:**

| Scenario | With credit | Without credit |
|---|---|---|
| Bear | −$156 | −$372 |
| Base | +$1,289 | +$1,073 |
| Bull | +$10,824 | +$10,608 |

- Base year-1 profit goes from +$68 to −$4 without the credit.
- Break-even moves by about 2.3 annual subscribers.
- It cannot pay for production, Apple, Google, the domain, Sentry or CI, which together are 100% of the modelled costs.
- Running production on it would save only $18–42/yr and risk suspension of the history store. Don't.
- If the award lapses, tear staging down between releases (about $1–2/month).

## 7. One-time build costs (not opex)

- **Claude Ultra:** $800 (4 months: 3.0 in 6–8 weeks, plus 3.1 in 5–6 weeks, plus slip). Plan limits are weekly and aren't published in tokens; measure usage with /usage on the first slice.
- **Optional:** about $200 in year 2 for the .NET 12 LTS migration. .NET 11 support ends 2028-11-14, which is month 24 of this model.
- **Google Play $25:** included in year-1 cost, to be conservative.
- **Premium's extra cost over a free-only relaunch:** about $10–30/yr of cash (collector and storage), plus about 21–28 developer days for 3.1 (app 15–20, backend 6–8).

## 8. Sensitivities (base ladder unless noted)

| Case | 3-year profit | Change |
|---|---|---|
| Base as modelled | +$1,289 | n/a |
| Judge's on-time schedule (relaunch month 2, Premium month 4) | +$1,317 | +$28 |
| Collect for subscribers only (paid share 1.75%, no founder burst) | +$701 | −$588 (−46%) |
| No MVP credit (staging paid) | +$1,073 | −$216 |
| Private repo (paid CI) | +$28 | −$1,261 |
| Stress: private CI + Sentry Team from launch + Art. 27 representative + no credit + stress cloud | −$1,975 | −$3,264 |
| Cloud at the judge's low end instead of high | about +$1,330 | about +$45 |
| Refunds 4.7% instead of 3% | about +$1,259 | about −$30 |
| No Apple Small Business Program (30% on first-year iOS subscriptions) | about +$1,050 | about −$240 (estimate) |
| Stretch: bull funnel, MAU 2,500 / 6,000 / 10,000 | +$20,571 (Y3 cost $763, cloud $296) | n/a |

## 9. Model structure and formulas

Month m = 1…36, where m = 1 is Dec 2026. Year 1 is months 1–12, Y2 is 13–24, Y3 is 25–36.

**Users and acquisitions**
- MAU(m) = 0 for m < m_relaunch (3). After that it is piecewise-linear through (m_relaunch, MAU_launch), (12, MAU_Y1), (24, MAU_Y2) and (36, MAU_Y3).
- New payers N(m) = p/12 × MAU(m) for m ≥ m_premium (5), where p is new payers per year as a share of MAU.
- Founder burst F = f × MAU(m_premium): annual plan, first year at $19.99, renewals at $39.99.
- Split of each month's new payers:
  - Pro share s = 0.10 from m_pro, otherwise 0.
  - Premium annual share a = 0.60. Pro annual share = 0.50.

**Cohort revenue**
- Monthly cohort: pays n × r^(m − m0) × price each month. r solves Σ_{k=0..11} r^k = PM, the paid months in year 1:
  - PM 4.0 → r = 0.759.
  - PM 4.5 → r = 0.791.
  - PM 5.0 → r = 0.818.
- Annual cohort: pays n × price at m0, n × R1 × price at m0 + 12, and n × R1 × R2 × price at m0 + 24.
- Net(m) = Gross(m) × (1 − 0.06) × (1 − 0.03) × (1 − 0.15) = Gross × 0.775.

**Costs**
- Cloud(m):
  - before relaunch: $0.50;
  - after: interp(high curve: 0 → $0.50, 500 → $1.50, 2,000 → $3.50, 10,000 → $31; linear, extrapolated);
  - plus the daily-collection uplift for m ≤ m_premium.
- Fixed(m):
  - Apple $99 and domain $20 in months 1, 13 and 25;
  - Google $25 in month 1;
  - Sentry $29 when MAU > 4,000;
  - CI, staging and Art. 27 only when their switches are on.

**Results**
- Profit_y = Σ Net − Σ (Cloud + Fixed) over the year's months.
- Build cost = $200 × 4, reported separately.
- Paying at end of year N = monthly survivors + annual subscribers inside a paid year, at month 12N.
- Single tier: p × k and f × k, with k = 0.5. Prices $9.99/$99.99, annual share 0.35, no Pro, no founder discount.
- Break-even subscribers = annual opex ÷ net per subscriber-year.

model_params_json holds every default, the scenario overrides, the formulas, and expected outputs for testing a calculator. The reference implementation is [model/forecast_model.py](model/forecast_model.py). Run `python3 forecast_model.py` to reproduce every number here.

## 10. Key assumptions and sources

- **Store fees:** Apple Small Business Program 15%; Google Play subscriptions 10% + 5% = 15% (US/EEA/UK since 2026-06-30).
- **Benchmarks (RevenueCat 2026, via secondary sources):**
  - North America median $9.99/mo and $39.99/yr.
  - Freemium download-to-paid by day 35: 2.1%.
  - All-app medians: iOS 2.6%, Android 0.9%.
  - Trial-to-paid median about 32.5%.
  - Annual retention 27–31%; Utilities annual renewal 35%.
- **Paid share, base 2.5%:**
  - Platform blend (65% iOS) gives about 1.97%.
  - A 25% uplift for history being saved for everyone gives about 2.5%.
  - Bear assumes no uplift plus friction; bull matches the 3–5% that developer-tool freemium benchmarks call "good".
- **Competition:** Repohistory $90/yr or $9/mo with 1 repo free (AGPL, self-hostable); RepoEasy €12/yr; several free self-hosted archivers.
- **Costs:** from the judge's monthly-cost table and the Azure research. GitHub Actions rates are from GitHub's docs ($0.062/min macOS, $0.006 Linux, $12/mo included on Free; free for public repos). Sentry is from secondary pricing sources ($26/$29 Team; the free plan is 1 user and about 5k errors).
- **Treatment:** revenue on a cash-at-purchase basis; payout lag and the trial delay are ignored; no income tax.

## 11. What changes the answer: decision gates

- **Gate A, month 6 (May 2027, one month after Premium):**
  - Measure: GitHub App install completion rate, the share of users who keep "save my history" on, trial starts, and Founding Member uptake.
  - On track for base: about 300+ MAU, 4+ payers, trial starts plus Founding Member purchases of 1.5%+ of MAU.
- **Gate B, month 12 (Nov 2027):**
  - Bear signal: under 400 MAU and under 5 payers. Freeze feature work and keep costs at about $11/month (Apple, domain, cloud). The free app and the vault still run at near-zero cost.
  - Pro signal: 600+ MAU and 1.5%+ of them paying (the base path). Build Pro (alerts and widgets).
  - Bull signal: 1,500+ MAU and 2.5%+ paying. Also consider the web dashboard and the US web checkout link-out (currently 0% Apple fee, but a fee is pending).
- **Biggest levers, in order:**
  1. MAU growth beyond the 2020 audience.
  2. Collecting history for everyone (about 1.8× profit, if the assumed conversion lift holds).
  3. Keeping fixed fees at $0.
  4. Conversion.

  Price structure and cloud architecture barely matter at this scale.

## 12. Caveats

- No category-specific elasticity or conversion data exists. All benchmarks are cross-category medians, and treat outputs as roughly ±50%.
- With 3–25 paying users, actual revenue will be lumpy; one annual subscriber is ±$31.
- Azure Table, Blob and Log Analytics prices come partly from secondary sources. The Sentry free-plan span quota is reported inconsistently.
- Apple's US link-out fee (0% now, up to 15% proposed) and the Supreme Court review could change web-checkout economics. Web checkout isn't modelled.
- The owner should supply historical MAU, the iOS/Android split and repos per user to recalibrate.


## Appendix: model parameters (JSON)

These are the defaults, scenario overrides, formulas and expected outputs. They are used to test any calculator built on this model.

```json
{
 "model": "GitTrends relaunch 3-year monthly cohort model v1 (2026-11-15). Expected-value (fractional) subscribers. Cash basis at purchase. USD, pre-income-tax.",
 "defaults": {
  "timeline": {
   "months": 36,
   "month1": "2026-12",
   "relaunch_month": 3,
   "premium_month": 5,
   "pro_month": 13,
   "build_months_claude": 4
  },
  "store": {
   "store_fee": 0.15,
   "tax_drag": 0.06,
   "refund_rate": 0.03
  },
  "ladder": {
   "premium_monthly": 4.99,
   "premium_annual": 39.99,
   "founder_first_year": 19.99,
   "pro_monthly": 9.99,
   "pro_annual": 99.99,
   "annual_share_new_payers": 0.6,
   "pro_share_new_payers": 0.1,
   "pro_annual_share": 0.5,
   "trial_to_paid": 0.33
  },
  "single_tier": {
   "monthly": 9.99,
   "annual": 99.99,
   "annual_share_new_payers": 0.35,
   "relative_conversion": 0.5
  },
  "retention": {
   "monthly_paid_months_y1": 4.5,
   "annual_renewal_first": 0.3,
   "annual_renewal_later": 0.5
  },
  "funnel": {
   "paid_share_annual_of_mau": 0.025,
   "founder_share_of_mau_at_premium": 0.01
  },
  "mau": {
   "launch": 250,
   "end_y1": 600,
   "end_y2": 900,
   "end_y3": 1200
  },
  "costs": {
   "cloud_curve_high": [
    [
     0,
     0.5
    ],
    [
     500,
     1.5
    ],
    [
     2000,
     3.5
    ],
    [
     10000,
     31.0
    ]
   ],
   "cloud_curve_low": [
    [
     0,
     0.2
    ],
    [
     500,
     0.4
    ],
    [
     2000,
     0.8
    ],
    [
     10000,
     5.0
    ]
   ],
   "cloud_curve_stress": [
    [
     0,
     1.0
    ],
    [
     500,
     2.0
    ],
    [
     2000,
     9.0
    ],
    [
     10000,
     52.0
    ]
   ],
   "cloud_curve_used": "high",
   "phase1_daily_uplift_curve": [
    [
     0,
     0.0
    ],
    [
     500,
     0.2
    ],
    [
     2000,
     0.5
    ],
    [
     10000,
     5.0
    ]
   ],
   "pre_relaunch_cloud_per_month": 0.5,
   "apple_developer_per_year": 99.0,
   "google_play_one_time": 25.0,
   "domain_per_year": 20.0,
   "dns_per_month": 0.0,
   "sentry_free_until_mau": 4000,
   "sentry_team_per_month": 29.0,
   "ci_public_repo": true,
   "ci_private_build_month": 60.0,
   "ci_private_steady_month": 31.0,
   "staging_per_month_without_credit": 6.0,
   "mvp_credit_covers_staging": true,
   "eu_art27_rep_per_year": 0.0,
   "legal_review_one_time": 0.0,
   "claude_ultra_per_month": 200.0
  }
 },
 "scenario_overrides": {
  "bear": {
   "mau": {
    "launch": 150,
    "end_y1": 300,
    "end_y2": 375,
    "end_y3": 400
   },
   "funnel": {
    "paid_share_annual_of_mau": 0.01,
    "founder_share_of_mau_at_premium": 0.005
   },
   "retention": {
    "monthly_paid_months_y1": 4.0,
    "annual_renewal_first": 0.25,
    "annual_renewal_later": 0.4
   },
   "timeline": {
    "pro_month": 999
   }
  },
  "base": {},
  "bull": {
   "mau": {
    "launch": 400,
    "end_y1": 1500,
    "end_y2": 3000,
    "end_y3": 5000
   },
   "funnel": {
    "paid_share_annual_of_mau": 0.05,
    "founder_share_of_mau_at_premium": 0.02
   },
   "retention": {
    "monthly_paid_months_y1": 5.0,
    "annual_renewal_first": 0.35,
    "annual_renewal_later": 0.6
   },
   "timeline": {
    "pro_month": 11
   }
  }
 },
 "derived": {
  "net_factor": 0.77503,
  "monthly_retention_r": {
   "PM_4.0": 0.7592,
   "PM_4.5": 0.7911,
   "PM_5.0": 0.8179
  },
  "net_per_subscriber_year": {
   "premium_annual": 30.99,
   "premium_monthly_active_12mo": 46.41,
   "founder_first_year": 15.49,
   "pro_or_single_annual": 77.5,
   "pro_or_single_monthly_active_12mo": 92.91
  }
 },
 "formulas": {
  "MAU(m)": "0 if m < relaunch_month; else piecewise-linear through (relaunch_month, mau.launch), (12, mau.end_y1), (24, mau.end_y2), (36, mau.end_y3)",
  "new_payers(m)": "paid_share_annual_of_mau/12 * MAU(m) for m >= premium_month (single tier: multiply by single_tier.relative_conversion)",
  "founder_burst": "founder_share_of_mau_at_premium * MAU(premium_month), annual plan, first year at founder_first_year, renewals at premium_annual (single tier: share * relative_conversion, priced at single_tier.annual)",
  "split": "pro share = pro_share_new_payers if m >= pro_month else 0; annual share = annual_share_new_payers (Pro uses pro_annual_share)",
  "r": "solve sum_{k=0..11} r^k = monthly_paid_months_y1 (bisection)",
  "monthly_cohort_gross(m)": "n * r^(m - m0) * monthly_price for m >= m0",
  "annual_cohort_gross": "n*price at m0; n*R1*price at m0+12; n*R1*R2*price at m0+24 (R1 = annual_renewal_first, R2 = annual_renewal_later)",
  "net(m)": "gross(m) * (1 - tax_drag) * (1 - refund_rate) * (1 - store_fee)",
  "cloud(m)": "pre_relaunch_cloud_per_month if m < relaunch_month else interp(cloud_curve_<used>, MAU(m)) + (m <= premium_month ? interp(phase1_daily_uplift_curve, MAU(m)) : 0); interp extrapolates linearly past last point",
  "fixed(m)": "apple_developer_per_year + domain_per_year + eu_art27_rep_per_year at m in {1,13,25}; google_play_one_time + legal_review_one_time at m=1; dns_per_month every month; sentry_team_per_month if MAU(m) > sentry_free_until_mau; if !ci_public_repo: ci_private_build_month for m <= premium_month else ci_private_steady_month; if !mvp_credit_covers_staging: staging_per_month_without_credit",
  "profit_y": "sum over the year's 12 months of net(m) - cloud(m) - fixed(m); Y1 = months 1-12 (Dec 2026-Nov 2027)",
  "one_time_build": "claude_ultra_per_month * build_months_claude (reported separately, not opex)",
  "paying_end_yN": "active monthly survivors + annual subscribers inside a paid year, at month 12N",
  "trial_starts": "annual Premium new payers / trial_to_paid (display only; paid share is already net of trial conversion)",
  "breakeven_subscribers": "recurring opex per year / net per subscriber-year (premium annual 39.99*net_factor)"
 },
 "sensitivities": {
  "stress_costs": {
   "ci_public_repo": false,
   "eu_art27_rep_per_year": 250,
   "mvp_credit_covers_staging": false,
   "sentry_free_until_mau": 0,
   "cloud_curve_used": "stress"
  },
  "subscriber_only_collection": {
   "paid_share_annual_of_mau": 0.0175,
   "founder_share_of_mau_at_premium": 0
  },
  "on_time_schedule": {
   "relaunch_month": 2,
   "premium_month": 4
  },
  "stretch_10k": {
   "base": "bull",
   "mau": {
    "launch": 500,
    "end_y1": 2500,
    "end_y2": 6000,
    "end_y3": 10000
   }
  },
  "single_tier_relative_conversion_sweep": [
   0.35,
   0.4,
   0.45,
   0.5,
   0.7,
   1.0
  ]
 },
 "expected_outputs_for_testing": {
  "bear_ladder": {
   "net_revenue": [
    50.5,
    97.8,
    118.2
   ],
   "total_cost": [
    154.7,
    133.2,
    134.3
   ],
   "profit": [
    -104.2,
    -35.4,
    -16.1
   ],
   "paying_end": [
    2.2,
    3.0,
    3.6
   ]
  },
  "base_ladder": {
   "net_revenue": [
    226.6,
    600.5,
    907.8
   ],
   "total_cost": [
    158.7,
    141.2,
    146.0
   ],
   "profit": [
    67.9,
    459.3,
    761.8
   ],
   "paying_end": [
    9.6,
    16.9,
    24.8
   ]
  },
  "bull_ladder": {
   "net_revenue": [
    1043.9,
    3612.3,
    6930.8
   ],
   "total_cost": [
    166.5,
    175.5,
    420.9
   ],
   "profit": [
    877.4,
    3436.8,
    6509.8
   ],
   "paying_end": [
    43.1,
    103.1,
    191.6
   ]
  },
  "bear_single": {
   "net_revenue": [
    67.8,
    92.9,
    109.5
   ],
   "total_cost": [
    154.7,
    133.2,
    134.3
   ],
   "profit": [
    -86.9,
    -40.3,
    -24.8
   ],
   "paying_end": [
    1.0,
    1.2,
    1.3
   ]
  },
  "base_single": {
   "net_revenue": [
    284.0,
    522.6,
    763.7
   ],
   "total_cost": [
    158.7,
    141.2,
    146.0
   ],
   "profit": [
    125.3,
    381.4,
    617.7
   ],
   "paying_end": [
    4.4,
    6.8,
    9.7
   ]
  },
  "bull_single": {
   "net_revenue": [
    1230.7,
    3126.7,
    5873.1
   ],
   "total_cost": [
    166.5,
    175.5,
    420.9
   ],
   "profit": [
    1064.2,
    2951.2,
    5452.2
   ],
   "paying_end": [
    19.8,
    42.8,
    77.2
   ]
  },
  "base_ladder_stress_costs": {
   "net_revenue": [
    226.6,
    600.5,
    907.8
   ],
   "total_cost": [
    1293.3,
    1199.7,
    1216.5
   ],
   "profit": [
    -1066.7,
    -599.2,
    -308.7
   ],
   "paying_end": [
    9.6,
    16.9,
    24.8
   ]
  },
  "single_vs_ladder_parity_relative_conversion": {
   "bear": 0.493,
   "base": 0.552,
   "bull": 0.566
  }
 }
}
```
