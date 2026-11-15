# GitTrends relaunch: fact-check

Part of the [relaunch plan](README.md).

Five verifiers were asked to *refute* the key facts behind the plan. They checked primary sources on 2026-11-15: Microsoft and GitHub documentation source files, the GitHub REST OpenAPI description, Microsoft's Product Terms, Apple developer pages, NuGet packages, the Aspire source at v13.6.5, the MCR tag list, and this repo's git history.

Some hosts were blocked from the research environment, including learn.microsoft.com, azure.microsoft.com and github.blog. A few prices and dates therefore come from search snippets. They are marked *medium confidence* and are on the [verify-before-building list](README.md#14-verify-before-building).

A few findings are tracked privately.

## Corrections that changed the plan

- `aspire deploy` to ACA can use GHCR: refuted. Aspire 13.6.5's ACA environment accepts only Azure Container Registry: it creates ACR Basic by default and throws on any other registry. The $0 GHCR option in arch-trust and arch-growth doesn't exist under `aspire deploy`.
- `aspire deploy` of a .NET 11 Functions project to ACA is broken today. The default base image tag 4-dotnet-isolated11.0 is missing from MCR, and the chiseled variant has neither the .NET 11 runtime nor a start script (Azure/azure-functions-dotnet-worker #3533 and #3534, still open). Flex code deploy of .NET 11 is GA; the rollout completed on 2026-11-11.
- The managed Aspire Dashboard component in ACA is on by default (except in Express mode). Turn it off with .WithDashboard(false). Its price is unpublished, and it may be billed like a fixed replica.
- Azure.Functions.Sdk is at 1.1.0 (2026-11-14); 1.0.2 shipped on 2026-11-09. The old Worker.Sdk 2.1.0 only warns on .NET 11; it doesn't block the build. No source confirms that AddAzureFunctionsProject works with the new SDK.
- Flex Consumption, per current docs:
  - The maximum instance count can be as low as 1, and it applies per function group (the HTTP group, each queue function, each timer function).
  - Minimum billable time is 1,000 ms, rounded up in 100 ms steps after that.
  - The host must initialize within 30 s.
  - Site-scoped managed certificates are supported.
  - Rolling updates replace deployment slots, which aren't available.
- The MVP benefit is the $150/month Visual Studio Enterprise NFR credit, renewed only while the MVP award lasts.
  - The Product Terms forbid production use.
  - Microsoft may suspend instances that run more than 120 hours continuously, or that it finds in production.
  - The credit doesn't cover Application Insights.
  - Quotas are lower than on a paid subscription.
- The Functions/Flex free grant (100k GB-s, 250k executions) applies only to paid consumption subscriptions, so it doesn't apply on the Visual Studio credit subscription.
- No MVP-specific Azure sponsorship that allows production could be verified, and the open-source Azure credits program is closed. Neither is in the budget.
- Microsoft for Startups since 2026-10-30: $200 for 90 days, then $4,800 for 180 days after business verification, which requires a registered legal entity. That corrects arch-growth's 'about $1k–5k'.
- Azure SQL free tier: auto-pause is fixed at 15 minutes and there is no SLA. This doesn't matter here because the design uses no SQL.
- Table ($0.045/GB), Blob Cold ($0.0036/GB) and Log Analytics ($2.30/GB in East US) prices come from secondary or regional sources. Confirm them in the pricing calculator.
- GitHub requires client_secret for the code exchange even when PKCE is used. Refreshing a token also needs the secret unless the token came from device flow.
- GitHub advises against enabling device flow outside CLI, IoT or headless clients, because of phishing. The device-flow fallback proposed by arch-frugal and arch-growth is dropped.
- 'Request user authorization during installation' always redirects to the first callback URL, disables the Setup URL and carries no PKCE challenge. It stays off.
- A GitHub App user token reaches only repos where the App is installed, so every user, free ones included, must install it.
- Repo admins can't self-install an app that requests Repository administration on org repos. An org owner must install it, and owners can also turn off install requests.
- /stargazers/history counts stars created per week. It doesn't subtract removed stars, its boundaries aren't aligned to UTC, and it allows per_page up to 30 and page up to 100. Take totals from /stargazers/count or GraphQL stargazerCount.
- For GitHub Apps, listing stargazers requires Contents: write, so the server never fetches the stargazer list.
- Since 2026-04-27, installation tokens are rolling out in a variable-length format, ghs_APPID_JWT.
- Traffic for private repos may require a GitHub Pro or Team plan on the owner. Don't promise private-repo history for repos owned by GitHub Free accounts until tested.
- The current day is a partial bucket, and views and clones update hourly. Every poll upserts all 14 days.
- Administration: read also unlocks 44 other read endpoints, such as branch protection, deploy keys, runners and invitations. Consent copy must say GitTrends calls only the traffic and metadata routes, and an egress allowlist enforces that.
- GitHub's terms don't ban a paid app built on a user's own data, but AUP §6 and the ToS 'resale' wording are broad. Ask GitHub for written comfort. This is not legal advice.
- Apple's US link-out fee is 0% today. Apple's remand proposal is tiered: 15% for standard apps and first-year subscriptions, 10% for renewals, 5% for Small Business Program members. The Supreme Court review covers only the contempt question.
- Google Play subscriptions since 2026-06-30 in the US, EEA and UK: a 10% service fee plus a 5% billing fee, still 15% in total.
- RevenueCat charges 1% of all tracked revenue in any month above $2,500, including the first $2,500.
- Conversion benchmarks: the iOS 2.6% and Android 0.9% figures are medians across all apps, not freemium apps, so freemium Android is likely below 0.9%. The 42.5% figure is trial-to-paid for 17–32-day trials, and the median trial-to-paid rate is about 32.5%. Forecasts use about 2% on iOS and under 1% on Android.
- Competitors: Repohistory charges $90/yr or $9/mo, offers 1 repo free, and is AGPL and self-hostable. RepoEasy offers 3 repos free and Pro at €1.50/mo or €12/yr.
- Personal Google Play accounts created before 2023-11-13 are exempt from the 12-tester, 14-day closed-test rule. The inactivity rules still apply.
- AppStore build configuration: the SDK defines APPSTORE (uppercase), so every #if AppStore block is dead code. Sentry 5.16.2 throws on a null DSN, so the AppStore build likely crashes at launch, and it is also debuggable.
- Startup blocks only when the caches are empty, which is the state of every fresh install. Statistics initialization blocks in every configuration.
- Backend-dependent tests: 79 of 397 test cases (about 20%), or 77 of 186 test methods (about 41%), not '~25%'. Budget for reworking 80–100 tests.
- Without a UIApplicationSceneManifest, building with .NET 11 against SDK 27 fails with error MT7199. It is a build failure, not just a launch crash.
- Syncfusion.Maui.Toolkit 1.0.12 and Plugin.InAppBilling 11.0.1 ship net10 builds only, with no net11 target. Plugin.InAppBilling's Play Billing Library 9.1 is accepted until August 2028.
- MAUI 11 removes Mono: RunAOTCompilation=false now fails with XA1044, and the Compatibility package is gone.
- Notification Hubs: the Free tier allows 500 devices with no SLA and isn't for production; Basic is $10 per namespace per month. The design avoids it.

## Claim-by-claim results

### Azure and the MVP credit

**1. The Microsoft MVP Azure benefit is a Visual Studio Enterprise (NFR) subscription with a $150/month Azure credit, renewable monthly.**  
*Verdict: confirmed.*

- What's true: Same. The eligibility table lists 'Visual Studio Enterprise - NFR*' at '$150 monthly credit', Renewable: Yes. The footnote says NFR 'Includes: Not for Resale (NFR), Most Valuable Professional (MVP), Regional Director (RD)…' and excludes MAICPP. The credit runs on an 'individual Azure credit subscription' activated through my.visualstudio.com. It lapses if the Visual Studio subscription (that is, the MVP award) lapses.
- Plan impact: None to the numbers. Budget for at most $150/month of dev/test capacity, available only while the MVP award is renewed each year.
- Evidence: raw.githubusercontent.com/MicrosoftDocs/visualstudio-docs/main/subscriptions/vs-azure-eligibility.md (ms.date 2026-04-17). subscriptions/azure-access.md (ms.date 2024-09-16): credits stop when the subscription expires. Saved copy: (research workspace) factcheck-azure/vs-azure-eligibility.md

**2. Visual Studio subscriber credits are for individual dev/test only; running production on them violates the offer terms. With no payment method, Azure services stop when the monthly credit is used up.**  
*Verdict: confirmed.*

- What's true: Same, with stronger terms than the reports said:
- Product Terms: 'Any online service made available with Customer's Visual Studio Subscription may not be used in a Production Environment.'
- Subscriber FAQ: 'specifically for individual dev/test usage only. To run production workloads, you need to upgrade to a paid Azure subscription such as pay-as-you-go'.
- FAQ: Microsoft 'reserve[s] the right to suspend any instance (VM or cloud service) that runs continuously for more than 120 hours or if we determine that the instance is being used for production'. No financially backed SLA; best-effort capacity.
- FAQ: the credit does NOT apply to Application Insights, support plans and some other services (FAQ dated 2024-09-26).
- When the credit runs out with no card on file, services are disabled for the rest of the billing period. VMs are deallocated, storage becomes read-only, and service resumes automatically next period.
- Removing the spending limit needs a payment method and does not change the dev/test restriction.
- Plan impact: Production must run on a pay-as-you-go subscription. Use the MVP credit for dev, staging and load tests only. Don't put workspace App Insights or OpenTelemetry export on the credit subscription and expect it to be covered; check the meter or keep telemetry in the pay-as-you-go subscription. Also expect lower quotas on the credit subscription.
- Evidence: microsoft.com/licensing/terms/en-US/productoffering/VisualStudioSubscriptions/EES and /OL (current Product Terms, Visual Studio 2026). visualstudio-docs subscriptions/faq/subscriber/azure/includes/credits-for-production.md and credit-limitations.md (ms.date 2024-09-26). vs-azure-eligibility.md (2026-04-17): 'If no payment method is on file, Azure usage automatically stops'. azure-docs devtest/offer/quickstart-individual-credit.md (2026-06-30): 'intended for development and testing workloads only'. azure-docs cost-management-billing/manage/spending-limit.md (2026-04-29).

**3. There is NO separate MVP-specific Azure sponsorship (beyond the $150 VS credit) available in 2026 that permits production use.**  
*Verdict: unverifiable.*

- What's true: Neither proven nor disproven. No official 2026 source describes an MVP-specific sponsorship. There are anecdotal signs that one existed:
- A Microsoft Q&A question titled 'MVP Azure Sponsorship' (posted 2025-05-20): the poster holds one and can't link it to a subscription.
- A 2024 post on X: '$150/month of Azure credits (Extendible to $1000/month)'.
- A personal MVP blog: 'Azure MVPs… get 1000$ worth of free monthly Azure credit'.
- The MVP FAQ lists 'Azure Credits' with no amount.

Other programs found:
- Azure credits for open-source projects: the official page says 'The application form is not currently open'. A maintainer's guide says Azure Sponsored Subscriptions for open-source maintainers were discontinued 2025-09-01.
- Sponsorship offers (MS-AZR-0036P) are invite-only and carry no dev/test restriction.
- The Microsoft AI Cloud Partner Program credit change of 2026-02-13 does not apply to MVPs.
- Plan impact: Don't base the budget on an MVP sponsorship. The owner should check the MVP portal benefits page (and ask their MVP community program manager) for an 'Azure Sponsorship' option. If one exists, it would likely allow production, unlike the Visual Studio credit, and could cover the small pay-as-you-go bill.
- Evidence: learn.microsoft.com/en-us/answers/questions/2277160/mvp-azure-sponsorship (2025-05-20, via search snippet). x.com/FrancescoCiull4/status/1843251373434900668 (about 2024, via search). lovelacecoding.hashnode.dev/the-microsoft-mvp-mystery (undated, via search). mvp.microsoft.com/en-US/faq?section=mvp (via search; site blocked here). opensource.microsoft.com/azure-credits (via search: form not open). eliostruyf.com 'Who's funding open-source in 2025' (via search). vs-azure-eligibility.md footnote excludes MAICPP.

**4. Azure Functions Flex Consumption free grant = 100,000 GB-s + 250,000 executions per subscription per month (on-demand only); on-demand rate ~$0.000026/GB-s.**  
*Verdict: confirmed.*

- What's true: Same.
- The pricing page says the free grant of 250,000 executions and 100,000 GB-s is 'per month per subscription in pay-as-you-go on-demand pricing across all function apps in that subscription'.
- Footnote: grants apply 'to paid, consumption subscriptions only'. The function app's default storage account is not included in the grant.
- Always ready billing has no free grants.
- On-demand rates: $0.000026/GB-s and $0.40 per million executions.
- The Microsoft docs give no numbers themselves and defer to the pricing page.
- Plan impact: None. The Flex Consumption + Table Storage model stands, as long as it runs on a paid pay-as-you-go subscription (see claim 6).
- Evidence: azure-docs includes/functions-flex-consumption-billing-table.md (ms.date 2024-11-05): 'minus a free grant…', 'In always ready billing, there are no free grants'. azure-docs azure-functions/functions-consumption-costs.md (2025-02-10) uses '$0.000026 GB-s' and '$0.40 per million'. azure.microsoft.com/pricing/details/functions/ (via search snippets, Nov 2026). Third-party Retail Prices API snapshot elecnix/infra-cost-model seed_prices.json (checked 2026-10-02, meters effective 2024-12-01) shows the same numbers.

**5. Azure Container Apps consumption free grant = 180,000 vCPU-s + 360,000 GiB-s + 2M requests per subscription per month; scale-to-zero costs nothing; jobs bill at active rate.**  
*Verdict: confirmed.*

- What's true: Same. Details from the billing doc:
- 'The following resources are free during each calendar month, per subscription: The first 180,000 vCPU-seconds, The first 360,000 GiB-seconds, The first 2 million HTTP requests'.
- 'When a revision is scaled to zero replicas, no resource consumption charges are incurred.'
- Jobs: 'charged the active rate. Idle charges don't apply to jobs.'
- Only requests from outside the environment are billable; health probes are not.
- Private endpoints and planned maintenance add a Dedicated plan management charge.
- The managed OpenTelemetry agent 'runs at no extra compute cost'.
- Plan impact: None to the model. Things that still cost money: Log Analytics ingestion from the environment, ACR (or use GHCR) and storage. Avoid private endpoints, which bring a management fee.
- Evidence: raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/container-apps/billing.md (ms.date 2025-12-09). Saved copy in (research workspace) factcheck-azure/billing.md

**6. Whether those free grants apply on a Visual Studio credit subscription (pricing footnote says 'paid, consumption subscriptions only'?).**  
*Verdict: partially_correct.*

- What's true: The footnote is real for Functions (Consumption and Flex on-demand): 'Free grants apply to paid, consumption subscriptions only.' A 2022 Microsoft Q&A moderator answer says the grants are 'only provided for the paid/consumption azure subscription (pay as you go) and not to the free trial subscription/VS code subscription'. That is unofficial and old, but it points to no Functions grant on the Visual Studio credit subscription.

Other services differ:
- Container Apps: the billing doc says only 'per subscription', with no paid-only wording. Unknown in practice.
- Azure SQL free tier: 'available with most Azure subscription types'; only Azure for Students Starter is excluded.
- Visual Studio credit subscriptions also have lower quotas and 'may be restricted in ways paid subscriptions aren't'.
- Plan impact: Another reason to run production on pay-as-you-go: that is where the Functions grants clearly apply. On the dev/test credit subscription, assume Functions usage is billed against the $150 from the first GB-s. At dev scale that is trivial.
- Evidence: azure.microsoft.com/pricing/details/functions/ footnote (via search snippets, Nov 2026). learn.microsoft.com/en-us/answers/questions/789037/azure-function-app-price (2022 moderator answer, via search). container-apps/billing.md (2025-12-09). sql-docs azure-sql/database/free-tier.md (ms.date 2026-10-30). visualstudio-docs faq/subscriber/azure/includes/benefit-restrictions.md (2024-09-26).

**7. Table Storage LRS ~$0.045/GB-month; Blob Cold LRS ~$0.0036/GB-month; Log Analytics Analytics-logs ingestion ~$2.30/GB after 5 GB free per billing account per month.**  
*Verdict: unverifiable.*

- What's true: All three figures agree across independent sources, but I couldn't check them against the official pages (blocked here; search snippets showed only placeholders).
- Blob Cold LRS $0.0036 (East US) matches a 2026-10-02 snapshot of the Retail Prices API.
- Table LRS $0.045/GB-month and $0.00036 per 10,000 transactions come from secondary sources, one citing the Retail Prices API as of June 2026.
- Log Analytics $2.30/GB (East US) with the first 5 GB per billing account per month free comes from secondary sources and the structure of the Azure China pricing page. The rate varies by region; one Microsoft Q&A thread quotes $2.76/GB for a different region.
- Microsoft docs (cost-logs.md, ms.date 2026-09-02) confirm that ingestion includes 31 days of retention, but give no price.
- Plan impact: Small. Storage stays at pennies whichever number is right, so the 'collect for everyone' conclusion holds. Confirm the Log Analytics rate for the chosen region in the pricing calculator, and keep sampling on, since telemetry is the item most likely to grow.
- Evidence: elecnix/infra-cost-model seed_prices.json (Blob-Cold-LRS 0.0036, effective 2023-05-01, checked 2026-10-02). Search snippets: techtarget, devops.com and lucidity.cloud for Table; monitoringcost.com and Microsoft Q&A 5917219 for Log Analytics. azure-monitor-docs logs/cost-logs.md (2026-09-02). azure.microsoft.com pricing pages blocked.

**8. Cosmos DB lifetime free tier = 1000 RU/s + 25 GB, one per subscription, not for serverless. Azure SQL Database free offer = up to 10 serverless DBs, each 100k vCore-seconds + 32 GB/month.**  
*Verdict: confirmed.*

- What's true: Same, with small corrections.

Cosmos DB:
- 1000 RU/s and 25 GB for the lifetime of the account.
- Up to one free-tier account per subscription, opted into at creation.
- 'Currently not available for serverless accounts.'

Azure SQL (now called the 'free tier', ms.date 2026-10-30):
- Per database: '100,000 vCore seconds, 32 GB of data, and 32 GB of backup storage free per month for the lifetime of your subscription'.
- 'Up to 10 free tier General Purpose databases' (serverless) per subscription.
- At the monthly limit, choose auto-pause until next month (database inaccessible) or continue with overage charges; you can't switch back to auto-pause.
- Auto-pause after 15 minutes of inactivity is FIXED and can't be changed (the reports said 'at least 15 minutes').
- No SLA; recommended 'primarily for development and proof-of-concept scenarios' (not prohibited for production).
- Available on most subscription types.
- Plan impact: Minor. If the SQL option is chosen, note that the free tier has no SLA. Keep the design where only the batch job touches SQL and the app reads pre-built Blob snapshots, because the fixed 15-minute auto-pause means any live read path burns vCore-seconds.
- Evidence: sql-docs (live branch) azure-sql/database/free-tier.md and free-tier-faq.yml (ms.date 2026-10-30). learn.microsoft.com/azure/cosmos-db/free-tier and how-pricing-works (via search snippets, Nov 2026).

**9. Notification Hubs Free = 500 devices / 1M pushes (not recommended for production); Basic ~$10/month.**  
*Verdict: confirmed.*

- What's true: Same.
- Free: 'not recommended for production apps. You get 500 devices and 1 million pushes included per subscription per month, with no service level agreement (SLA)'.
- Basic: 200,000 devices and 10M pushes; 'recommended for smaller production apps'; 99.9% SLA.
- Standard: 10M devices and 10M pushes.
- Price: Basic $10 per namespace per month; Standard $200 per namespace per month (localized pricing pages; English page showed placeholders).
- Plan impact: Free is not for production, so either pay $10/month for Basic or send through APNs and FCM directly (free). Direct sending fits the cost-cutting goal.
- Evidence: raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/notification-hubs/notification-hubs-push-notification-faq.yml (ms.date 2025-05-01). azure.microsoft.com/*/pricing/details/notification-hubs/ (localized pages via search snippets).

**10. Microsoft for Startups (Founders Hub) offers a solo developer meaningful Azure credits usable for production (amounts, eligibility, need for a legal entity).**  
*Verdict: partially_correct.*

- What's true: Amounts dropped recently and a legal entity is needed for most of the money.

For startups without an investor (Microsoft FAQ, updated 2026-10-30):
- 'If you're new to Azure, you can start with $200 of initial startup credits for 90 days, then an additional $4,800 for 180 days after business verification.'
- Before 2026-10-30 it was $1,000 for 90 days + $4,000 for 180 days.

Eligibility:
- Business verification requires that 'your startup must be a registered legal business entity'. Verification can be submitted only once.
- A Microsoft Q&A community answer says a solo founder before incorporation does not qualify for the credits.
- Higher amounts ($100k–$150k) need a referral code from a Microsoft for Startups Investor Network partner, or a progression through credit tiers.
- The offer targets startups 'new to Azure', which may count against the owner's earlier Azure use (unclear).
- The 'Visual Studio Enterprise – Microsoft for Startups' subscription has no monthly credit.

Use: I found no dev/test-only restriction; these are sponsorship credits for running the business. But they expire after about 9 months total, so they are not a lasting source.
- Plan impact: Don't count on startup credits. Without an LLC or similar, expect only $200 for 90 days. With an entity, a total of about $5,000 over about 9 months could pay for the first year of a $1–9/month production backend. Not worth forming a company for that alone, but useful if the owner forms one for Premium sales or tax reasons anyway.
- Evidence: github.com/robhunter/agentdeals/issues/3144, quoting learn.microsoft.com/en-us/startups/microsoft-for-startups/mfs-faqs (updated 2026-10-30) and the 2026-10-13 archived copy. learn.microsoft.com/en-us/azure/signups/startup-programs (via search: registered legal business entity; earlier $1,000 → $5,000). Microsoft Q&A answers via search. vs-azure-eligibility.md (Microsoft for Startups: 'Not available').

### GitHub platform

**1. GitHub repo traffic (views, clones, popular referrers, popular paths) is still retained for only 14 days; views/clones are daily, referrers/paths are top-10 aggregates over 14 days.**  
*Verdict: confirmed.*

- What's true: Same.
- Views and clones: "total number of views/clones and breakdown per day or week for the last 14 days". The `per` parameter takes `day` (default) or `week`; timestamps are UTC midnight and weeks start Monday.
- Referrers and paths: "top 10 … over the last 14 days", with no daily breakdown.
- Docs: views and clones update hourly; referrers and paths update daily. The REST page says the data is for repos "that you have write access to".
- Extra nuance: the insights page says the traffic graph covers public repos on GitHub Free and Team for orgs, and private repos only on Pro, Team and Enterprise Cloud. It is not available on GHE.com data residency. I did not verify whether the REST API enforces the same plan rule.
- Plan impact: - No change to the core premise.
- The current day in each response is partial and updates hourly, so the collector should overwrite the last 1–2 days on every poll. Polling every 7 days or more often loses nothing.
- Referrers and paths need their own daily snapshots; they cannot be backfilled.
- Do not promise private-repo history to GitHub Free users until tested.
- Evidence: All accessed 2026-11-15.
- OpenAPI operations repos/get-views, repos/get-clones, repos/get-top-referrers and repos/get-top-paths, plus components.parameters.per: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
- https://raw.githubusercontent.com/github/docs/main/content/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository.md (intro and product front-matter)
- https://raw.githubusercontent.com/github/docs/main/content/rest/metrics/traffic.md

**2. For GitHub Apps and fine-grained PATs the traffic endpoints require repository permission "Administration: read". What else does Administration: read expose?**  
*Verdict: confirmed.*

- What's true: Same. All four traffic endpoints map to Administration: read for installation tokens, GitHub App user tokens and fine-grained PATs, and no other permission is needed. No lower permission exists for traffic.

Official description of the permission: "repository creation, deletion, settings, teams, and collaborators creation". The consent screen shows the generic "Administration" label, which can alarm users.

Administration: read covers 45 read endpoints: 44 on the repo and GET /user/repository_invitations, which works with user tokens only. Beyond traffic, they expose:
- Branch-protection settings (10 endpoints).
- Actions permissions and fork-PR settings (7).
- Self-hosted runners: list, details, labels, downloads (5).
- Deploy keys (public keys).
- Pending collaborator invitations.
- Teams with access to the repo.
- Autolinks.
- Ruleset rule-suite evaluation history.
- Code-scanning default setup and code-security configuration.
- Copilot code-review settings.
- Dependabot runner settings.
- Deployment-protection-rule apps.
- Settings for immutable releases, interaction limits, vulnerability alerts, automated security fixes, and the Actions cache retention limit.

It grants no code contents and no write access. The permission also has 109 write endpoints, which this app would not request.
- Plan impact: - Request only Administration: read plus Metadata: read.
- Write consent and privacy copy that lists what the app actually reads (traffic only) and says it never writes.
- Because the app asks for "Repository administration", repo admins cannot self-install it on org repos (see claim 7).
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/src/github-apps/data/fpt-2022-11-28/server-to-server-permissions.json (key "administration": 154 entries, 45 read; traffic entries show access=read, user-to-server=true, server-to-server=true, additional-permissions=false)
- https://raw.githubusercontent.com/github/docs/main/src/github-apps/data/fpt-2022-11-28/fine-grained-pat-permissions.json (same mapping)
- OpenAPI components.schemas.app-permissions.properties.administration description, in the api.github.com.json linked under claim 1

**3. GitHub App installation access tokens last 1 hour, are minted server-side from the app private key without a user present, and get >=5,000 requests/hour per installation (scaling to 12,500).**  
*Verdict: confirmed.*

- What's true: Same.
- Lifetime and minting: a token "will expire after 1 hour". It is created with POST /app/installations/{id}/access_tokens, authenticated by a JWT signed with the app's private key; no user is involved after the one-time install. Docs say native apps must never ship the private key, so minting must happen on the server.
- Rate limit: minimum 5,000/hour per installation. Installations with more than 20 repos get +50/hour per repo, and orgs with more than 20 users get +50/hour per user, capped at 12,500. Enterprise Cloud org or enterprise installations get 15,000.
- Tokens can be scoped down to specific repos (up to 500) and permissions.
- New: since 2026-04-27 tokens are rolling out in a stateless format `ghs_APPID_JWT` and are no longer exactly 40 characters.
- Secondary limit: no more than 2,000 "OAuth access token requests per hour" for GitHub Apps and OAuth Apps. Whether installation-token minting counts toward it is not stated.
- Plan impact: - Server-side collection without storing user tokens is supported. Each user's own installation has its own budget of at least 5,000/hour, far above what about 4 calls per repo per day need.
- Cache each token for about 55 minutes and spread minting over the day.
- Store tokens in a variable-length field.
- Keep the private key in Key Vault or a secret store, never in the app.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation.md (line ~33)
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/generate-installation-access-token.md
- https://raw.githubusercontent.com/github/docs/main/data/reusables/rest-api/primary-rate-limit-github-app-installations.md
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/ghs-stateless-token-format.md
- https://raw.githubusercontent.com/github/docs/main/data/reusables/rest-api/secondary-rate-limit-rest-graphql.md
- https://raw.githubusercontent.com/github/docs/main/content/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app.md (lines 33-67)

**4. Since ~July 2026 listing stargazers is restricted to repo admins/collaborators; GitHub App permission for listing stargazers is "Contents: write"; new GET /repos/{owner}/{repo}/stargazers/history and /stargazers/count exist and need only Metadata: read.**  
*Verdict: partially_correct.*

- What's true: The core is confirmed. The docs say: "In July 2026 … Access to the stargazers listing endpoints will be limited to admins and collaborators", linking the changelog of 2026-06-30.

Permissions:
- Listing stargazers maps to Contents: write for GitHub Apps (installation and user tokens) and fine-grained PATs. It is flagged additional-permissions=true, meaning Metadata is also implied.
- /stargazers/count and /stargazers/history map to Metadata: read.

How /stargazers/history works:
- It returns weekly buckets {week (unix start), total, days[7], Sunday first}, newest first.
- per_page is at most 30 and page at most 100.
- "Week and day boundaries are not guaranteed to align with UTC."
- It counts stars created, so removed stars are not subtracted.

/stargazers/count returns the current count and excludes removed stars.

Unverified:
- The exact launch date of /history. Search snippets point to the changelog of 2026-09-04, "New API endpoint provides privacy-safe star history data"; github.blog was blocked.
- Whether the GraphQL `stargazers` connection is restricted. The public schema has no note about it.
- Search snippets say the 2026-06-30 post also restricted /subscribers (watchers) and deprecated /users/{username}/subscriptions. The OpenAPI file does not mark either as deprecated.
- Plan impact: - Server collection should use /stargazers/history weekly and /stargazers/count daily, so the app needs only Metadata: read and never Contents: write.
- Use /count for current totals, not a cumulative sum of /history.
- Users already need push access to see traffic, so they are collaborators; on-device stargazer listing with their own token probably keeps working. Moving to /history is still simpler and doesn't need per-stargazer data.
- Test the GraphQL path before relying on it.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/rest/activity/starring.md (section "New access restrictions")
- https://raw.githubusercontent.com/github/docs/main/src/github-apps/data/fpt-2022-11-28/server-to-server-permissions.json (contents: GET /stargazers write; metadata: /stargazers/count and /stargazers/history read)
- https://raw.githubusercontent.com/github/docs/main/src/github-apps/scripts/sync.ts (calculateAdditionalPermissions)
- OpenAPI activity/get-stargazer-history-for-repo, activity/get-stargazer-count-for-repo and schemas.stargazer-history, in the api.github.com.json linked under claim 1
- https://raw.githubusercontent.com/github/docs/main/src/graphql/data/fpt/schema.docs.graphql
- Search snippets only: https://github.blog/changelog/2026-06-30-upcoming-access-restrictions-to-public-api-endpoints-and-ui-views/ and https://github.blog/changelog/2026-09-04-new-api-endpoint-provides-privacy-safe-star-history-data
- Local code: GitTrends/Services/GitHubGraphQLApiService.cs:65-85

**5. GitHub supports PKCE for OAuth Apps and GitHub Apps (since ~July 2025). OAuth Apps gained multiple redirect URIs and token refresh/expiring tokens (~Aug 2026).**  
*Verdict: confirmed.*

- What's true: Same, with these details.

PKCE:
- `code_challenge` and `code_challenge_method` are accepted, S256 only; `plain` is not supported.
- Both are "strongly recommended", not required.
- The docs feature flag pkce_support covers GitHub.com and Enterprise Cloud for both GitHub Apps and OAuth Apps.
- The changelog is dated 2025-07-14 (search snippet).

OAuth Apps:
- Up to 10 callback URLs.
- Wildcard matching is now a per-callback setting. Apps with a single callback before August 3, 2026 keep wildcard matching on.
- Expiring tokens: access tokens last 8 hours and refresh tokens 6 months without use. They are on by default for new OAuth Apps. Existing apps opt in under Optional features or by requesting the `offline_access` scope per sign-in.
- Refreshing a token requires client_secret unless the token came from device flow.
- The changelog is dated 2026-08-14, "multiple redirect URIs and token refresh for OAuth apps" (search snippet).
- Plan impact: - Add PKCE (S256) and `state` to whichever flow ships. This closes the 'no PKCE' gap.
- Turn off wildcard matching on the callback and register an exact custom-scheme or universal-link URI.
- If any OAuth App is kept, enable expiring tokens.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps.md (lines ~43-59, 87-113, 331-361, 369-400)
- https://raw.githubusercontent.com/github/docs/main/data/features/pkce_support.yml
- https://raw.githubusercontent.com/github/docs/main/data/features/oauth-token-expiration.yml
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/redirect-uri-wildcard-matching.md
- https://raw.githubusercontent.com/github/docs/main/content/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app.md (lines 50-62)
- Search snippets: https://github.blog/changelog/2025-07-14-pkce-support-for-oauth-and-github-app-authentication/ and https://github.blog/changelog/2026-08-14-multiple-redirect-uris-and-token-refresh-for-oauth-apps

**6. A single GitHub App can provide both user sign-in (user-to-server) and installation (server-to-server) so the OAuth App can be dropped; 'Request user authorization (OAuth) during installation' combines both. Does GitHub App sign-in still need a client secret, or can a mobile app use PKCE without one?**  
*Verdict: partially_correct.*

- What's true: One GitHub App can issue both user access tokens (web or device flow) and installation tokens. "Request user authorization (OAuth) during installation" starts the web flow right after install. Limits of that option:
- It always redirects to the first callback URL, so `redirect_uri` cannot be chosen.
- The Setup URL is disabled.
- For org installs, other org members still need their own web or device flow.

The client secret is still REQUIRED to exchange the code, even with PKCE. `code_verifier` is only "strongly recommended". Refreshing a token also needs the secret unless the token came from device flow. GitHub's best-practices page says public clients (native apps) "cannot secure your client secret. You do have to ship the client secret in the application's code, and you should use PKCE", and warns that public clients are "trivially spoofable" for gating your own services. Another GitHub page (REST rate limits) says never to put a client secret in code that runs on a user device; the guidance conflicts.

Device flow needs no secret, but GitHub says not to enable it outside CLIs, IoT or headless use, because of phishing.

Caveats:
- A GitHub App user token reaches only repos that both the user and an installation of the app can access, so users must install the app.
- User tokens expire after 8 hours by default; refresh tokens last 6 months.
- Plan impact: - Drop the OAuth App and replace it with one GitHub App (Administration: read + Metadata: read), with PKCE.
- Keep the code exchange and refresh on the backend, which holds the client secret. The backend must exist anyway for the private-key collector and to tie a subscription to a verified GitHub user ID.
- If startup must not depend on the backend, shipping the secret with PKCE is GitHub-sanctioned but weaker. Never gate Premium on device-side tokens alone.
- Expect a reinstall and re-consent for all users.
- Handle the `github_app_authorization` and `installation` deleted webhooks to stop collecting and purge data.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app.md (intersection rules, 8h expiry, section on generating a token when a user installs the app)
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/web-app-flow-exchange-code.md (client_secret **Required**, code_verifier strongly recommended)
- https://raw.githubusercontent.com/github/docs/main/content/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens.md (line 57)
- https://raw.githubusercontent.com/github/docs/main/content/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app.md (lines 49-59)
- https://raw.githubusercontent.com/github/docs/main/content/rest/using-the-rest-api/rate-limits-for-the-rest-api.md (line 75)
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/install-vs-authorize.md
- Search snippet of the 2025-07-14 changelog: GitHub "does not distinguish between public and confidential clients"

**7. Installing a GitHub App on organization repos requires org-owner approval (members can only request).**  
*Verdict: partially_correct.*

- What's true: In general:
- Organization owners install apps on the org.
- Members and outside collaborators can only request an install, and owners can disable requests via app access request policies.
- Repository admins CAN install an app for repos they administer, but only if it requests no organization permissions and not the "Repository administration" permission.
- Org owners can also block repo-admin installs altogether.
- Once an owner has installed an app, repo admins can add their own repos to that installation regardless of its permissions.
- The "app manager" role cannot install apps.

For this app the claim effectively holds: it needs Administration: read, so a repo admin cannot self-install it on org repos and an org owner must install or approve it.

The current classic OAuth App has a similar barrier: new orgs have OAuth App access restrictions on by default, which require owner approval.
- Plan impact: - Org-owned repos need the owner's approval, so personal repos are the main market.
- Add an in-app 'request access from your org owner' path and explain it in onboarding.
- Pricing and forecasts should assume org repos convert more slowly.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/apps/using-github-apps/installing-a-github-app-from-a-third-party.md ("Requirements to install a GitHub App")
- https://raw.githubusercontent.com/github/docs/main/data/reusables/apps/repo-admin-install-restriction.md
- https://raw.githubusercontent.com/github/docs/main/data/features/github-app-repository-permission-improvements.yml
- https://raw.githubusercontent.com/github/docs/main/content/apps/using-github-apps/requesting-a-github-app-from-your-organization-owner.md
- https://raw.githubusercontent.com/github/docs/main/data/reusables/organizations/oauth_app_restrictions_default.md

**8. The classic OAuth scope public_repo grants write access to public repos and does not cover private-repo traffic; private repos need the "repo" scope.**  
*Verdict: confirmed.*

- What's true: Same.
- `public_repo`: "Limits access to public repositories. That includes read/write access to code, commit statuses, repository projects, collaborators, and deployment statuses for public repositories and organizations."
- `repo`: "Grants full access to public and private repositories including read and write access to code…", and also lets the app manage org projects, invitations, team memberships and webhooks.
- Classic OAuth has no read-only scope for private repos.
- The app currently requests `public_repo read:user read:org`.
- Plan impact: - Strong reason to move to a GitHub App: Administration: read is read-only and limited to the repos the user picks, where `repo` would mean full write access to all private repos.
- Do not expand the OAuth App to `repo`.
- Evidence: - Accessed 2026-11-15: https://raw.githubusercontent.com/github/docs/main/content/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps.md (lines 45, 48, 56, 64)
- Local code: GitTrends.Shared/Constants/GithubConstants.cs:19 and GitTrends.Common/Constants/GithubConstants.cs:19

**9. GitHub's Terms/AUP do not prohibit a paid app that stores a user's own traffic data at their request (not legal advice).**  
*Verdict: partially_correct.*

- What's true: No clause prohibits this explicitly, and GitHub runs paid apps on Marketplace itself, keeping 5% (Developer Agreement 6.3). There are ambiguities and obligations.

Clauses that apply:
- ToS H (API Terms): abuse or excessive API use can lead to suspension. "You may not share API tokens to exceed GitHub's rate limitations." API data may not be used for spam or for selling personal information. "GitHub may offer subscription-based access to our API for those Users who require high-throughput access or access that would result in resale of GitHub's Service." The undefined word 'resale' is ambiguous.
- AUP section 6: "You will not reproduce, duplicate, copy, sell, resell or exploit any portion of the Service, use of the Service, or access to the Service without our express written permission." This is broad. A value-added analytics and storage service built on the user's own data is common practice, but 'exploit' is undefined.
- AUP section 7: no spam and no selling personal info. Use of the data must follow the GitHub Privacy Statement.
- AUP section 8: personal information may be used only for the purpose the user authorized, must be reasonably secured, and removal requests must be answered promptly.
- If listed on Marketplace, Developer Agreement 3.5 forbids repackaging or reselling 'a GitHub API, Personal Data, or Usage Data', and 3.1/5.1 require a privacy notice and consent.

Traffic counts, referrer domains and paths are aggregates and mostly not personal data. Login and user ID are personal data.

Ambiguity remains around AUP section 6 and ToS H's 'resale'. For certainty, ask GitHub for written confirmation or list on Marketplace.
- Plan impact: - Position Premium as storage and analytics of the user's own repo data, not as access to GitHub's API.
- Publish a privacy policy, which the app stores also require.
- If data is collected for everyone before they subscribe, disclose it at install and in onboarding, and collect it only from users who installed the app.
- Delete data on uninstall or request.
- Never collect or show stargazer identities.
- Keep API usage modest and do not pool tokens.
- Optionally consider a Marketplace listing (5% fee, verified publisher required) or written confirmation from GitHub.
- Evidence: All accessed 2026-11-15.
- https://raw.githubusercontent.com/github/docs/main/content/site-policy/github-terms/github-terms-of-service.md (effective April 27, 2026; Section H, lines 217-229)
- https://raw.githubusercontent.com/github/docs/main/content/site-policy/acceptable-use-policies/github-acceptable-use-policies.md (sections 6-8, lines 80-101)
- https://raw.githubusercontent.com/github/docs/main/content/site-policy/github-terms/github-marketplace-developer-agreement.md (effective May 27, 2025; 3.1, 3.5, 5.1, 6.3)
- https://raw.githubusercontent.com/github/docs/main/content/apps/github-marketplace/selling-your-app-on-github-marketplace/pricing-plans-for-github-marketplace-apps.md

### .NET 11, MAUI 11, Aspire and Functions

**1. .NET 11 GA on 2026-11-10, STS, 24-month support -> EOS ~2028-11-14; .NET 10 LTS EOS 2028-11-14; .NET 8 and 9 EOS 2026-11-10.**  
*Verdict: confirmed.*

- What's true: same. 11.0 is sts with eol-date 2028-11-14 and latest release 11.0.0 on 2026-11-10. 10.0 is lts with eol 2028-11-14. 9.0 and 8.0 are both eol on 2026-11-10, with final patches 9.0.23 and 8.0.34 released that day.
- Plan impact: None. .NET 10 and .NET 11 end support on the same day, so targeting net11 costs no support time. Falling back to net10 for any one component, such as the backend (see claim 4), also costs no support time.
- Evidence: raw.githubusercontent.com/dotnet/core/main/release-notes/releases-index.json (fetched 2026-11-15); dotnet/core release-notes/11.0/README.md:3 ('.NET 11 is a Standard Term Support (STS) release ... supported ... for two years, from November 10, 2026, to November 14, 2028'); release-notes/11.0/11.0.0/11.0.0.md:1 ('.NET 11.0.0 - November 10, 2026', SDK 11.0.100)

**2. Azure Functions .NET 11 support GA on 2026-11-10, isolated worker only, requires the new Azure.Functions.Sdk project SDK (>=1.0.1); runs on Flex Consumption.**  
*Verdict: confirmed.*

- What's true: Gist holds, with these details:
- The docs list .NET 11 as GA in the isolated model; the in-process model does not support .NET 11.
- .NET 11 needs Azure.Functions.Sdk 1.0.1 or later plus an explicit Microsoft.Azure.Functions.Worker reference (2.50.0+ recommended).
- Azure.Functions.Sdk versions: 1.0.0 (2026-09-01), 1.0.1 (09-04), 1.0.2 (2026-11-09, which the discovery missed) and 1.1.0 (2026-11-14).
- The old Microsoft.Azure.Functions.Worker.Sdk 2.1.0 only warns on net11 ('Targeting .NET 11 is not supported ... Migrate to Azure.Functions.Sdk'); it is unsupported but does not block the build.
- Flex Consumption lists .NET 11.
- The platform rollout finished on 2026-11-11 in public Azure, for both Flex and Linux Dedicated/Elastic Premium.
- Linux Consumption stops at .NET 9.
- Plan impact: Migrate GitTrends.Functions from Worker.Sdk 2.0.5 (Directory.Packages.props:25, GitTrends.Functions.csproj:15) to `<Project Sdk="Azure.Functions.Sdk/1.1.0">`. A net11 code (zip) deploy to Flex is officially supported. VS Code tooling still has gaps (vscode-azurefunctions#5197).
- Evidence: MicrosoftDocs/azure-docs:
- articles/azure-functions/dotnet-isolated-process-guide.md:68, :105-117, :148-153
- includes/functions-supported-languages.md (ms.date 2026-11-09): v4 isolated table '.NET 11 | GA'
- articles/azure-functions/flex-consumption-plan.md:195 ('.NET 8, .NET 9, .NET 10, .NET 11')

NuGet registration (api.nuget.org) for azure.functions.sdk, 2026-11-15.

microsoft.azure.functions.worker.sdk 2.1.0 nupkg, build/Microsoft.Azure.Functions.Worker.Sdk.targets (net11 Warning).

GitHub Azure/azure-functions-dotnet-worker#3436, update of 2026-11-11 (rollout complete).

**3. Latest Aspire = 13.6.5 (2026-11-10). Aspire.Hosting.Azure.Functions first stable at 13.1.0. Aspire deploys Functions projects as containers to Azure Container Apps; it cannot deploy to Flex Consumption.**  
*Verdict: confirmed.*

- What's true: Same, with two caveats:
- Versions: all Aspire packages (Aspire.Hosting, AppHost, Cli, Azure.*) top out at 13.6.5, published to NuGet 2026-11-10T17:14Z (tag v13.6.5 commit b33d222 is dated 2026-11-09). There is no 13.7 or 14 prerelease on nuget.org. Aspire.Hosting.Azure.Functions went from 13.0.2-preview (2025-12-04) to 13.1.0 (2025-12-17), its first stable release.
- The docs now say this explicitly: Aspire deploys Functions to ACA, or as a function app through the preview App Service integration, which creates a Premium V3 plan. 'In both cases, your project is deployed as a container.'
- Flex Consumption is code-only; containers are not supported. So Aspire cannot target Flex. The open feature request microsoft/aspire#11307 (Backlog) confirms there is no serverless/code-deploy path.
- New caveat: container deployment of a net11 Functions project currently fails (see claim 4).
- Plan impact: Two options remain: (A) Aspire for local development and the dashboard only, with Functions deployed to Flex by azd, Bicep or GitHub Actions zip deploy (cheapest, works for net11 today); or (B) `aspire deploy` to ACA. Option B means an ACR (claim 6), a dashboard you should disable (claim 7), and a net11 container workaround (claim 4). Never choose the App Service function-app route: it creates a Premium V3 plan.
- Evidence: api.nuget.org flat-container and registration data for aspire.hosting.azure.functions (49 versions), aspire.hosting, aspire.cli and aspire.apphost.sdk; git ls-remote microsoft/aspire tags (v13.6.5 = b33d222).

MicrosoftDocs/azure-docs:
- articles/azure-functions/aspire-integration.md (ms.date 2026-09-04), section 'Hosting the application'
- articles/azure-functions/functions-scale.md:56 ('Flex Consumption plan | Code-only | Container (not supported)')

github.com/microsoft/aspire/issues/11307 (open, Backlog).

**4. Whether Aspire's AddAzureFunctionsProject works with a project using Azure.Functions.Sdk (net11) — any issue/doc either way.**  
*Verdict: partially_correct.*

- What's true: No doc or Aspire issue covers Azure.Functions.Sdk.
- The Functions/Aspire doc still lists Microsoft.Azure.Functions.Worker.Sdk as a requirement.
- microsoft/aspire main has no reference to Azure.Functions.Sdk; its Functions playground uses Worker.Sdk 2.1.0.

Local run is probably fine:
- AddAzureFunctionsProjectCore does not depend on which SDK the project uses. It needs `func` on PATH and runs the project with `--port`.
- Azure.Functions.Sdk 1.1.0 sets RunCommand=func, RunArguments=`start ...`, exactly as Worker.Sdk 2.1.0 does.
- This is untested.

Deploy is broken today for net11:
- Container publishing defaults the base image to `4-dotnet-isolated11.0`.
- That tag is absent from MCR, which publishes only `4-dotnet-isolated11.0-chiseled` and `-azurelinux3`, so publishing fails with CONTAINER1015.
- Issue #3533 (open, 2026-11-11) reports exactly this with `aspire deploy` to ACA.
- Issue #3534 (open, no linked PR) says just changing the tag is not enough, because the chiseled image has no shell or start script and contains only the .NET 10.0.14 runtime.
- The reporter says a custom Dockerfile through PublishAsDockerFile works (2026-11-14). Maintainers have not validated it end to end.
- Azure.Functions.Sdk 1.1.0 still emits the bad tag.
- Plan impact: Do a one-day spike before committing. If the backend must use `aspire deploy` to ACA now, either target net10.0 (the base image exists and end of support is the same day) or carry the custom-Dockerfile workaround until #3534 ships. If using Flex (option A), net11 with Azure.Functions.Sdk is fine, and Aspire is only used locally.
- Evidence: microsoft/aspire @v13.6.5, src/Aspire.Hosting.Azure.Functions/AzureFunctionsProjectResourceExtensions.cs (AddAzureFunctionsProjectCore, WithFunctionsHttpEndpoint); git grep of microsoft/aspire main 81af9cf (2026-11-15) finds no 'Azure.Functions.Sdk'; playground/AzureFunctionsEndToEnd/.../AzureFunctionsEndToEnd.Functions.csproj uses Worker.Sdk.

azure.functions.sdk 1.1.0 nupkg:
- targets/Azure.Functions.Sdk.targets:75-86 (RunCommand)
- targets/publish/Azure.Functions.Sdk.Publish.targets:59-61 (base image tag)

mcr.microsoft.com/v2/azure-functions/dotnet-isolated/tags/list (2026-11-15): no '4-dotnet-isolated11.0'; '4-dotnet-isolated10.0' exists.

github.com/Azure/azure-functions-dotnet-worker/issues/3533 and /3534 (read 2026-11-15).

azure-docs articles/azure-functions/aspire-integration.md ('Azure Functions project' requirements).

**5. Aspire.Hosting.Maui is preview and "local dev only".**  
*Verdict: confirmed.*

- What's true: same.
- Only -preview builds exist; the latest is 13.6.5-preview.1.26559.7 (2026-11-10T17:15Z).
- The package description reads 'MAUI integration for Aspire (local dev only)'.
- The csproj sets SuppressFinalPackageVersion=true, so no stable package is produced.
- The README describes 'local development and debugging'. Emulators and devices reach the dashboard's OTLP endpoint through dev tunnels.
- Plan impact: Use it only for inner-loop debugging and telemetry viewing. It is not a production dependency, and the app must not depend on it.
- Evidence: api.nuget.org registration for aspire.hosting.maui (description field); microsoft/aspire @v13.6.5 src/Aspire.Hosting.Maui/Aspire.Hosting.Maui.csproj:7 and :9; src/Aspire.Hosting.Maui/README.md:3 and :67

**6. Aspire deployment to ACA can use a non-ACR registry (e.g., GHCR) — or does it always provision Azure Container Registry? Any way to avoid the ACR Basic fee?**  
*Verdict: refuted.*

- What's true: Aspire 13.6.5's ACA environment always needs an Azure Container Registry, and GHCR cannot be used:
- AddAzureContainerAppEnvironment creates a default `<env>-acr` registry with SKU Basic (Premium only if private endpoints are used).
- WithAzureContainerRegistry(...) replaces it with your own ACR, and AsExisting reuses an existing one.
- Any non-ACR registry throws: 'Only Azure Container Registry resources are supported.'
- Main (2026-11-15) behaves the same.

Ways to limit or avoid the fee:
- Reuse one existing ACR across environments and apps (one Basic fee instead of several).
- Skip `aspire deploy`: deploy containers from GHCR with your own Bicep or CLI. ACA itself accepts private registries with username/password credentials. You can start from `aspire publish` output and remove the ACR.
- Use Flex Consumption (code deploy, no registry at all).

I did not re-verify the ACR Basic price itself; azure.microsoft.com is blocked.
- Plan impact: Option B (`aspire deploy`) carries a fixed ACR Basic charge on top of compute. That favours option A (Flex) for the cost goal. If you use ACA, put the ACR on the MVP dev/test credit only for non-production, or deploy from GHCR outside the Aspire pipeline.
- Evidence: microsoft/aspire @v13.6.5:
- src/Aspire.Hosting.Azure.AppContainers/AzureContainerAppExtensions.cs:639-642 (CreateDefaultAzureContainerRegistry)
- src/Shared/ContainerRegistryInfrastructure.cs:50 (ContainerRegistrySkuName.Basic)
- src/Aspire.Hosting.Azure.AppContainers/AzureContainerAppEnvironmentResource.cs:190-195 (default removed when explicit) and :345-352 (throws for non-ACR)
- src/Aspire.Hosting.Azure.ContainerRegistry/README.md
- test snapshot AzureContainerAppsTests.DefaultContainerRegistryUsesAzdNamingWhenEnvironmentDoes.verified.bicep (sku 'Basic')

MicrosoftDocs/azure-docs:
- articles/azure-functions/aspire-integration.md ('pushing it to Azure Container Registry')
- articles/container-apps/containers.md:206-221 (private registry credentials)

**7. Whether the managed Aspire Dashboard component in ACA incurs cost and whether Aspire enables it by default on deploy (and how to disable).**  
*Verdict: confirmed.*

- What's true: Default: on. EnableDashboard defaults to true unless the environment uses AsExpress(); Express is experimental (ASPIREACAEXPRESS001) and does not provision the dashboard.

What gets deployed: Aspire emits a `Microsoft.App/managedEnvironments/dotNetComponents` resource named 'aspire-dashboard' (ComponentType AspireDashboard, API 2025-10-02-preview).

How to turn it off: `.WithDashboard(false)` on the environment (documented). For an existing environment, `az containerapp env dotnet-component delete`.

Cost: unverifiable. Neither the ACA Aspire-dashboard doc nor the ACA billing doc gives a price. ACA's managed Java components are documented as fixed 0.5 vCPU / 1 GiB with one replica (min = max = 1), billed at active/idle rates. If the dashboard is billed the same way, an always-on replica would use about 1.3M vCPU-s and 2.6M GiB-s a month, well above the free grant of 180k vCPU-s and 360k GiB-s. One user reported unexpected charges on Microsoft Q&A; I could not fetch that page.
- Plan impact: Always add `.WithDashboard(false)` to production ACA environments. Use the local Aspire dashboard for development and Azure Monitor or another OTLP backend in production.
- Evidence: microsoft/aspire @v13.6.5:
- src/Aspire.Hosting.Azure.AppContainers/AzureContainerAppEnvironmentResource.cs:252-254 (`_enableDashboard ?? !IsExpress`)
- AzureContainerAppExtensions.cs:427-437 (dotNetComponent), :1029 (Express note), :1059 (WithDashboard)

MicrosoftDocs/azure-docs:
- articles/container-apps/aspire-dashboard.md (ms.date 2026-09-04): 'includes the Aspire dashboard by default ... To omit the dashboard, chain .WithDashboard(false)'
- articles/container-apps/billing.md (ms.date 2025-12-09): no component pricing
- articles/container-apps/java-eureka-server.md:38-40 and java-config-server.md:42-44 (Java component billing)

**8. MAUI 11 GA (Microsoft.Maui.Controls 11.0.10); iOS workload requires Xcode 27.2 / macOS Tahoe 26.6+; Microsoft.Maui.Controls.Compatibility not shipped for 11; CoreCLR is the only mobile runtime in .NET 11.**  
*Verdict: confirmed.*

- What's true: Same, with these details:
- Controls 11.0.0 shipped 2026-11-10 and 11.0.10 on 2026-11-11, with TFMs net11.0-android37.0, net11.0-ios27.0 and net11.0-maccatalyst27.0.
- The iOS/Mac SDK 27.2.11039 'requires Xcode 27.2 or later, which requires macOS Tahoe 26.6 or later'. Minimum deployment targets are iOS 15.0 and Mac Catalyst 17.0.
- The Compatibility package has not been built since Preview 6; its last NuGet build is 11.0.0-preview.5.26304.4 (2026-06-09).
- Mono is removed: on iOS, tvOS and Mac Catalyst 'UseMonoRuntime=true produces a build error', and 'Mono isn't supported for .NET MAUI apps that target .NET 11+'.
- Nuance: NativeAOT remains an opt-in publish alternative (experimental on Android). 'CoreCLR is the only runtime' is accurate in practice.
- Plan impact: Budget for a Mac on macOS Tahoe 26.6+ with Xcode 27.2, locally or in CI. Remove the Compatibility reference. Drop any Mono-specific MSBuild settings (UseInterpreter, MtouchInterpreter and similar) and any RunAOTCompilation=false; on Android the latter now fails with error XA1044.
- Evidence: api.nuget.org registration for microsoft.maui.controls, microsoft.maui.controls.compatibility and microsoft.ios.sdk.net11.0_27.2 (27.2.11039, 2026-11-10).

raw.githubusercontent.com/wiki/dotnet/macios/.NET-11-release-notes.md: Requirements section, and 'Mono is no longer supported' (around line 198-200).

dotnet/docs-maui:
- docs/whats-new/dotnet-11.md:192-194 (Compatibility removal), :24-33 and :598-608 (CoreCLR)
- docs/deployment/runtimes-compilation.md:35

GitTrends: latest/GitTrends/GitTrends.csproj:108 and Directory.Packages.props:29 still reference Compatibility 9.0.120.

**9. Xcode 27 builds require adopting the UIScene lifecycle or apps can terminate after launch (Microsoft guidance Oct 2026).**  
*Verdict: confirmed.*

- What's true: Confirmed, and stronger than stated:
- Microsoft's MAUI doc (ms.date 2026-10-21) says apps built against the iOS 27 or Mac Catalyst 27 SDK without the scene lifecycle crash at launch on iOS 27 or Mac Catalyst 27, logging 'UIScene life cycle is required for apps built with this SDK.'
- In .NET 11 GA, building against SDK 27.0+ checks the merged Info.plist and reports error MT7199 when `UIApplicationSceneManifest` is missing. It is a build failure, not only a runtime crash.
- The fix: add a `SceneDelegate : MauiUISceneDelegate` registered as 'SceneDelegate', plus a UIApplicationSceneManifest that uses `__MAUI_DEFAULT_SCENE_CONFIGURATION__`, for both iOS and Mac Catalyst. Updating packages does not retrofit existing projects.
- This also affects .NET 10 apps built with Xcode 27 (.NET 10 needs MAUI 10.0.110+).
- The latest GitTrends source has no UIApplicationSceneManifest and no SceneDelegate.
- Plan impact: Add SceneDelegate.cs and the Info.plist scene manifest under Platforms/iOS (and MacCatalyst if shipped) as an early migration task; the iOS build will not pass without them. Then retest the custom ShellWithLargeTitlesHandler and the OAuth WebAuthenticator callback under scene-based startup.
- Evidence: dotnet/docs-maui docs/ios/uikit-scene-lifecycle.md (ms.date 2026-10-21).

dotnet/core release-notes/11.0/11.0.0/dotnetmaui.md:142-157 (MT7199, dotnet/macios#26988; templates via dotnet/maui#38601).

dotnet/macios wiki .NET-11-release-notes, 'Apps built with Xcode 27 must adopt the UIScene lifecycle'.

devblogs post of 2026-10-19 found by web search; not fetched because the host is blocked.

grep of the latest snapshot for UIApplicationSceneManifest|SceneDelegate: no matches.

**10. Syncfusion.Maui.Toolkit (MIT) includes SfCartesianChart, AreaSeries, DateTimeAxis, NumericalAxis, ChartZoomPanBehavior, ChartTrackballBehavior; latest version and TFMs.**  
*Verdict: confirmed.*

- What's true: Same.
- Latest version: 1.0.12 (2026-11-12). Earlier: 1.0.11 (2026-09-03), 1.0.10 (2026-05-19).
- The package contains LICENSE.txt with 'The MIT License (MIT) Copyright (c) 2024-2025 Syncfusion Inc.'
- lib TFMs: net10.0, net10.0-android36.0, net10.0-ios26.0, net10.0-maccatalyst26.0 and net10.0-windows10.0.19041.0. There is no net11 build, and the GitHub main csproj targets net9 and net10 only.
- The nuspec declares no dependencies.
- The XML docs and the iOS DLL contain SfCartesianChart, AreaSeries, SplineAreaSeries, DateTimeAxis, NumericalAxis, ChartZoomPanBehavior, ChartTrackballBehavior and ChartLegendIconType.
- Low-risk indicator: MAUI 10's Controls DLL grants InternalsVisibleTo only to CommunityToolkit assemblies, not Syncfusion. So the .NET 11 removal of those grants, which broke older CommunityToolkit versions, should not affect the Toolkit's use of Controls.
- Plan impact: Switch Syncfusion.Maui.Charts to the Toolkit, which removes the license handout endpoint. Run an early MAUI 11 smoke build of the trends charts, since the Toolkit is net10-only, and keep Syncfusion.Maui.Charts 35.x (net11) as the fallback.
- Evidence: api.nuget.org registration for syncfusion.maui.toolkit; flat-container nupkg 1.0.12, inspected: LICENSE.txt, nuspec, lib/*/Syncfusion.Maui.Toolkit.xml and .dll.

raw.githubusercontent.com/syncfusion/maui-toolkit/main/maui/src/Syncfusion.Maui.Toolkit.csproj (TargetFrameworks).

downloaded maui10 and maui11 packages: Microsoft.Maui.Controls.dll strings.

**11. Plugin.InAppBilling 11.0.1 (2026-11-14), net10 TFMs, StoreKit 2 default on iOS, Play Billing 9.1 on Android; Google requires PBL 8+ since 2026-08-31.**  
*Verdict: confirmed.*

- What's true: Same.
- 11.0.1 was published 2026-11-14T06:48Z.
- TFMs: net10.0, -android36.0, -ios26.0, -maccatalyst26.0, -macos26.0 and -windows10.0.19041. There is no net11 build.
- On Android it depends on Xamarin.Android.Google.BillingClient 9.1.0.2 (Play Billing Library 9.1) and Microsoft.Maui.Essentials 10.0.11.
- The README says iOS and Mac Catalyst default to StoreKit 2 and require iOS / Mac Catalyst 15+, with a legacy opt-out; native macOS still uses original StoreKit.
- Google's deadlines: PBL 7 for new apps and updates was 2026-08-31, with extensions to 2026-11-01, which has now passed, so PBL 8+ is strictly required today. PBL 8 is accepted until 2027-08-31 and PBL 9 until 2028-08-31.
- Plan impact: Plugin.InAppBilling 11.0.1 meets Google's PBL rule until August 2028 and uses StoreKit 2 on iOS, but it is net10-only, so test it on MAUI 11. StoreKit 2 transaction JWS and Play purchase tokens need server-side verification, and that verification is a backend feature Premium needs.
- Evidence: api.nuget.org registration for plugin.inappbilling; nupkg 11.0.1, inspected: nuspec dependencies and README 'Important Version Information'.

https://developer.android.com/google/play/billing/deprecation-faq (fetched 2026-11-15): support timeline table, and banner 'By Aug 31, 2026, all new apps and updates to existing apps must use Billing Library version 8 or later'.

### Store economics and competitors

**Apple App Store Small Business Program: 15% for developers under $1M prior-year proceeds (enrollment required); without SBP, subscriptions pay 30% in the first paid year then 15%.**  
*Verdict: confirmed.*

- What's true: Same, with these details. Developers with up to $1M in proceeds (sales after Apple's commission and certain taxes) in the prior calendar year qualify, and so do developers new to the App Store. Proceeds from Associated Developer Accounts count toward the limit. Enrollment is required. Passing $1M in the current year puts future sales on the standard rate. Without SBP the rule is per subscriber: Apple pays you 70% during that subscriber's first year of paid service, then 85%. Free trials don't count toward the year. If a subscription lapses for more than 60 days, the count restarts. SBP members get 85% from the first payment. EU, Japan and China have different rates.
- Plan impact: Enroll in SBP (and accept the Paid Apps agreement) before the first paid build so the iOS model uses 15% from day one. If enrollment is missed, first-year subscribers net only 70%.
- Evidence: https://developer.apple.com/app-store/small-business-program/ (fetched 2026-11-15): 'made up to 1 million USD in proceeds in the prior calendar year', 'reduced commission rate of 15%', enrollment steps, 'standard commission rate will apply to future sales' if passed. https://developer.apple.com/app-store/subscriptions/ (fetched 2026-11-15): 'During a subscriber's first year of service, you receive 70%... After a subscriber accumulates one year of paid service... 85%'; 'Free trials and renewal extensions are excluded'; resubscribing after 60 days resets the count; SBP members get 85% 'regardless'.

**Google Play: subscriptions pay 15% total in US/UK/EEA — a new structure from 2026-06-30 of 10% service fee + 5% Google Play billing fee. (Before it, subscriptions were 15% flat.)**  
*Verdict: confirmed.*

- What's true: Same. Since 2026-06-30 in the US, EEA and UK, the service fee is 10% on the first $1M of annual earnings and on all auto-renewing subscriptions. A 5% billing fee is added only when Google Play's billing system is used, so subscriptions pay 15% in total. Alternative billing and external web links don't pay the 5%. Google says it will announce billing fees for other markets later, and rollout elsewhere is staggered (secondary sources disagree on the Japan date). Before this, subscriptions paid a flat 15% from 2022-01-01 (announced 2021-10-21).
- Plan impact: Model 15% on Android. Moving US Android users to alternative billing saves only the 5% billing fee, which a card processor's fees (about 3% + $0.30) mostly cancel out, so stay with Play Billing.
- Evidence: https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play (dated 24 Jun 2026, fetched 2026-11-15): 'separating our service fee from the billing fee. This starts on June 30, 2026, beginning with the United States, European Economic Area, and United Kingdom... service fee starts at 10% on your first $1M... This 10% service fee also applies to all auto-renewing subscriptions... In the United States, United Kingdom, and the European Economic Area, the billing fee is set at 5%.' Prior 15% flat: 2021-10-21 announcement (android-developers.googleblog.com/2021/10/evolving-business-model.html, via search; TechCrunch/The Register coverage). Play Console help page 16954621 blocked.

**Apple currently charges 0% commission on US link-out (external web purchase) transactions under the Epic v. Apple contempt order; Supreme Court granted cert (No. 25-1311) on 2026-06-30; Apple proposed up to a 15% fee on remand.**  
*Verdict: confirmed.*

- What's true: All three points hold. Details: (a) certiorari was granted 2026-06-30, limited to Question 1 (whether a court can hold a party in civil contempt for violating an injunction's 'spirit'). The worldwide-scope question was not taken. Justice Kagan denied a stay of the district court proceedings (No. 26A194). Apple filed its merits brief 2026-09-14 and Epic filed its response later; I found no confirmed argument date. (b) Apple's remand filing of 2026-08-13 is tiered: 15% for standard apps and for a subscription's first year, 10% for subscription renewals and partner programs, 5% for Small Business Program apps. Epic opposes it, and no rate had been set as of mid-November 2026. (c) Apple's 2026-08-12 stay application and news coverage say Apple charges 0% on link-outs in the meantime. The App Review Guidelines confirm US apps need no entitlement for buttons or external links.
- Plan impact: If Apple's proposal is adopted, a Small Business Program app would pay 5% on US link-outs instead of 15% for in-app purchase. After Stripe's ~3.6% + $0.30, that saves only about 6 points, and the Supreme Court could change things in 2027. Keep in-app purchase as the main path and treat a US web checkout as optional later work.
- Evidence: Primary docket pages are blocked; the search tool surfaced supremecourt.gov docket PDFs for 25-1311 (cert reply 2026-06-09, merits brief 2026-09-14) and 26A194 (stay application 2026-08-12). Grant date and scope: MacRumors and Daring Fireball 2026-06-30, IPWatchdog 2026-06-30, Mealey's ('limits review... to civil contempt holding'). Fee proposal: 9to5mac 2026-08-13 'up to 15%', MLex 'Apple proposes 5% to 15% commissions', macobserver, Subscription Insider ('15% year-one, 10% on renewals'). Guidelines 3.1.1(a) and 3.1.3 fetched 2026-11-15 from developer.apple.com/app-store/review/guidelines/: 'These entitlements are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps.' Ninth Circuit: 161 F.4th 1162 (2025-12-11).

