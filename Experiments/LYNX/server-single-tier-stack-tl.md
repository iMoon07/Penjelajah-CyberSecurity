# Server Single-Tier Stack

[🇬🇧 Read in English](server-single-tier-stack-en.md)  
[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)  
[🇲🇾 Baca dalam Bahasa Melayu](server-single-tier-stack-ms.md)

﷽

![Server single tier](single-tier-stack.png)

Tinalakay sa artikulong ito ang **Single-Tier Server para sa Web Apps**. Ibig sabihin, ang web server, server-side runtime, database, at optional cache ay nasa **iisang makina** lamang.

Ang layunin ay maunawaan:
- Kung anong mga stack ang maaaring piliin
- Ang mga bentahe at disbentahe ng bawat pagpipilian
- Mga bagay sa seguridad na kailangang isaalang-alang
- Kung paano ito gagamitin para sa pagsasanay

## 1. Deployment: Bare Metal, VM, Container

| Paraan | Ano ang ginagawa nito | Mga bentahe | Mga disbentahe | Kailan gagamitin |
|---|---|---|---|---|
| **Bare Metal** | Tumatakbo nang direkta ang operating system sa physical hardware. | Pinakamahusay na CPU, disk, at input/output performance. Magagamit mo nang buo ang hardware. | Mahirap mabilisang i-copy o i-restore. Mas mahal ang hardware. Mahirap ilipat sa ibang machine. Kung iisa lang ang machine, ito ay **Single Point of Failure (SPOF)**. | Para sa performance testing, o kapag gusto mong gamitin nang buo ang hardware. |
| **Virtual Machine: KVM/QEMU, VirtualBox, VMware** | Nagpapatakbo ng ibang operating system sa ibabaw ng hypervisor. | Malakas ang separation sa pagitan ng host at guest. Maaaring gumawa ng snapshots at i-restore ang mga ito. Maaaring magpatakbo ng ibang OS mula sa host. Maganda para sa labs at testing. | Gumagamit ng mas maraming CPU, memory, at input/output dahil sa hypervisor. Kailangan ng mas malaking RAM at CPU mula sa host. Maaaring bahagyang mas mabagal ang disk at network kumpara sa bare metal. SPOF pa rin kung nasa iisang VM ang buong stack nang walang backup system. | Pinakakaraniwang pagpipilian para sa single-tier lab. Ligtas, flexible, at madaling kopyahin. |
| **Container: Docker/Podman** | Tumatakbo ang application sa isolated space, pero shared ang host kernel. | Napakagaan. Gumagamit ng mas kaunting resources. Mabilis mag-start at mag-stop. Madaling gawing muli gamit ang images. Maganda para sa mabilis na testing. | Dahil shared ang host kernel, mas mahina ang isolation kaysa VM. Maaaring maapektuhan ng kernel issue ang lahat ng containers. Hindi maaaring magpatakbo ng ibang kernel. Hindi lahat ng kernel modules o drivers ay pwedeng i-isolate. Mas kumplikado ang networking at storage setup. SPOF pa rin kung nasa iisang host ang lahat. | Maganda para sa mabilis at reproducible na labs. Hindi ideal kung kailangan mo ng napakalakas na isolation o ibang kernel. |

> **Note:** Para sa single-tier, maaaring ilagay ng VM o container ang buong stack: web server, runtime, at database. Dahil nasa iisang machine o host ang lahat, ito ay **Single Point of Failure (SPOF)**. Kapag namatay ang machine na iyon, mamamatay din ang website, application, at database.

## 2. Operating System

