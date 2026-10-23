# Hardening Single-Tier Stack

[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)

﷽

Tinalakay ng artikulong ito ang **hardening ng single-tier stack**: lahat ng layer (web server, runtime, database, cache) ay tumatakbo sa isang makina, at aataman natin ito mula sa simula—hindi pag-install mula sa simula, kundi security configuration para sa bawat layer.

![Hardening single tier stack](hardening-single-tier-stack.png)

Layunin:
- Maayos na pagkakasunud-sunod ng hardening
- Pamantayan tulad ng CIS bilang gabay
- Mga setting ng seguridad bawat layer
- Pag-verify pagkatapos ng hardening
- Mga karaniwang pagkakamali na dapat iwasan

##  Mga Pangunahing Prinsip ng Hardening

Ang hardening ay hindi isang pindutan. Ito ay unti-unting proseso:

1. **Minimize attack surface** — buksan lamang ang mga port at serbisyo na kailangan.
2. **Least privilege** — bawat serbisyo ay tumatakbo bilang user na hindi nangangailangan ng root.
3. **Defense in depth** — firewall, WAF, TLS, logging, lahat ay may layer.
4. **Update at patch** — ang hindi napapanahong sistema ay target.
5. **Monitoring** — hindi mo madedetect ang hindi mo nakikita.
6. **Recovery** — ang hardening ay hindi kapalit ng backup at plano ng pagbawi.

> **Warning:** Huwag mag-hardening nang direkta sa production. Palaging subukan muna sa lab o VM.

##  Pamantayan ng Hardening: CIS

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

> **Note:** Ang CIS Benchmark ay binubuo ng Level 1 (minimum baseline) at Level 2 (mas mahigpit). Ang compliance score ay nakadepende sa benchmark profile, bersyon, at mga kontrol na angkop sa iyong kapaligiran. Ang pag-apply ng Level 1 + Level 2 ay hindi nangangahulugang "100% ligtas"—ang pagsunod ay gabay lamang, hindi garantiya ng ganap na seguridad. Pumili ng angkop na level, i-dokumento ang mga exception, suriin bawat kontrol, subukan sa lab, at i-roll out nang unti-unti.

##  Operating System

| Aspeto | Gagawin | Bakit mahalaga |
|---|---|---|
| Update at patch | Regular na i-update ang OS at mga package | Sinasara ang kilalang vulnerabilities |
| User at privilege | Huwag mag-login bilang root, gumawa ng regular user na may sudo | Binabawasan ang epekto kung may account na na-leak |
| SSH | I-disable ang root login at password auth, gumamit ng SSH key | Ang SSH ang pangunahing pintuan ng server |
| Host firewall | Default deny incoming, payagan lamang ang mga port na kinakailangan ayon sa arkitektura (hal., 22, 80, 443) | Binabawasan ang exposure ng port |
| Auto patch | I-enable ang unattended upgrades para sa security patches | Pinapanatiling ligtas ang sistema nang walang manual na interbensyon |
| Service minimization | I-disable ang mga hindi ginagamit na serbisyo | Mas kaunting serbisyo = mas maliit na attack surface |
| Kernel parameters | I-apply ang relevant sysctl hardening | Binabawasan ang network-level abuse risk |

> **Important:** Huwag buksan ang mga database port (3306, 5432) sa publiko—ang access sa database ay dapat limitado sa `127.0.0.1` o Unix socket. Maaaring paghigpitan ang SSH sa VPN/admin network, at ang HTTP ay maaari lamang gamitin para sa pag-redirect sa HTTPS. Isaalang-alang din ang mga madalas na nakakaligtaang aspeto:
> - **Pag-install & footprint:** sa pag-install, i-enable ang disk encryption (LUKS) at hiwalay na partisyon para sa `/`, `/var`, `/tmp`, `/home`. Ilapat ang mount options na `noexec`, `nosuid`, `nodev` lamang sa mga sensitibong partisyon ayon sa kanilang tungkulin at laging subukan sa lab (maaaring masira ang ilang aplikasyon).
> - **Pamamahala ng memorya at disk:** i-encrypt ang swap, limitahan ang laki ng log, i-rotate ang log, at i-monitor ang paggamit ng disk upang maiwasan ang DoS dahil sa puno ang disk.
> - **Hardening ng kernel at serbisyo:** ilapat ang kinakailangang sysctl parameter, i-enable ang SELinux/AppArmor, bawasan ang serbisyo, i-disable ang hindi ginagamit na module.