**RevenueCat State of Subscription Apps 2026: median monthly price ~$10 and yearly ~$34.80 overall (North America $9.99/$39.99); freemium download->paid by day 35 ~2.1% (iOS ~2.6%, Android ~0.9%); trials of 17–32 days convert ~42.5%.**  
*Verdict: partially_correct.*

- What's true: Several secondary write-ups support the price medians ($10/mo and $34.80/yr overall; $9.99 and $39.99 in North America). They also support the day-35 download-to-paid split of 2.1% for freemium apps vs 10.7% for hard paywalls. Correction: the iOS 2.6% / Android 0.9% split is the median across all apps, not a freemium-only figure, so a freemium Android app likely converts below 0.9%. Trial-to-paid is about 32.5–32.6% on both stores. The 42.5% is trial-to-paid for 17–32-day trials (vs 25.5% for trials of 4 days or less), not download-to-paid. I could not open RevenueCat's own pages to confirm any of these numbers.
- Plan impact: Forecast freemium conversion at about 2% of iOS downloads and below 1% on Android. Don't apply 42.5% to downloads; use it only for users who start a trial. At the old scale of about 500 users that is roughly 5–10 paying subscribers, so the infrastructure has to cost close to nothing.
- Evidence: www.revenuecat.com was blocked (ENOTFOUND and proxy 403). Search excerpts quoting RevenueCat's blog 'android-paywall-gap' ('On Android, the median download to paid conversion at day 35 sits at 0.9%, while iOS lands at 2.6%', trial-to-paid 32.5% vs 32.6%), SaaStr, Airbridge 'Hard Paywall vs Freemium in 2026' (10.7% vs 2.1%), pricepush and apppricinglab ('annual median rose to $34.80', North America $39.99/$9.99), and trial-length tables (17–32 days 42.5%, ≤4 days 25.5%). Searched 2026-11-15.

