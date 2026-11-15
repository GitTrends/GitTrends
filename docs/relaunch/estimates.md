# GitTrends relaunch: effort, calendar and token estimates

Part of the [relaunch plan](README.md). Two estimators worked independently from the same architecture:
- **Bottom-up:** about 95 work items, each sized in human hours, then converted to Claude agent-hours by type of work.
- **Top-down:** analogies, including this repo's own Xamarin-to-MAUI port, typical MAUI major-version bumps, typical subscription backends and typical store-review cycles.

The plan uses the reconciled numbers below. The two original reports follow as appendices.

**Terms used:**
- **Claude agent-hours:** active agent-session hours, summed across parallel sessions and subagents. Wall-clock time can be lower when sessions run in parallel.
- **Owner hours:** your hands-on time. This covers consoles, signing, Mac and device QA, PR review, decisions and store submissions.
- **Tokens:** everything processed, including cache reads.

## 1. Reconciled estimate

| Phase | Bottom-up Claude h | Top-down Claude h | **Reconciled Claude h** | Bottom-up owner h | Top-down owner h | **Reconciled owner h** |
|---|---|---|---|---|---|---|
| 0 Stabilize and secure | 16 | 10 | **about 13** | 15 | 11 | **about 13** |
| 1 App platform port | 62 | about 45 (its 65 includes 3.0 client features) | **about 55** | 31 | about 22 | **about 25** |
| 2 Backend, through prod go-live | 105 | 50 | **about 75** | 22 | 18 | **about 20** |
| 3 Release 3.0 (client integration, compliance, beta, store) | 75 | about 32 (spread across its Phases 1 and 4) | **about 50** | 38 | about 28 | **about 33** |
| 4 Release 3.1 Premium | 107 | about 71 (62 build + about 9 store) | **about 90** | 46 | about 47 | **about 46** |
| 5 Post-launch operations | 40 (12 weeks) | 27 (8–12 weeks) | **about 33** | 21 | 25 | **about 23** |
| **Total** | **405** (327–498) | **235** (148–324) | **about 310** (235–415) | **173** (137–214) | **150** (100–200) | **about 160** (130–210) |

**Why the estimators differ.** Bottom-up sizes the backend and Premium larger: two-store verification, entitlement state, webhooks, backups and integration tests, item by item. Top-down compresses greenfield backend work 3–4× against a senior engineer. Reconciled figures sit near the midpoint, with the range spanning both centrals.

**Doing it without Claude:** about 525–1,030 engineer-hours. With Claude, your hands-on time is about 160 hours, mostly work that can't be delegated.

## 2. Calendar

Weeks count from Monday 2026-11-16. The holidays probably add a week.

| Milestone | You at 15 h/week | You at 5 h/week |
|---|---|---|
| Phase 0 done (accounts, Apps, spikes) | week 1–2 | week 2–3 |
| Prod backend live, history banking starts | week 6–7 | week 13–14 |
| **3.0 free relaunch in stores** | **around week 10** (8–12): late January 2027 | **around week 20** (12–28): April 2027 |
| **3.1 Premium live** | **around week 15** (13–19): early to mid March 2027 | **around week 32** (21–40): late June to July 2027 |
| Post-launch window ends | around week 27 | around week 45 |

