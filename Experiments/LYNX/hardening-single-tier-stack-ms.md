# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)  
[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

Artikel ini membincangkan **hardening single-tier stack**: semua layer (web server, runtime, database, cache) berjalan pada satu mesin, dan kita akan mengamankannya daripada asas—bukan pemasangan dari kosong, tetapi konfigurasi keselamatan bagi setiap layer.

Tujuannya adalah memahami:
- Urutan hardening yang munasabah
- Standard rujukan seperti CIS
- Tetapan keselamatan bagi setiap layer
- Pengesahan selepas hardening
- Kesilapan umum yang perlu dielakkan

##  Prinsip Asas Hardening

Hardening bukan satu butang. Ia ialah proses berperingkat:

1. **Minimize attack surface** — buka hanya port dan service yang diperlukan.
2. **Least privilege** — setiap service berjalan sebagai user yang tidak memerlukan root.
3. **Defense in depth** — firewall, WAF, TLS, logging, semuanya berlapis.
4. **Update dan patch** — sistem yang tidak dikemas kini ialah sasaran.
5. **Monitoring** — anda tidak dapat mengesan apa yang tidak anda lihat.
6. **Recovery** — hardening tidak menggantikan backup dan rancangan pemulihan.

> **Warning:** Jangan lakukan hardening terus dalam production. Sentiasa uji dalam lab atau VM dahulu.

##  Standard Hardening: CIS

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

> **Note:** CIS Benchmark terdiri daripada Level 1 (baseline minimum) dan Level 2 (lebih ketat). Skor pematuhan bergantung pada profil benchmark, versi, dan kawalan yang berkenaan untuk persekitaran anda. Mengaplikasikan Level 1 + Level 2 tidak bermakna "100% selamat"—pematuhan adalah panduan, bukan jaminan keselamatan mutlak. Pilih Level yang sesuai, dokumentasikan pengecualian, nilaikan setiap kawalan, uji di makmal, kemudian laksanakan secara berperingkat.

##  Sistem Operasi

| Aspek | Yang dilakukan | Mengapa penting |
|---|---|---|
| Update dan patch | Kemas kini OS dan package secara berkala | Menutup celah yang sudah diketahui |
| User dan privilege | Jangan log masuk sebagai root, buat user biasa dengan sudo | Mengurangkan kesan jika akaun bocor |
| SSH | Matikan root login dan password auth, gunakan SSH key | SSH ialah pintu masuk utama server |
| Firewall host | Default deny incoming, benarkan hanya port yang diperlukan mengikut seni bina (cth., 22, 80, 443) | Mengurangkan pendedahan port |
| Auto patch | Aktifkan unattended upgrades untuk patch keselamatan | Mengekalkan keselamatan sistem tanpa campur tangan manual |
| Service minimization | Matikan service yang tidak digunakan | Semakin sedikit service, semakin kecil attack surface |
| Parameter kernel | Terapkan sysctl hardening yang relevan | Mengurangkan risiko penyalahgunaan pada tahap rangkaian |

> **Important:** Jangan buka port pangkalan data (3306, 5432) kepada awam—akses pangkalan data hanya melalui `127.0.0.1` atau soket Unix. SSH boleh dihadkan kepada VPN/rangkaian pentadbir, dan HTTP boleh digunakan hanya untuk pengalihan ke HTTPS. Selain itu, perhatikan aspek lain yang sering diabaikan:
> - **Jejak & pemasangan:** semasa pemasangan, aktifkan penyulitan cakera (LUKS) dan partisyen berasingan untuk `/`, `/var`, `/tmp`, `/home`. Gunakan pilihan pemasangan `noexec`, `nosuid`, `nodev` hanya pada partisyen sensitif mengikut fungsinya dan sentiasa uji dalam makmal (boleh merosakkan aplikasi tertentu).
> - **Pengurusan memori & cakera:** sulitkan swap, hadkan saiz log, putar log, dan pantau penggunaan cakera bagi mengelak denial-of-service akibat cakera penuh.
> - **Pengukuhan kernel & perkhidmatan:** parameter sysctl, SELinux/AppArmor, minimumkan perkhidmatan, nyahaktifkan modul yang tidak digunakan.

##  Service, Fail, dan Secret

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Service minimum | Buang atau nyahaktifkan service yang tidak digunakan | Setiap service yang aktif adalah pintu masuk potensial, semakin sedikit service, semakin kecil attack surface |
| Kebenaran fail | Hadkan kebenaran config, log, dan fail sensitif (chmod 600/640, chown root:root) | Menghalang user non-privileged daripada membaca atau mengubah fail yang mengandungi konfigurasi atau data sensitif |
| Umask | Gunakan kebenaran lalai yang ketat (umask 027 atau 077) | Fail baharu yang dibuat tidak serta-merta world-readable, mengurangkan kebocoran data yang tidak disengajakan |
| SELinux/AppArmor | Aktifkan mengikut distro (enforcing mode) | Mengehadkan tingkah laku service jika berlaku compromise—walaupun service dibobol, kerosakan terhad kepada policy yang dibenarkan |
| Rahsia | Jangan letak kata laluan atau kunci API dalam repo atau fail yang boleh dibaca semua | Kelayakan yang bocor membolehkan akses tidak dibenarkan |
| Penyimpanan rahsia | Simpan dalam fail berpermission ketat atau pengurus rahsia (Vault, SOPS). Hadkan akses, putar, dan audit. | Mengurangkan risiko kebocoran, memudahkan putaran, dan mengekalkan jejak audit |
| `.gitignore` | Tambah `.env`, `*.key`, `*.pem`, `backup/` ke `.gitignore` dari awal | Menghalang kelayakan, kunci SSH, dan sandaran daripada masuk ke repositori secara tidak sengaja |

> **Warning:** Fail `.env`, credential database, SSH key, dan backup tidak boleh masuk ke Git. Gunakan `.gitignore` dari awal, dan jika sudah terlanjur commit, rotasi credential segera (anggap bocor).

**Jika sudah bocor ke Git, lakukan:**
1. **Hapus dari history** — gunakan `git filter-repo` atau BFG Repo-Cleaner untuk menghapus file/secret dari seluruh history, lalu force-push.
2. **Rotasi semua credential** — password, API key, SSH key, token yang bocor dianggap compromised, ganti semuanya.
3. **Revoke akses lama** — cabut key lama, tutup session aktif, blokir IP yang mencurigakan.
4. **Audit** — cek log akses untuk mengetahui apakah secret sudah disalahgunakan.
5. **Pencegahan** — tambahkan secret scanning (gitleaks, trufflehog) di CI/CD dan pre-commit hook.

##  Pengukuhan Pelayan Web & Pelanggan Web

### Pelayan Web (server-side)

| Pelayan Web | Tetapan penting | Matlamat |
|---|---|---|
| Nginx | `server_tokens off`, pengepala keselamatan di pelayan, hadkan kaedah HTTP, nyahaktifkan autoindex, TLS moden, had kadar (`limit_req`), WAF (ModSecurity) | Menyembunyi versi, mengehadkan permintaan berbahaya, melindungi daripada penyalahgunaan/DDoS |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, pengepala keselamatan di pelayan, TLS moden, WAF ModSecurity | Menyembunyi maklumat pelayan dan menolak kaedah berbahaya |
| Caddy | Pengepala keselamatan, proksi songsang dengan TLS automatik | Konfigurasi ringkas dengan lalai selamat |

**Pengepala keselamatan biasa yang ditetapkan di pelayan web:**
- `Strict-Transport-Security (HSTS)` — memaksa HTTPS (lihat bahagian TLS)
- `X-Content-Type-Options: nosniff` — menghalang MIME sniffing
- `X-Frame-Options: SAMEORIGIN` — menghalang clickjacking (boleh ditambah/diganti oleh `Content-Security-Policy: frame-ancestors`)
- `Referrer-Policy: strict-origin-when-cross-origin` — kawalan kebocoran referrer
- `Permissions-Policy` — mengehadkan akses ciri pelayar
- `Content-Security-Policy (CSP)` — mengehadkan sumber skrip/gaya/imej untuk mitigasi XSS

> **Nota:** Pengepala mengurangkan risiko tertentu, tetapi **tidak menggantikan** pengesahan input, pengekodan output, pengesahan, dan kebenaran. Tanggungjawab tersebut kekal pada aplikasi.

**Had kadar & WAF (server-side):**
- Hadkan permintaan setiap IP/pengguna di pelayan web (`limit_req`, `mod_evasive`).
- Pasang WAF (ModSecurity/OWASP CRS) untuk menapis SQLi, XSS, dan muatan berbahaya.
- Sekat IP yang kerap menyalahgunakan (fail2ban).

**Proksi songsang / pengimbang beban (jika ada):**
- Hantar `X-Forwarded-For` dengan betul; jangan percaya secara membuta tuli.
- Hadkan akses titik akhir pentadbir kepada IP tertentu.
- Aktifkan pengelogan akses dan ralat.

### Pengukuhan Pelanggan Web / Pelayar

Fokus pada kawalan yang **tidak boleh diselesaikan oleh pengepala pelayan sahaja**:
- **CSP ketat**: elakkan `unsafe-inline`/`unsafe-eval`; guna nonce/hash.
- **Subresource Integrity (SRI)**: cincang aset CDN bagi mengelak gangguan.
- **Keselamatan kuki**: `Secure`, `HttpOnly`, `SameSite=Strict/Lax`, domain/laluan betul, tamat tempoh pendek.
- **Token anti-CSRF** untuk permintaan yang mengubah keadaan.
- **Pengurusan sesi**: jana semula ID sesi selepas log masuk, tamat masa tidak aktif/mutlak, tidak sahkan semasa log keluar.
- **CORS**: hadkan asal secara ketat; jangan guna wildcard `*` untuk titik akhir sensitif.
- **Storan**: elak menyimpan token sensitif dalam `localStorage`/`sessionStorage` (risiko XSS), lebih baik guna kuki `HttpOnly`.
- **Skrip pihak ketiga**: audit/minimumkan, guna SRI, sandbox iframe.
- **Kandungan bercampur**: sekat sumber HTTP pada halaman HTTPS.

##  TLS / HTTPS

| Aspek | Cadangan | Mengapa |
|---|---|---|
| TLS minimum | TLS 1.2, lebih baik TLS 1.3 | Protocol lama mempunyai celah |
| Cipher | Hanya cipher moden (ECDHE, GCM, ChaCha20-Poly1305) | Menghalang downgrade attack |
| HSTS | Aktifkan dengan `max-age` yang panjang (`max-age=31536000; includeSubDomains; preload`) | Memaksa HTTPS dalam browser |
| Sertifikat | Let's Encrypt melalui Certbot, pembaharuan automatik | Percuma dan umum digunakan |
| Session | Hadkan session timeout, pertimbangkan menyahaktifkan session tickets | Mengurangkan risiko penggunaan semula session |
| OCSP Stapling | Aktifkan OCSP stapling | Mempercepatkan pengesahan sertifikat dan privasi |
| Redirect | Redirect HTTP → HTTPS (301) | Mencegah akses yang tidak disulitkan |
| Saiz kunci | RSA 2048+ atau ECDSA P-256/P-384 | Menghalang brute force kunci |
| Cipher order | Server-side cipher preference | Mencegah client memilih cipher lemah |

**Amalan tambahan:**
- Uji konfigurasi dengan SSL Labs (sasaran gred A).
- Nyahaktifkan TLS compression (CRIME) dan renegotiation.
- Gunakan `ssl_protocols TLSv1.2 TLSv1.3;` dalam Nginx.
- Simpan private key dengan kebenaran ketat (600) dan jangan commit ke Git.

##  WAF: Web Application Firewall

| Komponen | Fungsinya | Nota |
|---|---|---|
| ModSecurity | WAF engine untuk Apache/Nginx | Perlu tuning supaya tidak berlaku false positive |
| OWASP CRS | Rule set standard industri | Mulakan dengan mod `DetectionOnly` |
| Coraza | Alternatif WAF berasaskan Go | Ringan dan sesuai untuk setup moden |

**Cara pasang (contoh Nginx + ModSecurity):**
1. Pasang module ModSecurity dan OWASP CRS.
2. Aktifkan dalam config Nginx: `modsecurity on; modsecurity_rules_file /etc/modsecurity/crs/crs-setup.conf;`
3. Tetapkan `SecRuleEngine DetectionOnly` pada permulaan.
4. Pantau log (`/var/log/modsec_audit.log`) untuk false positive.
5. Tuning rule: exclude rule yang false positive untuk endpoint tertentu.
6. Setelah stabil, tukar ke `SecRuleEngine On` (blocking).

**Yang perlu diwaspadai:**
- False positive pada endpoint upload, API, atau form kompleks.
- Overhead prestasi, monitor latency.
- Kemas kini rule secara berkala (release CRS baharu).

> **Warning:** Jangan terus aktifkan WAF mod blocking dalam production. Rule WAF (terutamanya OWASP CRS) sering false positive pada traffic yang sah (upload form, API, query kompleks); jika blocking diaktifkan serta-merta, user yang sah boleh disekat dan service boleh down. Mulakan dengan `DetectionOnly`, analisis log untuk kenal pasti false positive, tuning rule, kemudian aktifkan blocking secara berperingkat.

##  Hardening Database

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Pemasangan selamat | Jalankan secure installation lalai database | Buang anonymous user, test database, dan remote root |
| Least privilege | Buat user aplikasi dengan hak terhad: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Jika bocor, kesannya terhad |
| Bind address | Database hanya listen pada `127.0.0.1` atau soket Unix | Database tidak boleh diakses dari luar |
| Password | Gunakan password yang kukuh, PostgreSQL menyokong SCRAM-SHA-256 | Menghalang brute force |
| Akses jauh | Matikan remote login untuk root database | Root dari luar sangat berbahaya |
| Backup | Backup berkala dan uji restore | Hardening tidak melindungi daripada human error atau kerosakan disk |
| Penyulitan semasa rehat | Aktifkan TDE *jika disokong* oleh enjin/versi/edisi pangkalan data. Jika tidak, gunakan LUKS pada volum data + sandaran disulitkan | Melindungi data jika cakera dicuri; sokongan TDE berbeza mengikut MySQL/MariaDB/PostgreSQL |
| Audit logging | Aktifkan query log untuk operasi sensitif (DDL, DML pada tabel penting) | Mengesan akses yang tidak dibenarkan dan memenuhi compliance |
| Keselamatan sambungan | Gunakan TLS untuk sambungan database (walaupun localhost dalam setup multi-tenant) | Mencegah sniffing credential/data |
| Pemantauan query | Monitor query lambat dan anomali (pg_stat_statements, slow query log) | Mengesan abuse atau injection yang lolos WAF |
| Penyulitan sandaran | Sulitkan sandaran (GPG/LUKS), simpan offsite, uji restore | Mencegah kebocoran data daripada sandaran yang dicuri |
| Pengasingan rangkaian | Jangan dedahkan port DB kepada awam, guna firewall/VPN untuk akses pentadbir | Mengurangkan permukaan serangan |

**Catatan praktis:**
- Pisahkan user DB per aplikasi, jangan gunakan root untuk app.
- Rotasi credential DB secara berkala.
- Hadkan jumlah sambungan maksimum (connection pool) untuk cegah DoS.
- Matikan ciri DB yang tidak digunakan (xp_cmdshell, LOAD DATA LOCAL, dll).

##  Hardening Runtime

| Runtime | Tetapan penting | Matlamat |
|---|---|---|
| PHP-FPM | Jalankan sebagai `www-data`; hadkan `pm.max_children`; nyahaktifkan fungsi berbahaya; `expose_php Off` | Mengurangkan resource abuse dan information leak |
| Node.js | Jalankan sebagai user bukan root melalui systemd, gunakan PM2 atau service manager | Pengasingan process dan auto-restart |
| Python | Gunakan virtual environment, jalankan Gunicorn/uWSGI sebagai user biasa | Pengasingan dependency dan privilege |
| Java | Tetapkan had memory JVM, jalankan sebagai user biasa | Menghalang memory exhaustion |
| .NET | Jalankan Kestrel sebagai user bukan root, gunakan reverse proxy di hadapannya | Pengasingan process dan kawalan akses |

##  Logging dan Monitoring

| Komponen | Fungsinya | Mengapa |
|---|---|---|
| `auditd` | Merekod perubahan fail sensitif dan akses | Mengesan aktiviti pelik |
| `journald` | Logging sistem yang berterusan | Siasatan insiden |
| `logrotate` | Putar log supaya disk tidak penuh | Mengekalkan ketersediaan |
| Fail2ban | Sekat IP selepas kegagalan log masuk berulang | Perlindungan SSH dan log masuk service |
| Baseline | Rekod keadaan normal: port, user, service, log | Tanpa baseline, sukar mengetahui mana yang pelik |

##  Backup dan Recovery

| Aspek | Yang dilakukan | Mengapa |
|---|---|---|
| Backup database | Backup berkala dan automatik | Data aplikasi ialah aset utama |
| Backup konfigurasi | Backup Nginx/Apache, systemd, firewall, dan config WAF | Mempercepat pembinaan semula server |
| Ujian restore | Uji restore secara berkala | Backup yang belum diuji belum terbukti boleh digunakan |
| Recovery runbook | Tulis langkah pemulihan | Semasa insiden, anda tidak perlu meneka dari kosong |
| Retensi | Tentukan berapa lama backup disimpan | Mengimbangi kos storage dan keperluan recovery |

> **Important:** Backup yang disimpan pada server yang sama masih berisiko. Simpan sekurang-kurangnya satu salinan di lokasi berasingan.

##  Incident Response

| Peringkat | Yang dilakukan |
|---|---|
| Pengesanan | Semak log SSH, web server, WAF, database, dan `auditd` |
| Containment | Sekat IP, matikan service yang dijangkiti, atau asingkan VM |
| Siasatan | Cari masa pertama, akaun yang digunakan, fail yang diubah, dan request yang mencurigakan |
| Pemulihan | Restore daripada backup bersih, tukar credential, patch celah |
| Penilaian | Rekod punca dan perbaiki hardening yang kurang |

Incident response tidak perlu kompleks untuk lab. Yang penting anda tahu: **apa yang dilihat, apa yang dilakukan, dan cara memulihkan server.**

##  Pengesahan Pengukuhan

Guna pendekatan `check → execute → verify`:

| Kawalan | Check | Execute | Verify |
|---|---|---|---|
| Port & firewall | Senaraikan port terbuka (`ss -tulnp`, `ufw status`) | Default deny + benarkan hanya port diperlukan | Hanya port yang diluluskan terbuka |
| Akses DB | Semak bind address | Listen di `127.0.0.1` atau soket Unix, tolak akses awam | Tiada sambungan DB dari luar hos |
| SSH | Semak config sshd | Nyahaktifkan `PermitRootLogin`, `PasswordAuthentication`, guna kunci | Log masuk root & kata laluan ditolak |
| TLS | Semak sijil & cipher | TLS 1.2/1.3, cipher moden, HSTS, HTTP→HTTPS | Uji dengan `openssl s_client` atau testssl.sh (sasaran A) |
| Pengepala keselamatan | Semak respons HTTP | Tetapkan pengepala di pelayan web | Pengepala muncul seperti dikonfigurasi |
| WAF | Semak mod WAF | Mula `DetectionOnly`, penalaan, kemudian `Blocking` berperingkat | Log permintaan ujian direkod, false positive ditangani |
| Fail2ban | Semak status jail | Aktifkan jail berkaitan | Uji di makmal (ban/unban berfungsi) |
| Audit/FIM | Semak `auditd`, AIDE/tripwire | Baseline & peraturan audit untuk fail/konfigurasi kritikal | Perubahan dijejak/di-alert |
| Egress | Semak sambungan keluar | Cerapan → allowlist/deny berperingkat mengikut keperluan | Hanya destinasi dibenarkan boleh diakses |
| Sandaran & restore | Semak jadual sandaran | Automatik, sulitkan, simpan berasingan, uji restore | Restore di persekitaran terasing berjaya & aplikasi berfungsi |
| Rahsia | Semak repo/fail | Pastikan `.env`/kunci tidak di-commit, permission ketat | Imbasan/sejarah bersih, permission betul |

##  Kesilapan Umum

1. **Membuka port pangkalan data kepada awam** — pangkalan data mesti hanya pada `127.0.0.1` atau soket Unix.
2. **Log masuk root SSH diaktifkan & pengesahan kata laluan dibenarkan** — guna kunci SSH, nyahaktifkan kedua-duanya.
3. **Tidak mengemas kini** — CVE lama boleh dieksploitasi walaupun patch wujud.
4. **WAF dalam mod blocking tanpa penalaan** — mula dari `DetectionOnly`, analisis false positive, aktifkan blocking secara berperingkat.
5. **Sandaran tidak pernah diuji** — sandaran mesti diuji restore dalam persekitaran terasing.
6. **Rahsia masuk ke Git** — guna `.gitignore`, pengurus rahsia, dan jika bocor putar kelayakan & bersihkan sejarah.
7. **Menganggap pengepala sudah mencukupi** — pengepala mengurangkan risiko, tetapi pengesahan input, pengesahan, dan kebenaran tetap wajib dalam aplikasi.

##  Pengesanan dan Pemulihan: Sempadan Pengukuhan pada Tumpukan Satu-Tingkat

### Sempadan keselamatan satu-tingkat

Satu-tingkat bermaksud beberapa komponen berkongsi satu OS. Pengasingan proses secara logik tidak sama dengan pengasingan keselamatan. Jika masa jalan dikompromi, penyerang boleh mencuri kelayakan DB, menanam kegigihan, atau mengekstrak data. Pengukuhan mesti merangkumi pencegahan, pembendungan, pengesanan, dan pemulihan.

### Network hardening

Tiga jalur: **Ingress** (sambungan luar — SSH, HTTP/HTTPS: hadkan sumber, buka hanya port yang perlu), **East-west** (komunikasi antarkomponen melalui loopback/Unix socket: hadkan akses antara proses), **Egress** (sambungan keluar — DNS, NTP, update, backup, API: default-deny + allowlist).

UFW membantu ingress tetapi tidak automatik mengehadkan egress atau mengasingkan proses. Untuk mengurangkan lateral movement: akaun service berasingan bagi setiap komponen, user DB khusus app, AppArmor/SELinux, policy jaringan container, atau VM berasingan jika impak tinggi.

### Logging dan monitoring

Logging = pencatatan kejadian. Monitoring = pemeriksaan untuk menemukan anomali. Alerting = pemberitahuan apabila tindakan diperlukan.

Peta monitoring hujung-ke-hujung: (1) titik masuk (SSH, HTTP/HTTPS, firewall, WAF, TLS, auth app), (2) pelaksanaan app (web server → runtime), (3) akses data (runtime → DB → fail/backup), (4) aktiviti OS & egress (proses, user, systemd, cron, fail sensitif, DNS, sambungan keluar), (5) korelasi & respons (kumpul log, sinkronkan masa, korelasikan event, alert, triase).

Monitoring setiap layer: firewall (sambungan, port, destinasi), akaun SSH/OS (login, user baru), web server/WAF (URL, status, rule), runtime (error, restart, proses anak), database (login, privilege, query sensitif), integriti fail (hash, kebenaran, owner), OS (sudo, audit event, cron, kernel), sumber (CPU/RAM/disk/latency), backup (status job, saiz, retensi).

### auditd

Merekod kejadian mengikut aturan audit. Objek penting: sshd_config, sudoers, passwd/group/shadow, unit systemd, cron, authorized_keys, config web server/WAF/DB, web root, config firewall, binari kritikal.

Pengguna: admin sistem (perubahan config/user), security analyst (kronologi), incident responder (persistence/escalation), auditor (jejak perubahan).

Had: aturan yang salah melepaskan aktiviti, terlalu banyak aturan membebani disk/noise, perubahan sah (deployment) juga direkod, penyerang root boleh padam log lokal, audit tidak automatik menjelaskan request HTTP yang mencetuskan.

Bezakan: auditd (aktiviti mengikut aturan), journald (mesej OS/app), FIM (perubahan vs baseline), network monitoring (sambungan), SIEM (korelasi & alert).

### journald, logrotate, Fail2ban, baseline

- **journald**: kumpul mesej OS/app, persistensi bergantung config & retensi. Pantau SSH, service gagal, kernel, kegagalan sumber. Hantar log penting ke sistem berasingan.
- **logrotate**: urus kitar hidup log (rotasi, mampatan, retensi). Pastikan rotasi tidak menghentikan penulisan log, retensi cukup untuk siasatan.
- **Fail2ban**: baca log, sekat sumber selepas pola (login gagal berulang). Membantu brute force ringkas, tidak mencegah eksploitasi web, kecurian credential, eksfiltrasi. Boleh false positive.
- **Baseline**: rekod keadaan normal (port, user, service, proses, hash fail, aturan firewall, corak login/request/egress, versi). Kemas kini melalui perubahan sah (deployment/patch).

### Monitoring yang berkesan

Tetapkan keadaan normal kemudian alert. Contoh isyarat: login admin SSH dari sumber tidak dikenali (tinggi), user baru/grup admin di luar tetingkap perubahan (tinggi), fail config berubah tanpa deployment (tinggi), proses baru tidak sepadan dengan perilaku app (tinggi), runtime membuka sambungan ke destinasi baru (tinggi jika disahkan), perubahan privilege DB atau eksport data besar (tinggi), perubahan aturan firewall tanpa kelulusan (tinggi), lonjakan request WAF menyerupai eksploitasi (perlu korelasi), lonjakan CPU/RAM/disk/latency (perlu triase), job backup gagal/salinan tidak tersedia (tinggi).

WAF hanya melihat trafik yang melalui titik inspeksinya, tidak melihat proses lokal, perubahan user/sudo, fail yang diubah melalui SSH, akses DB melalui loopback, egress non-WAF, perubahan firewall, pemadaman log, perubahan backup. Audit OS juga tidak menggantikan log aplikasi (request sah secara sintaks tetapi menyalahgunakan autorisasi).

Log lokal sahaja tidak cukup: penyerang root boleh memadam log lokal. Hantar log penting ke sistem berasingan (VM dengan hak akses berasingan). CISA mengesyorkan pengumpulan log terpusat, alert kejadian berisiko tinggi, perlindungan log daripada perubahan tidak dibenarkan, retensi jelas.

Tentukan pemilik alert: admin (kesihatan service/config), developer (deployment/error), security analyst (korelasi/containment), pemilik backup (ketersediaan/restore), pemilik perkhidmatan (impak perniagaan).

### Backup dan pemulihan

Objek yang perlu dipertimbangkan: database (data+skema+role+metadata), fail app (versi rilis yang diketahui bersih), upload pengguna, config OS/service, secret/sijil (dengan akses/enkripsi sesuai), kunci enkripsi (berasingan dari backup), log/bukti, dokumentasi pemulihan (versi, dependensi, urutan pemulihan).

Aliran: sumber produksi → backup konsisten (kaedah sesuai engine DB, rekod masa/versi/status) → enkripsi & pemindahan (saluran terlindung, identiti backup khusus) → penyimpanan berasingan (lokasi berbeza, kredensial berasingan, retensi, perlindungan pemadaman) → pengesahan & ujian restore (integriti, restore ke persekitaran terasing, uji app+data).

Backup mesti berasingan: penyerang dengan hak tinggi boleh memadam data produksi DAN backup lokal. Gunakan akaun backup khusus, elakkan memberikan server produksi hak untuk memadam semua salinan historis, immutable storage, enkripsi + pengurusan kunci berasingan, pantau kegagalan & perubahan retensi, uji restore. Pendekatan 3-2-1: 3 salinan, 2 jenis media, 1 offsite. Untuk ransomware, tambah salinan offline/immutable.

RPO (recovery point objective) = kehilangan data yang boleh diterima (rentang masa). RTO (recovery time objective) = masa maksimum perkhidmatan boleh down. Frekuensi backup tidak automatik menjamin RPO, backup tidak automatik menjamin RTO jika restore lambat.

Kesukaran pemulihan: DB dan upload dari masa berbeza, backup terbaru mungkin sudah mengandungi data rosak/fail berbahaya, secret yang bocor perlu rotasi bukan sekadar restore, config lama mungkin mengembalikan kelemahan, backup terenkripsi tidak berguna jika kunci hilang, app mungkin gagal semasa restore, persistence mungkin ikut kembali. Oleh itu ujian restore di persekitaran terasing: sahkan DB, login app, fungsi perniagaan, kebenaran, service, TLS, firewall, monitoring sebelum perkhidmatan kembali.

### Incident response

Respons pantas (minit pertama): sahkan alert (sistem, masa, akaun, proses, penunjuk), nilai impak (perkhidmatan, data sensitif, akaun admin, egress), containment (hadkan jalur serangan melalui kawalan jaringan/pengasingan), lindungi bukti (simpan log, timestamp, alert, metadata, catat setiap tindakan), lindungi akses (rancang pencabutan sesi, rotasi secret, penggantian key melalui sistem dipercayai), tentukan eskalasi (root compromise, kecurian data, ransomware → insiden serius).

Siasatan mendalam — soalan wajib: bila aktiviti pertama berlaku? (log terpusat, auth, web, WAF, audit, DB) Apakah titik masuk? (request web, SSH, perubahan app, config lemah) Akaun apa digunakan? (login, user ID, privilege, session, key, sudo) Proses apa berjalan? (process tree, parent, executable, service, scheduler) Fail apa berubah? (audit event, FIM, hash, metadata, sejarah deployment) Data apa diakses? (audit DB, app, akses fail, volum trafik) Adakah data keluar? (flow log, DNS, log proxy/firewall, proses pemilik sambungan) Adakah akses masih bertahan? (akaun, key, service, cron, config, persistence lain) Apa yang masih boleh dipercayai? (integriti sistem, provenance backup, config, bukti luaran).

Jika OS dikuasai root: jangan percaya output dari OS yang disyaki, asingkan melalui kawalan jaringan luar host, pertahankan log yang dihantar terpusat, kumpul bukti volatil jika ada prosedur, elakkan menjalankan alat yang menimpa bukti, pertimbangkan snapshot/image forensik mengikut prosedur platform, prioritaskan rebuild dari media/image bersih, rotasi credential/token/key/secret, periksa akses ke backup & sistem lain menggunakan identiti server yang terkompromi.

Containment bukan sekadar blokir IP: jika penyerang menggunakan akaun/sesi yang sah, akses melalui VPN/proxy, eksploitasi lokal, credential DB dicuri, persistence ditanam, atau root diperoleh — blokir IP tidak cukup. Containment boleh bermaksud: nyahaktifkan akaun, cabut sesi/key, asingkan VM, hadkan egress, hentikan service tertentu, tutup endpoint yang terjejas.

Pemulihan & pengesahan sebelum diisytiharkan selesai: jalur masuk ditutup/dimitigasi, image/paket/fail app dari sumber tepercaya, data dipulihkan dari backup yang disahkan, credential/sesi yang bocor ditangani, user/key/service/scheduler/firewall sepadan dengan baseline yang diluluskan, logging/audit/FIM/monitoring aktif, egress & akses DB mengikut polisi, app lulus ujian fungsi & keselamatan, dokumentasi kronologi/impak/tindakan/pekerjaan lanjutan.

### Matriks korelasi (contoh insiden)

Runtime disyaki menjalankan proses yang tidak semestinya selepas request web:
1. Indikasi awal: WAF & access log → request tidak normal, endpoint, masa, status.
2. Pengesahan proses: log runtime & info proses → proses anak, parent, owner, masa mula.
3. Perubahan sistem: auditd & FIM → fail baru, perubahan kebenaran, unit service/cron.
4. Perluasan akses: log auth, sudo, DB → akaun baru, perubahan privilege, akses data sensitif.
5. Komunikasi keluar: firewall, DNS, flow log → destinasi baru, timing, volum.
6. Containment: firewall luaran/pengasingan host → adakah aktiviti masih berlangsung?
7. Pemulihan: backup, baseline, image tepercaya → bolehkah sistem & data dipulihkan dengan selamat?
8. Penilaian: semua bukti → jalur masuk, skop impak, kawalan yang gagal.

### Kesukaran dan batasan

| Kawalan | Kesukaran utama | Risiko jika tanpa penilaian |
|---|---|---|
| Egress default-deny | Menyusun allowlist destinasi lengkap & terpelihara | Update/DNS/API/backup gagal |
| auditd | Memilih aturan, mengendalikan volum event | Disk penuh, noise, event penting terlepas |
| FIM | Mengemas kini baseline selepas perubahan sah | Alert berlebihan atau perubahan berbahaya dianggap normal |
| SIEM/log terpusat | Kos storage, parsing, korelasi, pengurusan alert | Banyak alert tanpa tindakan lanjut |
| Fail2ban | Menentukan filter & ambang | False positive, sekat pengguna sah |
| Database auditing | Menentukan operasi yang dicatat tanpa beban/kebocoran data | Beban tinggi atau log mengandungi data sensitif |
| Backup offsite | Mengurus identiti, enkripsi, retensi, ujian restore | Backup tidak dapat diakses/didekripsi/dipulihkan |
| Incident response | Mengimbangi containment, pemeliharaan bukti, kesinambungan perkhidmatan | Bukti hilang atau kompromi berterusan |
| Rebuild server | Memastikan image bersih, dependensi tersedia, data konsisten | Penyerang/config rentan masuk semula |

### Urutan implementasi yang masuk akal

1. Tetapkan baseline & inventori (port, service, user, config, dependensi, jalur data, perkhidmatan luaran).
2. Amankan ingress & akses tempatan (hadkan SSH, tutup port tidak perlu, hadkan privilege runtime, lindungi akses DB).
3. Terapkan polisi egress (cerap sambungan normal → pembatasan berperingkat → uji alur app).
4. Aktifkan logging yang relevan (auth, web, runtime, DB, OS, firewall, backup).
5. Tambah audit & integriti fail (objek kritikal, aturan audit, baseline, perubahan yang wajib disiasat).
6. Bina monitoring & alert (aturan berdasarkan senario risiko, pemilik alert, uji ketersediaan bukti).
7. Asingkan backup & log penting (lindungi daripada pemadaman oleh akaun server produksi).
8. Latih incident response (simulasi login mencurigakan, perubahan fail, egress tidak diharapkan, restore backup di lab).
9. Sahkan & semak semula (uji kawalan selepas perubahan, catat pengecualian, nilai semula baseline).

### Referensi

- [Ubuntu Server — Firewall](https://ubuntu.com/server/docs/firewalls/) — perilaku dan pengurusan firewall host menggunakan UFW.
- [Linux Audit System — auditd](https://www.linux.org/docs/man5/auditd.html) — peranan daemon audit dan pemrosesan rekod audit.
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/use-logging-on-business-systems) — sumber log, alert, pengumpulan terpusat, perlindungan log.
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — logging, backup, perlindungan salinan, pemulihan.
- [FBI — Ten Actions to Improve Cyber Resiliency](https://www.fbi.gov/investigate/cyber/ten-actions-to-improve-cyber-resiliency) — perlindungan log dan backup offline/immutable.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — panduan incident response (April 2025).

Pengajaran utama: pada single-tier, sasarannya bukan hanya mencegah akses dari internet. Anda juga perlu mengehadkan apa yang boleh dilakukan oleh proses yang sudah dibobol, mengurangkan peluang perpindahan akses dan eksfiltrasi, mempertahankan bukti yang boleh dipercayai, serta memastikan sistem boleh dipulihkan tanpa membawa kompromi kembali.

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