**Repohistory (repohistory.com) archives GitHub traffic beyond 14 days; Free = 1 repo; Pro = $7.50/mo billed yearly ($90/yr), unlimited repos; saves data starting at first sign-in. Also check any other paid competitor (mobile or web) that archives GitHub traffic, with prices.**  
*Verdict: confirmed.*

- What's true: Same for Repohistory, and there are extra details. Pro is $7.50/mo billed yearly ($90/yr) or $9/mo billed monthly. Free covers 1 repo with history beyond 14 days and data export. Pro adds unlimited repos, a user/org traffic overview and priority support. It is open source under AGPL-3.0 (about 440 stars, last push 2026-03-04), so it can be self-hosted for free. It collects through a GitHub App, with a cron job that loops over every installation, and stores data in Supabase. The public code contains no payment code, so I could not confirm that Pro can actually be bought on the live site (blocked). Other competitors: RepoEasy (hosted, plus self-hosting under MIT) has a free plan for 3 tracked and 10 followed repos, and Pro at €1.50/mo or €12/yr with unlimited repos, 6-hour sync, API, webhooks and badges (repo last pushed 2026-10-13, tiny project). Free options: TrafficKeep (Chrome extension), github-traffic-tracker (GitHub Actions saving to a Gist), Repo-rter (desktop app, price unknown), and several CLIs. I found no paid mobile competitor.
- Plan impact: $99.99/yr is about 11% above Repohistory and about 8x RepoEasy's €12/yr, and free self-hosted options exist. The selling points have to be the mobile app and history that is already there when a user subscribes. Consider a much cheaper yearly price (about $20–40/yr). Repohistory's GitHub App plus daily cron design supports the planned collection architecture.
- Evidence: git clone https://github.com/repohistory/repohistory (HEAD 9dd4ac2, 2026-03-04): landing/app/pricing/pro-card.tsx `price={isYearly ? 7.5 : 9}` and 'Track unlimited repositories'; landing/app/pricing/page.tsx free features 'Track 1 repository', 'Traffic history beyond 14 days'; README 'save traffic data every day, starting from first sign-in'; web/src/cron.ts `app.eachInstallation(... updateTraffic(installation.id))`. Pricing commit 'feat(landing): pricing' dated 2025-07-14. RepoEasy: https://raw.githubusercontent.com/Siekwie/RepoEasy/main/README.md (fetched 2026-11-15): 'free plan archives traffic for 3 repositories... Pro is €1.50 a month or €12 a year'. Search 2026-11-15: repohistory.com/pricing snippet '$7.5 per month, billed yearly'; TrafficKeep Chrome Web Store listing.