##  Mga Serbisyo, File, at Secret

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Minimal na serbisyo | Alisin o i-disable ang mga hindi ginagamit na serbisyo | Bawat aktibong serbisyo ay potensyal na entry point, mas kaunting serbisyo = mas maliit na attack surface |
| Mga pahintulot ng file | Limitahan ang pahintulot sa config, log, at sensitibong file (chmod 600/640, chown root:root) | Pinipigilan ang non-privileged user na magbasa o magbago ng file na may config o sensitibong data |
| Umask | Gumamit ng mahigpit na default na pahintulot (umask 027 o 077) | Ang bagong file ay hindi agad world-readable, binabawasan ang aksidenteng pag-leak ng data |
| SELinux/AppArmor | I-enable ayon sa distro (enforcing mode) | Nililimitahan ang kilos ng serbisyo kung na-compromise—kahit nabigyan ng access ang serbisyo, limitado ang pinsala sa pinapayagang patakaran |
| Mga lihim | Huwag ilagay ang password o API key sa repo o sa mga file na mababasa ng lahat | Ang mga credential na nalabas ay nagbibigay-daan sa hindi awtorisadong access |
| Pag-iimbak ng lihim | Itago sa file na may mahigpit na pahintulot o secret manager (Vault, SOPS). Limitahan ang access, i-rotate, at i-audit. | Binabawasan ang panganib ng leak, nagpapadali ng rotation, at nagpapanatili ng audit trail |
| `.gitignore` | Idagdag ang `.env`, `*.key`, `*.pem`, `backup/` sa `.gitignore` mula sa simula | Pinipigilan ang mga credential, SSH key, at backup na mapunta sa Git nang hindi sinasadya |

> **Warning:** Ang `.env`, database credential, SSH key, at backup ay hindi dapat mapunta sa Git. Gumamit ng `.gitignore` mula sa simula, at kung na-commit na, i-rotate agad ang credential (ituring na bocor).

**Kung nabocor na sa Git, gawin ito:**
1. **Alisin sa history** — gamitin ang `git filter-repo` o BFG Repo-Cleaner para tanggalin ang file/secret sa buong history, pagkatapos i-force-push.
2. **I-rotate ang lahat ng credential** — password, API key, SSH key, token na nabocor ay ituring na compromised, palitan lahat.
3. **I-revoke ang lumang access** — bawiin ang lumang key, isara ang aktibong session, i-block ang kahina-hinalang IP.
4. **I-audit** — suriin ang access log upang malaman kung ginamit ang secret nang hindi awtorisado.
5. **Pigilan** — magdagdag ng secret scanning (gitleaks, trufflehog) sa CI/CD at pre-commit hook.

##  Hardening ng Web Server at Web Client

### Web Server (server-side)

| Web Server | Mahahalagang setting | Layunin |
|---|---|---|
| Nginx | `server_tokens off`, security headers sa server, limitahan ang HTTP methods, i-disable ang autoindex, modern TLS, rate limiting (`limit_req`), WAF (ModSecurity) | Itago ang bersyon, limitahan ang mapanganib na request, protektahan laban sa abuse/DDoS |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers sa server, modern TLS, ModSecurity WAF | Itago ang impormasyon ng server at tanggihan ang mapanganib na method |
| Caddy | Security headers, reverse proxy na may awtomatikong TLS | Simpleng config na may ligtas na default |

**Mga karaniwang security header na itinakda sa web server:**
- `Strict-Transport-Security (HSTS)` — pinipilit ang HTTPS (tingnan ang seksyon ng TLS)
- `X-Content-Type-Options: nosniff` — pinipigilan ang MIME sniffing
- `X-Frame-Options: SAMEORIGIN` — pinipigilan ang clickjacking (maaaring dagdagan/palitan ng `Content-Security-Policy: frame-ancestors`)
- `Referrer-Policy: strict-origin-when-cross-origin` — kontrol sa pag-leak ng referrer
- `Permissions-Policy` — limitahan ang access sa mga feature ng browser
- `Content-Security-Policy (CSP)` — limitahan ang mga source ng script/style/image upang mabawasan ang XSS

> **Tala:** Ang mga header ay nagbabawas ng ilang panganib, ngunit **hindi pinapalitan** ang input validation, output encoding, authentication, at authorization. Nanatili ang mga iyon sa responsibilidad ng aplikasyon.

**Rate limiting at WAF (server-side):**
- Limitahan ang request bawat IP/user sa web server (`limit_req`, `mod_evasive`).
- Mag-deploy ng WAF (ModSecurity/OWASP CRS) para salain ang SQLi, XSS, at mapanganib na payload.
- I-block ang paulit-ulit na mapang-abusong IP (fail2ban).

**Reverse proxy / load balancer (kung mayroon):**
- I-forward nang tama ang `X-Forwarded-For`; huwag basta maniwala.
- Limitahan ang admin endpoint sa mga tinukoy na IP.
- I-enable ang access at error logging.

### Hardening ng Web Client / Browser