| OS | Package manager | Mga bentahe | Mga disbentahe | Kailan gagamitin |
|---|---|---|---|---|
| **Windows Server** | MSI / Windows Update | Napakahusay na gumagana sa IIS, .NET, Active Directory, at Microsoft tools. | Kailangan ng license. Mas malaki ang RAM usage. Minsan nagpaparestart ang updates. Hindi karaniwan sa open-source LAMP/LEMP stacks. | Gamitin lang kung kailangan talaga ng application ang .NET o IIS. |
| **Debian** | APT (.deb) | Napakastable, simple, at malinis ang dependency handling. Maraming Linux distributions ang batay dito. Napakakaraniwan para sa web servers. | Madalas mas luma ang packages dahil mabagal magbago ang Debian. Mas technical minsan ang advanced documentation. | Napakaganda para sa single-tier lab, lalo na sa open-source LAMP/LEMP stack. |
| **Ubuntu Server (LTS)** | APT (.deb) | Batay sa Debian. Napakaraming documentation. Sapat na bago ang packages para sa normal na pangangailangan. Beginner-friendly. | Maaaring mas marami ang default packages. Mas madalas ang updates kumpara sa pure Debian. | Maganda para sa beginners hanggang intermediate learners na gusto ng maraming guides. |
| **Fedora Server** | DNF (.rpm) | Gumagamit ng mas bagong technology, tulad ng newer SELinux, systemd, at modern tools. Maganda para sa pag-aaral ng modern concepts. | Maikli ang support period, humigit-kumulang 13 buwan. Hindi ideal kung gusto mong i-set up at iwanan na. | Maganda para sa pagsubok ng bagong technology, hindi para sa long-term use nang walang update plan. |
| **RHEL** | DNF (.rpm) | Napakastable. May enterprise documentation, structured security updates, at long-term support. | Bayad ang full support. Kailangan ng subscription para sa official repositories. | Mas angkop para sa production. Para sa simpleng practice, madalas hindi efficient dahil sa licensing. |
| **Rocky Linux / AlmaLinux** | DNF (.rpm) | Libre at compatible sa RHEL. Mahabang support at malakas na RPM ecosystem. | Walang direct vendor support tulad ng RHEL. Maaaring magkaiba ang behavior ng ilang RHEL-specific enterprise tools. | Magandang libreng RHEL-like option para sa single-tier lab. |
| **openSUSE Leap / SUSE Linux Enterprise** | Zypper (.rpm) | Pinapadali ng YaST ang configuration. Stable at may magagandang admin tools. | Mas maliit ang community kumpara sa Debian/Ubuntu para sa web-stack topics. Maaaring magkaiba ang file paths at settings sa karaniwang LAMP/LEMP guides. | Maganda para pag-aralan, pero maaaring kailanganin mong i-adjust ang common web-app guides. |
| **Alpine Linux** | APK (.apk) | Napakaliit at magaan. Kaunti ang memory usage at mabilis mag-start. Napakakaraniwan sa containers. | Gumagamit ito ng `musl` libc, hindi `glibc`. Maaaring hindi gumana ang ilang programs o PHP extensions. Napakabasic ng tools. Mas kailangang mag-ingat sa security settings. | Maganda para sa container-based single-tier setups o napakaliit na servers. Test your app first. |
| **Arch Linux** | Pacman (.pkg.tar.zst) | Rolling release. Napakabago ng packages. Napakarami sa AUR. Nagtuturo ng deep troubleshooting. | Ang rolling release ay maaaring magdulot ng breakage pagkatapos ng updates. Kailangan ng malalim na system knowledge. | Gamitin lang kung pangunahing layunin mo ay pag-aaral ng system. Hindi ito ang pinakasafe o pinakamadaling choice para sa simpleng lab. |
| **FreeBSD** | pkg / Ports | May Jails, built-in `pf` firewall, at magandang documentation sa Handbook. Stable para sa services. Hindi ito Linux. | Maraming web-app guides ang nag-aassume na Linux ang system. Kailangang i-build sa Ports ang ilang PHP modules o packages, kaya mas matagal. Mas maliit ang ecosystem ng ilang tools. | Maganda para sa pag-explore ng BSD-based single-tier setup. Mas maraming effort ang kailangan para sundan ang Linux guides. |
| **OpenBSD** | pkg_add / Ports | Napakafocus sa security. Secure by default at gumagamit ng tools tulad ng privsep, pledge, at unveil. Napakaminimal. | Mas kaunti ang available packages. Kailangan ng ibang configuration steps ang maraming web apps. Mas maliit ang web-stack community kumpara sa Linux. | Maganda para sa pag-aaral ng security hardening at minimal systems. Hindi ang pinakapraktikal na choice para sa ordinary web apps. |