**Apple guideline 5.1.1(v) requires in-app account deletion if an app supports account creation; Google Play requires an account-deletion web link + in-app path.**  
*Verdict: confirmed.*

- What's true: Same. Apple: 'If your app supports account creation, you must also offer account deletion within the app.' Deletion must remove the whole account record and the personal data tied to it; deactivation alone is not enough. Linking to a web page to finish deletion is allowed. Subscribers must be told that billing continues through Apple and be offered a way to cancel. Google: an app that lets users create an account must let them request deletion in the app and must also provide a working web link where users can request deletion of their account and data. This is declared in the Data safety form. An account created through a flow outside the app also counts.
- Plan impact: Once Premium stores per-user data on the server (GitHub user, stored history, entitlement), both stores' rules apply. The app needs in-app 'Delete account and data' that removes the stored history, a public web page for deletion requests, the Play Data safety deletion answers, and a notice about cancelling the subscription. The current sign-in uses MAUI Browser.OpenAsync with the system-preferred in-app browser (GitTrends/Services/DeepLinkingService.cs:44-58), not the external browser, so it is acceptable. WebAuthenticator would be a better fit.
- Evidence: https://developer.apple.com/app-store/review/guidelines/ 5.1.1(v) (fetched 2026-11-15). https://developer.apple.com/support/offering-account-deletion-in-your-app/ (fetched 2026-11-15): 'Offer to delete the entire account record...'; 'notify them that billing will continue through Apple'; it also says linking out to the default web browser to sign in is 'not appropriate, per App Review Guideline 4'. Google: support.google.com/googleplay/android-developer/answer/13327111 (blocked; quoted in search excerpts 2026-11-15: in-app request plus 'web link resource', Data safety deletion questions).

