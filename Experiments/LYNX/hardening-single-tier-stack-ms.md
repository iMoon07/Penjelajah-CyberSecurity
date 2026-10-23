# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)  
[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

Artikel ini membincangkan **hardening single-tier stack**. Maksudnya, semua layer—web server, runtime, database, dan cache—berada pada satu server, dan kita akan mengamankannya daripada asas tanpa perlu membincangkan pemasangan dari kosong.

Tujuannya adalah memahami:
- Urutan hardening yang munasabah
- Standard rujukan seperti CIS
- Tetapan keselamatan bagi setiap layer
- Pengesahan selepas hardening
- Kesilapan umum yang perlu dielakkan

## 1. Prinsip Asas Hardening

Hardening bukan satu butang. Ia ialah proses berperingkat:

1. **Minimize attack surface** — buka hanya port dan service yang diperlukan.
2. **Least privilege** — setiap service berjalan sebagai user yang tidak memerlukan root.
3. **Defense in depth** — firewall, WAF, TLS, logging, semuanya berlapis.
4. **Update dan patch** — sistem yang tidak dikemas kini ialah sasaran.
5. **Monitoring** — anda tidak dapat mengesan apa yang tidak anda lihat.
6. **Recovery** — hardening tidak menggantikan backup dan rancangan pemulihan.

> **Warning:** Jangan lakukan hardening terus dalam production. Sentiasa uji dalam lab atau VM dahulu.

## 2. Standard Hardening: CIS

Hardening tidak perlu diteka. Terdapat standard yang boleh digunakan sebagai rujukan:

| Standard | Fungsinya | Relevansi untuk single-tier |
|---|---|---|
| **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** | Panduan konfigurasi selamat untuk OS, web server, database, Docker, dan produk lain | Rujukan konkrit untuk mengamankan setiap layer |
| **[CIS Controls](https://www.cisecurity.org/controls/cis-controls-list)** | 18 kawalan keselamatan yang diprioritaskan | Rangka kerja besar: inventory, patch, access control, logging, recovery, incident response |
| **Vendor hardening guide** | Panduan rasmi daripada Debian, Ubuntu, Red Hat, Nginx, MariaDB, PostgreSQL, dan lain-lain | Butiran konfigurasi mengikut distro dan perisian yang digunakan |

Untuk single-tier, benchmark yang paling relevan:

| Layer | CIS Benchmark yang relevan |
|---|---|
| OS | CIS Ubuntu Linux Benchmark, CIS Debian Linux Benchmark, CIS Red Hat Enterprise Linux Benchmark |
| Web server | CIS Nginx Benchmark, CIS Apache HTTP Server Benchmark |
| Database | CIS MariaDB Benchmark, CIS MySQL Benchmark, CIS PostgreSQL Benchmark |
| Container | CIS Docker Benchmark |
| Orchestration | CIS Kubernetes Benchmark, hanya jika stack berkembang ke Kubernetes |

CIS Benchmarks ialah cadangan konfigurasi selamat yang dibangunkan melalui konsensus pengamal keselamatan dan tersedia percuma dalam format PDF untuk kegunaan bukan komersial. CIS Controls memetakan amalan tersebut kepada 18 kawalan keutamaan, daripada inventory asset sehingga penetration testing. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)

> **Note:** CIS bukan bermakna perlu diterapkan 100%. Pilih tahap mengikut keperluan lab atau production, kemudian dokumentasikan apa yang diterapkan dan apa yang sengaja dilepaskan.

## 3. Sistem Operasi

| Aspek | Yang dilakukan | Mengapa penting |
|---|---|---|
| Update dan patch | Kemas kini OS dan package secara berkala | Menutup celah yang sudah diketahui |
| User dan privilege | Jangan log masuk sebagai root; buat user biasa dengan sudo | Mengurangkan kesan jika akaun bocor |
| SSH | Matikan root login dan password auth; gunakan SSH key | SSH ialah pintu masuk utama server |
| Firewall host | Default deny incoming; buka hanya 22, 80, 443 | Mengurangkan exposure port |
| Auto patch | Aktifkan unattended upgrades untuk patch keselamatan | Mengekalkan keselamatan sistem tanpa campur tangan manual |
| Service minimization | Matikan service yang tidak digunakan | Semakin sedikit service, semakin kecil attack surface |
| Parameter kernel | Terapkan sysctl hardening yang relevan | Mengurangkan risiko penyalahgunaan pada tahap rangkaian |

> **Important:** Jangan buka port database (3306, 5432) kepada awam. Database hanya boleh diakses daripada localhost atau rangkaian dalaman.

## 4. Service, Fail, dan Secret

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Service minimum | Buang atau nyahaktifkan service yang tidak digunakan | Mengurangkan laluan masuk dan beban server |
| Kebenaran fail | Hadkan kebenaran config, log, dan fail sensitif | Menghalang akses yang tidak perlu |
| Umask | Gunakan kebenaran lalai yang ketat | Fail baharu tidak serta-merta terbuka kepada semua user |
| SELinux/AppArmor | Aktifkan mengikut distro | Mengehadkan tingkah laku service jika berlaku compromise |
| Secret | Jangan letak password atau API key dalam repo atau fail world-readable | Menghalang kebocoran credential |
| Environment variable | Simpan secret dalam fail dengan kebenaran ketat atau secret manager | Mengurangkan risiko kebocoran konfigurasi |

> **Warning:** Fail `.env`, credential database, SSH key, dan backup tidak boleh masuk ke Git. Gunakan `.gitignore` dari awal.

## 5. Hardening Web Server

| Web server | Tetapan penting | Matlamat |
|---|---|---|
| Nginx | `server_tokens off`, security headers, hadkan method HTTP, nyahaktifkan autoindex | Menyembunyikan versi dan mengehadkan request berbahaya |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers | Menyembunyikan maklumat server dan menolak method berbahaya |
| Caddy | Security header, reverse proxy dengan TLS automatik | Konfigurasi ringkas dengan lalai yang selamat |

Security header yang sebaiknya ada:

- `X-Frame-Options: SAMEORIGIN` — menghalang clickjacking
- `X-Content-Type-Options: nosniff` — menghalang MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin` — kawalan referrer
- `Permissions-Policy` — mengehadkan akses ciri browser

## 6. TLS / HTTPS

| Aspek | Cadangan | Mengapa |
|---|---|---|
| TLS minimum | TLS 1.2, lebih baik TLS 1.3 | Protocol lama mempunyai celah |
| Cipher | Hanya cipher moden, contohnya ECDHE dan GCM | Menghalang downgrade attack |
| HSTS | Aktifkan dengan `max-age` yang panjang | Memaksa HTTPS dalam browser |
| Sertifikat | Let's Encrypt melalui Certbot, pembaharuan automatik | Percuma dan umum digunakan |
| Session | Hadkan session timeout dan pertimbangkan menyahaktifkan session tickets | Mengurangkan risiko penggunaan semula session |

## 7. WAF: Web Application Firewall

| Komponen | Fungsinya | Nota |
|---|---|---|
| ModSecurity | WAF engine untuk Apache/Nginx | Perlu tuning supaya tidak berlaku false positive |
| OWASP CRS | Rule set standard industri | Mulakan dengan mod `DetectionOnly` |
| Coraza | Alternatif WAF berasaskan Go | Ringan dan sesuai untuk setup moden |

> **Warning:** Jangan terus aktifkan WAF mod blocking dalam production. Mulakan dengan `DetectionOnly`, analisis log, kemudian aktifkan secara berperingkat.

## 8. Hardening Database

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Pemasangan selamat | Jalankan secure installation lalai database | Buang anonymous user, test database, dan remote root |
| Least privilege | Buat user aplikasi dengan hak terhad: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Jika bocor, kesannya terhad |
| Bind address | Database hanya listen pada `127.0.0.1` | Database tidak boleh diakses dari luar |
| Password | Gunakan password yang kukuh; PostgreSQL menyokong SCRAM-SHA-256 | Menghalang brute force |
| Akses jauh | Matikan remote login untuk root database | Root dari luar sangat berbahaya |
| Backup | Backup berkala dan uji restore | Hardening tidak melindungi daripada human error atau kerosakan disk |

## 9. Hardening Runtime

| Runtime | Tetapan penting | Matlamat |
|---|---|---|
| PHP-FPM | Jalankan sebagai `www-data`; hadkan `pm.max_children`; nyahaktifkan fungsi berbahaya; `expose_php Off` | Mengurangkan resource abuse dan information leak |
| Node.js | Jalankan sebagai user bukan root melalui systemd; gunakan PM2 atau service manager | Pengasingan process dan auto-restart |
| Python | Gunakan virtual environment; jalankan Gunicorn/uWSGI sebagai user biasa | Pengasingan dependency dan privilege |
| Java | Tetapkan had memory JVM; jalankan sebagai user biasa | Menghalang memory exhaustion |
| .NET | Jalankan Kestrel sebagai user bukan root; gunakan reverse proxy di hadapannya | Pengasingan process dan kawalan akses |

## 10. Logging dan Monitoring

| Komponen | Fungsinya | Mengapa |
|---|---|---|
| `auditd` | Merekod perubahan fail sensitif dan akses | Mengesan aktiviti pelik |
| `journald` | Logging sistem yang berterusan | Siasatan insiden |
| `logrotate` | Putar log supaya disk tidak penuh | Mengekalkan ketersediaan |
| Fail2ban | Sekat IP selepas kegagalan log masuk berulang | Perlindungan SSH dan log masuk service |
| Baseline | Rekod keadaan normal: port, user, service, log | Tanpa baseline, sukar mengetahui mana yang pelik |

## 11. Backup dan Recovery

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Backup database | Backup berkala dan automatik | Data aplikasi ialah aset utama |
| Backup konfigurasi | Backup Nginx/Apache, systemd, firewall, dan config WAF | Mempercepat pembinaan semula server |
| Ujian restore | Uji restore secara berkala | Backup yang belum diuji belum terbukti boleh digunakan |
| Recovery runbook | Tulis langkah pemulihan | Semasa insiden, anda tidak perlu meneka dari kosong |
| Retensi | Tentukan berapa lama backup disimpan | Mengimbangi kos storage dan keperluan recovery |

> **Important:** Backup yang disimpan pada server yang sama masih berisiko. Simpan sekurang-kurangnya satu salinan di lokasi berasingan.

## 12. Incident Response

| Peringkat | Yang dilakukan |
|---|---|
| Pengesanan | Semak log SSH, web server, WAF, database, dan `auditd` |
| Containment | Sekat IP, matikan service yang dijangkiti, atau asingkan VM |
| Siasatan | Cari masa pertama, akaun yang digunakan, fail yang diubah, dan request yang mencurigakan |
| Pemulihan | Restore daripada backup bersih, tukar credential, patch celah |
| Penilaian | Rekod punca dan perbaiki hardening yang kurang |

Incident response tidak perlu kompleks untuk lab. Yang penting anda tahu: **apa yang dilihat, apa yang dilakukan, dan cara memulihkan server.**

## 13. Pengesahan Hardening

Senarai semak selepas hardening:

- [ ] Hanya port 22, 80, dan 443 terbuka
- [ ] Database hanya listen pada `127.0.0.1`
- [ ] SSH root login ditolak
- [ ] Password auth SSH ditolak
- [ ] Konfigurasi TLS disahkan dengan OpenSSL atau testssl.sh
- [ ] Security header wujud dalam response
- [ ] WAF `DetectionOnly` merekod request ujian
- [ ] Fail2ban aktif dan peraturan ban telah diuji dalam lab
- [ ] Audit log merekod perubahan fail sensitif
- [ ] Backup database berjalan
- [ ] Restore backup pernah diuji
- [ ] Tiada secret dalam repository atau fail world-readable

## 14. Kesilapan Umum

1. **Buka port database kepada awam** — sasaran paling mudah.
2. **Root login SSH aktif** — sasaran brute force.
3. **Tidak membuat kemas kini** — CVE lama yang sebenarnya sudah ada patch.
4. **WAF terus blocking tanpa tuning** — false positive menyekat pengguna sebenar.
5. **Tiada backup** — hardening tidak melindungi daripada human error.
6. **Log tidak dipantau** — serangan tidak dikesan.
7. **Secret masuk Git** — credential bocor bersama repository.
8. **Backup tidak pernah diuji** — apabila diperlukan, ternyata tidak dapat dipulihkan.

## Kesimpulan

Hardening single-tier stack ialah tentang **mengurangkan risiko secara berperingkat**. Tiada sistem yang 100% selamat, tetapi dengan CIS sebagai rujukan, firewall, SSH key, TLS moden, WAF, database least-privilege, logging, dan backup yang teruji, server jauh lebih selamat berbanding lalai.

Matlamat utamanya bukan hanya membuat aplikasi berjalan.  
Matlamat utamanya ialah memahami setiap lapisan pertahanan, cara mengesahkannya, dan cara memulihkannya apabila berlaku masalah.

> **Note:** Hardening ialah proses berterusan. Semak konfigurasi secara berkala, kemas kini patch keselamatan, dan uji semula backup serta detection.

## Rujukan

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — panduan konfigurasi selamat bagi setiap produk. [cisecurity](https://www.cisecurity.org/cis-benchmarks)
- [CIS Benchmarks Overview](https://www.cisecurity.org/cis-benchmarks-overview) — penjelasan benchmark dan pemetaannya kepada CIS Controls. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — 18 kawalan keselamatan keutamaan. [cisecurity](https://www.cisecurity.org/cis-controls-list)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) — hardening untuk host, daemon, image, dan runtime container. [docs.docker](https://docs.docker.com/dhi/explore/security-concepts/cis/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) — relevan jika stack berkembang ke container orchestration. [cisecurity](https://www.cisecurity.org/benchmark/kubernetes)