Pagtuunan ng pansin ang mga kontrol na **hindi malulutas ng mga header ng server lamang**:
- **Mahigpit na CSP**: iwasan ang `unsafe-inline`/`unsafe-eval`; gumamit ng nonce/hash.
- **Subresource Integrity (SRI)**: i-hash ang mga CDN asset upang maiwasan ang pag-tamper.
- **Seguridad ng cookie**: `Secure`, `HttpOnly`, `SameSite=Strict/Lax`, tamang domain/path, maikli ang tagal.
- **Anti-CSRF token** para sa mga request na nagbabago ng estado.
- **Pamamahala ng session**: baguhin ang session ID pagkatapos mag-login, idle/absolute timeout, i-invalidate sa pag-logout.
- **CORS**: paghigpitan nang mahigpit ang origin; huwag gumamit ng wildcard `*` para sa sensitibong endpoint.
- **Storage**: iwasan ang pag-imbak ng sensitibong token sa `localStorage`/`sessionStorage` (panganib ng XSS), mas mainam na gumamit ng `HttpOnly` cookie.
- **Mga third-party script**: i-audit/bawasan, gumamit ng SRI, i-sandbox ang iframe.
- **Mixed content**: i-block ang HTTP resource sa HTTPS na pahina.

##  TLS / HTTPS

| Aspeto | Rekomendasyon | Bakit |
|---|---|---|
| Minimum TLS | TLS 1.2, mas mabuti TLS 1.3 | May kilalang flaws ang lumang protocol |
| Ciphers | Modern ciphers lamang (ECDHE, GCM, ChaCha20-Poly1305) | Pinipigilan ang downgrade attack |
| HSTS | I-enable na may mahabang max-age (`max-age=31536000; includeSubDomains; preload`) | Pinipilit ang HTTPS sa browser |
| Certificate | Let's Encrypt via Certbot, automatic renewal | Libre at malawakang ginagamit |
| Session | Limitahan ang session timeout, isaalang-alang ang pag-disable ng session tickets | Binabawasan ang risk ng session reuse |
| OCSP Stapling | I-enable ang OCSP stapling | Pinabilis ang certificate validation at privacy |
| Redirect | I-redirect ang HTTP → HTTPS (301) | Pinipigilan ang hindi naka-encrypt na access |
| Sukat ng key | RSA 2048+ o ECDSA P-256/P-384 | Pinipigilan ang brute force ng key |
| Cipher order | Server-side cipher preference | Pinipigilan ang client na pumili ng mahinang cipher |

**Karagdagang practice:**
- Subukan ang config gamit ang SSL Labs (target grade A).
- I-disable ang TLS compression (CRIME) at renegotiation.
- Gumamit ng `ssl_protocols TLSv1.2 TLSv1.3;` sa Nginx.
- Itago ang private key na may mahigpit na permission (600) at huwag i-commit sa Git.

##  WAF: Web Application Firewall

| Komponente | Layunin | Tala |
|---|---|---|
| ModSecurity | WAF engine para sa Apache/Nginx | Kailangan ng tuning para maiwasan ang false positive |
| OWASP CRS | Industry-standard rule set | Magsimula sa mode `DetectionOnly` |
| Coraza | Go-based alternative WAF | Magaan, angkop sa modern setup |

**Paano i-deploy (halimbawa Nginx + ModSecurity):**
1. I-install ang ModSecurity module at OWASP CRS.
2. I-enable sa Nginx config: `modsecurity on; modsecurity_rules_file /etc/modsecurity/crs/crs-setup.conf;`
3. Itakda ang `SecRuleEngine DetectionOnly` sa simula.
4. Bantayan ang log (`/var/log/modsec_audit.log`) para sa false positive.
5. I-tune ang rule: i-exclude ang rule na false positive sa specific endpoint.
6. Kapag stable na, palitan ng `SecRuleEngine On` (blocking).

**Dapat bantayan:**
- False positive sa upload, API, o kumplikadong form endpoint.
- Performance overhead, i-monitor ang latency.
- I-update ang rule nang regular (bagong CRS release).

> **Warning:** Huwag i-enable ang WAF blocking mode nang direkta sa production. Ang WAF rule (lalo na OWASP CRS) ay madalas mag-false positive sa lehitimong traffic (form upload, API, kumplikadong query); kung agad na i-enable ang blocking, maaaring ma-block ang lehitimong user at ma-down ang service. Magsimula sa `DetectionOnly`, analisahin ang log upang makilala ang false positive, i-tune ang rule, pagkatapos ay i-enable nang unti-unti ang blocking.