**Google Play requires personal developer accounts created after Nov 2023 to run a closed test (12+ testers for 14 days) before production access — and whether it applies to an older account / existing listing.**  
*Verdict: confirmed.*

- What's true: Personal accounts created after 2023-11-13 must run a closed test with at least 12 testers who stay opted in for 14 days in a row, then apply for production access. The requirement started at 20 testers and was cut to 12. Organization accounts and personal accounts created before 2023-11-13 are exempt, so the owner's account (which shipped the app in Feb 2020) does not have to do this for the existing listing or a new one. A separate risk: an account with apps can be marked for closure if its apps have fewer than 1,000 combined lifetime installs, its contact details are unverified, and Play Console hasn't been used in 180 days.
- Plan impact: No 14-day closed-test gate if the old account is reused, which saves about 2–3 weeks. The owner should sign in to Play Console now to check for inactivity or identity-verification warnings so the account isn't closed before the relaunch.
- Evidence: support.google.com/googleplay/android-developer/answer/14151465 (blocked; quoted in search excerpts 2026-11-15: 'accounts created after November 13, 2023... at least 12 testers... 14 days continuously'). Inactive-account rules: support.google.com/googleplay/android-developer/answer/11605267 (via search excerpts 2026-11-15).

**Apple Family Sharing for a subscription cannot be turned off once enabled.**  
*Verdict: confirmed.*

