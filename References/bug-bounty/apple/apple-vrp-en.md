# Apple Security Bounty — Bug Bounty Writeup Index (EN)

![Apple Security Bounty](thumbnail.png)

[🇮🇩 Read in Bahasa Indonesia](apple-vrp-id.md)

﷽

<details>
<summary><b>Details — Apple Security Bounty</b></summary>

- **Program**: Apple Security Bounty (product-security@apple.com).
- **Scope**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS, Safari/WebKit, iCloud, Apple services.
- **Max reward**: up to $2,000,000 (zero-click kernel RCE chain); bonuses can exceed $5M total.
- **Not eligible**: third-party apps, web apps, issues on non-latest software/hardware.
- **Submit**: Apple Security Research portal.
- **In scope**: kernel RCE, sandbox escape, UXSS, Gatekeeper bypass, TCC bypass, iCloud access.

</details>

> Curated writeups for Apple Security Bounty. Fields: title, publication date, author, reported reward, type (blog/video), and a direct link to the original report. Rewards are as reported by the researcher/curator and are not a guarantee for similar findings.

## 1. Summary

| Item | Value |
|---|---|
| Total unique entries | 14 |
| Entries with reported reward | 9 |
| Highest reported reward | $288,500 |
| Date range | 2020-04-03 s/d 2026-07-10 |

## 2. Top 5 Highest Reported Rewards

| # | Reward | Writeup | Author | Date | Type | Link |
|---|---|---|---|---|---|---|
| 1 | **$288,500** | We Hacked Apple for 3 Months: Here's What We Found | Sam Curry et al. | 2020-10-07 | blog | [open](https://samcurry.net/hacking-apple) |
| 2 | **$100,500** | Safari UXSS + iCloud ShareBear exploit chain | Ryan Pickren | 2022-01-26 | blog | [open](https://www.ryanpickren.com/safari-uxss) |
| 3 | **$100,000** | Zero-day in Sign in with Apple | Bhavuk Jain | 2020-05-30 | blog | [open](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/) |
| 4 | **$100,000** | Safari to Kernel Zero-day at Pwn2Own 2021 | Jack Dates | 2021-04-08 | blog | [open](https://www.macrumors.com/2021/04/08/pwn2own-safari-exploit-demonstrated/) |
| 5 | **$75,000** | iPhone Camera Hack - Safari zero-click exploit chain | Ryan Pickren | 2020-04-03 | blog | [open](https://www.ryanpickren.com/webcam-hacking-overview) |

## 3. All Entries (newest first)

### 3.1 With reported reward

| Date | Reward | Writeup | Author | Type | Link |
|---|---|---|---|---|---|
| 2026-03-27 | $1,000 | Abusing the Admin Framework for fun and profit | Ryan Dowd | blog | [open](https://rdowd.com/abusing-system-administration-for-fun-and-profit-part-1-of-3/) |
| 2025-09-05 | $1,000 | When the Back Button Becomes Dangerous: My Safari Bug Bounty Journey | Syarif Sajjad | blog | [open](https://medium.com/@syarifsajjad07/when-the-back-button-becomes-dangerous-my-safari-bug-bounty-journey-8b7dee70debb) |
| 2025-07-31 | $1,000 | CVE-2025-30466 UXSS in Safari (RenwaX23) | RenwaX23 | blog | [open](https://www.macworld.com/article/2863434/bounty-hunter-got-1000-from-apple.html) |
| 2024-05-14 | $60,000 | CVE-2024-27834 PAC Bypass in Safari (Pwn2Own) | Manfred Paul | blog | [open](https://www.bleepingcomputer.com/news/apple/apple-fixes-safari-webkit-zero-day-flaw-exploited-at-pwn2own/) |
| 2022-01-26 | $100,500 | Safari UXSS + iCloud ShareBear exploit chain | Ryan Pickren | blog | [open](https://www.ryanpickren.com/safari-uxss) |
| 2021-04-15 | $9,000 | My First Critical Bug in Bug Bounty Hunting: iCloud | Fernale | blog | [open](https://fernale.blogspot.com/p/an-interesting-xss-exploit-that-i-found.html) |
| 2021-04-08 | $100,000 | Safari to Kernel Zero-day at Pwn2Own 2021 | Jack Dates | blog | [open](https://www.macrumors.com/2021/04/08/pwn2own-safari-exploit-demonstrated/) |
| 2020-10-07 | $288,500 | We Hacked Apple for 3 Months: Here's What We Found | Sam Curry et al. | blog | [open](https://samcurry.net/hacking-apple) |
| 2020-05-30 | $100,000 | Zero-day in Sign in with Apple | Bhavuk Jain | blog | [open](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/) |
| 2020-04-03 | $75,000 | iPhone Camera Hack - Safari zero-click exploit chain | Ryan Pickren | blog | [open](https://www.ryanpickren.com/webcam-hacking-overview) |

### 3.2 Without reported reward

| Date | Reward | Writeup | Author | Type | Link |
|---|---|---|---|---|---|
| 2026-07-10 | — | State of the Apple Security Bounty program | Gergely Kalman | blog | [open](https://gergelykalman.com/state-of-the-apple-security-bounty-program.html) |
| 2024-11-28 | — | Some Experience In Apple Security Bug Program | Zhongquan Li | blog | [open](https://imlzq.com/experience/2024/11/28/Some-Experience-In-ASB.html) |
| 2020-04-03 | — | Bugs that let sites hijack Mac and iPhone cameras | Dan Goodin | blog | [open](https://arstechnica.com/information-technology/2020/04/bugs-that-let-sites-hijack-mac-and-iphone-cameras-fetches-75k-bounty/) |
| 2021-04-06 | — | Safari to Kernel RCE at Pwn2Own 2021 (video) | Jack Dates | video | [open](https://www.youtube.com/watch?v=cfbT1IdAt) |

## 4. Notes

- `n/a` = date not stated in the source.
- Reward = amount **reported** by the author/curator, not an official program figure.
- Video entries are conference/meetup recordings, not written reports.
- Links point to the original writeup, not to the program page.