# Microsoft / MSRC — Indeks Writeup Bug Bounty (ID)

> Kumpulan writeup untuk Microsoft / MSRC. Kolom: judul, tanggal publikasi, penulis, reward yang **dilaporkan**, jenis (blog/video), dan tautan langsung ke laporan asli. Nominal adalah yang dilaporkan penulis/kurator, bukan jaminan untuk temuan serupa.

## 1. Ringkasan

| Item | Nilai |
|---|---|
| Total entri unik | 92 |
| Entri dengan reward dilaporkan | 43 |
| Reward tertinggi | $200,000 |
| Rentang tanggal | 2017-09-12 s/d 2026-10-28 |

## 2. 20 Reward Tertinggi (Dilaporkan)

| # | Reward | Tulisan | Penulis | Tanggal | Jenis | Tautan |
|---|---|---|---|---|---|---|
| 1 | **$200,000** | Azure's Weakest Link: Five Full Cross-Tenant Compromises | Haakon Wik Gulbrandsrud | 2026-10-02 | blog | [buka](https://www.binarysecurity.no/posts/2026/10/one-root-case) |
| 2 | **$175,000** | The Last Proof of Human Craft: Microsoft Edge Full Chain | Orange Tsai | 2026-10-28 | blog | [buka](https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/) |
| 3 | **$150,000** | How I Hacked Microsoft Teams and got 150000 in Pwn2Own | Masato Kinugawa | 2023-07-31 | blog | [buka](https://speakerdeck.com/masatokinugawa/how-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own) |
| 4 | **$140,000** | Agentic Vulnerability Reasoning on Windows COM Binaries | Hwiwon Lee et al. | 2026-05-06 | blog | [buka](https://arxiv.org/abs/2605.05000) |
| 5 | **$50,000** | How I Might Have Hacked Any Microsoft Account | Laxman Muthiyah | 2021-03-02 | blog | [buka](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account) |
| 6 | **$48,000** | Breaking the M365 Copilot Sandbox with ChatMate | Ori Lahav | 2026-08-06 | blog | [buka](https://zerolabs.rubrik.com/blog/breaking-m365-copilot-sandbox-chatmate) |
| 7 | **$40,000** | Critical Vulnerability in Microsoft Azure Cosmos DB | Wiz | 2021-08-26 | blog | [buka](https://chaosdb.wiz.io/) |
| 8 | **$40,000** | BingBang: AAD misconfiguration led to Bing results manipulation | Hillai Ben-Sasson | 2023-03-29 | blog | [buka](https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration) |
| 9 | **$40,000** | Azure's Weakest Link: Full Cross-Tenant Compromise | Haakon Holm Gulbrandsrud | 2025-08-20 | blog | [buka](https://www.binarysecurity.no/posts/2025/08/azures-weakest-link-part2) |
| 10 | **$30,000** | Azure Cloud Shell Kubernetes Cluster Takeover | Chen Cohen | 2021-02-15 | blog | [buka](https://hencohen10.medium.com/i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-unsecured-558621519cf9) |
| 11 | **$30,000** | Lets Dance in the Cache: Destabilizing Hash Table on IIS | Orange Tsai | 2022-08-18 | blog | [buka](https://blog.orange.tw/posts/2022-08-lets-dance-in-the-cache-destabilizing-hash-table-on-microsoft-iis/) |
| 12 | **$20,000** | Microsoft Dynamics Container Sandbox RCE via Docker API | Chen Cohen | 2021-06-25 | blog | [buka](https://hencohen10.medium.com/microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-20-000-bounty-7f726340a93b) |
| 13 | **$20,000** | Microsoft Dynamics Container Sandbox RCE | Chen Cohen | 2022-06-01 | blog | [buka](https://hencohen10.medium.com/microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-20-000-bounty-7f726340a93b) |
| 14 | **$20,000** | Cross-Tenant Access Exploit in Microsoft Entra ID | Bashir Mohamed | 2025-09-16 | blog | [buka](https://medium.com/@bashir69emceeaka5/cross-tenant-access-exploit-in-microsoft-entra-id-breaking-governance-with-a-simple-trick-a06d88fe309e) |
| 15 | **$20,000** | Agentic 0day Research: Edge VBS Bypass | Alex Bernier | 2026-02-08 | blog | [buka](https://blindcyber.com/2026/02/08/Agentic-0day-Research/) |
| 16 | **$15,000** | Finding SSRFs in Azure DevOps | Torjus Bryne Retterstol | 2025-01-17 | blog | [buka](https://binarysecurity.no/posts/2025/01/finding-ssrfs-in-devops) |
| 17 | **$10,000** | 10000 for automatic email confirmation bug in Edge | Karan Chaudhary | 2021-01-22 | blog | [buka](https://0xkaran.medium.com/10-000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser-22f15ceccb4a) |
| 18 | **$10,000** | Finding SSRFs in Azure DevOps Part 2 | Sofia Lindqvist | 2025-05-30 | blog | [buka](https://www.binarysecurity.no/posts/2025/05/finding-ssrfs-in-devops-part2) |
| 19 | **$10,000** | How I Found the Worst ASP.NET Vulnerability | Siddhant Kalgutkar | 2025-11-07 | blog | [buka](https://www.praetorian.com/blog/how-i-found-the-worst-asp-net-vulnerability-a-10k-bug-cve-2025-55315/) |
| 20 | **$8,000** | When Validate Hwnd Isnt a Gate: CVE-2026-54107 | Pravin Choudhary | 2026-07-14 | blog | [buka](https://medium.com/@pravin1214choudhary/when-validate-hwnd-isnt-a-gate-root-causing-cve-2026-54107-ce4eeacb530a) |

## 3. Semua Entri (terbaru dulu)

### 3.1 Dengan reward dilaporkan

| Tanggal | Reward | Tulisan | Penulis | Jenis | Tautan |
|---|---|---|---|---|---|---|
| 2026-10-28 | $175,000 | The Last Proof of Human Craft: Microsoft Edge Full Chain | Orange Tsai | blog | [buka](https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/) |
| 2026-10-02 | $200,000 | Azure's Weakest Link: Five Full Cross-Tenant Compromises | Haakon Wik Gulbrandsrud | blog | [buka](https://www.binarysecurity.no/posts/2026/10/one-root-case) |
| 2026-09-25 | $5,000 | How I Could've Accessed 17 Trillion Microsoft Records | Faav | blog | [buka](https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records) |
| 2026-08-19 | $5,000 | Microsoft Teams Community Invitation Bypass | Muhammad Alqi Fahrezi | blog | [buka](https://www.kacateknologi.com/en/microsoft-teams-community-invitation-bypass-cve-2025-49731) |
| 2026-08-06 | $48,000 | Breaking the M365 Copilot Sandbox with ChatMate | Ori Lahav | blog | [buka](https://zerolabs.rubrik.com/blog/breaking-m365-copilot-sandbox-chatmate) |
| 2026-07-14 | $8,000 | When Validate Hwnd Isnt a Gate: CVE-2026-54107 | Pravin Choudhary | blog | [buka](https://medium.com/@pravin1214choudhary/when-validate-hwnd-isnt-a-gate-root-causing-cve-2026-54107-ce4eeacb530a) |
| 2026-05-06 | $140,000 | Agentic Vulnerability Reasoning on Windows COM Binaries | Hwiwon Lee et al. | blog | [buka](https://arxiv.org/abs/2605.05000) |
| 2026-03-04 | $5,000 | Azure DevOps Privilege Escalation via OIDC Abuse | Cody Burkard | blog | [buka](https://dazesecurity.io/blog/azureDevOpsPrivEsc) |
| 2026-02-08 | $20,000 | Agentic 0day Research: Edge VBS Bypass | Alex Bernier | blog | [buka](https://blindcyber.com/2026/02/08/Agentic-0day-Research/) |
| 2026-01-19 | $5,000 | Exploiting RCE in Windows Telephony Service | Sergey Bliznyuk | blog | [buka](https://ptswarm.com/blog/whos-on-the-line-exploiting-rce-in-windows-telephony-service/) |
| 2026-01-02 | $2,500 | How Simple Recon Led to a High-Severity Microsoft Vulnerability | Sreejith A R | blog | [buka](https://medium.com/@0xzoro.hack/how-simple-recon-led-to-a-high-severity-microsoft-vulnerability-and-an-msrc-bounty-a9009bac0d3c) |
| 2025-12-15 | $5,000 | Uncovering CVE-2025-64669 in Windows Admin Center | Cymulate Research Lab | blog | [buka](https://cymulate.com/blog/cve-2025-64669-windows-admin-center/) |
| 2025-11-07 | $10,000 | How I Found the Worst ASP.NET Vulnerability | Siddhant Kalgutkar | blog | [buka](https://www.praetorian.com/blog/how-i-found-the-worst-asp-net-vulnerability-a-10k-bug-cve-2025-55315/) |
| 2025-09-16 | $20,000 | Cross-Tenant Access Exploit in Microsoft Entra ID | Bashir Mohamed | blog | [buka](https://medium.com/@bashir69emceeaka5/cross-tenant-access-exploit-in-microsoft-entra-id-breaking-governance-with-a-simple-trick-a06d88fe309e) |
| 2025-08-24 | $2,500 | Leaking Microsoft employee secrets through diagnostic data | careful and Doc | blog | [buka](https://careful.net/blog/powerlift/) |
| 2025-08-20 | $40,000 | Azure's Weakest Link: Full Cross-Tenant Compromise | Haakon Holm Gulbrandsrud | blog | [buka](https://www.binarysecurity.no/posts/2025/08/azures-weakest-link-part2) |
| 2025-08-05 | $7,500 | Microsoft Partner Leak: 700M+ Partner Records | Faav | blog | [buka](https://blog.faav.net/microsoft-partner-leak) |
| 2025-07-25 | $7,500 | How a Simple Endpoint Earned Me a 7500 Bounty | Gouri Sankar A | blog | [buka](https://medium.com/@gourisankara357/how-a-simple-endpoint-earned-me-a-7500-bounty-from-microsoft-1891a35d40be) |
| 2025-05-30 | $10,000 | Finding SSRFs in Azure DevOps Part 2 | Sofia Lindqvist | blog | [buka](https://www.binarysecurity.no/posts/2025/05/finding-ssrfs-in-devops-part2) |
| 2025-01-17 | $15,000 | Finding SSRFs in Azure DevOps | Torjus Bryne Retterstol | blog | [buka](https://binarysecurity.no/posts/2025/01/finding-ssrfs-in-devops) |
| 2024-10-08 | $5,000 | How I got a 5000 Bounty from Microsoft | Bashir Mohamed | blog | [buka](https://medium.com/@bashir69emceeaka5/how-i-got-a-5000-bounty-from-microsoft-fb2e27fd40f7) |
| 2024-10-08 | $3,000 | From 401 Unauthorized Access to 3000 Bounty | Bashir Mohamed | blog | [buka](https://medium.com/@bashir69emceeaka5/from-401-unauthorized-access-to-3000-bounty-from-microsoft-53b086379a08) |
| 2024-08-07 | $3,000 | Persistent XSS on Microsoft Bing.com by poisoning Bingbot | Supakiad S | blog | [buka](https://infosecwriteups.com/persistent-xss-vulnerability-on-microsoft-bings-video-indexing-system-a46db992ac7b) |
| 2023-07-31 | $150,000 | How I Hacked Microsoft Teams and got 150000 in Pwn2Own | Masato Kinugawa | blog | [buka](https://speakerdeck.com/masatokinugawa/how-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own) |
| 2023-03-29 | $40,000 | BingBang: AAD misconfiguration led to Bing results manipulation | Hillai Ben-Sasson | blog | [buka](https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration) |
| 2023-01-21 | $3,000 | Reflected XSS Leads to 3000 Bounty from Microsoft Forms | Supakiad S | blog | [buka](https://infosecwriteups.com/reflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261) |
| 2022-08-18 | $30,000 | Lets Dance in the Cache: Destabilizing Hash Table on IIS | Orange Tsai | blog | [buka](https://blog.orange.tw/posts/2022-08-lets-dance-in-the-cache-destabilizing-hash-table-on-microsoft-iis/) |
| 2022-07-13 | $6,000 | Microsoft Teams Cross Site Scripting Bypass CSP | numanturle | blog | [buka](https://medium.com/@numanturle/microsoft-teams-stored-xss-bypass-csp-8b4a7f5fccbf) |
| 2022-06-01 | $20,000 | Microsoft Dynamics Container Sandbox RCE | Chen Cohen | blog | [buka](https://hencohen10.medium.com/microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-20-000-bounty-7f726340a93b) |
| 2021-12-10 | $5,000 | Remote Deserialization Bug in Microsoft RDP Client | Valentino Ricotta | blog | [buka](https://blog.thalium.re/posts/deserialization-bug-through-rdp-smart-card-extension/) |
| 2021-08-26 | $40,000 | Critical Vulnerability in Microsoft Azure Cosmos DB | Wiz | blog | [buka](https://chaosdb.wiz.io/) |
| 2021-06-25 | $20,000 | Microsoft Dynamics Container Sandbox RCE via Docker API | Chen Cohen | blog | [buka](https://hencohen10.medium.com/microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-20-000-bounty-7f726340a93b) |
| 2021-03-02 | $50,000 | How I Might Have Hacked Any Microsoft Account | Laxman Muthiyah | blog | [buka](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account) |
| 2021-02-15 | $30,000 | Azure Cloud Shell Kubernetes Cluster Takeover | Chen Cohen | blog | [buka](https://hencohen10.medium.com/i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-unsecured-558621519cf9) |
| 2021-01-22 | $10,000 | 10000 for automatic email confirmation bug in Edge | Karan Chaudhary | blog | [buka](https://0xkaran.medium.com/10-000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser-22f15ceccb4a) |
| 2021-01-10 | $2,000 | Unauthorized Access to OData Entities | Borna Nematzadeh | blog | [buka](https://infosecwriteups.com/unauthorized-access-to-odata-entities-2k-bounty-from-microsoft-e070b2ef88c2) |
| 2020-06-28 | $3,000 | Taking over Azure DevOps Accounts with 1 Click | Sean Yeoh | blog | [buka](https://www.assetnote.io/resources/research/taking-over-azure-devops-accounts-with-1-click) |
| 2020-05-27 | $3,000 | iOS Outlook Stored XSS | kminthein | blog | [buka](https://medium.com/kminthein/ios-outlook-stored-xss-write-up-ce34d7da192b) |
| 2020-05-14 | $1,000 | My Weirdest Bug Bounty: Getting PII from O365 | Omaid Faizyar | blog | [buka](https://omaidfaizyar.medium.com/my-weirdest-bug-bounty-getting-pii-from-o365-b4477f4739e) |
| 2019-04-14 | $1,000 | XSS Stored in Outlook.com (iOS browsers) | Omar Espino | blog | [buka](https://omespino.com/write-up-1000-usd-in-5-minutes-xss-stored-in-outlook-com-ios-browsers/) |
| 2018-10-12 | $500 | Microsoft CSRF Vulnerability | Adesh Kolte | blog | [buka](https://ad3sh.medium.com/how-i-got-500-from-microsoft-for-csrf-vulnerability-700accaf48b9) |
| 2018-04-15 | $1,500 | Bypass CSP by Abusing XSS Filter in Edge | Xiaoyin Liu | blog | [buka](https://infosecwriteups.com/bypass-csp-by-abusing-xss-filter-in-edge-43e9106a9754) |
| 2017-09-12 | $5,000 | Uncovering a Bug I Found in Outlook | cem | blog | [buka](https://cems.fun/2022/12/26/CVE-2017-8758.html) |

### 3.2 Tanpa reward

| Tanggal | Reward | Tulisan | Penulis | Jenis | Tautan |
|---|---|---|---|---|---|---|
| 2026-10-23 | — | AuthMask: Microsoft Authenticator Token Handover | Ofek Levin | blog | [buka](https://enclave.ai/blog/authmask-we-made-microsoft-authenticator-hand-over-tokens) |
| 2026-10-23 | — | Signed Sealed and Relayed: Bypassing LDAP Signing | Raj Patel | blog | [buka](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/) |
| 2026-09-30 | — | From SELECT to SYSADMIN with SQL Copilot | Johann Rehberger | blog | [buka](https://embracethered.com/blog/posts/2026/from-select-to-sysadmin-sql-copilot-bluehat-asia/) |
| 2026-09-21 | — | Windows Exploitation: Dangling COM Object Registrations | James Forshaw | blog | [buka](https://projectzero.google/2026/09/windows-dangling-com.html) |
| 2026-09-17 | — | Bypassing VS Code Workspace Trust with a Single Link | Omri Dar | blog | [buka](https://remedio.io/research/vulnerability-disclosures/bypassing-vs-code-workspace-trust-with-a-single-link/) |
| 2026-09-03 | — | Read-Only Is a Lie: An Entra ID Privilege Escalation | Cymulate Research Lab | blog | [buka](https://cymulate.com/blog/entra-id-global-reader-privilege-escalation/) |
| 2026-08-18 | — | CoSnitch: When Your AI Assistant Becomes Its Own Whistleblower | Lior Adar | blog | [buka](https://www.varonis.com/blog/cosnitch) |
| 2026-08-12 | — | Nice2Meet: Teams Mobile Meetings Account Takeover | Yanir Tsarimi | blog | [buka](https://enclave.ai/blog/nice2meet-we-turned-teams-mobile-meetings-into-a-silent-account-takeover) |
| 2026-08-10 | — | CVE-2026-63520: SharePoint RCE | Stephen Fewer | blog | [buka](https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/) |
| 2026-08-07 | — | Python in Excel: Root Privilege Escalation | Ron Ben Yizhak | blog | [buka](https://www.safebreach.com/blog/python-in-excel-vulnerability-root-escalation-cve-2026-45459/) |
| 2026-07-30 | — | CosmosEscape: Taking Over Every Azure Cosmos DB | Yuval Avrahami and Lior Maman | blog | [buka](https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db) |
| 2026-07-22 | — | Dark Elevator (CVE-2026-50343) | Carlos Roque | blog | [buka](https://calif.io/research/dark-elevator) |
| 2026-07-13 | — | CVE-2026-63520: Microsoft SharePoint RCE | Stephen Fewer | blog | [buka](https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/) |
| 2026-07-13 | — | CVE-2026-55040: SharePoint JWT Token Auth Bypass | Stephen Fewer | blog | [buka](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/) |
| 2026-07-01 | — | Extending an EPM Poisoning Technique in Windows | Ron Ben Yizhak | blog | [buka](https://www.safebreach.com/blog/an-update-on-you-snooze-you-lose-winning-lpes-by-racing-services-for-rpc-endpoints/) |
| 2026-06-30 | — | Azure Monitor Agent Metrics Extension Vulnerability | Cristhian Parrot | blog | [buka](https://www.kroll.com/en/publications/cyber/azure-monitor-agent-metrics-extension-vulnerability) |
| 2026-06-16 | — | CVE-2026-20824: UI Redirection Attack Vector | Allan Hedegaard | blog | [buka](https://www.linkedin.com/pulse/cve-2026-20824-ui-redirection-new-attack-vector-using-hedegaard-iwiue) |
| 2026-06-15 | — | SearchLeak: M365 Copilot One-Click Data Exfiltration | Dolev Taler | blog | [buka](https://www.varonis.com/blog/searchleak) |
| 2026-06-02 | — | FlagLeft: Microsoft 365 Apps Silent Account Takeover | Yanir Tsarimi | blog | [buka](https://enclave.ai/blog/flagleft-microsoft-365-android-forgotten-flag-account-takeover) |
| 2026-06-02 | — | 1-Click GitHub Token Stealing via a VSCode Bug | Ammar Askar | blog | [buka](https://blog.ammaraskar.com/github-token-stealing/) |
| 2026-05-28 | — | MapRoot: Two Zero-Days Leading to Cross-Tenant RCE | Yanir Tsarimi | blog | [buka](https://enclave.ai/blog/maproot-two-cross-tenant-rce-on-microsoft-planetary-computer/) |
| 2026-05-21 | — | Envade: One-Click RCE in VS Code | Elad Luz | blog | [buka](https://pages.oasis.security/rs/106-PZV-596/images/envade-technical-report.pdf) |
| 2026-05-13 | — | AKS RunCommand Vulnerability Enables Cross-Cluster Privilege Escalation | Ben Zamir | blog | [buka](https://cymulate.com/blog/aks-runcommand-token-theft-cross-cluster-lateral-movement/) |
| 2026-05-04 | — | Copirate 365 at DEF CON: Plundering Microsoft Copilot | Johann Rehberger | blog | [buka](https://embracethered.com/blog/posts/2026/defcon-talk-copirate-365/) |
| 2026-04-30 | — | Bypassing Windows Authentication Reflection Mitigations Part 2 | Guillaume Andre | blog | [buka](https://www.synacktiv.com/en/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part) |
| 2026-04-27 | — | Bypassing Windows Authentication Reflection Mitigations Part 1 | Guillaume Andre | blog | [buka](https://www.synacktiv.com/en/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1) |
| 2026-04-20 | — | How We Could Watch Your Azure SRE Agent in Real Time | Yanir Tsarimi | blog | [buka](https://enclave.ai/blog/anyone-could-watch-your-azure-ai-agents-conversations-in-real-time) |
| 2026-04-15 | — | ShareLeak: Taking the Wheel of Microsoft Copilot Studio | Bar Kaduri | blog | [buka](https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520) |
| 2026-04-06 | — | CVE-2026-26117: Hijacking Azure Arc on Windows | Cymulate Research Lab | blog | [buka](https://cymulate.com/blog/cve-2026-26117-azure-arc-windows-lpe-cloud-identity-takeover/) |
| 2026-03-24 | — | Azure APIM Signup Bypass: 97.9% of Developer Portals Exploitable | Bernard Yip and Elgin Lee | blog | [buka](https://www.praetorian.com/blog/azure-apim-signup-bypass/) |
| 2026-03-05 | — | AST-Filtered eval Is Not a Sandbox: RCE in Semantic Kernel | Daridor | blog | [buka](https://daridor.blog/2026/03/05/ast-filtered-eval-is-not-a-sandbox-remote-code-execution-in-microsoft-semantic-kernel-and-the-ai-infrastructure-pattern-behind-it/) |
| 2026-02-27 | — | Total Recall: Retracing Steps Back to NT AUTHORITY SYSTEM | Filip Dragovic | blog | [buka](https://www.mdsec.co.uk/2026/02/total-recall-retracing-your-steps-back-to-nt-authoritysystem/) |
| 2026-02-26 | — | Ghosts in the Cloud: Hijacking Orphaned Azure Blob Storage | Jotte Sonneveld and Jacob Virsilas | blog | [buka](https://labs.eye.security/ghosts-in-the-cloud-hijacking-orphaned-azure-blob-storage/) |
| 2026-02-12 | — | Bypassing Administrator Protection by Abusing UI Access | James Forshaw | blog | [buka](https://projectzero.google/2026/02/windows-administrator-protection.html) |
| 2026-01-26 | — | Bypassing Windows Administrator Protection | James Forshaw | blog | [buka](https://projectzero.google/2026/26/windows-administrator-protection.html) |
| 2026-01-15 | — | MSSQL and SCCM Elevation of Privilege Vulnerabilities | Chris Thompson | blog | [buka](https://specterops.io/blog/2026/01/15/mssql-and-sccm-elevation-of-privilege-vulnerabilities/) |
| 2026-01-14 | — | CVE-2026-20965: Tenant-Wide RCE via Azure Windows Admin Center | Cymulate Research Lab | blog | [buka](https://cymulate.com/blog/cve-2026-20965-azure-windows-admin-center-tenant-wide-rce/) |
| 2026-01-14 | — | Reprompt: Single-Click Microsoft Copilot Data Theft | Dolev Taler | blog | [buka](https://www.varonis.com/blog/reprompt) |
| 2025-11-20 | — | When Updates Backfire: RCE in Windows Update Health Tools | Martin Warmer | blog | [buka](https://labs.eye.security/rce-windows-update-health-tools/) |
| 2025-11-17 | — | Deleting the BCD through COM as low privileged user | Sarah Dezijn | blog | [buka](https://warpnet.nl/blog/deleting-the-bcd-through-com-as-low-privileged-user/) |
| 2025-09-17 | — | One Token to Rule Them All: Global Admin in every Entra ID tenant | Dirk-jan Mollema | blog | [buka](https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/) |
| 2025-08-12 | — | Zero Click One NTLM: Microsoft Security Patch Bypass | Ruben Enkaoua | blog | [buka](https://cymulate.com/blog/zero-click-one-ntlm-microsoft-security-patch-bypass-cve-2025-50154/) |
| 2025-08-12 | — | GitHub Copilot Remote Code Execution via Prompt Injection | Johann Rehberger | blog | [buka](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) |
| 2025-08-07 | — | Consent and Compromise: Abusing Entra OAuth | Vaisha Bernard | blog | [buka](https://labs.eye.security/consent-and-compromise/) |
| 2025-07-25 | — | How We Rooted Copilot | Eye Security | blog | [buka](https://labs.eye.security/how-we-rooted-copilot/) |
| 2025-06-11 | — | EchoLeak: Zero-Click Prompt Injection in Production LLM | Aim Labs | blog | [buka](https://www.aim.security/lp/aim-labs-echoleak-blogpost) |
| 2025-05-21 | — | BadSuccessor: Abusing dMSA to Escalate Privileges in AD | Yuval Gordon | blog | [buka](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory) |
| 2025-01-02 | — | Microsoft 365 Copilot Generated Images Accessible Without Auth | Johann Rehberger | blog | [buka](https://embracethered.com/blog/posts/2025/m365-copilot-image-generation-without-authentication/) |
| 2021-06-10 | — | Active Directory forest trusts part 2: Trust transitivity | Dirk-jan Mollema | blog | [buka](https://dirkjanm.io/active-directory-forest-trusts-part-two-trust-transitivity/) |

## 4. Catatan

- `n/a` = tanggal tidak dicantumkan di sumber.
- Reward = nominal yang **dilaporkan** penulis/kurator, bukan angka resmi program.
- Entri video adalah rekaman konferensi/meetup, bukan tulisan.
- Tautan mengarah ke tulisan asli, bukan halaman program.