##  Database Hardening

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Secure installation | Patakbuhin ang built-in secure installation ng database | Inaalis ang anonymous user, test database, at remote root |
| Least privilege | Gumawa ng app user na may limitadong karapatan: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Kung na-leak, limitado ang epekto |
| Bind address | Ang database ay nakikinig lamang sa `127.0.0.1` o Unix socket | Hindi maabot mula sa labas |
| Password | Gumamit ng malakas na password, sinusuportahan ng PostgreSQL ang SCRAM-SHA-256 | Pinipigilan ang brute force |
| Remote access | I-disable ang remote login para sa database root | Napakadelikado ng remote root |
| Backup | Regular na backup at restore test | Ang hardening ay hindi nagpoprotekta laban sa human error o disk failure |
| Encryption at rest | I-enable ang TDE *kung sinusuportahan* ng engine/bersyon/edisyon, kung hindi gumamit ng LUKS sa data volume + encrypted na backup | Pinoprotektahan ang data kung ninakaw ang disk; iba-iba ang suporta ng TDE sa MySQL/MariaDB/PostgreSQL |
| Audit logging | I-enable ang query log para sa sensitibong operasyon (DDL, DML sa mga key table) | Natutuklasan ang hindi awtorisadong access at nakakasunod sa compliance |
| Connection security | Gumamit ng TLS para sa koneksyon sa database (kahit localhost sa multi-tenant setup) | Pinipigilan ang sniffing ng credential/data |
| Query monitoring | I-monitor ang mabagal na query at anomalya (pg_stat_statements, slow query log) | Natutuklasan ang abuse o injection na nakalusot sa WAF |
| Backup encryption | I-encrypt ang backup (GPG/LUKS), itago sa labas, subukan ang restore | Pinipigilan ang data leak mula sa ninakaw na backup |
| Network isolation | Huwag i-expose ang DB port sa publiko, gumamit ng firewall/VPN para sa admin access | Binabawasan ang attack surface |

**Praktikal na tala:**
- Maghiwalay ng DB user bawat app, huwag gumamit ng root para sa app.
- Regular na i-rotate ang DB credential.
- Limitahan ang max connections (connection pool) upang maiwasan ang DoS.
- I-disable ang hindi ginagamit na DB feature (xp_cmdshell, LOAD DATA LOCAL, atbp.).

##  Runtime Hardening

| Runtime | Mahahalagang setting | Layunin |
|---|---|---|
| PHP-FPM | Patakbuhin bilang `www-data`; limitahan ang `pm.max_children`; i-disable ang mapanganib na function; `expose_php Off` | Binabawasan ang resource abuse at information leak |
| Node.js | Patakbuhin bilang non-root via systemd, gumamit ng PM2 o service manager | Isolation ng process at auto-restart |
| Python | Gumamit ng virtual environment, patakbuhin ang Gunicorn/uWSGI bilang regular user | Isolation ng dependency at privilege |
| Java | Itakda ang JVM memory limit, patakbuhin bilang regular user | Pinipigilan ang memory exhaustion |
| .NET | Patakbuhin ang Kestrel bilang non-root, gumamit ng reverse proxy sa harap | Isolation ng process at access control |

##  Logging at Monitoring

| Komponente | Layunin | Bakit |
|---|---|---|
| `auditd` | Nagtatala ng pagbabago sa sensitive files at access | Nakakadetect ng kahina-hinalang aktibidad |
| `journald` | Persistent system logging | Pagsisiyasat ng insidente |
| `logrotate` | Nagro-rotate ng log para hindi mapuno ang disk | Pinapanatili ang availability |
| Fail2ban | Binablock ang IP pagkatapos ng paulit-ulit na failed login | Proteksyon sa SSH at login services |
| Baseline | Itala ang normal na estado: port, user, service, log | Walang baseline, mahirap makita ang anomaly |

##  Backup at Recovery

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Database backup | Regular at automated na backup | Ang data ng app ang pangunahing asset |
| Configuration backup | I-backup ang Nginx/Apache, systemd, firewall, at WAF config | Pinabilis ang rebuild ng server |
| Restore test | Subukan ang restore nang pana-panahon | Ang hindi nate-test na backup ay hindi napatunayang magagamit |
| Recovery runbook | Isulat ang mga hakbang sa pagbawi | Sa oras ng insidente, hindi ka maghuhula mula sa zero |
| Retention | Tukuyin kung gaano katagal itatago ang backup | Binabalanse ang storage cost at pangangailangan ng recovery |

> **Important:** Ang backup na nakaimbak sa parehong server ay may risk pa rin. Magtago ng hindi bababa sa isang kopya sa labas.

##  Incident Response

| Yugto | Gagawin |
|---|---|
| Detection | Suriin ang SSH, web server, WAF, database, at `auditd` log |
| Containment | I-block ang IP, itigil ang infected service, o i-isolate ang VM |
| Investigation | Hanapin ang unang oras, account na ginamit, nagbago na file, at kahina-hinalang request |
| Recovery | I-restore mula sa malinis na backup, i-rotate ang credential, i-patch ang butas |
| Review | Itala ang root cause at ayusin ang kakulangan sa hardening |

Ang incident response ay hindi kailangang maging kumplikado para sa lab. Ang mahalaga ay alam mo: **ano ang nakikita, ano ang gagawin, at paano ibalik ang server.**

##  Pag-verify ng Hardening

Gamitin ang `check → execute → verify`:

| Kontrol | Check | Execute | Verify |
|---|---|---|---|
| Mga port at firewall | Ilista ang bukas na port (`ss -tulnp`, `ufw status`) | Default deny + payagan lamang ang kinakailangan | Tanging mga aprubadong port lamang ang bukas |
| Access sa DB | Suriin ang bind address | I-bind sa `127.0.0.1` o Unix socket, tanggihan ang pampublikong access | Walang koneksyon sa DB mula sa labas ng host |
| SSH | Suriin ang sshd config | I-disable ang `PermitRootLogin`, i-disable ang password auth, gumamit ng key | Tinanggihan ang root at password auth |
| TLS | Suriin ang cert/cipher | I-configure ang TLS 1.2/1.3, modern ciphers, HSTS, HTTP→HTTPS | Subukan gamit ang `openssl s_client` o testssl.sh (target A) |
| Security headers | Suriin ang HTTP response | Itakda ang headers sa web server | Nasa response ang mga headers ayon sa config |
| WAF | Suriin ang mode ng WAF | Magsimula sa `DetectionOnly`, i-tune, unti-unting gawing `Blocking` | Na-log ang test request, na-address ang false positive |
| Fail2ban | Suriin ang status ng jail | I-enable ang nauugnay na jail | Na-test sa lab (gumagana ang ban/unban) |
| Audit/FIM | Suriin ang `auditd`, AIDE/tripwire | Gumawa ng baseline at audit rule para sa kritikal na file/config | Nasusubaybayan/na-alert ang pagbabago |
| Egress | Suriin ang outbound na koneksyon | Obserbahan → ilapat ang allowlist/deny nang unti-unti kung kinakailangan | Tanging pinapayagang destinasyon lamang ang maa-access |
| Backup at restore | Suriin ang iskedyul ng backup | I-automate, i-encrypt, hiwalay na storage, subukan ang restore | Ang restore sa isolated env ay matagumpay at gumagana ang app |
| Mga lihim | Suriin ang repo/file | Siguruhin na hindi na-commit ang `.env`/key, mahigpit ang pahintulot | Malinis ang scan/history, tama ang pahintulot |

##  Mga Karaniwang Pagkakamali

1. **Pagbubukas ng database port sa publiko** — ang database ay dapat lamang sa `127.0.0.1` o Unix socket.
2. **Naka-enable ang SSH root login at pinapayagan ang password auth** — gumamit ng SSH key, i-disable ang dalawa.
3. **Hindi nag-a-update** — ang mga lumang CVE ay maaaring ma-exploit kahit may patch na.
4. **WAF sa blocking mode nang walang tuning** — magsimula sa `DetectionOnly`, suriin ang false positive, i-enable ang blocking nang unti-unti.
5. **Hindi kailanman nasubukan ang backup** — kinakailangan na subukan ang restore sa isolated na kapaligiran.
6. **Mga lihim sa Git** — gumamit ng `.gitignore`, secret manager, at kung nalabas na i-rotate ang credential at linisin ang history.
7. **Pag-aakala na sapat na ang mga header** — binabawasan ng mga header ang panganib, ngunit kinakailangan pa rin ang input validation, authentication, at authorization sa aplikasyon.

##  Pagtuklas at Pagbawi: Mga Hangganan ng Hardening sa Single-Tier Stack

### Hangganan ng seguridad ng single-tier

Ang single-tier ay nangangahulugang maraming komponente ang nagbabahagi ng isang OS. Ang logical separation ng proseso ay hindi kapareho ng security isolation. Kung na-compromise ang runtime, maaaring nakawin ang DB credential, magtanim ng persistence, o mag-eksfiltrate ng data. Sakop ng hardening ang prevention, containment, detection, at recovery.

### Network hardening

Tatlong landas: **Ingress** (koneksyon mula sa labas — SSH, HTTP/HTTPS: limitahan ang source, buksan lamang ang kinakailangang port), **East-west** (komunikasyon ng komponente via loopback/Unix socket: limitahan ang access sa pagitan ng proseso), **Egress** (outbound DNS, NTP, update, backup, API: default-deny + allowlist).

Tumutulong ang UFW sa ingress ngunit hindi awtomatikong naglilimita ng egress o nag-iisolate ng proseso. Upang mabawasan ang lateral movement: magkahiwalay na service account bawat komponente, dedikadong DB app user, AppArmor/SELinux, container network policy, o hiwalay na VM kung mataas ang impact.

### Logging at monitoring

Logging = pagtatala ng event. Monitoring = pagsusuri para sa anomalya. Alerting = pagbibigay-alam kung kailangang kumilos.

End-to-end na mapa: (1) entry point (SSH, HTTP/HTTPS, firewall, WAF, TLS, app auth), (2) execution ng app (web server → runtime), (3) access sa data (runtime → DB → file/backup), (4) aktividad ng OS at egress (proseso, user, systemd, cron, sensitibong file, DNS, outbound connection), (5) korelasyon at respons (kolektahin ang log, i-sync ang oras, i-korelasyon ang event, alert, triage).

