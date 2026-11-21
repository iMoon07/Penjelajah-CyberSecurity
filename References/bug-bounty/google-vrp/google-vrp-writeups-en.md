# Google & Alphabet VRP — Bug Bounty Writeup Index (EN)

[🇮🇩 Read in Bahasa Indonesia](google-vrp-writeups-id.md)

﷽

> Kumpulan writeup bug bounty Google (dan akuisisi/produk terkait) yang dipublikasikan researcher. Data: judul, tanggal publikasi, author, nominal reward yang **dilaporkan**, jenis (blog/video), dan link laporan live. Nominal bukan jaminan untuk temuan serupa.

## 1. Ringkasan

| Item | Nilai |
|---|---|
| Total entri unik | 196 |
| Entri dengan reward dilaporkan | 119 |
| Reward tertinggi | $500,000 |
| Rentang tanggal | 2021-04-02 s/d 2026-06-11 |

## 2. Top 20 Reward Tertinggi

| # | Reward | Writeup | Author | Date | Type | Link |
|---|---|---|---|---|---|---|
| 1 | **$500,000** | Hacking Google with A.I. for 500000 | brutecat | 2026-06-11 | blog | [open](https://brutecat.com/articles/hacking-google-with-ai/) |
| 2 | **$250,000** | Zero to Calc in Six Days: Inside XBOWs Chrome Full Chain | Brendan Dolan-Gavitt | 2026-10-13 | blog | [open](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain) |
| 3 | **$165,174** | Hacking into Googles Network for 133337 | LiveOverflow | 2021-03-17 | video | [open](https://www.youtube.com/watch?v=g-JgA1hvJzA) |
| 4 | **$148,337** | StubZero: 148337 RCE in Google Cloud Production | brutecat | 2026-05-22 | blog | [open](https://brutecat.com/articles/google-cloud-rce/) |
| 5 | **$107,500** | Turning Google smart speakers into wiretaps for 100k | Matt Kunze | 2022-12-26 | blog | [open](https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html) |
| 6 | **$100,000** | 100k Hacking Prize: Security Bugs in Google Cloud Platform | LiveOverflow | 2020-03-11 | video | [open](https://www.youtube.com/watch?v=J2icGMocQds) |
| 7 | **$97,604.40** | Breaking into Googles GFile for 100k | brutecat | 2026-09-11 | blog | [open](https://bughunters.google.com/blog/breaking-into-googles-gfile-for-100k) |
| 8 | **$90,000** | How I Found a 90000 Remote Code Execution Vulnerability in Google | Simon Kock | 2026-10-12 | blog | [open](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce) |
| 9 | **$70,000** | Accidental 70k Google Pixel Lock Screen Bypass | David Schutz | 2022-11-10 | blog | [open](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/) |
| 10 | **$58,837** | Google Cloud Platform vulnerabilities: BugSWAT | Ezequiel Pereira | 2018-11-14 | video | [open](https://www.youtube.com/watch?v=9pviQ19njIs) |
| 11 | **$50,000** | We Hacked Google A.I. for 50000 | Lupin | 2024-03-04 | blog | [open](https://www.landh.tech/blog/20240304-google-hack-50000/) |
| 12 | **$36,337** | 36k Google App Engine RCE | Ezequiel Pereira | 2019-08-31 | blog | [open](https://www.ezequiel.tech/p/36k-google-app-engine-rce.html) |
| 13 | **$31,337** | RCE in Google Cloud Deployment Manager | Ezequiel Pereira | 2020-05-21 | blog | [open](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html) |
| 14 | **$31,337** | 31k SSRF in Google Cloud Monitoring led to metadata exposure | David Nechuta | 2020-11-12 | blog | [open](https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html) |
| 15 | **$31,337** | 31337 Google Cloud blind SSRF and HANDS-ON labs | Bug Bounty Reports Explained | 2021-04-06 | video | [open](https://www.youtube.com/watch?v=ashSoc59z1Y) |
| 16 | **$31,337** | Explaining the exploit to 31337 Google Cloud blind SSRF | Bug Bounty Reports Explained | 2021-04-09 | video | [open](https://www.youtube.com/watch?v=q0YgfwOndOw) |
| 17 | **$30,000** | The mass CSRFing of *.google.com products | Missoum Said | 2020-10-08 | blog | [open](http://www.missoumsai.com/google-csrfs.html) |
| 18 | **$25,401.10** | 4 Weird Google VRP Bugs in 40 Minutes: Hacktivity 2021 | David Schutz | 2021-10-08 | video | [open](https://www.youtube.com/watch?v=nP_y-Z-FXr0) |
| 19 | **$22,500** | XSS in Google IDX Workstation | sudi | 2025-07-02 | blog | [open](https://sudistark.github.io/2025/07/02/idx.html) |
| 20 | **$20,000** | Few bugs in the google cloud shell | Obmi | 2022-12-26 | blog | [open](https://obmiblog.blogspot.com/2022/12/gcp-2022-few-bugs-in-google-cloud-shell.html) |

## 3. Semua Entri (urut tanggal terbaru)

### 3.1 Dengan reward

| Date | Reward | Writeup | Author | Type | Link |
|---|---|---|---|---|---|
| n/a | $5,000 | Google VRP : oAuth token stealing | Harsh Jaiswal | blog | [open](http://bugdisclose.blogspot.com/2017/08/google-vrp-oauth-token-stealing.html) |
| n/a | $3,133.70 | Open redirects that matter | Tomasz Bojarski | blog | [open](https://sites.google.com/site/bughunteruniversity/best-reports/openredirectsthatmatter) |
| 2026-10-13 | $250,000 | Zero to Calc in Six Days: Inside XBOWs Chrome Full Chain | Brendan Dolan-Gavitt | blog | [open](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain) |
| 2026-10-12 | $90,000 | How I Found a 90000 Remote Code Execution Vulnerability in Google | Simon Kock | blog | [open](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce) |
| 2026-09-11 | $97,604.40 | Breaking into Googles GFile for 100k | brutecat | blog | [open](https://bughunters.google.com/blog/breaking-into-googles-gfile-for-100k) |
| 2026-07-15 | $13,337 | Confused Deputy: Google IdP Universal Account Takeover via Device Code Flow Hijacking | Mohamed Benchikh | blog | [open](https://weirdmachine64.github.io/research/google-oauth-device-code-hijacking.html) |
| 2026-06-11 | $500,000 | Hacking Google with A.I. for 500000 | brutecat | blog | [open](https://brutecat.com/articles/hacking-google-with-ai/) |
| 2026-05-22 | $148,337 | StubZero: 148337 RCE in Google Cloud Production | brutecat | blog | [open](https://brutecat.com/articles/google-cloud-rce/) |
| 2026-03-31 | $14,337 | Hacking Google Support: Leaking millions of customer records | Michael Dalton | blog | [open](https://michaeldalton.au/posts/hacking-google-support) |
| 2025-11-10 | $20,000 | Hacking Gemini: A Multi-Layered Approach | Valentino Massaro | blog | [open](https://buganizer.cc/hacking-gemini-a-multi-layered-approach-md) |
| 2025-07-02 | $22,500 | XSS in Google IDX Workstation | sudi | blog | [open](https://sudistark.github.io/2025/07/02/idx.html) |
| 2025-07-01 | $3,133.70 | My first bug in Google Cloud: Command injection in Vertex AI | Valentino Massaro | blog | [open](https://blog.3133700.xyz/bug_vertex_ai) |
| 2025-06-27 | $13,340 | 1-click Oauth client takeover through henhouse UI | rand0m_unk0wn | blog | [open](https://random-unknown-username.github.io/) |
| 2025-06-09 | $5,000 | Bruteforcing the phone number of any Google user | brutecat | blog | [open](https://brutecat.com/articles/leaking-google-phones) |
| 2025-05-22 | $8,500 | Client-side RCE via improper URL parsing in Google Web Designer for Windows (CVE-2025-4613) | Balint Magyar | blog | [open](https://balintmagyar.com/articles/google-web-designer-path-traversal-client-side-rce-cve-2025-4613) |
| 2025-04-02 | $11,250 | Client-side RCE via symlink following in Google Web Designer for macOS/Linux (CVE-2025-1079) | Balint Magyar | blog | [open](https://balintmagyar.com/articles/google-web-designer-symlink-client-side-rce-cve-2025-1079) |
| 2025-03-13 | $20,000 | Disclosing YouTube Creator Emails for a 20k Bounty | brutecat | blog | [open](https://brutecat.com/articles/youtube-creator-emails) |
| 2025-02-12 | $10,000 | Leaking the email of any YouTube user for 10000 | brutecat | blog | [open](https://brutecat.com/articles/leaking-youtube-emails) |
| 2024-09-25 | $4,837 | XS-Search on Google Photos | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2024/09/25/photos/) |
| 2024-09-19 | $4,133.70 | Using YouTube to steal your files | Lyra Rebane | blog | [open](https://lyra.horse/blog/2024/09/using-youtube-to-steal-your-files/) |
| 2024-08-01 | $3,133.70 | idx.google.com XSS | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2024/08/01/projectidx/) |
| 2024-07-17 | $8,500 | Unveiling TE.0 HTTP Request Smuggling | Paolo Arnolfo | blog | [open](https://www.bugcrowd.com/blog/unveiling-te-0-http-request-smuggling-discovering-a-critical-vulnerability-in-thousands-of-google-cloud-websites/) |
| 2024-03-04 | $50,000 | We Hacked Google A.I. for 50000 | Lupin | blog | [open](https://www.landh.tech/blog/20240304-google-hack-50000/) |
| 2023-11-14 | $10,000 | Uncovering a crazy privilege escalation from Chrome extensions | Derin Eryilmaz | blog | [open](https://0x44.xyz/blog/cve-2023-4369/) |
| 2023-08-18 | $18,833.70 | Google Extensions | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2023/08/18/extensions/) |
| 2023-06-21 | $4,133.70 | Unveiling a Critical Authentication Bypass Vulnerability in Google Cloud API Gateway | Securing Bits | blog | [open](https://securingbits.com/bypassing-google-cloud-api-gateway) |
| 2023-06-11 | $7,500 | googlesource.com access_token leak | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2023/06/11/googlesource/) |
| 2023-06-09 | $6,000 | XSS in GMAIL Dynamic Email (AMP for Email) | asdqw3 | blog | [open](https://asdqw3.medium.com/xss-in-gmail-dynamic-email-amp-for-email-3872d6052a0d) |
| 2023-03-13 | $5,000 | The Time I Hacked Googles Manual Actions Database | Tom Anthony | blog | [open](https://www.tomanthony.co.uk/blog/googles-manual-actions-hack/) |
| 2023-03-11 | $1,837 | CCAI XSS | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2023/03/11/ccai/) |
| 2023-01-15 | $3,133.70 | XSS using postMessage in Google Cloud Theia notebooks | Sreeram KL | blog | [open](https://blog.geekycat.in/xss-using-postmessage-in-google-cloud-theia-notebooks/) |
| 2023-01-13 | $3,133.70 | Bypassing authorization in Google Cloud Workstations | Sivanesh Ashok | blog | [open](https://blog.stazot.com/ssh-key-injection-google-cloud/) |
| 2023-01-12 | $6,000 | SSH key injection in Google Cloud Compute Engine | Sivanesh Ashok | blog | [open](https://blog.stazot.com/auth-bypass-in-google-cloud-workstations/) |
| 2023-01-12 | $3,133.70 | Client-Side SSRF to Google Cloud Project Takeover | Sreeram KL | blog | [open](https://blog.geekycat.in/client-side-ssrf-to-google-cloud-project-takeover/) |
| 2023-01-06 | $2,337 | Identity-Aware Proxy Misconfiguration: Google Cloud Vulnerability | Borna Nematzadeh | blog | [open](https://medium.com/@LogicalHunter/identity-aware-proxy-misconfiguration-google-cloud-vulnerability-813d2a07a4ed) |
| 2022-12-26 | $107,500 | Turning Google smart speakers into wiretaps for 100k | Matt Kunze | blog | [open](https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html) |
| 2022-12-26 | $20,000 | Few bugs in the google cloud shell | Obmi | blog | [open](https://obmiblog.blogspot.com/2022/12/gcp-2022-few-bugs-in-google-cloud-shell.html) |
| 2022-11-10 | $70,000 | Accidental 70k Google Pixel Lock Screen Bypass | David Schutz | blog | [open](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/) |
| 2022-09-06 | $3,133.70 | IDOR leads to removing members from any Google Chat Space | Vivek M | blog | [open](https://web.archive.org/web/20220906173240/https://hopesamples.blogspot.com/2022/09/idor-leads-to-removing-members-from-any.html) |
| 2022-07-26 | $8,133.70 | Google Play and DevSite XSS | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2022/07/26/google-xss/) |
| 2022-04-23 | $1,337 | Launching a Supply Chain Counterattack Against Google and OpenSSF | Alan Cao | blog | [open](https://codemuch.tech/2022/04/23/supply-chain-counterattack/) |
| 2022-02-06 | $2,674 | Auth Bypass in Google Assistant | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0012) |
| 2022-02-06 | $1,337 | Auth Bypass in com.google.android.googlequicksearchbox | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0013) |
| 2021-12-30 | $5,000 | Email storage leaking ticket-attachment | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2021/12/30/ticket-attachments/) |
| 2021-12-28 | $3,133.70 | RCE in Google Cloud Dataflow | Mike Brancato | blog | [open](https://mbrancato.github.io/2021/12/28/rce-dataflow.html) |
| 2021-12-21 | $5,000 | Google Cloud Shell XSS | NDevTK | blog | [open](https://ndevtk.github.io/writeups/2021/12/30/cloud-shell-xss/) |
| 2021-12-05 | $6,267.40 | SSRF vulnerability in AppSheet | David Nechuta | blog | [open](https://nechudav.blogspot.com/2021/12/ssrf-vulnerability-in-appsheet-google.html) |
| 2021-10-24 | $7,500 | A 7500 Google sites IDOR | r0ckin | blog | [open](https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/) |
| 2021-10-08 | $25,401.10 | 4 Weird Google VRP Bugs in 40 Minutes: Hacktivity 2021 | David Schutz | video | [open](https://www.youtube.com/watch?v=nP_y-Z-FXr0) |
| 2021-09-10 | $1,337 | Bypassing GCP Org Policy with Custom Metadata | Kat Traxler | blog | [open](https://kattraxler.github.io/gcp/hacking/2021/09/10/gcp-org-policy-bypass-ai-notebooks.html) |
| 2021-09-06 | $4,133.70 | 2 CSRF 1 IDOR on Google Marketing Platform | Apapedulimu | blog | [open](https://apapedulimu.click/story-of-idor-on-google-product/) |
| 2021-06-13 | $3,133.70 | Privilege escalation on dialogflow.cloud.google.com | lalka | blog | [open](https://medium.com/@lalka_test/google-vrp-privilege-escalation-on-https-dialogflow-cloud-google-com-599af6c4516d) |
| 2021-06-09 | $500 | Author spoofing in Google Colaboratory | Zohar Shacha | blog | [open](https://www.ehpus.com/post/author-spoofing-in-google-colaboratory) |
| 2021-05-31 | $10,000 | AppCaches forgotten tales | Luan Herrera | blog | [open](https://blog.lbherrera.me/posts/appcache-forgotten-tales/) |
| 2021-04-13 | $1,337 | Google Photos Theft of Database and Arbitrary Files Android Vulnerability | Rahul Kankrale | blog | [open](https://servicenger.com/blog/mobile/google-photos-theft-of-database-arbitrary-files-android-vulnerability/) |
| 2021-04-09 | $31,337 | Explaining the exploit to 31337 Google Cloud blind SSRF | Bug Bounty Reports Explained | video | [open](https://www.youtube.com/watch?v=q0YgfwOndOw) |
| 2021-04-06 | $31,337 | 31337 Google Cloud blind SSRF and HANDS-ON labs | Bug Bounty Reports Explained | video | [open](https://www.youtube.com/watch?v=ashSoc59z1Y) |
| 2021-04-05 | $6,000 | I Built a TV That Plays All of Your Private YouTube Videos | David Schutz | blog | [open](https://bugs.xdavidhu.me/google/2021/04/05/i-built-a-tv-that-plays-all-of-your-private-youtube-videos/) |
| 2021-04-02 | $100 | Play a game get Subscribed to my channel: YouTube Clickjacking Bug | Sriram Kesavan | blog | [open](https://infosecwriteups.com/play-a-game-get-subscribed-to-my-channel-youtube-clickjacking-bug-googlevrp-6ce1d15542d3) |
| 2021-03-17 | $165,174 | Hacking into Googles Network for 133337 | LiveOverflow | video | [open](https://www.youtube.com/watch?v=g-JgA1hvJzA) |
| 2021-03-11 | $3,133.70 | How I Get Blind XSS At Google With Dork | Rio Mulyadi Pulungan | blog | [open](https://apapedulimu.click/google-vrp-how-i-get-blind-xss-at-google-with-dork-first-bounty-and-hof/) |
| 2021-03-08 | $5,000 | 5000 YouTube IDOR | Bug Bounty Reports Explained | video | [open](https://www.youtube.com/watch?v=FzT3Z7tgDSQ) |
| 2021-01-18 | $1,337 | The Embedded YouTube Player Told Me What You Were Watching | David Schutz | blog | [open](https://bugs.xdavidhu.me/google/2021/01/18/the-embedded-youtube-player-told-me-what-you-were-watching-and-more/) |
| 2021-01-11 | $5,000 | Stealing Your Private YouTube Videos One Frame at a Time | David Schutz | blog | [open](https://bugs.xdavidhu.me/google/2021/01/11/stealing-your-private-videos-one-frame-at-a-time/) |
| 2021-01-08 | $3,133.70 | Blind XSS in Google Analytics Admin Panel | Ashish Dhone | blog | [open](https://ashketchum.medium.com/blind-xss-in-google-analytics-admin-panel-3133-70-2185d1cce82a) |
| 2020-11-12 | $31,337 | 31k SSRF in Google Cloud Monitoring led to metadata exposure | David Nechuta | blog | [open](https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html) |
| 2020-10-27 | $6,337 | The YouTube bug that allowed unlisted uploads to any channel | Ryan Kovatch | blog | [open](https://infosecwriteups.com/the-youtube-bug-that-allowed-uploads-to-any-channel-3b41c7b7902a) |
| 2020-10-08 | $30,000 | The mass CSRFing of *.google.com products | Missoum Said | blog | [open](http://www.missoumsai.com/google-csrfs.html) |
| 2020-10-01 | $5,000 | Google bug bounty: XSS to Cloud Shell instance takeover (RCE as root) | Omar Espino | blog | [open](https://omespino.com/write-up-google-bug-bounty-xss-to-cloud-shell-instance-takeover-rce-as-root-5000-usd/) |
| 2020-09-20 | $500 | How I earned 500 from Google: Flaw in Authentication | Hemant Patidar | blog | [open](https://infosecwriteups.com/how-i-earned-500-from-google-flaw-in-authentication-a40018c05616/) |
| 2020-09-10 | $15,000 | Universal XSS in Android WebView (CVE-2020-6506) | Alesandro Ortiz | blog | [open](https://alesandroortiz.com/articles/uxss-android-webview-cve-2020-6506/) |
| 2020-09-08 | $10,000 | XSS Fix Bypass: 10000 bounty in Google Maps | Zohar Shacha | blog | [open](https://www.ehpus.com/post/xss-fix-bypass-10000-bounty-in-google-maps) |
| 2020-09-07 | $1,337 | My first bug in google and how i got CSRF token for victim account | Oday Alhalbe | blog | [open](https://medium.com/@odayalhalbe1/my-first-bug-in-google-and-how-i-got-csrf-token-for-victim-account-rather-than-bypass-it-1337-bf01261feb47) |
| 2020-08-25 | $1,337 | How I Tracked Your Mother: Tracking Waze drivers using UI elements | Peter Gasper | blog | [open](https://www.malgregator.com/post/waze-how-i-tracked-your-mother/) |
| 2020-07-31 | $4,133.70 | Script Gadgets! Google Docs XSS Vulnerability Walkthrough | LiveOverflow | video | [open](https://www.youtube.com/watch?v=aCexqB9qi70) |
| 2020-07-28 | $1,337 | Authorization bypass in Googles ticketing system (Google-GUTS) | Zohar Shacha | blog | [open](https://www.ehpus.com/post/authorization-bypass-in-google-s-ticketing-system) |
| 2020-07-17 | $5,000 | Idor in google product | baluz | blog | [open](https://balook.medium.com/idor-in-google-datastudio-google-com-f2fa51b763de) |
| 2020-07-14 | $6,267.40 | Hunting postMessage Vulnerabilities | Gary O'leary-Steele | blog | [open](https://web.archive.org/web/20211016075506/https://insight.claranet.co.uk/technical-blogs/hunting-postmessage-vulnerabilities) |
| 2020-06-15 | $3,133.70 | SMTP Injection in Gsuite | Zohar Shacha | blog | [open](https://www.ehpus.com/post/smtp-injection-in-gsuite) |
| 2020-06-06 | $500 | How i earned 500 from google by change one character | Oday Alhalbe | blog | [open](https://medium.com/@odayalhalbe1/how-i-earned-500-from-google-by-change-one-character-8350d2b618e5) |
| 2020-05-21 | $31,337 | RCE in Google Cloud Deployment Manager | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html) |
| 2020-05-08 | $4,133.70 | Bypass XSS filter using HTML Escape | Syahri Ramadan | blog | [open](https://medium.com/@adonkidz7/bypass-xss-filter-using-html-escape-f2e06bebc8c3) |
| 2020-05-07 | $3,133.70 | DOM-Based XSS at accounts.google.com by Google Voice Extension | Missoum Said | blog | [open](http://www.missoumsai.com/google-accounts-xss.html) |
| 2020-04-30 | $6,267.40 | Researching Polymorphic Images for XSS on Google Scholar | Lorenzo Stella | blog | [open](https://blog.doyensec.com/2020/04/30/polymorphic-images-for-xss.html) |
| 2020-03-27 | $3,133.70 | 3133.7 Google Bug Bounty Writeup: XSS Vulnerability | Pethuraj M | blog | [open](https://pethuraj.com/blog/google-bug-bounty-writeup/) |
| 2020-03-11 | $100,000 | 100k Hacking Prize: Security Bugs in Google Cloud Platform | LiveOverflow | video | [open](https://www.youtube.com/watch?v=J2icGMocQds) |
| 2020-03-10 | $3,133.70 | Cookie Tossing to RCE on Google Cloud JupyterLab | s1r1us | blog | [open](https://blog.s1r1us.ninja/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks) |
| 2020-03-08 | $6,000 | The unexpected Google wide domain check bypass | David Schutz | blog | [open](https://bugs.xdavidhu.me/google/2020/03/08/the-unexpected-google-wide-domain-check-bypass/) |
| 2020-03-07 | $5,000 | Google Ads Self-XSS and Html Injection 5000 | Syahri Ramadan | blog | [open](https://medium.com/@adonkidz7/google-ads-self-xss-html-injection-5000-52280da76c80) |
| 2019-12-30 | $3,133.70 | How did I earn 3133.70 from Google Translator (XSS) | Beri Bey | blog | [open](https://medium.com/monetary/how-did-i-earn-3133-70-from-google-translator-9becf942dbdc) |
| 2019-12-15 | $5,000 | The File uploading CSRF in Google Cloud Shell Editor | Obmi | blog | [open](https://obmiblog.blogspot.com/2019/12/gcp-5k-file-uploading-csrf.html) |
| 2019-12-15 | $5,000 | The oauth token hijacking in Google Cloud Shell Editor | Obmi | blog | [open](https://obmiblog.blogspot.com/2019/12/gcp-5k-oauth-token-hijack.html) |
| 2019-12-15 | $5,000 | The XSS (type II) in Google Cloud Shell Editor | Obmi | blog | [open](https://obmiblog.blogspot.com/2019/12/gcp-5k-xss-type-ii.html) |
| 2019-11-29 | $1,337 | Writeup for the 2019 Google Cloud Platform VRP Prize | Missoum Said | blog | [open](https://medium.com/@missoum1307/writeup-for-the-2019-google-cloud-platform-vrp-prize-4e104ef9f204) |
| 2019-10-01 | $5,000 | Google Paid Me to Talk About a Security Issue | LiveOverflow | video | [open](https://www.youtube.com/watch?v=E-P9USG6kLs) |
| 2019-08-31 | $36,337 | 36k Google App Engine RCE | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/p/36k-google-app-engine-rce.html) |
| 2019-07-20 | $13,337 | Into the Borg: SSRF inside Google production network | Enguerran Gillier | blog | [open](https://opnsec.com/2018/07/into-the-borg-ssrf-inside-google-production-network/) |
| 2019-05-21 | $13,337 | Google Bug Bounty: LFI on Production Servers in springboard.google.com | Omar Espino | blog | [open](https://omespino.com/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/) |
| 2019-03-26 | $3,133.70 | How I could have hijacked a victims YouTube notifications | Yash Sodha | blog | [open](https://hackademic.co.in/youtube-bug/) |
| 2019-01-30 | $7,500 | 7.5k Google Cloud Platform organization issue | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html) |
| 2019-01-25 | $3,133.70 | How I abused 2FA to maintain persistence after a password change | Luke Berner | blog | [open](https://medium.com/@lukeberner/how-i-abused-2fa-to-maintain-persistence-after-a-password-change-7e3f455b71a1) |
| 2019-01-18 | $10,000 | 10k host header | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/p/10k-host-header.html) |
| 2018-12-05 | $500 | Billion Laugh Attack in https://sites.google.com | Antonio Sanso | blog | [open](https://blog.intothesymmetry.com/2018/12/billion-laugh-attack-in.html) |
| 2018-11-14 | $58,837 | Google Cloud Platform vulnerabilities: BugSWAT | Ezequiel Pereira | video | [open](https://www.youtube.com/watch?v=9pviQ19njIs) |
| 2018-11-11 | $7,500 | Clickjacking on Google MyAccount Worth 7500 | Apapedulimu | blog | [open](https://apapedulimu.click/clickjacking-on-google-myaccount-worth-7500/) |
| 2018-04-06 | $5,000 | Missing access control in Google play store | Vishwaraj Bhattrai | blog | [open](https://vishwarajbhattrai.wordpress.com/2019/06/03/missing-access-control-at-play-store/) |
| 2018-03-31 | $5,000 | 5k Service dependencies | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/p/5k-service-dependencies.html) |
| 2018-03-07 | $13,337 | Stored XSS, and SSRF in Google using the Dataset Publishing Language | Craig Arendt | blog | [open](https://s1gnalcha0s.github.io/dspl/2018/03/07/Stored-XSS-and-SSRF-Google.html) |
| 2018-02-24 | $13,337 | Bypassing Googles authentication to access their Internal Admin panels | Vishnu Prasad P G | blog | [open](https://infosecwriteups.com/bypassing-googles-fix-to-access-their-internal-admin-panels-12acd3d821e3) |
| 2018-02-14 | $7,500 | 7.5k Google services mix-up | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/p/75k-google-services-mix-up.html) |
| 2017-10-30 | $15,600 | How I hacked Googles bug tracking system itself for 15600 in bounties | Alex Birsan | blog | [open](https://medium.com/@alex.birsan/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5) |
| 2017-03-09 | $5,000 | How I found a 5000 Google Maps XSS (by fiddling with Protobuf) | Marin Moulinier | blog | [open](https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff) |
| 2017-02-26 | $3,133.70 | Exploiting Clickjacking Vulnerability To Steal User Cookies | Jasminder Pal Singh | blog | [open](https://jasminderpalsingh.info/exploiting-google-clickjacking-vulnerability-to-steal-user-cookies/) |
| 2016-10-09 | $6,000 | How I got 6000$ from Google (Google Cloudshell RCE) | Pranav Venkat | blog | [open](https://medium.com/@pranavvenkats/how-i-got-6000-from-google-a4670aa4158d) |
| 2016-08-26 | $500 | getClass | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/p/500-getclass.html) |
| 2015-06-26 | $3,133.70 | Youtube Editor XSS Vulnerability | Jasminder Pal Singh | blog | [open](https://jasminderpalsingh.info/youtube-editor-stored-dom-based-and-self-executed-xss-vulnerability/) |
| 2014-10-31 | $5,000 | The 5000$ Google XSS | Patrik Fehrenbach | blog | [open](https://blog.it-securityguard.com/bugbounty-the-5000-google-xss/) |
| 2014-10-26 | $1,337 | Youtube XSS Vulnerability (Stored to Self Executed) | Jasminder Pal Singh | blog | [open](https://jasminderpalsingh.info/youtube-xss-vulnerability-stored-self-executed/) |
| 2013-09-15 | $3,133.70 | XSRF and Cookie manipulation on google.com | Michele Spagnuolo | blog | [open](https://blog.miki.it/2013/9/15/xsrf-cookie-setting-google/) |

### 3.2 Tanpa reward / tidak dipublikasikan

| Date | Reward | Writeup | Author | Type | Link |
|---|---|---|---|---|---|
| n/a | — | Unauth meetings access | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/google-meet/authorization-bugs) |
| n/a | — | XSS vulnerability in Google Cloud Shell code editor through mini-browser endpoint | Psi | blog | [open](https://xn--9xa.fun/i/ZK9Kv) |
| n/a | — | Information leakage vulnerability in Google Cloud Shell proxy service | Psi | blog | [open](https://xn--9xa.fun/i/KPMGz) |
| n/a | — | XSS vulnerability in Google Cloud Shell code editor through SVG files | Psi | blog | [open](https://xn--9xa.fun/i/92uQC) |
| n/a | — | CSWSH vulnerability in Google Cloud Shell code editor | Psi | blog | [open](https://xn--9xa.fun/i/yvpMj) |
| n/a | — | Voice Squatting and Voice Masquerading Attack against Amazon Alexa and Google Home Actions | VoiceVPAsec | blog | [open](https://sites.google.com/site/voicevpasec/) |
| n/a | — | Blind XSS against a Googler | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/hire-with-google/blind-xss) |
| n/a | — | Multiple XSSs on hire.withgoogle.com | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/hire-with-google/xsses) |
| n/a | — | Auth Issues on hire.withgoogle.com | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/hire-with-google/auth-issues) |
| n/a | — | G Suite - Device Management XSS | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/gsuite/bookmark-xss-device-management) |
| 2022-03-08 | — | Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities | Unit 42 | blog | [open](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/) |
| 2021-07-13 | — | Unencrypted HTTP Links to Google Scholar in Search | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0010) |
| 2021-07-08 | — | IDOR on clientauthconfig.googleapis.com | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0009) |
| 2021-06-25 | — | Google Compute Engine (GCE) VM takeover via DHCP flood | Imre Rad | blog | [open](https://github.com/irsl/gcp-dhcp-takeover-code-exec) |
| 2021-05-05 | — | How I Hacked Google App Engine: Anatomy of a Java Bytecode Exploit | Robert Grosse | blog | [open](https://blog.polybdenum.com/2021/05/05/how-i-hacked-google-app-engine-anatomy-of-a-java-bytecode-exploit.html) |
| 2021-04-29 | — | De-anonymising Anonymous Animals in Google Workspace | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0003) |
| 2021-04-20 | — | Auth Bypass in Google Workspace Real Time Collaboration | David Schutz | blog | [open](https://feed.bugs.xdavidhu.me/bugs/0002) |
| 2021-03-22 | — | File System Access API vulnerabilities (CVE-2021-21123) | Maciej Pulikowski | blog | [open](https://github.com/Puliczek/CVE-2021-21123-PoC-Google-Chrome) |
| 2021-03-21 | — | How I made it to Google HOF | Sudhanshu Rajbhar | blog | [open](https://infosecwriteups.com/how-i-made-it-to-google-hof-f1cec85fdb1b) |
| 2021-03-08 | — | Google VRP N/A: SSRF Bypass with Quadzero in Google Cloud Monitoring | Omar Espino | blog | [open](https://omespino.com/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/) |
| 2021-02-28 | — | Metadata service MITM allows root privilege escalation (EKS / GKE) | Etienne Champetier | blog | [open](https://blog.champtar.fr/Metadata_MITM_root_EKS_GKE/) |
| 2021-02-16 | — | Dropping a shell in Googles Cloud SQL (the speckle-umbrella story) | Imre Rad | blog | [open](https://irsl.medium.com/dropping-a-shell-in-googles-cloud-sql-the-speckle-umbrella-story-f9375bd4960d) |
| 2021-01-27 | — | Hijacking Google Drive Files through Google Docs Sharing | santuySec | blog | [open](https://santuysec.id/2021/01/27/hijacking-google-drive-files-documents-photo-video-through-google-docs-sharing/) |
| 2020-12-30 | — | Getting my first Google VRP trophies | Imre Rad | blog | [open](https://irsl.medium.com/getting-my-first-google-vrp-trophies-b56d700face) |
| 2020-12-27 | — | Google VRP Hijacking Google Docs Screenshots | Sreeram KL | blog | [open](https://blog.geekycat.in/google-vrp-hijacking-your-screenshots/) |
| 2020-12-22 | — | SSTI in Google Maps | Zohar Shacha | blog | [open](https://www.ehpus.com/post/ssti-in-google-maps) |
| 2020-12-21 | — | Remote code execution when open a project in android studio | houjingyi | blog | [open](https://seclists.org/fulldisclosure/2020/Dec/43) |
| 2020-12-19 | — | Google VRP: Sandboxed RCE as root on Apigee API proxies | Omar Espino | blog | [open](https://omespino.com/write-up-google-vrp-n-a-sandboxed-rce-as-root-on-apigee-api-proxies/) |
| 2020-10-26 | — | Deciphering Googles mysterious batchexecute system | Ryan Kovatch | blog | [open](https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c) |
| 2020-10-15 | — | CVE-2020-15157 ContainerDrip Write-up | Brad Geesaman | blog | [open](https://darkbit.io/blog/cve-2020-15157-containerdrip) |
| 2020-09-29 | — | Public Bucket Allowed Access to Images on Upcoming Google Cloud Blog Posts | Thomas Orlita | blog | [open](https://websecblog.com/vulns/public-google-cloud-blog-bucket/) |
| 2020-08-26 | — | Auth bypass: Leaking Google Cloud service accounts and projects | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/2020/08/leaking-google-cloud-projects.html) |
| 2020-08-22 | — | The Short tale of two bugs on Google Cloud Product | Sriram Kesavan | blog | [open](https://medium.com/bugbountywriteup/the-short-tale-of-two-bugs-on-google-cloud-product-google-vrp-resolved-47c913dca8fc) |
| 2020-08-19 | — | The Confused Mailman: Sending SPF and DMARC passing mail as any Gmail or G Suite customer | Allison Husain | blog | [open](https://ezh.es/blog/2020/08/the-confused-mailman-sending-spf-and-dmarc-passing-mail-as-any-gmail-or-g-suite-customer/) |
| 2020-08-18 | — | How to contact Google SRE: Dropping a shell in Cloud SQL | Ezequiel Pereira | blog | [open](https://www.ezequiel.tech/2020/08/dropping-shell-in.html) |
| 2020-08-18 | — | Three More Google Cloud Shell Bugs Explained | David Dworken | blog | [open](https://blog.daviddworken.com/posts/cloud-shell-bugs-explained/) |
| 2020-08-17 | — | Firebase Cloud Messaging Service Takeover | Abss | blog | [open](https://abss.me/posts/fcm-takeover/) |
| 2020-08-15 | — | How I was able to send Authentic Emails as others | Sriram Kesavan | blog | [open](https://infosecwriteups.com/how-i-was-able-to-send-authentic-emails-as-others-google-vrp-resolved-2af94295f326) |
| 2020-06-04 | — | Privilege Escalation in Google Cloud Platforms OS Login | Chris Moberly | blog | [open](https://gitlab.com/gitlab-com/gl-security/gl-redteam/red-team-tech-notes/-/tree/master/oslogin-privesc-june-2020) |
| 2020-06-04 | — | Three Privilege Escalation Bugs in Google Cloud Platforms OS Login | initstring | blog | [open](https://initblog.com/2020/oslogin-privesc/) |
| 2020-05-10 | — | Bypassing Firebase authorization to create custom goo.gl subdomains | Thomas Orlita | blog | [open](https://websecblog.com/vulns/bypassing-firebase-authorization-to-create-custom-goo-gl-subdomains/) |
| 2020-05-07 | — | Google Acquisition XSS (Apigee) | TnMch | blog | [open](https://medium.com/@TnMch/google-acquisition-xss-apigee-5479d7b5dc4) |
| 2020-05-03 | — | DOM XSS in Gmail with a little help from Chrome | Enguerran Gillier | blog | [open](https://opnsec.com/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome/) |
| 2020-01-12 | — | Information Disclosure Vulnerability in the Google Cloud Speech-to-Text API | Dan Maas | blog | [open](https://www.dcine.com/2020/01/12/information-disclosure-vulnerability-in-the-google-cloud-speech-to-text-api/) |
| 2019-12-19 | — | SSRF in Google Cloud Platform StackDriver | Ron Chan | blog | [open](https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/) |
| 2019-12-16 | — | 4 Google Cloud Shell bugs explained | Wouter ter Maat | blog | [open](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-introduction/) |
| 2019-12-09 | — | BlackAlps 2019: Google Bug Hunters | Eduardo Vela Nava | video | [open](https://www.youtube.com/watch?v=DTXUMBc1zEc) |
| 2019-11-18 | — | XSS in GMail AMP4Email via DOM Clobbering | Michal Bentkowski | blog | [open](https://research.securitum.com/xss-in-amp4email-dom-clobbering/) |
| 2019-09-09 | — | Combination of techniques lead to DOM Based XSS in Google | Sasi Levi | blog | [open](http://sasi2103.blogspot.com/2016/09/combination-of-techniques-lead-to-dom.html) |
| 2019-07-10 | — | Gsuite Hangouts Chat 5k IDOR | Cameron Vincent | blog | [open](https://secreltyhiddenwriteups.blogspot.com/2018/07/gsuite-hangouts-chat-5k-idor.html) |
| 2019-04-27 | — | Broken Access: Posting to Google private groups through any user in the group | Elber Andre | blog | [open](https://medium.com/@elber333/broken-access-posting-to-google-private-groups-through-any-user-in-the-group-3becfa818894) |
| 2019-04-23 | — | Best Of Google VRP 2018 | Daniel Stelter-Gliese | video | [open](https://www.youtube.com/watch?v=mJwZfRXs83M) |
| 2019-03-31 | — | XSS on Google Search: Sanitizing HTML in The Client | LiveOverflow | video | [open](https://www.youtube.com/watch?v=lG7U3fuNw3A) |
| 2019-03-29 | — | Inserting arbitrary files into anyones Google Earth Projects Archive | Thomas Orlita | blog | [open](https://websecblog.com/vulns/google-earth-studio-vulnerability/) |
| 2019-02-12 | — | Hacking YouTube for fun and profit | Alexandru Coltuneac | blog | [open](https://www.linkedin.com/pulse/hacking-youtube-fun-profit-alexandru-coltuneac/) |
| 2019-01-31 | — | LFI in Apigee portals | Wouter ter Maat | blog | [open](https://offensi.com/2019/01/31/lfi-in-apigee-portals/) |
| 2018-12-12 | — | XSSing Google Code-in thanks to improperly escaped JSON data | Thomas Orlita | blog | [open](https://websecblog.com/vulns/google-code-in-xss/) |
| 2018-12-11 | — | Clickjacking DOM XSS on Google.org | Thomas Orlita | blog | [open](https://websecblog.com/vulns/clickjacking-xss-on-google-org/) |
| 2018-11-25 | — | XSS in Googles Acquisition | Abartan Dhakal | blog | [open](https://www.secjuice.com/google-hall-of-fame/) |
| 2018-11-19 | — | XS-Searching Googles bug tracker to find out vulnerable source code | Luan Herrera | blog | [open](https://medium.com/@luanherrera/xs-searching-googles-bug-tracker-to-find-out-vulnerable-source-code-50d8135b7549) |
| 2018-10-04 | — | GoogleMeetRoulette: Joining random meetings | Martin Vigo | blog | [open](https://www.martinvigo.com/googlemeetroulette/) |
| 2018-09-05 | — | Reflected XSS in Google Code Jam | Thomas Orlita | blog | [open](https://websecblog.com/vulns/reflected-xss-in-google-code-jam/) |
| 2018-08-22 | — | Liking GitHub repositories on behalf of other users: Stored XSS in WebComponents.org | Thomas Orlita | blog | [open](https://websecblog.com/vulns/stored-xss-in-webcomponents-org/) |
| 2018-05-25 | — | Waze remote vulnerabilities | PanguTeam | blog | [open](http://blog.appscan.io/index.php/2018/05/25/waze-remote-vulnerability-technical-report/) |
| 2018-03-28 | — | Stored XSS on biz.waze.com | Rojan Rijal | blog | [open](https://sites.google.com/securifyinc.com/vrp-writeups/waze/waze-xss) |
| 2018-02-19 | — | Google bugs stories and the shiny pixelbook | Missoum Said | blog | [open](https://web.archive.org/web/20210426142214/https://bughunt1307.herokuapp.com/googlebugs.html) |
| 2017-06-21 | — | nullcon Goa 2017: Great Bugs In Google VRP In 2016 | Martin Straka and Karshan Sharma | video | [open](https://www.youtube.com/watch?v=zs_nEJ9fh_4) |
| 2017-06-08 | — | RuhrSec 2017: Secrets of the Google VRP | Krzysztof Kotowicz | video | [open](https://www.youtube.com/watch?v=ueEsOnHJZ80) |
| 2017-03-01 | — | Ok Google Give Me All Your Internal DNS Information | Julien Ahrens | blog | [open](https://www.rcesecurity.com/2017/03/ok-google-give-me-all-your-internal-dns-information/) |
| 2017-01-04 | — | fastboot oem sha1sum | Roee Hay | blog | [open](https://securityresear.ch/2017/01/04/fastboot-oem-sha1sum/) |
| 2016-11-29 | — | War Stories from Googles Vulnerability Reward Program | Gabor Molnar | video | [open](https://www.youtube.com/watch?v=QoE0M7v84ZU) |
| 2016-02-28 | — | Stored Reflected and DOM XSS in Google for Work Connect (GWC) | Ashar Javed | blog | [open](http://respectxss.blogspot.com/2016/02/stored-reflected-and-dom-xss-in-google.html) |
| 2015-12-08 | — | Creative bug which result Stored XSS on m.youtube.com | Sasi Levi | blog | [open](http://sasi2103.blogspot.com/2015/12/creative-bug-which-result-stored-xss-on.html) |
| 2015-10-29 | — | XSS in YouTube Gaming | Ashar Javed | blog | [open](http://respectxss.blogspot.com/2015/10/xss-in-youtube-gaming.html) |
| 2014-08-13 | — | I hate you so I pawn your Google Open Gallery | Ahmad Ashraff | blog | [open](https://blog.yappare.com/2014/08/i-hate-you-so-i-pawn-your-google-open.html) |
| 2014-01-10 | — | Again from Nay to Yay in Google Vulnerability Reward Program | Ahmad Ashraff | blog | [open](https://blog.yappare.com/2014/01/again-from-nay-to-yay-in-google.html) |
| 2013-07-08 | — | Stored XSS in GMail | Michele Spagnuolo | blog | [open](https://blog.miki.it/2013/7/8/stored-xss-in-gmail/) |

## 4. Catatan

- `n/a` = tanggal tidak dicantumkan di sumber.
- Nominal = reward yang **dilaporkan** researcher/kurator, bukan angka resmi Google.
- Sebagian entri video (YouTube) adalah rekaman conference/meetup, bukan writeup teks.
- Link mengarah ke writeup asli (blog/researcher), bukan ke halaman program.