- What's true: Same. It is set per subscription product in App Store Connect and 'can't be undone'. Subscribers can still stop sharing on their side. A developer who wants sharing off would have to create a new product, which is a forum suggestion, not Apple guidance.
- Plan impact: Leave Family Sharing off on Premium products, because each shared family member adds stored history and cost. Decide this before the first release, since it cannot be reversed.
- Evidence: https://developer.apple.com/app-store/subscriptions/ (fetched 2026-11-15): 'You can enable Family Sharing for your subscription in App Store Connect. Please note that this can't be undone.' The App Store Connect help page on purchase options says the same ('you won't be able to turn it off', via search excerpt 2026-11-15).

**RevenueCat is free below $2,500 monthly tracked revenue, then 1%.**  
*Verdict: confirmed.*

- What's true: Same, with one clarification. On the Pro plan, in any month tracked revenue goes over $2,500, the charge is 1% of all tracked revenue, including the first $2,500, not just the amount above it. Invoices are rounded down to whole dollars. Months under $2,500 are free. Tracked revenue covers every purchase and renewal. Once over the limit, some dashboard features are locked until payment succeeds. Sources date this pricing to Sept 2023.
- Plan impact: At the expected scale (well under $2,500 a month) RevenueCat costs $0. Above the limit the charge applies to the whole month's revenue, roughly $25 at $2,500. Cost is not the problem with RevenueCat. The problem is that there is no official MAUI SDK, only community bindings.
- Evidence: RevenueCat's own repo: https://raw.githubusercontent.com/RevenueCat/ai-toolkit/main/revenuecat/skills/revenuecat-billing/SKILL.md lines 38-44 (fetched 2026-11-15): 'Pro has a free allowance of $2,500 MTR. If that threshold is crossed in a month, the user is billed 1% of all tracked revenue... including the portion below $2,500.' revenuecat.com/pricing blocked.