Monitoring bawat layer: firewall (koneksyon, port, destinasyon), SSH/OS account (login, bagong user), web server/WAF (URL, status, rule), runtime (error, restart, child process), database (login, privilege, sensitibong query), integridad ng file (hash, permission, owner), OS (sudo, audit event, cron, kernel), resource (CPU/RAM/disk/latency), backup (status ng job, laki, retention).

### auditd

Nagtatala ng event ayon sa audit rule. Mahahalagang object: sshd_config, sudoers, passwd/group/shadow, systemd unit, cron, authorized_keys, config ng web server/WAF/DB, web root, config ng firewall, kritikal na binary.

Consumer: sysadmin (pagbabago ng config/user), security analyst (chronology), incident responder (persistence/escalation), auditor (trail ng pagbabago).

Limitasyon: maling rule ay nakakaligtaan ng aktividad, sobrang dami ng rule ay nagbibigay ng disk pressure/noise, lehitimong pagbabago (deployment) ay naitatala rin, root attacker ay maaaring magbura ng lokal na log, hindi awtomatikong ipinapaliwanag ng audit ang HTTP request na nag-trigger.

Iba sa: auditd (aktividad ayon sa rule), journald (mensahe ng OS/app), FIM (pagbabago vs baseline), network monitoring (koneksyon), SIEM (korelasyon at alert).

### journald, logrotate, Fail2ban, baseline

- **journald**: nagkolekta ng mensahe ng OS/app, ang persistensya ay nakadepende sa config at retention. Bantayan ang SSH, nabigong service, kernel, pagkabigo ng resource. I-forward ang kritikal na log sa hiwalay na sistema.
- **logrotate**: namamahala sa lifecycle ng log (rotation, compression, retention). Siguraduhing hindi humihinto ang pagsusulat ng log sa rotation, sapat ang retention para sa imbestigasyon.
- **Fail2ban**: nagbabasa ng log, nagba-block ng source pagkatapos ng pattern (paulit-ulit na failed login). Tumutulong sa simpleng brute force, hindi pinipigilan ang web exploit, credential theft, eksfiltrasyon. Maaaring mag-false positive.
- **Baseline**: talaan ng normal na estado (port, user, service, proseso, hash ng file, firewall rule, pattern ng login/request/egress, bersyon). I-update via lehitimong pagbabago (deployment/patch).

### Epektibong monitoring

Itakda ang normal na kondisyon pagkatapos ay mag-alert. Halimbawang signal: SSH admin login mula sa hindi kilalang source (mataas), bagong OS user/admin group sa labas ng change window (mataas), config file nagbago nang walang deployment (mataas), bagong proseso na hindi tumutugma sa perilaku ng app (mataas), runtime nagbubukas ng koneksyon sa bagong destinasyon (mataas kung nakumpirma), pagbabago ng DB privilege o malaking pag-export ng data (mataas), pagbabago ng firewall rule nang walang pag-apruba (mataas), pagtaas ng request sa WAF na kahawig ng eksploitasyon (kailangan ng korelasyon), pagtaas ng CPU/RAM/disk/latency (kailangan ng triage), pagkabigo ng backup job/hindi available ang kopya (mataas).

Ang WAF ay nakikitang trafik lamang na dumadaan sa inspection point nito, hindi nito nakikitang lokal na proseso, pagbabago ng user/sudo, file na binago via SSH, access sa DB via loopback, non-WAF egress, pagbabago ng firewall, pagbura ng log, pagbabago ng backup. Hindi rin pinapalitan ng OS audit ang app log (syntactically valid na request na nang-aabuso ng authorization).

Ang lokal na log lamang ay hindi sapat: maaaring magbura ng lokal na log ang root attacker. I-forward ang kritikal na log sa hiwalay na sistema (VM na may hiwalay na admin rights). Inirerekomenda ng CISA ang centralized logging, alerting sa high-risk event, proteksyon ng log mula sa hindi awtorisadong pagbabago, malinaw na retention.

Tukuyin ang may-ari ng alert: admin (kalusugan ng service/config), developer (deployment/error), security analyst (korelasyon/containment), may-ari ng backup (availability/restore), may-ari ng serbisyo (epekto sa negosyo).

### Backup at recovery

Mga object na dapat isaalang-alang: database (data+schema+role+metadata), app file (kilalang malinis na release version), upload ng user, config ng OS/service, secret/sertipiko (na may angkop na access/encryption), encryption key (hiwalay sa backup), log/ebidensya, dokumentasyon ng recovery (bersyon, dependensiya, pagkakasunod-sunod ng restore).