## 3. Web Server

| Web server | Type | Mga bentahe | Mga disbentahe | Kailan gagamitin |
|---|---|---|---|---|
| **[Apache](https://httpd.apache.org/)** | Process/thread-based at module-based | Napakaflexible sa `.htaccess`. Maraming modules, tulad ng mod_rewrite at ModSecurity connectors. Tugma sa halos lahat ng PHP shared-hosting guides. | Maaaring mas malaki ang memory usage per connection sa default settings. Maaaring kailanganin mong i-adjust ang event o MPM settings. Kapag sobrang dami ng virtual hosts o modules, magulo ang configuration. | Maganda para sa single-tier setup na nangangailangan ng flexibility, lalo na kung gumagamit ng `.htaccess`. |
| **[Nginx](https://nginx.org/)** | Event-driven at asynchronous | Napakahusay sa maraming sabay-sabay na connections. Mas kaunti ang RAM usage. Mabilis para sa static files. Maganda ang compatibility sa PHP-FPM. | Hindi maaaring gumamit ng `.htaccess`. Kailangang i-configure ang rules sa virtual host file. Walang katumbas ang ilang Apache modules sa Nginx. Maaaring magkaiba ang debugging kung sanay ka sa Apache. | Napaka-efficient para sa single-tier server na may medium o high traffic, o limited resources. |
| **[Caddy](https://caddyserver.com/)** | Event-driven na may built-in reverse proxy | Napakasimple ng configuration. Maaaring kumuha ng HTTPS certificates automatically gamit ang ACME. Madali ang syntax. Simple ang reverse proxy setup. | Mas kaunti ang modules kumpara sa Apache o Nginx. Kailangan ng plugins ang ilang special use cases. Nakadepende sa ACME at DNS ang TLS. | Maganda para sa mabilis na lab na may automatic HTTPS. Kailangan mo pa ring maunawaan ang settings at limitations nito. |
| **[IIS](https://www.iis.net/)** | Integrated sa Windows | Natural na gumagana sa Windows. May graphical admin tool. Maganda ang integration sa .NET at ASP.NET. | Windows lang ang kayang patakbuhin. Mas malaki ang resource usage. Mas hindi flexible para sa non-.NET stacks. Hindi karaniwan sa Linux open-source tools. | Gamitin lang kung talagang Windows o .NET-based ang stack mo. |

## 4. Server-Side Runtime

| Runtime | Ano ang ginagawa nito | Mga bentahe | Mga disbentahe | Kailan gagamitin |
|---|---|---|---|---|
| **[PHP-FPM](https://www.php.net/manual/en/install.fpm.php)** | FastCGI service para sa PHP | Napakakaraniwan sa LAMP/LEMP. Tugma sa maraming applications. Maaaring i-configure ang pools, users, process limits, at iba pang settings. | Para lang sa PHP. Kailangang i-set nang tama ang socket o port permissions. Maaaring magsayang ng resources ang maling pool configuration. | Kailangan para sa PHP applications sa single-tier setup. |
| **[Node.js](https://nodejs.org/)** | JavaScript runtime, event-driven | Maganda para sa input/output work. Angkop para sa real-time APIs. Maaaring gamitin ang JavaScript para sa buong application. Napakalaki ng npm ecosystem. | Kailangang panatilihing tumatakbo ang process, halimbawa gamit ang systemd o PM2. Maaaring maging seryoso ang memory leaks sa iisang server. Kailangang maayos ang error handling. | Maganda para sa JavaScript o TypeScript applications. Kailangan ng process management dahil hindi laging auto-start tulad ng PHP-FPM. |
| **[Python](https://www.python.org/)** gamit ang Gunicorn o uWSGI | Python runtime | Malalakas na frameworks tulad ng Django, Flask, at FastAPI. Napakaflexible. | Hindi maaaring direktang patakbuhin ng web server ang Python. Kailangan ng WSGI o ASGI app server. Dapat gumamit ng virtual environments at maayos na dependency management. | Maganda para sa Python applications. Sa single-tier setup, kailangan mo ng separate app server. |
| **[Java](https://openjdk.org/)** gamit ang Tomcat, Jetty, o Undertow | JVM runtime | Stable at malakas para sa complex applications. Maaaring i-tune ang garbage collection. | Mas malaki ang memory usage, lalo na sa maliit na server. Mas mabagal ang startup. Kailangang pansinin ang JVM settings. | Maganda para sa Java o Jakarta EE applications. Hindi pinaka-efficient para sa maliit na VM o resources. |
| **[.NET](https://dotnet.microsoft.com/)** gamit ang Kestrel at reverse proxy | .NET runtime | Magandang performance. Gumagana sa Linux at Windows. Modern integration. | Kailangang tugma ang .NET runtime version sa application. Sa Linux, karaniwang nilalagyan ng Nginx o Apache ang harap ng Kestrel. Kailangang pansinin ang resource usage. | Maganda kung .NET ang ginamit sa application. Pwede pa ring gamitin sa single-tier Linux setup. |

## 5. Database at Cache para sa Single-Tier

| Komponent | Type | Mga bentahe | Mga disbentahe | Kailan gagamitin |
|---|---|---|---|---|
| **[MariaDB](https://mariadb.org/)** | Relational SQL database | Open source. Para sa karamihan ng cases, katulad ng paggana ng MySQL. Karaniwan sa LAMP. Maraming documentation. | May pagkakaiba ang ilang features mula sa MySQL sa certain versions. Maaaring kailanganin ang tuning para sa special workloads. | Napaka-relevant para sa single-tier, lalo na sa PHP stacks. |
| **[MySQL](https://www.mysql.com/)** | Relational SQL database | Napakakaraniwan. Malaking ecosystem at maraming tools. | Tingnan ang license at distribution dahil Oracle ang may-ari ng MySQL. Nakadepende sa edition ang ilang features. | Relevant, pero mas madalas irekomenda ang MariaDB para sa pure open-source learning. |
| **[PostgreSQL](https://www.postgresql.org/)** | Relational SQL database | Napakalakas para sa data integrity. Maraming data types at advanced SQL features. Solid ang ACID support. Popular sa modern applications. | Mas strict, kaya kailangang maunawaan ang schemas at permissions. Maaaring mas malaki ang resource usage kumpara sa MySQL para sa simpleng projects. | Ideal para sa single-tier kung kailangan ng application ang mas complex relational features. |
| **[SQLite](https://sqlite.org/)** | File-based relational database | Walang setup na kailangan. Isang file lamang. Magaan at hindi kailangan ng separate service. Maganda para sa isang user o low traffic. | Hindi dinisenyo para sa maraming processes na sabay-sabay na nagsusulat. Hindi angkop para sa heavy multi-connection work. Gumagamit ng file locking. | Maganda para sa maliliit na applications, prototypes, o internal tools na may low traffic. |
| **[SQL Server Express](https://www.microsoft.com/sql-server/sql-server-downloads)** | Relational SQL database | Malakas at tugma sa .NET. Libre ang Express edition, pero may limits. | May limits ang Express sa RAM at database size, depende sa version. Pinakaangkop sa Windows. Sa Linux, mas karaniwan ang MariaDB at PostgreSQL sa labs. | Gamitin lang para sa .NET single-tier stack. |
| **[Redis](https://redis.io/)** | In-memory key-value store | Napakabilis para sa cache at sessions. Magaan at madaling gamitin. Maaaring bawasan ang database load. | Nasa RAM ang data, kaya kailangan ng persistence kung gusto mong i-save. Hindi replacement para sa relational database. Kailangang i-set ang `maxmemory` at eviction policy. Tingnan ang license ng version na ginamit. | Optional. Napak useful para sa applications na maraming reads, caching, o sessions. Hindi required. |

## 6. Open Source para sa Production: Mga Bentahe, Risiko, at Responsibilidad

**Pangunahing bentahe:**
1. **Transparency/audit** — maaaring suriin ang implementasyon ng auth, permission, encryption, secret handling; nagpapadali ng security review & compliance.
2. **Portability** — maaaring lipat ng provider nang walang rewrite; flexibility sa migrasyon.
3. **Customization** — patches, integrations, features ayon sa pangangailangan.
4. **Ecosystem** — dokumentasyon, bug reports, komunidad; karaniwang isyu maaaring naiayos na ng iba.
5. **Kontrol sa data/infra** — self-hosted: lokasyon ng data, access, log retention, backup ayon sa policy.
6. **Gastos** — walang lisensya per core/user/instance; ngunit may gastos sa engineer, infra, support, audit.
7. **Reproducibility** — i-pin ang dependency versions, automate ang builds, staging na malapit sa production.

**Tunay na risiko:**
- **Hindi awtomatikong secure** — Snyk 2023: 40% respondents hindi gumagamit ng SCA/SAST, 96% supply chain handling ad hoc. Open source ≠ audited.
- **Ketergantungan sa maintainer** — maaaring nakasalalay ang proyekto sa iilang maintainer; suriin ang release history, activity, responsible disclosure, bilang ng maintainer.
- **Supply chain** — event-stream (2018), ua-parser-js (2021), XZ Utils (2024) nagpapakita na maaaring masusupi ang dependencies. Gumamit ng lockfile, artifact verification, SBOM, build isolation.
- **PHP CVE 2026** — CVE-2026-109618/109619 (RCE nang walang auth) sa PHP 8.5.12/8.4.27/8.3.36/8.2.35. Patch kinakailangan; ang impact ay nakadepende sa process config. Ref: [PHP Security Advisory](https://www.php.net/archive/2026.php), [NCSC UK](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php).
- **Patch vs downtime** — pag-delay ng patch = mananatiling vulnerable; update nang walang test = errors/downtime. Kailangan ng patch management: tukuyin → risk assessment → test → staged deploy → i-verify → rollback.
- **Compatibility** — musl (Alpine) vs glibc; maaaring mabigo ang PHP/Python native/Node.js extensions. Pumili ng OS batay sa pangangailangan ng app, i-pin ang versions, test sa environment na malapit sa production.
- **Lisensya** — hindi awtomatikong pinipilit ng GPL/AGPL ang pag-open source ng buong codebase; nakadepende sa paggamit/distribusyon. Black Duck 2026: 87% codebase may ≥1 vulnerability (audit sample, hindi universal). Lisensya inventory + legal review para sa commercial.
- **Dokumentasyon/suporta** — maliliit na proyekto: iilang maintainer, mabagal na respons. Para sa critical systems, isaalang-alang ang commercial support.

**Risiko vs kontrol:**

| Risiko | Kontrol |
|---|---|
| Vulnerability | SCA, official advisories, patch management, testing |
| Supply-chain | Lockfile, provenance, artifact verification, build isolation |
| Hindi napananatili ang proyekto | Project health eval, support plan, migration alternatives |
| Downtime dahil sa upgrade | Staging, integration test, staged deploy, recovery plan |
| Non-compliance sa lisensya | SBOM, license scanning, legal review |
| Data leak | Least privilege, secret management, encryption, monitoring |
| Pagkabigo ng recovery | Hiwalay na backup, restore test, recovery documentation |

Karamihan sa mga risikong ito ay mayroon din sa proprietary software. Ang pagkakaiba: access model, distribution, support, at pagbahagi ng responsibilidad.

**Production readiness checklist:**
- Seguridad: may security advisory, mekanismo para sa vulnerability reporting, traceable update process.
- Maintenance: sapat na ebidensya ng pagpapanatili, responsible maintainer, fix path.
- Dependency: direct & transitive na maaaring i-inventory, i-scan, i-pin ang version.
- Integrity ng distribution: signature, checksum, o provenance na available.
- Compatibility: OS, runtime, extension, library versions na tumugma sa target environment.
- Lisensya: lahat ng lisensya ng komponente ay kilala at nasuri ang mga obligasyon.
- Operasyon: monitoring, logging, backup, deployment docs, recovery procedures.
- Sustainability: maintenance cost, support needs, migration options na katanggap-tanggap.

Ref: [OpenSSF Concise Guide](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html), [OpenSSF Project Security Baseline](https://baseline.openssf.org/versions/2026-08-28).

**Estrategiya ng deployment (single-tier):**
1. **Pagpili & inventory** — pumili ng software, i-inventory ang versions & licenses, tukuyin ang dependencies, italaga ang owner.
2. **Hardening & testing** — minimal config, least privilege, pagbabawas ng ingress/egress, proteksyon ng secret, compatibility test bago deploy.
3. **Monitoring & patch management** — subaybayan ang bagong vulnerabilities, processes, pagbabago ng file, auth, connections, kalusugan ng service. I-prioritize ang patches batay sa risk.
4. **Recovery & incident response** — hiwalay na backup, restore test, idokumento ang credential rotation, maghanda ng isolation & rebuild procedures.

Sa single-tier, lahat ng komponente ay nasa isang makina. Ang kompromiso ng isang runtime/process na may mataas na privilege ay maaaring magbanta sa iba pang komponente. Ang open source ay hindi nag-aalis ng risikong ito; ang pagbabawas ng privilege, network controls, at paghihiwalay ng backup ay kinakailangan pa rin.

**Konklusyon:** Ang open source ay lubos na angkop para sa production kapag kailangan ng organisasyon ang transparency, flexibility, portability, kontrol sa infrastruktura, at kakayahang i-customize ang mga sistema. Ang pinakamalaking bentahe: mas maraming pagpili at kontrol — maaaring suriin ang implementasyon, pumili ng deployment method, i-audit ang dependencies, i-customize ang config, at magplano ng migrasyon. Ngunit ang kontrol ay may kasamang responsibilidad: siguraduhing napananatili ang software, hinaharap ang vulnerabilities, pinagkakatiwalaan ang dependencies, nasusunod ang licenses, nasubok ang updates, at maaaring maibalik ang mga sistema.

- Open source nang walang pamamahala = nakatagong source ng risk.
- Open source nang may maayos na pamamahala = mataas na halaga ng transparency at kontrol.
- Ang proprietary software ay nangangailangan pa rin ng security management; ang vendor support ay hindi nag-aalis ng responsibilidad ng organisasyon.

Ang layunin ay hindi ang pumili ng open source dahil laging mas mabuti, kundi pumili ng software batay sa pangangailangan, risk, operational capability, at kinakailangang antas ng kontrol.

## 7. Online Access: Domain, DNS, Tunnel, Mga Bentahe at Disbentahe

| Access method | Mga kailangan | Mga bentahe | Mga disbentahe at risks | Kailan gagamitin |
|---|---|---|---|---|
| **Direct public IP mula sa home/ISP** | Public IP mula sa ISP, port forwarding sa router, at firewall. Maaaring humadlang ang CGNAT. | Ikaw ang may kontrol mula simula hanggang dulo. Walang third-party service na kailangan para sa routing. | Maraming home ISPs ang gumagamit ng CGNAT, kaya maaaring hindi gumana ang port forwarding. Maaaring i-scan nang direkta ang IP mo. Nakadepende sa home power, internet, at router. Maaaring magbago ang ISP settings. | Gamitin lang kung totoong public IP ang binibigay ng ISP at naiintindihan mo ang exposure risk. |
| **VPS na may public IP** | VPS account, OS sa VPS, at firewall settings. Optional ang domain. | Stable na access mula sa internet. Hindi nakadepende sa home network. Mas madaling i-access publicly. Maaaring tumakbo 24/7 habang up ang provider. | May bayad ang VPS. Maaari pa ring i-scan ang public IP. Nakadepende sa provider at data center. Kailangang i-harden ang SSH, firewall, at updates. | Pinakapraktikal na choice para sa medium- o long-term public access na may full control sa origin server. |
| **Domain + DNS: A, AAAA, o CNAME records** | Registered domain at DNS provider. Maaaring gamitin kasama ang public IP o VPS. | Madaling basahin ng tao. Pinapadali ang TLS gamit ang Let's Encrypt. Flexible: pwedeng i-point sa IP, VPS, o proxy. | May taunang bayad ang domain. Kailangang i-manage ang DNS records. Kapag down ang DNS, maaaring mag-fail ang name resolution. Kailangan pa ring online ang origin server. | Halos required kung gusto mo ng HTTPS na may domain name o gusto mong mag-publish ng website publicly. |
| **Reverse proxy: Nginx, Apache, o Caddy** | Web server at virtual-host configuration. Karaniwang ginagamit kasama ang public IP o domain. | Maaaring mag-host ng maraming sites sa iisang IP. Maaaring paghiwalayin ang routing. Maaaring magdagdag ng security headers. Maaaring ikonekta ang WAF. | Nagdaragdag ng configuration. Maaaring ma-expose ang private paths dahil sa maling setting. Kailangan pa rin ng open ports sa firewall o router kung walang tunnel. | Mahalagang maunawaan para sa malinis na single-tier setup, whether gumagamit ka ng tunnel o hindi. |
| **Cloudflare Tunnel: cloudflared, dating Argo Tunnel** | Cloudflare account, kadalasang domain na naka-manage sa Cloudflare, `cloudflared` sa server, at outgoing connection papunta sa Cloudflare. | **Hindi na kailangang buksan ang incoming ports.** Maaaring manatiling sarado ang ports 80 at 443. Maaaring i-expose ang local home service sa internet. Maaaring gamitin ang Cloudflare rules. Maganda para sa labs na walang public IP o may CGNAT. | **Karaniwang kailangan ng domain** para sa custom hostname. Full dependency ka sa Cloudflare: tunnel, DNS, at Cloudflare network. Kapag namatay ang local server o internet, mamamatay ang tunnel. Kapag may problema ang Cloudflare, maaaring mag-fail ang access. Pwedeng gamitin ang Quick Tunnel para sa testing nang walang sariling domain, pero hindi ideal para sa fixed domain name. Dapat pa ring secure ang origin server. Hindi replacement ang tunnel para sa hardening. Nakadepende sa account o product plan ang ilang features. | Napakaganda para sa home lab, lalo na kapag may CGNAT, o kapag gusto mong mas kaunti ang open incoming ports. Publishing method lang ito, hindi full application security. |

**Mahahalagang punto tungkol sa online access:**

- **Hindi required ang domain** kung ipapasok mo lang ang server gamit ang public IP at port.  
- **Required ang domain** kung gusto mo ng custom hostname sa pamamagitan ng Cloudflare Tunnel gamit ang normal settings.  
- **Gumagamit ng outgoing connection ang Cloudflare Tunnel** mula sa server papunta sa Cloudflare. Kaya maaaring isara nang buo ang incoming ports.  
- **Maaaring magdagdag ng network filtering ang Cloudflare proxy**, pero target pa rin ang origin server. Kapag down ang origin, hindi kayang gawing gumana ng Cloudflare ang application mo.  
- **Dependencies:** Home lab + Tunnel ay nakadepende sa power, ISP, server, at Cloudflare. VPS + Tunnel o Proxy ay nakadepende sa VPS, provider, at Cloudflare. Mas maraming middle services, mas maraming possible failure points.  
- **Para sa practice,** mas mahalagang maunawaan ang trade-offs na ito kaysa simply gawing reachable ang app.

## 8. Operations & Maintenance (Single-Tier)

| Aspeto | Gagawin | Bakit |
|---|---|---|
| Lokal na monitoring | Subaybayan ang CPU, RAM, disk, status ng service (systemd), error logs (journald) | Makadetect ng isyu bago mapansin ng mga user |
| Uptime check | Gumamit ng Uptime Kuma o Healthchecks para mag-ping ng endpoint nang periodiko | Malalaman kung down ang server |
| Simpleng alerting | Magpadala ng notifikasi (email/Telegram) kung down ang service o puno ang disk | Mabilis na respons nang walang complex dashboard |
| Backup | Regular na pg_dump/mysqldump, restic/borg sa offsite storage (S3/R2/B2) | Mababawi mula sa disk failure o human error |
| Restore test | Subukan ang restore sa hiwalay na VM/container nang periodiko | Ang hindi natesting backup ay hindi napatunayang magagamit |
| Pamamahala ng log | Persistent journald + logrotate, retention ayon sa pangangailangan | Imbestigasyon ng insidente & pagtipid ng disk |
| Sizing at gastos | Pumili ng minimal VPS spec (RAM/CPU/disk) ayon sa stack; i-upgrade kung bottleneck | Makatipid, mag-scale kung kinakailangan |
| Kailan lalabas sa single-tier | Indicators: mataas na trafik, malaking DB, risk ng SPOF, pangangailangan ng horizontal scaling | Malalaman kung kailan hindi na sapat ang single-tier |

**Simpleng praktis:**
- Cron para sa daily backup, ipadala offsite.
- Systemd para sa auto-restart ng service.
- `df -h` at `free -h` para sa routine resource check.
- Idokumento ang credentials at rebuild steps.

## Architecture: Single-Tier

```mermaid
flowchart TB
    C["Client / Browser"]
    CF["Cloudflare DNS / Proxy / Tunnel (Optional)"]

    subgraph SERVER["Single-Tier Server (Bare Metal / VM / Container Host)"]
        subgraph STACK["All Layers on One Server"]
            WS["Web Server\n(Apache / Nginx / Caddy / IIS)"]
            WAF["WAF\n(ModSecurity/Coraza + OWASP CRS)"]
            RT["Server-Side Runtime\n(PHP-FPM / Node.js / Python / Java / .NET)"]
            DB[("Database\n(MariaDB / MySQL / PostgreSQL / SQLite / SQL Server)")]
            CACHE[("Cache - Optional\n(Redis)")]
        end
        WS --> WAF
        WAF --> RT
        RT --> DB
        RT -.-> CACHE
    end

    C --> CF
    CF -. Tunnel/Proxy .-> WS
    C -. Direct access (IP:Port) .-> WS
```

## Konklusyon

Ang **single-tier setup** ay maganda para sa web-app experiments dahil maaari mong pag-aralan ang lahat ng pangunahing bahagi sa iisang machine.

Ang pagpili mo ng operating system, web server, runtime, database, WAF, at publishing method ay nakakaapekto sa:
- Performance
- Complexity
- Security

Ang pangunahing layunin ay hindi lamang ang pagpapatakbo ng application.  
Ang pangunahing layunin ay maunawaan kung paano gumagana ang bawat bahagi, kung paano nag-uusap ang mga bahaging ito, at kung paano sila gawing secure.