### Facts from this repo

**2. Android package: Play/Xamarin used com.minnick.gittrends (lowercase), MAUI csproj uses ApplicationId com.minnick.GitTrends; check for Android-specific override.**  
*Verdict: confirmed.*

- What's true: Xamarin's AndroidManifest package was "com.minnick.gittrends" (lowercase). The Play URLs in the code and README use id=com.minnick.gittrends. The MAUI csproj sets ApplicationId com.minnick.GitTrends unconditionally. The MAUI Platforms/Android/AndroidManifest.xml has no package attribute, and there is no Android-conditional ApplicationId in the csproj, Directory.Build.props/targets or azure-pipelines.yml. So the Android build would get package com.minnick.GitTrends.

iOS used com.minnick.GitTrends in both apps, so iOS is consistent. The live Play listing itself was not checked (privacy rule); the evidence comes from repo links only.
- Plan impact: Add <ApplicationId Condition="android target">com.minnick.gittrends</ApplicationId>, or the Play update will be rejected or end up as a separate app. Keep the iOS bundle ID as it is.
- Evidence: git show 6232ef65:GitTrends.Android/Properties/AndroidManifest.xml:2
6232ef65:GitTrends/Constants/AppStoreConstants.cs:13
pr1:GitTrends/Constants/AppStoreConstants.cs:11
pr1:README.md:24,58
pr1:GitTrends/GitTrends.csproj:15
pr1:GitTrends/Platforms/Android/AndroidManifest.xml:2 (no package=)
6232ef65:GitTrends.iOS/Info.plist:25-26
pr1:GitTrends/Platforms/iOS/Info.plist:31