Daloy: pinagmulan ng production → konsistenteng backup (paraan na angkop sa DB engine, itala ang oras/bersyon/status) → encryption at transfer (protektadong channel, dedikadong identidad ng backup) → hiwalay na storage (iba't ibang lokasyon, hiwalay na kredensyal, retention, proteksyon sa pagbura) → beripikasyon at restore test (integridad, restore sa isolated env, subukan ang app+data).

Dapat hiwalay ang backup: maaaring magbura ng production data AT lokal na backup ang attacker na may mataas na privilege. Gumamit ng dedikadong backup account, iwasang bigyan ng karapatan ang production server na magbura ng lahat ng historical copy, immutable storage, encryption + hiwalay na pamamahala ng key, bantayan ang pagkabigo at pagbabago ng retention, subukan ang restore. Pamamaraang 3-2-1: 3 kopya, 2 uri ng media, 1 offsite. Para sa ransomware, magdagdag ng offline/immutable na kopya.

RPO (recovery point objective) = katanggap-tanggap na pagkawala ng data (window ng oras). RTO (recovery time objective) = pinakamahabang oras na maaaring down ang serbisyo. Hindi awtomatikong ginagarantiya ng dalas ng backup ang RPO, hindi rin awtomatikong ginagarantiya ng backup ang RTO kung mabagal ang restore.

Mga kahirapan sa recovery: DB at upload mula sa iba't ibang oras, ang pinakabagong backup ay maaaring may sirang/mapanganib na data, ang na-leak na secret ay kailangang i-rotate hindi lamang i-restore, ang lumang config ay maaaring magbalik ng kahinaan, walang saysay ang encrypted backup kung nawala ang key, maaaring mabigo ang app sa restore, maaaring maibalik ang persistence. Kaya restore test sa isolated environment: beripikahin ang DB, login ng app, business function, permission, service, TLS, firewall, monitoring bago ibalik ang serbisyo.

### Incident response

Mabilisang respons (unang minuto): beripikahin ang alert (sistema, oras, account, proseso, indicator), suriin ang impact (serbisyo, sensitibong data, admin account, egress), containment (limitahan ang attack path via network control/isolation), protektahan ang ebidensya (i-save ang log, timestamp, alert, metadata, itala ang bawat aksyon), protektahan ang access (planuhin ang pagrevoke ng session, rotation ng secret, pagpapalit ng key via trusted system), tukuyin ang escalation (root compromise, pagnanakaw ng data, ransomware → seryosong insidente).

Malalim na imbestigasyon — mahahalagang tanong: kailan naganap ang unang aktividad? (centralized log, auth, web, WAF, audit, DB) Ano ang entry point? (web request, SSH, pagbabago ng app, mahinang config) Anong account ang ginamit? (login, user ID, privilege, session, key, sudo) Anong proseso ang tumakbo? (process tree, parent, executable, service, scheduler) Anong file ang nagbago? (audit event, FIM, hash, metadata, deployment history) Anong data ang na-access? (DB audit, app, file access, volume ng trafik) Lumabas ba ang data? (flow log, DNS, proxy/firewall log, nagmamay-ari ng koneksyon) Patuloy ba ang access? (account, key, service, cron, config, iba pang persistence) Ano ang maaari pang pagkatiwalaan? (integridad ng sistema, provenance ng backup, config, external evidence).

Kung na-compromise ang OS ng root: huwag pagkatiwalaan ang output mula sa pinaghihinalaang OS, i-isolate via external network control, panatilihing naka-forward ang log, kolektahin ang volatile evidence kung may prosedura, iwasang magpatakbo ng tool na tumatapak sa ebidensya, isaalang-alang ang forensic snapshot/image ayon sa prosedura ng platform, unahin ang rebuild mula sa malinis na media/image, i-rotate ang credential/token/key/secret, suriin ang access sa backup at iba pang sistema gamit ang identidad ng compromised server.

Ang containment ay hindi simpleng pag-block ng IP: kung gumagamit ang attacker ng lehitimong account/session, kumonekta via VPN/proxy, nag-eksploit nang lokal, nakawin ang DB credential, nagtanim ng persistence, o nakuha ang root — hindi sapat ang pag-block ng IP. Maaaring mangahulugan ang containment ng: pag-disable ng account, pagrevoke ng session/key, pag-isolate ng VM, paglimita ng egress, paghinto ng specific service, pagsara ng apektadong endpoint.

Recovery at beripikasyon bago ideklarang tapos: entry point naisara/dinimitigahan, image/package/app file mula sa pinagkakatiwalaang source, data naibalik mula sa beripikadong backup, na-handle ang na-leak na credential/session, user/key/service/scheduler/firewall ayon sa inaprubahang baseline, aktibo ang logging/audit/FIM/monitoring, egress at access sa DB ayon sa polisiya, pumasa ang app sa functional at security test, dokumentasyon ng chronology/impact/aksyon/follow-up.

### Matriks ng korelasyon (halimbawang insidente)

Runtime pinaghihinalaang tumakbo ng hindi inaasahang proseso pagkatapos ng web request:
1. Paunang indikasyon: WAF at access log → hindi normal na request, endpoint, oras, status.
2. Beripikasyon ng proseso: log ng runtime at impormasyon ng proseso → child process, parent, owner, oras ng simula.
3. Pagbabago ng sistema: auditd at FIM → bagong file, pagbabago ng permission, unit ng service/cron.
4. Pagpapalawak ng access: auth, sudo, DB log → bagong account, pagbabago ng privilege, access sa sensitibong data.
5. Outbound communication: firewall, DNS, flow log → bagong destinasyon, oras, volume.
6. Containment: external firewall/isolation ng host → patuloy pa ba ang aktividad?
7. Recovery: backup, baseline, pinagkakatiwalaang image → maaari bang ligtas na maibalik ang sistema at data?
8. Pagsusuri: lahat ng ebidensya → entry path, saklaw ng impact, nabigong kontrol.

### Mga kahirapan at limitasyon

| Kontrol | Pangunahing kahirapan | Risk kung walang pagsusuri |
|---|---|---|
| Egress default-deny | Paggawa/pagpapanatili ng kumpletong destination allowlist | Update/DNS/API/backup mabibigo |
| auditd | Pagpili ng rule, pagkontrol ng volume ng event | Disk puno, noise, na-miss na event |
| FIM | Pag-update ng baseline pagkatapos ng lehitimong pagbabago | Alert fatigue o mapanganib na pagbabago na itinuturing na normal |
| SIEM/centralized log | Gastos sa storage, parsing, korelasyon, pamamahala ng alert | Maraming alert, walang follow-through |
| Fail2ban | Tuning ng filter at threshold | False positive, pag-block ng lehitimong user |
| Database auditing | Pagpili kung ano ang itatala nang walang overhead/leak ng data | Mataas na load o log na naglalaman ng sensitibong data |
| Offsite backup | Pamamahala ng identidad, encryption, retention, restore test | Backup hindi ma-access/ma-decrypt/ma-restore |
| Incident response | Pagbabalanse ng containment, preserbasyon ng ebidensya, kontinuitas ng serbisyo | Nawawala ang ebidensya o nagpapatuloy ang compromise |
| Rebuild ng server | Pagtiyak ng malinis na image, available na dependensiya, konsistenteng data | Muling pumasok ang attacker/mahinang config |

### Makatwirang pagkakasunod-sunod ng implementasyon

1. Itakda ang baseline at inventory (port, service, user, config, dependensiya, data path, external service).
2. Seguruhin ang ingress at lokal na access (limitahan ang SSH, isara ang hindi kinakailangang port, limitahan ang privilege ng runtime, protektahan ang access sa DB).
3. Ipatupad ang polisiya ng egress (obserbahan ang normal na koneksyon → unti-unting paghihigpit → subukan ang app flow).
4. I-enable ang relevanteng logging (auth, web, runtime, DB, OS, firewall, backup).
5. Magdagdag ng audit at integridad ng file (kritikal na object, audit rule, baseline, pagbabago na nangangailangan ng imbestigasyon).
6. Bumuo ng monitoring at alert (rule batay sa risk scenario, may-ari ng alert, subukan ang availability ng ebidensya).
7. Ihiwalay ang backup at kritikal na log (protektahan mula sa pagbura ng production server account).
8. Sanayin ang incident response (simulahin ang kahina-hinalang login, pagbabago ng file, hindi inaasahang egress, restore ng backup sa lab).
9. Beripikahin at suriin muli (subukan ang kontrol pagkatapos ng pagbabago, itala ang exception, muling suriin ang baseline).

### Mga sanggunian

- [Ubuntu Server — Firewall](https://ubuntu.com/server/docs/firewalls/) — perilaku at pamamahala ng firewall host gamit ang UFW.
- [Linux Audit System — auditd](https://www.linux.org/docs/man5/auditd.html) — papel ng audit daemon at pagproseso ng audit record.
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/use-logging-on-business-systems) — source ng log, alerting, centralization, proteksyon ng log.
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — logging, backup, proteksyon ng kopya, recovery.
- [FBI — Ten Actions to Improve Cyber Resiliency](https://www.fbi.gov/investigate/cyber/ten-actions-to-improve-cyber-resiliency) — proteksyon ng log at offline/immutable backup.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — gabay sa incident response (Abril 2025).

Pangunahing aral: sa single-tier, ang layunin ay hindi lamang pigilan ang access mula sa internet. Kailangan mo ring limitahan kung ano ang magagawa ng na-compromise na proseso, bawasan ang tsansa ng lateral movement at eksfiltrasyon, panatilihing mapagkakatiwalaan ang ebidensya, at tiyakin na maaaring ipanumbalik ang sistema nang hindi muling nagdadala ng compromise.

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
