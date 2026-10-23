# Hardening Single-Tier Stack

[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)

﷽

Tinalakay ng artikulong ito ang **hardening ng single-tier stack**. Ibig sabihin, lahat ng layer—web server, runtime, database, cache—ay nasa isang makina, at aataman natin ito mula sa simula nang hindi na kailangang talakayin ang pag-install mula sa simula.

![Hardening single tier stack](linux-exposure-network-experiment.png)

Layunin:
- Maayos na pagkakasunud-sunod ng hardening
- Pamantayan tulad ng CIS bilang gabay
- Mga setting ng seguridad bawat layer
- Pag-verify pagkatapos ng hardening
- Mga karaniwang pagkakamali na dapat iwasan

## 1. Mga Pangunahing Prinsip ng Hardening

Ang hardening ay hindi isang pindutan. Ito ay unti-unting proseso:

1. **Minimize attack surface** — buksan lamang ang mga port at serbisyo na kailangan.
2. **Least privilege** — bawat serbisyo ay tumatakbo bilang user na hindi nangangailangan ng root.
3. **Defense in depth** — firewall, WAF, TLS, logging, lahat ay may layer.
4. **Update at patch** — ang hindi napapanahong sistema ay target.
5. **Monitoring** — hindi mo madedetect ang hindi mo nakikita.
6. **Recovery** — ang hardening ay hindi kapalit ng backup at plano ng pagbawi.

> **Warning:** Huwag mag-hardening nang direkta sa production. Palaging subukan muna sa lab o VM.

## 2. Pamantayan ng Hardening: CIS

Hindi kailangang hulaan ang hardening. May mga pamantayan na maaaring gamiting gabay:

| Pamantayan | Layunin | Kaugnayan sa single-tier |
|---|---|---|
| **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** | Gabay sa secure configuration para sa OS, web server, database, Docker, at iba pang produkto | Konkretong gabay para sa pag-secure ng bawat layer |
| **[CIS Controls](https://www.cisecurity.org/controls/cis-controls-list)** | 18 prayoridad na kontrol sa seguridad | Malaking larawan: inventory, patching, access control, logging, recovery, incident response |
| **Vendor hardening guide** | Opisyal na gabay mula sa Debian, Ubuntu, Red Hat, Nginx, MariaDB, PostgreSQL, atbp. | Detalye ng configuration ayon sa distro at software na ginagamit |

Pinaka-relevant na benchmark para sa single-tier:

| Layer | Relevant CIS Benchmark |
|---|---|
| OS | CIS Ubuntu Linux Benchmark, CIS Debian Linux Benchmark, CIS Red Hat Enterprise Linux Benchmark |
| Web server | CIS Nginx Benchmark, CIS Apache HTTP Server Benchmark |
| Database | CIS MariaDB Benchmark, CIS MySQL Benchmark, CIS PostgreSQL Benchmark |
| Container | CIS Docker Benchmark |
| Orchestration | CIS Kubernetes Benchmark, kung lumago ang stack sa Kubernetes |

> **Note:** Hindi ibig sabihin na 100% dapat i-apply ang CIS. Pumili ng level na angkop sa lab o production, at dokumentuhin kung ano ang inapply at ano ang sinadyang nilaktawan.

## 3. Operating System

| Aspeto | Gagawin | Bakit mahalaga |
|---|---|---|
| Update at patch | Regular na i-update ang OS at mga package | Sinasara ang kilalang vulnerabilities |
| User at privilege | Huwag mag-login bilang root; gumawa ng regular user na may sudo | Binabawasan ang epekto kung may account na na-leak |
| SSH | I-disable ang root login at password auth; gumamit ng SSH key | Ang SSH ang pangunahing pintuan ng server |
| Host firewall | Default deny incoming; buksan lamang ang 22, 80, 443 | Binabawasan ang exposure ng port |
| Auto patch | I-enable ang unattended upgrades para sa security patches | Pinapanatiling ligtas ang sistema nang walang manual na interbensyon |
| Service minimization | I-disable ang mga hindi ginagamit na serbisyo | Mas kaunting serbisyo = mas maliit na attack surface |
| Kernel parameters | I-apply ang relevant sysctl hardening | Binabawasan ang network-level abuse risk |

> **Important:** Huwag buksan ang database ports (3306, 5432) sa publiko. Ang database ay dapat maabot lamang mula sa localhost o internal network.

## 4. Mga Serbisyo, File, at Secret

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Minimal services | Alisin o i-disable ang mga hindi ginagamit na serbisyo | Binabawasan ang entry path at load ng server |
| File permissions | Limitahan ang permission sa config, log, at sensitive files | Pinipigilan ang hindi kinakailangang access |
| Umask | Gumamit ng mahigpit na default permission | Ang bagong file ay hindi agad world-readable |
| SELinux/AppArmor | I-enable ayon sa distro | Nililimitahan ang kilos ng serbisyo kung na-compromise |
| Secret | Huwag ilagay ang password o API key sa repo o world-readable files | Pinipigilan ang credential leak |
| Environment variable | Itago ang secret sa file na may mahigpit na permission o secret manager | Binabawasan ang risk ng configuration leak |

> **Warning:** Ang `.env`, database credential, SSH key, at backup ay hindi dapat mapunta sa Git. Gumamit ng `.gitignore` mula sa simula.

## 5. Web Server Hardening

| Web server | Mahahalagang setting | Layunin |
|---|---|---|
| Nginx | `server_tokens off`, security headers, limitahan ang HTTP methods, i-disable ang autoindex | Itago ang version at limitahan ang mapanganib na request |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers | Itago ang impormasyon ng server at tanggihan ang mapanganib na method |
| Caddy | Security headers, reverse proxy na may automatic TLS | Simpleng config na may ligtas na default |

Mga security header na dapat meron:

- `X-Frame-Options: SAMEORIGIN` — pinipigilan ang clickjacking
- `X-Content-Type-Options: nosniff` — pinipigilan ang MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin` — kontrol sa referrer
- `Permissions-Policy` — limitahan ang access sa browser features

## 6. TLS / HTTPS

| Aspeto | Rekomendasyon | Bakit |
|---|---|---|
| Minimum TLS | TLS 1.2, mas mabuti TLS 1.3 | May kilalang flaws ang lumang protocol |
| Ciphers | Modern ciphers lamang tulad ng ECDHE at GCM | Pinipigilan ang downgrade attack |
| HSTS | I-enable na may mahabang max-age | Pinipilit ang HTTPS sa browser |
| Certificate | Let's Encrypt via Certbot, automatic renewal | Libre at malawakang ginagamit |
| Session | Limitahan ang session timeout at isaalang-alang ang pag-disable ng session tickets | Binabawasan ang risk ng session reuse |

## 7. WAF: Web Application Firewall

| Komponente | Layunin | Tala |
|---|---|---|
| ModSecurity | WAF engine para sa Apache/Nginx | Kailangan ng tuning para maiwasan ang false positive |
| OWASP CRS | Industry-standard rule set | Magsimula sa mode `DetectionOnly` |
| Coraza | Go-based alternative WAF | Magaan, angkop sa modern setup |

> **Warning:** Huwag i-enable ang WAF blocking mode nang direkta sa production. Magsimula sa `DetectionOnly`, analisahin ang log, pagkatapos ay i-enable nang unti-unti.

## 8. Database Hardening

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Secure installation | Patakbuhin ang built-in secure installation ng database | Inaalis ang anonymous user, test database, at remote root |
| Least privilege | Gumawa ng app user na may limitadong karapatan: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Kung na-leak, limitado ang epekto |
| Bind address | Ang database ay nakikinig lamang sa `127.0.0.1` | Hindi maabot mula sa labas |
| Password | Gumamit ng malakas na password; sinusuportahan ng PostgreSQL ang SCRAM-SHA-256 | Pinipigilan ang brute force |
| Remote access | I-disable ang remote login para sa database root | Napakadelikado ng remote root |
| Backup | Regular na backup at restore test | Ang hardening ay hindi nagpoprotekta laban sa human error o disk failure |

## 9. Runtime Hardening

| Runtime | Mahahalagang setting | Layunin |
|---|---|---|
| PHP-FPM | Patakbuhin bilang `www-data`; limitahan ang `pm.max_children`; i-disable ang mapanganib na function; `expose_php Off` | Binabawasan ang resource abuse at information leak |
| Node.js | Patakbuhin bilang non-root via systemd; gumamit ng PM2 o service manager | Isolation ng process at auto-restart |
| Python | Gumamit ng virtual environment; patakbuhin ang Gunicorn/uWSGI bilang regular user | Isolation ng dependency at privilege |
| Java | Itakda ang JVM memory limit; patakbuhin bilang regular user | Pinipigilan ang memory exhaustion |
| .NET | Patakbuhin ang Kestrel bilang non-root; gumamit ng reverse proxy sa harap | Isolation ng process at access control |

## 10. Logging at Monitoring

| Komponente | Layunin | Bakit |
|---|---|---|
| `auditd` | Nagtatala ng pagbabago sa sensitive files at access | Nakakadetect ng kahina-hinalang aktibidad |
| `journald` | Persistent system logging | Pagsisiyasat ng insidente |
| `logrotate` | Nagro-rotate ng log para hindi mapuno ang disk | Pinapanatili ang availability |
| Fail2ban | Binablock ang IP pagkatapos ng paulit-ulit na failed login | Proteksyon sa SSH at login services |
| Baseline | Itala ang normal na estado: port, user, service, log | Walang baseline, mahirap makita ang anomaly |

## 11. Backup at Recovery

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Database backup | Regular at automated na backup | Ang data ng app ang pangunahing asset |
| Configuration backup | I-backup ang Nginx/Apache, systemd, firewall, at WAF config | Pinabilis ang rebuild ng server |
| Restore test | Subukan ang restore nang pana-panahon | Ang hindi nate-test na backup ay hindi napatunayang magagamit |
| Recovery runbook | Isulat ang mga hakbang sa pagbawi | Sa oras ng insidente, hindi ka maghuhula mula sa zero |
| Retention | Tukuyin kung gaano katagal itatago ang backup | Binabalanse ang storage cost at pangangailangan ng recovery |

> **Important:** Ang backup na nakaimbak sa parehong server ay may risk pa rin. Magtago ng hindi bababa sa isang kopya sa labas.

## 12. Incident Response

| Yugto | Gagawin |
|---|---|
| Detection | Suriin ang SSH, web server, WAF, database, at `auditd` log |
| Containment | I-block ang IP, itigil ang infected service, o i-isolate ang VM |
| Investigation | Hanapin ang unang oras, account na ginamit, nagbago na file, at kahina-hinalang request |
| Recovery | I-restore mula sa malinis na backup, i-rotate ang credential, i-patch ang butas |
| Review | Itala ang root cause at ayusin ang kakulangan sa hardening |

Ang incident response ay hindi kailangang maging kumplikado para sa lab. Ang mahalaga ay alam mo: **ano ang nakikita, ano ang gagawin, at paano ibalik ang server.**

## 13. Pag-verify ng Hardening

Checklist pagkatapos ng hardening:

- [ ] Tanging port 22, 80, 443 lamang ang bukas
- [ ] Ang database ay nakikinig lamang sa `127.0.0.1`
- [ ] Tinanggihan ang SSH root login
- [ ] Tinanggihan ang SSH password auth
- [ ] Na-verify ang TLS configuration gamit ang OpenSSL o testssl.sh
- [ ] May security headers sa response
- [ ] Ang WAF `DetectionOnly` ay nagtatala ng test request
- [ ] Aktibo ang Fail2ban at na-test na ang ban rules sa lab
- [ ] Ang audit log ay nagtatala ng pagbabago sa sensitive files
- [ ] Tumatakbo ang database backup
- [ ] Nasubukan na ang restore ng backup
- [ ] Walang secret sa repository o world-readable files

## 14. Mga Karaniwang Pagkakamali

1. **Pagbubukas ng database port sa publiko** — pinakamadaling target.
2. **SSH root login na naka-enable** — target ng brute force.
3. **Hindi nag-a-update** — lumang CVE na may patch na.
4. **WAF sa blocking mode nang walang tuning** — false positive na nagbablock sa totoong user.
5. **Walang backup** — ang hardening ay hindi nagpoprotekta laban sa human error.
6. **Hindi mino-monitor ang log** — hindi nadetect ang atake.
7. **Secret sa Git** — na-leak ang credential kasama ng repository.
8. **Hindi kailanman nate-test ang backup** — kapag kailangan, hindi ma-restore.

## Konklusyon

Ang hardening ng single-tier stack ay tungkol sa **unti-unting pagbawas ng risk**. Walang 100% ligtas na sistema, ngunit sa CIS bilang gabay, firewall, SSH key, modern TLS, WAF, least-privilege database, logging, at nate-test na backup, ang server ay mas ligtas nang malayo kaysa sa default.

Ang layunin ay hindi lamang pagpatakbo ng app.  
Ang layunin ay unawain ang bawat layer ng depensa, paano ito i-verify, at paano ibalik kapag may nangyari.

> **Note:** Ang hardening ay tuluy-tuloy na proseso. Regular na i-review ang configuration, i-update ang security patches, at subukan muli ang backup at detection.

## Mga Sanggunian

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — gabay sa secure configuration bawat produkto. [cisecurity](https://www.cisecurity.org/cis-benchmarks)
- [CIS Benchmarks Overview](https://www.cisecurity.org/cis-benchmarks-overview) — paliwanag ng benchmark at pag-map nito sa CIS Controls. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — 18 prayoridad na kontrol sa seguridad. [cisecurity](https://www.cisecurity.org/controls/cis-controls-list)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) — hardening para sa host, daemon, image, at container runtime. [docs.docker](https://docs.docker.com/dhi/explore/security-concepts/cis/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) — relevant kung lumago ang stack sa container orchestration. [cisecurity](https://www.cisecurity.org/benchmark/kubernetes)
