# Single-Tier Server Stack

[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)
[🇬🇧 Read in English](server-single-tier-stack-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](server-single-tier-stack-ms.md)

![Single-Tier Server Stack](single-tier-stack.png)

## Isang Server, Isang Stack

Ang **Single-Tier Server Stack** ay nangangahulugang ang [web server](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server), [application runtime](https://en.wikipedia.org/wiki/Runtime\_system), at [database](https://en.wikipedia.org/wiki/Database) ay lahat nasa **iisang makina lamang**.

Isipin mo ang isang karinderya na nasa iisang bubong. Ang cashier, kusina, at bodega ay nasa iisang gusali. Direktang naproseso ang order doon mismo.

Ganito rin ang nangyayari sa single-tier: lahat ng bahagi ay nasa iisang server para mas madaling maunawaan.

## Paano Ito Gumagana?

Kapag may bumisita sa website mo gamit ang [web browser](https://en.wikipedia.org/wiki/Web\_browser), ganito ang daloy:

1. **Browser** → Nagpapadala ng [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) sa server
2. **Web Server** → Tumatanggap at nagrere-route ng request sa aplikasyon
3. **Application Runtime** → Pinapagana ang [business logic](https://en.wikipedia.org/wiki/Business\_logic) ng app (form, login, validation, atbp.)
4. **Database** → Kinukuha, nagdadagdag, nag-update, o nagtatanggal ng kinakailangang data
5. **Response** → Nagpapadala ang web server ng [HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) (HTML, JSON, o file) pabalik sa browser

Lahat ito ay nangyayari sa **iisang makina lamang**.

## Mga Pangunahing Komponente

| Komponente | Tungkulin | Mga Sanggunian |
|---|---|---|
| **[Web Server](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server)** | Pintuan. Tumatanggap ng request, nagrere-route, at nagbabahagi ng response. | [Nginx](https://nginx.org/), [Apache HTTP Server](https://httpd.apache.org/), [Caddy](https://caddyserver.com/) |
| **[Application Runtime](https://en.wikipedia.org/wiki/Runtime\_system)** | Utak. Pinapagana ang code ng aplikasyon. | [PHP-FPM](https://www.php.net/manual/en/install.fpm.php), [Node.js](https://nodejs.org/), [Gunicorn](https://gunicorn.org/), [Kestrel (.NET)](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel) |
| **[Database](https://en.wikipedia.org/wiki/Database)** | Imbakan. Nagtatago at nagpapanatili ng data ng aplikasyon. | [MariaDB](https://mariadb.org/), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), [SQLite](https://sqlite.org/) |

Pwede rin magdagdag ng [cache](https://en.wikipedia.org/wiki/Cache\_(computing)) gaya ng [Redis](https://redis.io/) para mapabilis ang pag-access sa madalas na data.

## Mga Karaniwang Stack: LAMP, LEMP, WAMP, WIMP, FAMP at Iba Pa

Ang kombinasyon ng [operating system](https://en.wikipedia.org/wiki/Operating\_system), web server, database, at [programming language](https://en.wikipedia.org/wiki/Programming\_language) ang bumubuo sa [solution stack](https://en.wikipedia.org/wiki/Solution\_stack). Mga halimbawa lamang ang mga nasa ibaba, hindi mga obligadong patakaran.

| Acronym | Buong Pangalan | Tala |
|---|---|---|
| **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)** | *Linux, Apache, MySQL/MariaDB, PHP/Perl/Python* | Klasiko at pinakakaraniwang itinuturo sa mga nagsisimula. |
| **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** | *Linux, Nginx, MySQL/MariaDB, PHP-FPM* | LAMP na gamit ang [Nginx](https://nginx.org/) at [PHP-FPM](https://www.php.net/manual/en/install.fpm.php). Mas magaan at episyente. |
| **[WAMP](https://www.oreilly.com/library/view/learning-php-mysql/9780596157135/ch01.html)** | *Windows, Apache, MySQL/MariaDB, PHP* | Angkop sa lokal na pagsasanay sa [Windows](https://www.microsoft.com/windows). |
| **[WIMP](https://www.itmedia.co.jp/enterprise/articles/0903/17/news004.html)** | *Windows, IIS, MySQL/MariaDB, PHP* | Gumagamit ng [IIS](https://www.iis.net/) kapalit ng Apache. Tandaan na ang "WIMP" ay may hiwalay na kahulugan sa UI. |
| **[FAMP](https://en.wikipedia.org/wiki/FAMP)** | *FreeBSD, Apache, MySQL/MariaDB, PHP* | Nakabatay sa [FreeBSD](https://www.freebsd.org/). Hindi masyadong karaniwan sa mga nagsisimula. |
| **[LAPP](https://www.x386.org/guides/lapp/)** | *Linux, Apache, PostgreSQL, PHP* | LAMP kung saan pinalitan ang MySQL/MariaDB ng [PostgreSQL](https://www.postgresql.org/). |
| **[LEPP](https://lempstack.com/)** | *Linux, Nginx, PostgreSQL, PHP* | Nginx + PostgreSQL na variant. Hindi gaanong standard kumpara sa LAMP/LEMP. |

> **Tala:** Puwedeng palitan ang MySQL ng [MariaDB](https://mariadb.org/), gumamit ng ibang database, o palitan ang PHP ng iba pang runtime tulad ng [Node.js](https://nodejs.org/) o [Python](https://www.python.org/).

## Bare Metal, VM, o Container?

| Paraan | Paliwanag | Mga Sanggunian | Tala |
|---|---|---|---|
| **[Bare Metal](https://en.wikipedia.org/wiki/Bare\_machine)** | Direktang tumatakbo sa pisikal na hardware. | [IBM — Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers) | Direktang access sa hardware, depende sa specs at configuration ang performance. |
| **[Virtual Machine (VM)](https://en.wikipedia.org/wiki/Virtual\_machine)** | Virtual na kompyuter sa loob ng PC/laptop mo. | [KVM](https://www.linux-kvm.org/), [VirtualBox](https://www.virtualbox.org/), [VMware](https://www.vmware.com/) | **Pinakamainam para sa pag-aaral**. Madali i-snapshot at i-reset. |
| **[Container](https://en.wikipedia.org/wiki/Containerization\_(computing))** | Pinaghihiwalay ang app nang hindi kinakailangan ng buong OS. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) | Magaan, mabilis, nakakatipid ng resources. Mainam sa lokal na pagsasanay. |

## Mga Kalamangan, Kahinaan & SPOF

| Aspeto | Paliwanag |
|---|---|
| **Mga Kalamangan** | Simple, mura, madali maunawaan, nasa iisang lugar, perpekto sa pag-aaral. |
| **Mga Kahinaan** | Nagbabahagi ng resources, pwedeng magulo ang configuration, limitado ang scalability. |
| **[SPOF (Single Point of Failure)](https://en.wikipedia.org/wiki/Single\_point\_of\_failure)** | Kapag bumagsak ang iisang makina na ito, **sabaysabay ding babagsak ang web server, application runtime, at database**. Hindi na maa-access ang aplikasyon. |

## Kailan Ito Angkop at Kailan Kailangang Lumipat

| Sitwasyon | Hatol | Tala |
|---|---|---|
| **Pag-aaral, pagsasanay, prototyping** | **Angkop** | Angkop para maunawaan ang ugnayan ng mga bahagi. |
| **Maliit na personal na proyekto** | **Sapat pa rin** | Pwede basta malinis, binabantayan, at may backup. |
| **Dumarami na ang traffic** | **Isaalang-alang ang paghiwalay** | Mauubos na ang resources, lalo na ang database. |
| **Kailangan ng high uptime o malakihang scale** | **Kailangang isaalang-alang ang paghiwalay** | Pwede pa rin i-optimize ang single-tier. Ang paghiwalay ng tier ay dapat isaalang-alang batay sa availability, kapasidad, at arkitektura. |

## Mga Tip Para Magsimula

1. **Focus sa daloy** — Unawain ang `browser → web server → application runtime → database`.
2. **Pumili ng ISANG stack** — Magsimula sa **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** o **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)**. Masterin muna ito bago sa iba.
3. **Magsanay nang lokal** — Gumamit ng [VM](https://en.wikipedia.org/wiki/Virtual\_machine) o [container](https://en.wikipedia.org/wiki/Containerization\_(computing)) sa laptop mo. Gumamit ng `localhost`.
4. **Tandaan ang SPOF** — Mainam ito sa pag-aaral, hindi para sa mga aplikasyon na kailangang online 24/7.

**Sa madaling salita:** *Isang server, lahat ng komponente. Simple para matutunan, limitado sa pag-scale. Unawain muna ito para maunawaan kung bakit kailangan nang paghiwalayin ang mga komponente sa hinaharap.*