**What sets the pace:**
- **At 5 h/week:** your hours, the whole way through.
- **At 15 h/week:** Claude throughput (or Ultra's weekly limit) in weeks 2–7, when the app port and the backend run in parallel. After that, your device and store work.
- **App Review:** about 1–3 days per submission. Budget one rejection per release.

## 3. Tokens and Ultra

**Token rate per agent-hour:**
- Bottom-up: 3.0–5.5M (central 4.2M).
- Top-down: 2.5–7M.
- Measured on this planning session: research and verification agents read many large web pages, so they ran near the top of that range.

**Project total:** about **1.3B tokens** (0.8–2.5B).

**API-equivalent cost:**
- At the measured mix (about $0.60 per million): about $0.8k.
- At the estimators' more conservative mix ($0.85–1.50 per million): $1.1k–1.9k.

**Measured anchor (this planning session, 2026-11-15):**

| Item | Value |
|---|---|
| Model requests | about 965, on the main thread and 20 workflow agents |
| Fresh input | about 2k tokens |
| Cache writes | 4.9M |
| Cache reads | 157M |
| Output | 1.4M |
| **Total processed** | **about 163M** |
| API rates used | $4 input, $20 output, $0.20 cache read, $5–8 cache write per million |
| **API-equivalent cost** | **about $85–100** |

**Weekly profile at 15 h/week** (central values):

| Weeks | Work | Agent-h/week | Tokens/week | Compared with this session |
|---|---|---|---|---|
| 1–2 | Phase 0 and spikes | 5–16 | 15–70M | 0.1–0.4× |
| 2–7 | App port and backend in parallel (**peak**) | 25–42 | 110–175M (up to about 250M) | 0.7–1.1× (up to 1.5×) |
| 7–10 | 3.0 integration, beta, store | 15–21 | 50–90M | 0.3–0.55× |
| 10–15 | Premium | 15–26 | 75–110M | 0.45–0.7× |
| 15+ | Operations | 2–6 | 5–15M | 0.03–0.1× |

At 5 h/week the same total spreads over about 32 build weeks: about 25–46M a week on average, peaking around 50–120M.

**Calibration steps:**
1. **Now:** read `/usage` (or Settings > Usage). The share this session used is the yardstick *P*.
2. **Day-1 spikes:** record the weekly % before and after. They are a known amount of agent work, roughly 6–10 agent-hours.
3. **First parallel week (week 2 or 3):** record again. If the peak looks set to pass about 80%, run the app and backend streams one after the other. That adds 1–2 calendar weeks at 15 h/week and nothing at 5 h/week. The other option is usage credits, at about $3–5 per agent-hour.

## 4. Risks to the estimate

- **The .NET 11 / MAUI 11 toolchain is days old.** Shiny 6, Syncfusion Toolkit and Plugin.InAppBilling ship net10 builds only. Breakage adds 15–40 Claude hours or forces a fall back to .NET 10, which has the same end of support.
- **Shiny 3 to 6 has no migration notes.** This could double that item, or the background jobs could be rewritten natively.
- **The iOS loop runs without local Xcode.** Each `macos-26` runner build takes 20–45 minutes.
- **The custom Shell renderer** (758 lines, reflects into private fields) could add 5–20 hours, or be dropped.
- **Container limits.** The .NET and Android SDK hosts are blocked until the environment allowlist changes, and there is no KVM. Workarounds take 2–6 Claude hours.
- **Store rejections** cost 3–10 calendar days and 1–4 owner hours each.
- **The precedent.** The last port reached code-complete and stalled before the store for about a year. Strict scope and an early store checklist are the countermeasure.


## Appendix A: bottom-up report

## GitTrends relaunch: bottom-up effort, token and calendar estimate

*As of 2026-11-15. No repository files were modified.*

### 1. Headline

The phase-level results are in the table below. Claude hours are summed agent-session hours (parallel sessions and subagents add up). Tokens include cache reads. Dollar figures are API-equivalent.

| Phase | Claude agent-h (range) | Owner h (range) | Calendar, owner 15 h/wk | Calendar, owner 5 h/wk | Tokens M: low to high (central) | API-equiv $: low to high (central) |
|---|---|---|---|---|---|---|
| 0 Stabilize and secure | 16 (12–20) | 15 (11–19) | 1 wk | 3 wk | 36–110 (67) | 31–165 (73) |
| 1 App port to .NET 11 / MAUI 11 | 62 (50–76) | 31 (25–38) | 4.5 wk, alongside Phase 2 | ~10 wk, alongside Phase 2 | 150–418 (260) | 131–627 (283) |
| 2 Backend (Aspire, Flex, collector, IaC, go-live) | 105 (85–130) | 22 (17–28) | 5 wk, alongside Phase 1 | ~10.5 wk, alongside Phase 1 | 255–715 (441) | 222–1,073 (481) |
| 3 Release 3.0 (free relaunch and vault) | 75 (62–92) | 38 (31–46) | 3.5 wk | 8.5 wk | 186–506 (315) | 162–759 (343) |
| 4 Release 3.1 Premium | 107 (88–130) | 46 (38–56) | 6 wk | 10.5 wk | 264–715 (449) | 230–1,073 (489) |
| 5 Post-launch ops (12 wk) | 40 (30–50) | 21 (15–27) | 12 wk | 12 wk | 90–275 (168) | 78–413 (183) |
| **Total** | **405 (327–498)** | **173 (137–214)** | 3.0 at ~wk 9; 3.1 at ~wk 15 | 3.0 at ~wk 23; 3.1 at ~wk 33 | **981–2,739 (1,701)** | **853–4,109 (~1,850)** |

Doing everything by hand would take about **1,030 engineer-hours**. Claude cuts the owner's hands-on time by about 83%.

**Pro tier (Phase 3) is not in the totals.** It would add:
- Claude 50–75 h and owner 20–30 h;
- 150–410M tokens, $130–620;
- 6–10 weeks at 15 h/wk.

### 2. Method

**1. Inventory.** I read every `work_items` list in backend-inventory (BI), app-dataflow (AD), build-upgrade-surface (BU) and git-archaeology (GA), about 110 items, plus the recommended architecture (ARCH).

**2. De-duplication.** Items that appeared in several reports were merged:

| Merged item | Reports |
|---|---|
| Startup independence | BI, AD, BU, GA |
| Syncfusion license removal | BI, AD, BU, GA |
| Legacy endpoint guards (private) | BI, BU, GA |
| Privacy and compliance | BI, AD, BU, GA |
| Test decoupling from GetTestToken | BI, AD, BU, GA |
| CI to GitHub Actions | BI, BU, GA |
| Android package ID | AD, BU, GA, BI |
| OAuth / GitHub App | BI, AD, GA |
| Entitlements | BI, AD, GA |
| OTel | BI, AD, GA |

**3. Dropped items**, because ARCH supersedes them:
- the `/config` API (replaced by GitHub Pages config.json);
- Syncfusion key injection at build time (replaced by the MIT Toolkit);
- device snapshot uploads;
- Notification Hubs and remote push (moved to Pro);
- ACA Jobs and azd (replaced by Flex timers and Bicep);
- Appium port and Mac Catalyst (deferred);
- a raw OTel exporter on mobile (Sentry is used instead).

**4. Added items** that ARCH implies but no report listed: collector, sessions, ACL, webhooks, reconcile, backups, purchase binding, Bicep environments, Pages site, staging soak, load test, security review, prod go-live and post-launch operations. The result is about 95 items.

**5. Sizing in human-engineer hours:** XS 1–2, S 3–6, M 8–16, L 20–40.

**6. Conversion to Claude agent-hours:**

| Work type | Claude hours as a share of human hours |
|---|---|
| Mechanical edits | 0.25–0.30 |
| Backend code with tests | 0.30–0.35 |
| UI and iOS code Claude cannot run | 0.35–0.50 |
| QA bug-fixing | ~0.5 |

Each phase then gets 8–15% contingency.

**7. Owner hours** are itemised: consoles, Mac and device testing, screenshots, legal approval. They also include PR review at about 0.35 h per PR (about 60 PRs) and steering at about 5% of Claude hours.

**8. Token model.** I assume 45–75 requests per agent-hour at 55–90k average context, which gives **3.0–5.5M tokens per hour (central 4.2M)**.
- Calibration: the discovery run's 615 calls at 40–60k average context come to about 25–37M tokens. That is 13–19x the harness's 1.92M "subagent tokens", inside the stated 5–20x band.

**9. Price model.** At $4 input, $20 output, $0.20 cache read and $5 cache write per million tokens:
- 92% cache reads, 6% fresh input or cache writes, 2% output gives **$0.87/M**.
- 89%, 8.5% and 2.5% gives **$1.09/M**.
- 85%, 11% and 4% gives **$1.50/M**.
- Phase low = low hours × 3.0M × $0.87. Phase high = high hours × 5.5M × $1.50. Central = hours × 4.2M × $1.09.

**10. Calendar.** Owner hours divided by availability, plus external waits that don't overlap (beta, App Review, Play review, sandbox). I checked this against Claude throughput, about 33–42 agent-hours per week at peak with 2 parallel sessions.

**11. Container facts checked today:**
- No `/dev/kvm`, so there is no Android emulator and Claude can't see any UI.
- 4 vCPU and 15 GB RAM.
- The proxy **refuses `builds.dotnet.microsoft.com` and `dl.google.com`**, so neither the .NET SDK nor the Android SDK can be installed until the owner approves an environment allowlist.

### 3. Items by phase

Each table shows the human-engineer estimate (Human h), Claude agent-hours (Claude h) and owner hands-on hours (Owner h).

#### Phase 0: Stabilize and secure (Claude 16 h, owner 15 h)

| Item | Human h | Claude h | Owner h | Reasoning |
|---|---|---|---|---|
| Fast-forward master to pr1, rename to main, protect the branch (GA) | 1 | 0.5 | 0.5 | Git commands; the owner approves |
| Legacy endpoint guards (details private) (BI, GA, BU) | 6 | 2.5 | 1.5 | Claude writes the script; the owner checks the names and runs it |
| Revoke the old OAuth tokens and reset the secret, wildcard off; revoke the UITestToken PATs and the Syncfusion key (BI, GA) | 1 | 0.5 | 1.0 | Console work is the owner's |
| Prod pay-as-you-go subscription, $25 budget, locks; spending limit on the MVP VS subscription (BI) | 2 | 0.5 | 1.5 | Billing belongs to the owner |
| GitHub org; Dev, Staging and Prod GitHub Apps created from manifests (BI, AD, ARCH) | 3 | 1.0 | 2.0 | Manifests avoid mis-clicks; private keys go to the owner |
| Domain, DNS, Pages custom domain (BI, BU) | 1.5 | 0.5 | 1.0 | |
| Apple: Small Business Program, App Store Connect record and highest build; **start the Paid Apps Agreement, tax and banking** (BU, AD) | 2 | 0.3 | 1.5 | Long lead time that gates 3.1 |
| Play: account health, lowercase package, Play App Signing or upload-key reset, payments profile (BU, AD, GA) | 2 | 0.3 | 1.5 | A key reset takes days |
| Email GitHub about AUP §6 (ARCH) | 1 | 0.4 | 0.5 | |
| Cloud environment: host allowlist; setup script for SDK 11, maui-android, JDK 21, Android SDK, npm Azurite, func tools, Aspire CLI (new) | 5 | 2.5 | 0.5 | Blocked hosts confirmed today |
| Spike A: Azure.Functions.Sdk 1.1.0 plus AddAzureFunctionsProject, then a Flex deploy to staging through Actions OIDC (ARCH) | 10 | 4.0 | 1.0 | The owner creates the federated credential |
| Spike B: MAUI 11 Android build in the container, iOS on macos-26 or the owner's Mac, with InAppBilling 11.0.1 and Toolkit 1.0.12 (ARCH, BU) | 8 | 3.5 | 1.5 | The owner installs Xcode 27.2 |
| Steering | | | 1.0 | |

#### Phase 1: App port (Claude 62 h, owner 31 h; about 160 human hours)

| Item | Human h | Claude h | Owner h | Reasoning |
|---|---|---|---|---|
| TFM and SDK bump, strip Mono/Xamarin properties, OS-conditional TFMs, LangVersion latest (BU) | 4 | 1.0 | 0 | Mechanical |
| AppStore configuration: Release plus StoreBuild constant, fix the solution mapping (BU, ARCH) | 3 | 1.0 | 0 | Fixes the debuggable APK and the null Sentry DSN |
| Remove the Compatibility package, SkiaSharp and the Mac Catalyst TFM (BU) | 2.5 | 0.8 | 0.2 | |
| 47 CS0618 sites, plus any new .NET 11 obsoletions (BU) | 5 | 1.5 | 0 | The compiler finds them |
| Syncfusion Charts to the MIT Toolkit; delete the license plumbing in 12 files (BI, AD, BU, GA) | 12 | 3.5 | 1.5 | Charts need a visual check |
| Sharpnado to Border and Shadow, 5 classes plus themes (BU) | 12 | 3.5 | 1.5 | Design review in light and dark |
| Shiny 3.3.4 to 6.5.2 (~100 references in 19 files, BGTask IDs) plus the job-type bugs (BU, AD) | 22 | 8.0 | 2.5 | Highest uncertainty; background jobs only behave on real devices |
| CommunityToolkit 17, Markup 9, drop MediaElement (BU) | 12 | 3.5 | 1.0 | Onboarding check |
| StoreReview replaced by StoreKit and Play In-App Review (BU) | 4 | 1.5 | 0.5 | |
| sqlite-net 1.11 / SQLitePCLRaw 3 (BU) | 4 | 1.0 | 0.5 | Upgrade-in-place test |
| Refit 16, Sentry 7, M.E. 11, NUnit 5 (BU) | 12 | 3.5 | 0 | Tests depend on ApiException |
| UIScene lifecycle (MT7199); OAuth callback and notification taps move to the scene (BU) | 6 | 2.5 | 2.0 | Claude can't run it |
| Large-title Shell renderer (758 lines, private reflection): test, or remove in favour of built-in (BU) | 10 | 3.0 | 1.5 | |
| CoreCLR validation: cold start, size, memory (BU) | 8 | 1.0 | 3.0 | Device work |
| Manifest, plist and privacy-manifest fixes; **lowercase ApplicationId** (BU, AD, GA, BI) | 4 | 1.5 | 0.3 | |
| Delete dead code: Shared, UITests, backdoors, App Center and NH keys, ARM profiles (BI, BU, GA) | 3 | 1.0 | 0 | |
| Decouple 80–100 backend-dependent tests: PAT from env, MockHttp, favicon fixtures, MTP opt-in (all four reports) | 20 | 7.0 | 0.5 | Verifier count: 79 of 397 cases |
| Notification-tap crash (AD) | 3 | 1.0 | 0.5 | |
| GitHub Actions: ci, android (AAB to internal), ios (macos-26, Xcode 27.2, TestFlight), store-config check; delete Azure DevOps and the format bot; weekly Dependabot (BU, BI, GA) | 14 | 6.0 | 3.0 | The owner creates the ASC key, certificate, keystore and Play service account |
| Integration and debug contingency (~15%) | | 7.0 | 3.0 | Toolchain is 5 days old |
| Self-review and PR write-ups | | 3.0 | | |
| PR reviews (~15), steering, Mac fallback builds | | | 9.5 | |

#### Phase 2: Backend (Claude 105 h, owner 22 h; about 315 human hours)

| Item | Human h | Claude h | Owner h | Reasoning |
|---|---|---|---|---|
| AppHost (Azurite, Functions, mock, dev tunnel), ServiceDefaults, Backend.Core, Functions host with ASP.NET Core integration and OTel mode | 12 | 4.0 | 0 | Builds on spike A |
| Table data layer: 7 tables, key schemes, entity-group upserts, Brotli R/P, content hashes, retention class | 22 | 7.0 | 0 | |
| GitHub App plumbing: Key Vault RS256 signer and PEM, down-scoped 55-minute token cache, egress allowlist, Retry-After and ETags | 18 | 5.5 | 0 | |
| Auth: exchange with PKCE required, form POST, error mapping, 10/min/IP; gts_ sessions; re-mint; logout revoke (BI, AD) | 16 | 5.0 | 0 | |
| Installation sync and ACL (verifiedAt within 7 days) | 12 | 4.0 | 0 | |
| Webhooks: constant-time HMAC, delivery dedupe, the three event types into collect or purge queues | 12 | 4.0 | 0 | |
| **Collector:** hourly hashed scheduler with self-healing; queue worker (GraphQL nodes(), views and clones per day, conditional referrers and paths, ETags, concurrency caps, 1,000-repo cap, gap markers, heartbeat, poison handling) | 40 | 12.0 | 0 | The product's core |
| Reconcile (installation diff, webhook redelivery, inactivity pause) and Maintenance | 14 | 4.5 | 0 | |
| me, settings, export, DELETE me (revoke grant, uninstall), PurgeWorker, Audit | 16 | 5.0 | 0 | |
| POST /v1/sync (summary, teaser, events) and base history read | 12 | 4.0 | 0 | |
| Weekly incremental and monthly full backups to Cool, restore script and one drill | 12 | 4.0 | 0.5 | |
| Middleware: session auth, rate limits, ProblemDetails, redaction, token scrubber, URL templating | 10 | 3.0 | 0 | |
| OTel to the Azure Monitor exporter, sampling, custom metrics, /health and /health/collector (BI, GA) | 12 | 4.0 | 0 | |
| GitHub mock, Aspire.Hosting.Testing suite, Core unit tests | 30 | 9.0 | 0 | |
| Bicep: Flex, storage with lifecycle and locks, Key Vault non-exportable key, UAMI and RBAC, Log Analytics cap and App Insights, alerts, budget; 4 parameter sets (BI, GA) | 20 | 7.0 | 2.0 | Owner approves the first deploy and DNS |
| backend.yml (PR what-if, staging on main, prod on a tag after approval) and the health cron with keepalive | 12 | 4.0 | 2.0 | Owner sets OIDC subjects and environments |
| Pages site: landing and install, privacy, terms, delete-account, setup bounce, allowlist page, config.json | 16 | 5.0 | 2.0 | Owner approves the copy |
| Staging soak with the staging App on the owner's repos, plus fixes | 12 | 5.0 | 2.0 | At least 1 week elapsed |
| 10k-user load test against the mock (MVP credit) | 6 | 3.0 | 0.5 | |
| Security review pass and fixes | 6 | 2.5 | 1.0 | |
| **Prod go-live**: Key Vault key import, prod App webhooks, api.<domain>; **banking starts** | 6 | 3.0 | 3.0 | Takes the 30-day gate off the critical path |
| Contingency (~10%) for the new SDK and Aspire integration | | 6.0 | 1.0 | |
| PR reviews (~12) and steering | | | 8.0 | |

#### Phase 3: Release 3.0 (Claude 75 h, owner 38 h; about 185 human hours)

| Item | Human h | Claude h | Owner h | Reasoning |
|---|---|---|---|---|
| Startup independence: compiled defaults, config.json background refresh, MSBuild library list, client-side About stats (all four reports) | 12 | 4.0 | 0 | |
| GitHub App sign-in (PKCE, state), install flow, installations/sync, 'ask org owner'; remove the org-scope logout and EnableOrganizations | 24 | 8.0 | 2.5 | OAuth round trips on devices |
| databaseId everywhere; fix name-based dedupe and the .Single crashes; repo listing via installations (AD) | 14 | 4.5 | 0 | |
| Local SQLite fixes and a schema migration (AD) | 12 | 4.0 | 0.5 | |
| Stars via /stargazers/count and /history; retire per-star paging | 10 | 3.5 | 0 | |
| Popular paths and correct 14-day uniques (AD) | 13 | 4.5 | 0 | |
| Consent screen, toggles, 'N days saved' teaser and blur, Delete account, /v1/sync client and events | 24 | 8.0 | 1.5 | UX review |
| Sentry 7 scrubbing at 5% with opt-out; traceparent sent only to the API | 6 | 2.0 | 0 | |
| 12-language strings; CFBundleLocalizations nb and tr (AD, GA) | 8 | 3.0 | 1.0 | Machine translation |
| Demo mode for the new features; app tests | 14 | 5.0 | 0 | |
| Privacy.md, privacy labels, Data safety, age rating (Claude drafts, owner enters) | 6 | 3.0 | 3.0 | Counsel time not counted |
| Listing copy, screenshot automation; owner captures 6.9-inch, 13-inch and Play screenshots | 8 | 3.0 | 5.0 | |
| Release signing; TestFlight and Play internal builds | 4 | 2.0 | 2.0 | |
| **Beta and device QA regression, plus bug-fix budget** | 24 | 12.0 | 10.0 | Largest owner item |
| Submission, review notes, one rejection cycle; delete the old OAuth App and Azure DevOps | 6 | 2.3 | 3.5 | |
| Contingency (~8%) | | 6.0 | 1.5 | |
| PR reviews and steering | | | 7.5 | |

#### Phase 4: Release 3.1 Premium (Claude 107 h, owner 46 h; about 290 human hours)

| Item | Human h | Claude h | Owner h | Reasoning |
|---|---|---|---|---|
| Apple: JWS verification (pinned G3), App Store Server API (statuses, Set App Account Token), Server Notifications v2 | 24 | 8.0 | 0 | |
| Google: Pub/Sub OIDC, subscriptionsv2, linkedPurchaseToken, acknowledge | 20 | 6.5 | 2.0 | Owner sets up the GCP project and service account |
| HMAC binding, StoreLinks 409 and Move, entitlement state machine, daily reconcile | 20 | 6.5 | 0 | |
| Gated history endpoints and the cadence switch | 16 | 5.0 | 0 | |
| Backend tests (fixture JWS, mocked Play) and sandbox wiring to staging | 18 | 6.0 | 1.0 | |
| Plugin.InAppBilling IBillingService, restore, manage, binding tokens | 24 | 8.0 | 3.0 | Package is net10-only |
| EntitlementService; history sync, cache and merge; HistorySeries aggregation | 40 | 12.0 | 0 | |
| Trends Premium UI (range picker, zoom and pan, locked state) | 24 | 8.0 | 2.0 | |
| Referrer and path history; 30/90/365-day totals and sorting; badges | 22 | 7.0 | 0.5 | |
| Paywall and Settings row (3.1.2 disclosures, Founding offer) | 16 | 5.0 | 1.5 | |
| CSV, demo year of history, day-15 notification, strings, app tests | 36 | 12.5 | 1.5 | |
| App Store Connect and Play products, trial, offer codes, testers | 8 | 2.0 | 7.0 | Owner consoles |
| Terms/EULA and final pricing | 4 | 2.0 | 2.0 | |
| **Sandbox end-to-end matrix** (renew, cancel, refund, grace, restore, account switch, Android upgrade) | 12 | 4.0 | 6.0 | Physical devices |
| Beta, QA, submission (one IAP rejection), release, Founding codes | 14 | 7.0 | 8.0 | |
| Contingency (~8%) | | 7.0 | 2.0 | |
| PR reviews and steering | | | 10.0 | |

#### Phase 5: Operations for 12 weeks after 3.1 (Claude 40 h, owner 21 h)

| Item | Claude h | Owner h |
|---|---|---|
| Weekly triage: health, Sentry, cost, gaps | 12 | 6 |
| Dependabot and servicing | 8 | 3 |
| Two hotfix releases | 12 | 7 |
| Restore drill and forecast recalibration | 3 | 1 |
| HTTPS Universal Link / App Link callback | 5 | 2 |
| Steering | | 2 |

### 4. Critical path and milestones

The chain runs from Phase 0 accounts and spikes through the app port and backend (in parallel), 3.0 integration, beta and App Review, then the Premium build, sandbox testing and IAP review.

- **History banking starts at Phase 2 go-live:** about week 6 at 15 h/wk, or week 13 at 5 h/wk. The 30-days-banked gate is therefore never on the critical path.
- **At 15 h/wk:**
  - Claude throughput or the plan cap binds in weeks 2–6.
  - Owner device QA and review queues bind after that.
  - 3.0 ships around week 9 (range 8–11); 3.1 around week 15 (range 13–18).
- **At 5 h/wk:**
  - Owner hours bind the whole way.
  - 3.0 ships around week 23 (range 18–28); 3.1 around week 33 (range 27–40).
- **The architecture's target of "3.0 in 6–8 weeks"** needs about 20 owner hours a week, or deferring popular paths, star history and teaser polish to 3.0.1.
- **Single points of failure:**
  - the owner's Mac with Xcode 27.2;
  - a public repo, for free macOS runners;
  - the Play upload key;
  - Apple banking.

### 5. Weekly token profile at 15 h/wk owner time

| Weeks | Claude agent-h per week | Tokens per week, central (range) | API-equivalent per week |
|---|---|---|---|
| 1 (Phase 0) | 16 | 67M | $73 |
| 2–6 (Phases 1 and 2) | 33, peak 42 | 140M, peak 175M (125–230M) | $150, peak $190 |
| 7–9 (Phase 3) | 21 | 90M | $98 |
| 10–15 (Phase 4) | 18, peak 26 | 75M, peak 110M | $82 |
| 16–27 (ops) | 3.3 | 14M | $15 |

- Build-period average (weeks 1–15): about 102M tokens a week. Peak is about 1.7x that average.
- At 5 h/wk the build period averages about 46M tokens a week and peaks at about 76M.
- **Fit with a Claude plan.** Ultra's weekly cap isn't published in tokens, so measure it.
  1. Read the /usage weekly % before and after the day-1 spikes, which are a known number of agent-hours.
  2. If the cap binds in weeks 2–6, run the app and backend sessions one after the other (+1–2 weeks at 15 h/wk), or use usage credits at about $4.60 per agent-hour.
- On API-equivalent alone, the whole project costs about $1.85k central, against about $1.2–1.6k for 6–8 months of Ultra.

### 6. Owner-hour hotspots

| Area | Owner hours |
|---|---|
| Device QA and sandbox testing | ~30 |
| PR reviews and steering | ~40 |
| Store consoles and paperwork | ~25 |
| Screenshots | ~5 |
| Visual and design checks | ~10 |
| Account and key setup | ~15 |

Ways to save time:
- Lighter PR review, relying on CI plus Claude's review subagents: -10–15 h.
- Testers recruited for beta: -3–5 h.

### 7. Key assumptions and risks

The full lists are in the structured fields. The ones that move the numbers most:
- **MAUI 11 / .NET 11 is 5 days old**, and several key packages ship net10-only. Breakage adds 15–40 Claude hours, or forces a fall back to .NET 10.
- **The Shiny 6 migration** could double.
- **The iOS compile loop** depends on free macOS runners. If they aren't available: +10–20 owner hours.
- **The container** has blocked SDK hosts and no KVM.
- **Each store rejection** costs 3–7 days.
- **The tokens-per-hour figure** is ±50%.

## Appendix B: top-down report

## Top-down estimate: GitTrends relaunch (.NET 11, Flex backend, Premium)

**Method:** top-down, by analogy. It is independent of any bottom-up list and uses the same phase structure so the two can be reconciled. Date: 2026-11-15.

### 1. Headline

| | Range | Central |
|---|---|---|
| Claude agent-hours (summed sessions, including review subagents) | 148–324 | ~235 |
| Owner hands-on hours | 100–200 | ~150 |
| Tokens processed (including cache reads) | 0.37–2.27 B | ~1.05 B |
| API-equivalent cost at Opus 5.5 rates | $315–2,950 | ~$1,100 |
| Senior-human equivalent | 525–955 h (13–24 person-weeks) | ~720 h |

**Calendar from a 2026-11-16 start:**

| Milestone | Owner 15 h/week | Owner 5 h/week |
|---|---|---|
| 3.0 free relaunch live | week 7–12 (early Jan – mid Feb 2027; holidays likely +1 week) | week 12–23 (mid Feb – late Apr 2027) |
| 3.1 Premium live | week 12–19 (mid Feb – late Mar 2027) | week 21–40 (mid Apr – late Aug 2027) |
| Post-launch stabilised | ~week 20–27 | ~week 30–48 |

The architecture targets 3.0 in 6–8 weeks and 3.1 about 5–6 weeks after 3.0. Those dates only hold at 15 h/week, and only on the optimistic end.

### 2. Analogies used

| Analogy | Evidence | What it implies here |
|---|---|---|
| This repo's Xamarin.Forms to MAUI port, PR #783 (`8d74e686`) | 821 files, +25,132/-23,944 lines, 234 squashed sub-commits. PR numbering shows it opened no earlier than about May 2024; merged 2024-10-27. That is at most about 5 months of part-time work by an expert owner. The .NET 9 bump (#801) followed 6 weeks later, then about 10 idle months. The Oct–Nov 2025 store-prep commits never produced a release (3.0.0 build 66 never tagged). | The 9-to-11 port touches about 15–20% of the files the Xamarin port did, so the port alone is about 40–90 senior hours. **The finished code migration stalled at the store last mile for about a year.** That is the main schedule risk. |
| Typical MAUI major-version bump on an app of about 15k lines | 1–3 engineer-weeks each, dominated by third-party libraries and platform regressions (judgment) | Two majors, plus CoreCLR-only, UIScene, Compatibility removal and 5 library replacements: about 3–5 senior weeks for the port, plus 3.0 client features |
| Greenfield small subscription SaaS backend | 6–10 senior weeks for auth, collector, two-store entitlements, IaC, CI and observability. Two-store server verification alone is 2–4 weeks; RevenueCat exists because of that (judgment) | 3.0 backend: 120–240 h. Premium entitlements: about 60–110 h |
| Store cycles | Apple about 1–3 days per submission, Play updates hours to about 7 days. First subscriptions typically draw 1 or more rejections. Apple slows down around Dec 23–27 (judgment) | Fixed waits of 1–2 weeks per release, plus 3–10 days per rejection. These don't compress |

### 3. Claude compression versus a senior engineer

| Work type | Speed-up | Why |
|---|---|---|
| Porting and API migration with compiler feedback (shared code, Android) | 3–5x | The container builds net11 and Android, runs tests, and can work in parallel |
| Greenfield backend (Functions, Aspire, Azurite, mock GitHub) | 3–4x | Full local loop with Aspire.Hosting.Testing. Decisions are already made |
| MAUI UI (paywall, history charts, consent) | 1.5–2.5x | Code is fast; visual correctness needs owner screenshots or devices |
| iOS-only code (UIScene, Shell renderer, AppDelegate) | 1.2–2x | No Xcode in the container; each macOS-runner round trip takes 25–45 minutes |
| Device QA, sandbox purchases, consoles, signing, store review | 1x | Owner-bound wall-clock time |

### 4. Phases

| Phase | Senior-human baseline | Claude agent-hours (central) | Owner hours (central) | Calendar at 15 h/week | Calendar at 5 h/week | Tokens (M) | API-equivalent |
|---|---|---|---|---|---|---|---|
| 0 Stabilize & secure | 15–25 h | 6–14 (10) | 8–14 (11) | 1–2 weeks | 2–3 weeks | 15–98 | $13–127 |
| 1 .NET 11 port (app, 3.0 client scope) | 150–260 h | 45–85 (65) | 20–40 (30) | 4–6 weeks, alongside Phase 2 | 7–13 weeks, shares owner time with Phase 2 | 113–595 | $96–774 |
| 2 Aspire backend (Flex, 3.0 scope) | 120–240 h | 30–70 (50) | 12–25 (18) | 3–5 weeks, alongside Phase 1 | (as above) | 75–490 | $64–637 |
| 3 Premium (3.1) | 150–260 h | 40–85 (62) | 25–45 (35) | 3–5 weeks after 3.0 | 7–14 weeks | 100–595 | $85–774 |
| 4 Store relaunch (3.0, then 3.1) | 50–90 h | 12–30 (21) | 20–40 (30) | 2–4 weeks + 1–2 weeks | 3–7 weeks + 2–3 weeks | 30–210 | $26–273 |
| 5 Post-launch (8–12 weeks) | 40–80 h | 15–40 (27) | 15–35 (25) | 8–12 weeks, overlapping | 8–12 weeks, overlapping | 38–280 | $32–364 |
| **Total** | **525–955 h** | **148–324 (~235)** | **100–200 (~150)** | | | **370–2,268** | **$315–2,950** |

**Where the owner's hours go:**

| Activity | Hours |
|---|---|
| Accounts and consoles | 25–40 |
| Device QA and sandbox testing | 30–55 |
| Code review | 25–50 |
| Decisions and legal | 10–20 |
| Mac, toolchain and signing | 8–15 |
| Post-launch support | 15–35 |

**Phase notes**

- **Phase 0.**
  - Owner: private security actions for old builds; revoke the old OAuth App tokens and secret, the test PATs and the Syncfusion key; create the production subscription with budget and locks; register the GitHub org and 3 Apps; check the Play upload key and build numbers; install Xcode 27.2; fast-forward master to `main`.
  - Claude: legacy-guard Bicep; remove dead code; Actions skeleton.
  - Day-1 spikes: Functions SDK 1.1.0 under Aspire plus a Flex deploy; a MAUI 11 Android build; an iOS build on a macOS runner; InAppBilling and Toolkit smoke tests.
- **Phase 1.**
  - Platform: SDK and packages to 11; 47 obsolete calls (CS0618 is an error); UIScene; Shell renderer; AppStore configuration, Android ID, privacy manifest.
  - Libraries: Sharpnado, Shiny 3 to 6, StoreReview, Syncfusion Toolkit, SkiaSharp, sqlite, Refit, CommunityToolkit, Sentry.
  - Features: startup without the backend; GitHub App sign-in with PKCE and install flow; databaseId; popular paths; star endpoints; consent and teaser; delete account.
  - Tests and CI: rework 80–100 tests; mobile CI; translations.
- **Phase 2.**
  - AppHost and ServiceDefaults; auth and sessions; me, sync and delete endpoints.
  - Webhooks; collector using installation tokens signed in Key Vault; reconcile; backups and purge.
  - OTel; Bicep for staging, production and legacy; Actions over OIDC; integration tests; health cron.
  - GitHub Pages site.
  - **It must be live in production before the 3.0 beta,** so banking starts early.
- **Phase 3.**
  - Backend: Apple JWS, Status API and App Store Server Notifications v2; Google RTDN, subscriptionsv2 and acknowledgement; binding and StoreLinks; reconcile; gated history endpoints.
  - App: purchase flow and paywall; history UI; referrer/path history; CSV; demo mode with synthetic history; Founding Member offers; day-15 notification.
- **Phase 4.**
  - Signing and CI secrets; betas; privacy labels, Data safety, age rating; screenshots; review notes.
  - Submissions with 1–2 expected rejections; staged rollout.
- **Phase 5.** 2–5 hotfixes, collector reliability, Dependabot, funnel analytics, community launch, switching free collection to weekly.

### 5. Critical path

1. **Phase 0.**
2. **Phases 1 and 2 in parallel.** iOS loops run through macOS runners and the owner's devices. The backend reaches production.
3. **Phase 4 for 3.0.** Beta, review and rejections.
4. **Phase 3.** Starts during the 3.0 beta. Sandbox purchases and store products gate the release.
5. **Phase 4 for 3.1.**

**The binding constraint is owner hours, not Claude.** The at-least-30-days-banked gate costs nothing extra if the production collector goes live during the 3.0 beta. Phase 5 support competes with Phase 3 for owner time, which is why 3.1 slips to week 21–40 at 5 h/week.

### 6. Tokens and dollars

**Rate per agent-hour.**
- Calibration: the discovery run made 615 tool calls in about 7.7 agent-hours, about 80 requests per agent-hour.
- Its reported 1.92M tokens is read as the non-cache 5–10% of the total, which gives about 19–38M processed, or about 2.5–5M per agent-hour for research agents.
- Coding sessions carry larger contexts (source files, build logs), so I use **2.5–7M per agent-hour**.

**Blended price.**

| Mix | Cache reads at $0.20/M | Fresh input / cache writes at ~$4.5/M | Output at $20/M | Total per M tokens |
|---|---|---|---|---|
| Low | 92% → $0.184 | 6% → $0.27 | 2% → $0.40 | **$0.85** |
| High | 85% → $0.17 | 12% → $0.54 | 3% → $0.60 | **$1.31** |

**Cross-checks.**
- Requests: about 235 agent-hours × 80 requests × 45–60k context = 0.85–1.1B.
- Per file: 450–650 files touched × 0.2–0.7M per touch cycle × 1.5–2.5 for rework and review × about 1.8 for build, test and debug loops = 0.25–2.0B.
- Both agree with the range of **0.37–2.27B (central about 1.05B, about $1,100)**.

**Weekly profile at 15 h/week.**

| Weeks | Phase | Tokens/week |
|---|---|---|
| 1–2 | Phase 0 and spikes | 15–70M |
| 2–7 (peak) | Phases 1 and 2 | **60–270M** (central about 110–150M, about $115–160) |
| 7–10 | 3.0 store work | 30–150M |
| 10–15 | Phase 3 | 25–150M |
| After launch | Phase 5 | 5–40M |

- **Average:** 20–125M per week (central about 55M). Peak to average is about 2.5–3x.
- **At 5 h/week:** the same total spreads over 30–48 weeks, about 25–35M per week on average.
- **Plan fit:** plans don't publish token limits. Measure the week 1 spike and one parallel week with `/usage` before trusting the 15 h/week calendar.
- **Cost comparison:** an Ultra seat ($200/month) for 4–9 months costs about $800–1,800, comparable to the API-equivalent central figure.

### 7. Key assumptions

- **Scope:** v1 = Phase 0 + 3.0 + 3.1. Excluded: Pro, widgets, web dashboard, Mac Catalyst, Appium port (+8–15 agent-hours). UI tests are deleted.
- **Owner:** an expert MAUI developer with a Mac (macOS 26.6+, Xcode 27.2) and physical devices. Store accounts are active and the Play upload key is recoverable.
- **Runners:** the repo is public, so macOS runners are free. Otherwise iOS loops go through the owner's Mac.
- **Container:** builds the backend and Android and runs Aspire and tests. It probably has no Android emulator and has no Xcode.
- **Claude capacity:** 25–50 agent-hours a week.
- **Translations:** machine translation by Claude with light review.

### 8. Risks to the estimate (largest first)

1. **Historical stall at store release.** The 2025 MAUI 3.0 was never released. This is the main risk to the 5 h/week case.
2. **Owner availability and review depth.** In-depth review of auth, token and purchase code could add 25–50 h.
3. **New .NET 11 tooling.**
   - Functions SDK and Aspire integration: +5–15 agent-hours or a net10 fallback.
   - Net10-only libraries on CoreCLR: IAP fallback +10–25 agent-hours; Shiny 6 +5–15.
   - Shell renderer: +5–20.
4. **Store rejections and account surprises.** +3–10 days per rejection; a Play key reset takes days to weeks.
5. **Token accounting.** About ±2x, from the unclear calibration basis.
6. **Plan weekly caps** may throttle the week 2–7 peak by 1–3 weeks.
7. **Legal and counsel timing:** EEA consent, Terms/EULA, GitHub's reply on AUP §6.
8. **Scope creep** into Pro features: +10–60 agent-hours each.