**3. Last shipped version was 2.5.11 build 65 (Xamarin); MAUI is 3.0.0 build 66.**  
*Verdict: confirmed.*

- What's true: The version numbers are confirmed. Android versionCode 65 / versionName 2.5.11 and iOS CFBundleVersion 65 / CFBundleShortVersionString 2.5.11 come from 6232ef65 (2024-08-25), the last Xamarin version bump and the direct parent of the MAUI merge 8d74e686. MAUI is ApplicationDisplayVersion 3.0.0 / ApplicationVersion 66, unchanged since 8d74e686.

That 2.5.11 actually shipped to the stores, and that 3.0.0 never did, is an inference: the repo has no release tags beyond 0.9.0 and no store evidence.
- Plan impact: The owner should confirm the highest build numbers uploaded in App Store Connect and Play Console. The relaunch build must be higher than 65 (or 66 if 3.0.0 reached TestFlight).
- Evidence: git show 6232ef65 (manifest :2 versionCode 64->65, 2.5.10->2.5.11; Info.plist CFBundleShortVersionString/CFBundleVersion at :59-67)
git log 8d74e686^ -1 = 6232ef65
pr1:GitTrends/GitTrends.csproj:18-19
git log -G ApplicationVersion pr1 -- GitTrends/GitTrends.csproj shows only 8d74e686
git tag shows only 0.9.0

**4. AppStore build configuration lost DefineConstants/Optimize in commit 87a97619 so '#if AppStore' blocks never compile; consequences (Android Debuggable, Sentry DSN missing, etc.).**  
*Verdict: partially_correct.*

- What's true: Removal confirmed. 87a97619 ('Update to .NET 9', 2024-12-07) deleted the Directory.Build.props PropertyGroup for AppStore (Optimize=true, DefineConstants=AppStore) and the matching Release group. Nothing re-adds them in pr1.

The .NET SDK implicitly adds $(Configuration.ToUpperInvariant()), so an AppStore build defines APPSTORE. C# symbols are case-sensitive, so every #if AppStore and [Conditional("AppStore")] block is dead. Optimize is defaulted only for Debug and Release, so AppStore IL is unoptimized.

Consequences in pr1:
- MainApplication gets [Application(Debuggable = true)]. Release builds were always debuggable, too.
- MauiProgram: neither DEBUG, RELEASE nor 'AppStore' Sentry config compiles, so options.Dsn stays null. In Sentry 5.16.2 this is worse than a missing DSN: SettingLocator.GetDsn throws ArgumentNullException('You must supply a DSN...'), called from SentryMauiInitializer. An AppStore build would likely crash at startup (inferred from source, not run).
- ReviewService calls RequestReview(true), which is test mode.
- The '#error Missing API Keys' guards in both AzureConstants files never fire.
- FirstRunService's HandlePagePopped and the BackdoorMethodConstants test hooks are compiled in.

CI only builds -c Release, so nothing caught this.
- Plan impact: Restore <DefineConstants>$(DefineConstants);AppStore</DefineConstants> and <Optimize>true</Optimize> for AppStore, or switch the code to #if APPSTORE. Make Debuggable depend on DEBUG. Give Sentry a DSN in every configuration (or Dsn="" to disable). Add a CI job that builds -c AppStore and checks the manifest is not debuggable. Without this, the first store build is either rejected by Play (debuggable) or crashes on launch.
- Evidence: git show 87a97619 -- Directory.Build.props (removed lines: AppStore Optimize/DefineConstants/DebugSymbols; Release block)
git merge-base --is-ancestor 87a97619 pr1 = true
pr1: git grep '#if AppStore' -> GitTrends/Platforms/Android/MainApplication.cs:7-11, GitTrends/Services/ReviewService.cs:68-72, GitTrends/Services/FirstRunService.cs:24, GitTrends.Common/Constants/AzureConstants.cs:5-7, GitTrends.Shared/Constants/AzureConstants.cs:5, GitTrends.Mobile.Common/Constants/BackdoorMethodConstants.cs:1
pr1:GitTrends/MauiProgram.cs:228-253
pr1:Directory.Packages.props:51 (Sentry.Maui 5.16.2)
dotnet/sdk main: src/Tasks/Microsoft.NET.Build.Tasks/targets/Microsoft.NET.Sdk.CSharp.targets:16-31 (ImplicitConfigurationDefine), Microsoft.NET.Sdk.props:48-53 (Optimize only for Debug/Release)
getsentry/sentry-dotnet@5.16.2: src/Sentry/Internal/SettingLocator.cs:58-66; src/Sentry.Maui/Internal/SentryMauiInitializer.cs:9-16
pr1:azure-pipelines.yml:117

**5. Release-build startup awaits backend calls and shows 'Initialization Failed' if any fails (AppInitializationService.cs, SplashScreenPage.cs).**  
*Verdict: partially_correct.*

- What's true: Mostly true, with two nuances.

(1) Statistics initialization is awaited in all configurations, Debug included. Syncfusion and Libraries are awaited only in non-DEBUG builds.

(2) Each service blocks only when its cache is empty, so fresh installs dead-end with no retry.
- Plan impact: Make startup local-first. Use compiled defaults, use the MIT Syncfusion Toolkit or a bundled license, and make the library list and statistics best-effort and non-blocking. Add a retry or 'continue offline' path. Cache-empty is the state every new relaunch user starts in.
- Evidence: pr1:GitTrends/Services/AppInitializationService.cs:34-74 (lines 48-58)
pr1:GitTrends/Services/GitTrendsStatisticsService.cs:101-131
pr1:GitTrends/Services/LibrariesService.cs:32-45
pr1:GitTrends/Services/SyncfusionService.cs:21-45
pr1:GitTrends/Pages/SplashScreenPage.cs:198-218
pr1:GitTrends/App.cs:39-49

**6. GetTestToken has a duplicate dictionary key (since 815de5fa) that makes every call throw.**  
*Verdict: confirmed.*

- What's true: The same key appears twice in the static collection initializer (lines 18 and 20). It appeared when 815de5fa (2025-04-21) renamed the key on line 18 to match line 20.

The initializer calls Dictionary.Add, which throws ArgumentException inside the static field initializer. Every access to _testTokenDictionary at line 32 then throws TypeInitializationException, outside the try block, so every invocation fails (HTTP 500 from the Functions host). The function also injects services it never uses.
- Plan impact: Delete the function. Tests should read a token from a CI secret.
- Evidence: pr1:GitTrends.Functions/Functions/GetTestToken.cs:16-21, :32, :39
git show 815de5fa -- GitTrends.Functions/Functions/GetTestToken.cs (one-line change on line 18)
The latest snapshot file is identical to pr1.

**7. Client OAuth scope is 'public_repo read:user read:org', no PKCE, and the client logs users out if the token scope lacks 'org'.**  
*Verdict: confirmed.*

- What's true: Scope: confirmed (URL-encoded 'public_repo read:user read:org'). public_repo grants write access to public repos.

No PKCE on either side. Further details of the old flow are in the owner's private notes.

Logout: GitHubUserService.GetGitHubToken calls InvalidateToken() when token.Scope does not contain 'org'. That removes the stored token and sets IsAuthenticated=false, a silent logout. Added in 55c561e7 (2021-06-06).
- Plan impact: Move to a GitHub App (user-to-server tokens plus installation tokens for server collection) or an OAuth App with PKCE and least privilege. Drop public_repo. Do not log users out based on a scope substring when the auth model changes; plan a migration path for existing tokens.
- Evidence: pr1:GitTrends.Common/Constants/GithubConstants.cs:19 (also GitTrends.Shared/Constants/GithubConstants.cs:19)
pr1:GitTrends/Services/GitHubAuthenticationService.cs:87
pr1:GitTrends.Common/Interfaces/IGitHubAuthApi.cs:8-9
pr1:GitTrends.Functions/Functions/GenerateGitHubOAuthToken.cs:13-32
pr1:GitTrends/Services/GitHubUserService.cs:146-150, :191-195
git log -S 'Contains("org"' -> 55c561e7

**9. Star history is built by paging all stargazers via GraphQL (may break under GitHub's 2026 stargazer-listing restriction).**  
*Verdict: partially_correct.*

- What's true: Paging is confirmed. GitHubGraphQLApiService.GetStarGazers pages repository{stargazers(first:100, after:cursor){edges{starredAt,cursor}}} until done. The repo's star count is the length of that list (GetRepository line 56). TrendsViewModel and GitHubApiRepositoriesService use it. The REST GetStarGazers exists, but only tests call it.

The restriction is real: the GitHub docs source says that from July 2026 'Access to the stargazers listing endpoints will be limited to admins and collaborators'. But the app only fetches repos where the viewer is ADMIN, MAINTAIN or WRITE, so for its own use case the listing most likely still works. The GraphQL schema docs and upcoming-changes carry no restriction note for Repository.stargazers; whether GraphQL is covered is unverified.

Risks that remain: cost (about 1 call per 100 stars), and the 'empty response' failure mode mentioned in secondary coverage, which would show 0 stars. The new REST endpoints exist: /repos/{o}/{r}/stargazers/count, and /stargazers/history, which returns weekly buckets with per-day counts, per_page up to 30, page up to 100.
- Plan impact: Replace the full stargazer paging with /stargazers/count (or stargazerCount in GraphQL) for the total and /stargazers/history for the chart. This is cheaper and safe from the restriction. Server-side collection should use these endpoints as well, and the extra GitHub App permission each needs should be checked.
- Evidence: pr1:GitTrends.Common/Interfaces/IGitHubGraphQLAPI.cs:24-30
pr1:GitTrends/Services/GitHubGraphQLApiService.cs:37-63, :65-87, :195
pr1:GitTrends/Services/GitHubGraphQLApiService.cs:163,222 (permission filter)
pr1:GitTrends/Services/GitHubApiRepositoriesService.cs:212
pr1:GitTrends/ViewModels/TrendsViewModel.cs:483-485
github/docs main content/rest/activity/starring.md ('New access restrictions' section, links the 2026-06-30 changelog)
github/rest-api-description main api.github.com.json (v1.1.4): paths /repos/{owner}/{repo}/stargazers, /stargazers/count, /stargazers/history
github/docs src/graphql/data/fpt/schema.docs.graphql: Repository.stargazers has no restriction note
Secondary only: web search results for the github.blog 2026-06-30 and 2026-09-04 changelogs (github.blog is blocked from this session)

