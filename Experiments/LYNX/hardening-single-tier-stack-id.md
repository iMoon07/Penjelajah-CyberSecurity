# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

Ini membahas **hardening single-tier stack**: semua layer (web server, runtime, database, cache) berjalan di satu mesin yang sama, dan kita akan mengamankannya dari dasar—bukan instalasi dari nol, melainkan konfigurasi keamanan tiap layer.

![Hardening single tier stack](hardening-single-tier-stack.png)

Tujuannya adalah memahami:
- Urutan hardening yang masuk akal
- Standar acuan seperti CIS
- Pengaturan keamanan per layer
- Verifikasi setelah hardening
- Kesalahan umum yang harus dihindari

## 1. Prinsip Dasar Hardening

Hardening bukan satu tombol. Ia adalah proses bertahap:

1. **Minimize attack surface** — buka hanya port dan service yang dibutuhkan.
2. **Least privilege** — setiap service berjalan sebagai user yang tidak butuh root.
3. **Defense in depth** — firewall, WAF, TLS, logging, semuanya berlapis.
4. **Update dan patch** — sistem yang tidak diperbarui adalah target.
5. **Monitoring** — kamu tidak bisa mendeteksi apa yang tidak kamu lihat.
6. **Recovery** — hardening tidak menggantikan backup dan rencana pemulihan.

> **Warning:** Uji hardening di lab atau VM dulu bila memungkinkan. Jika terpaksa di production (misalnya insiden aktif), lakukan perubahan bertahap, backup config dulu, dan siapkan rollback plan.

## 2. Standar Hardening: CIS

Hardening tidak harus ditebak. Ada standar yang bisa dipakai sebagai acuan:

| Standar | Fungsinya | Relevansi untuk single-tier |
|---|---|---|
| **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** | Panduan konfigurasi aman untuk OS, web server, database, Docker, dan produk lain | Acuan konkret untuk mengamankan tiap layer |
| **[CIS Controls](https://www.cisecurity.org/controls/cis-controls-list)** | 18 kontrol keamanan yang diprioritaskan | Kerangka besar: inventory, patch, access control, logging, recovery, incident response |
| **Vendor hardening guide** | Panduan resmi dari Debian, Ubuntu, Red Hat, Nginx, MariaDB, PostgreSQL, dll | Detail konfigurasi sesuai distro dan software yang dipakai |

Untuk single-tier, benchmark yang paling relevan:

| Layer | CIS Benchmark yang relevan |
|---|---|
| OS | CIS Ubuntu Linux Benchmark, CIS Debian Linux Benchmark, CIS Red Hat Enterprise Linux Benchmark |
| Web server | CIS Nginx Benchmark, CIS Apache HTTP Server Benchmark |
| Database | CIS MariaDB Benchmark, CIS MySQL Benchmark, CIS PostgreSQL Benchmark |
| Container | CIS Docker Benchmark |
| Orchestration | CIS Kubernetes Benchmark, hanya jika stack berkembang ke Kubernetes |

CIS Benchmarks adalah rekomendasi konfigurasi aman yang dikembangkan melalui konsensus praktisi keamanan dan tersedia gratis dalam format PDF untuk penggunaan non-komersial. CIS Controls memetakan praktik tersebut ke dalam 18 kontrol prioritas, dari inventory asset sampai penetration testing. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)

> **Note:** CIS Benchmark terdiri dari Level 1 (baseline minimum) dan Level 2 (lebih ketat). "100%" berarti menerapkan seluruh kontrol Level 1 + Level 2 + semua sub-control. Dalam praktik, pilih Level sesuai kebutuhan—Level 1 untuk baseline, Level 2 untuk high-security—lalu dokumentasikan apa yang diterapkan dan apa yang sengaja dilewati. Jangan terapkan semua sekaligus tanpa prioritas, evaluasi per kontrol, uji di lab, baru terapkan bertahap.

## 3. Sistem Operasi

| Aspek | Yang dilakukan | Kenapa penting |
|---|---|---|
| Update dan patch | Rutin perbarui OS dan paket | Menutup celah yang sudah diketahui |
| User dan privilege | Jangan login root, buat user biasa dengan sudo | Mengurangi dampak jika akun bocor |
| SSH | Nonaktifkan root login dan password auth, pakai SSH key | SSH adalah pintu masuk utama server |
| Firewall host | Default deny incoming, buka hanya 22, 80, 443 | Mengurangi exposure port |
| Auto patch | Aktifkan unattended upgrades untuk patch keamanan | Menjaga sistem tetap aman tanpa intervensi manual |
| Service minimization | Matikan service yang tidak dipakai | Semakin sedikit service, semakin kecil attack surface |
| Kernel parameter | Terapkan sysctl hardening yang relevan | Mengurangi risiko network-level abuse |

> **Important:** Jangan buka port database (3306, 5432) ke publik—database hanya localhost atau jaringan internal. Selain itu, perhatikan aspek lain yang sering terlupakan:
- **Footprint & instalasi:** saat instalasi, pilih enkripsi disk (LUKS) dan partisi terpisah untuk `/`, `/var`, `/tmp`, `/home`; gunakan mount options `noexec`, `nosuid`, `nodev` pada partisi sensitif.
- **Manajemen memori & disk:** atur swap dengan enkripsi, batasi ukuran log, rotasi log, dan monitor penggunaan disk agar tidak denial-of-service akibat penuh.
- **Hardening kernel & service:** kernel parameter (sysctl), SELinux/AppArmor, minimasi service, dan disable module yang tidak dipakai.
Kenapa penting: setiap aspek ini mengurangi attack surface dan mencegah kebocoran data atau DoS.

## 4. Service, File, dan Secret

| Aspek | Yang dilakukan | Kenapa |
|---|---|---|
| Service minim | Hapus atau disable service yang tidak dipakai | Setiap service aktif adalah pintu masuk potensial, semakin sedikit service, semakin kecil attack surface |
| File permission | Batasi permission config, log, dan file sensitif (chmod 600/640, chown root:root) | Mencegah user non-privileged membaca atau mengubah file yang berisi konfigurasi atau data sensitif |
| Umask | Gunakan default permission ketat (umask 027 atau 077) | File baru yang dibuat tidak langsung world-readable, mengurangi kebocoran data tak sengaja |
| SELinux/AppArmor | Aktifkan sesuai distro (enforcing mode) | Membatasi perilaku service jika terkena compromise—meskipun service dibobol, kerusakan terbatas pada policy yang diizinkan |
| Secret | Jangan taruh password atau API key di repo atau file world-readable | Credential yang bocor ke Git atau file yang bisa dibaca semua user memungkinkan akses tidak sah |
| Environment variable | Simpan secret di file dengan permission ketat atau secret manager (Vault, SOPS) | Mengurangi risiko kebocoran konfigurasi dan memudahkan audit serta rotasi credential |
| `.gitignore` | Tambahkan `.env`, `*.key`, `*.pem`, `backup/` ke `.gitignore` sejak awal | Mencegah credential, SSH key, dan backup tidak sengaja masuk ke Git repository |

> **Warning:** File `.env`, database credential, SSH key, dan backup tidak boleh masuk ke Git. Gunakan `.gitignore` sejak awal, dan jika sudah terlanjur commit, rotasi credential segera (anggap bocor).

**Jika sudah bocor ke Git, lakukan:**
1. **Hapus dari history** — gunakan `git filter-repo` atau BFG Repo-Cleaner untuk menghapus file/secret dari seluruh history, lalu force-push.
2. **Rotasi semua credential** — password, API key, SSH key, token yang bocor dianggap compromised, ganti semuanya.
3. **Revoke akses lama** — cabut key lama, tutup session aktif, blokir IP yang mencurigakan.
4. **Audit** — cek log akses untuk mengetahui apakah secret sudah disalahgunakan.
5. **Pencegahan** — tambahkan secret scanning (gitleaks, trufflehog) di CI/CD dan pre-commit hook.

## 5. Web Server & Web Client Hardening

### 5.1 Web Server (server-side)

| Web server | Pengaturan penting | Tujuan |
|---|---|---|
| Nginx | `server_tokens off`, security headers, batasi method HTTP, nonaktifkan autoindex, TLS modern, rate limiting (`limit_req`), WAF (ModSecurity) | Menyembunyikan versi, membatasi request berbahaya, melindungi dari DDoS/abuse |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers, TLS modern, ModSecurity WAF | Menyembunyikan informasi server dan menolak method berbahaya |
| Caddy | Header security, reverse proxy dengan TLS otomatis, security headers | Konfigurasi sederhana dengan default yang aman |

**Security headers (web server + aplikasi):**
- `X-Frame-Options: SAMEORIGIN` — mencegah clickjacking
- `X-Content-Type-Options: nosniff` — mencegah MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin` — kontrol referrer
- `Permissions-Policy` — batasi akses fitur browser (camera, mic, geolocation)
- `Content-Security-Policy (CSP)` — batasi sumber script/style/image, mitigasi XSS
- `Strict-Transport-Security (HSTS)` — paksa HTTPS (detail di bagian 6)

**Rate limiting & WAF (server-side):**
- Batasi request per IP/user di web server (`limit_req`, `mod_evasive`).
- Pasang WAF (ModSecurity/OWASP CRS) untuk filter SQLi, XSS, dan payload berbahaya.
- Blokir IP berulang yang abusive (fail2ban).

**Reverse proxy / load balancer (jika ada):**
- Teruskan header `X-Forwarded-For` dengan benar; jangan percaya blindly.
- Batasi akses admin endpoint ke IP tertentu.
- Aktifkan logging akses dan error.

### 5.2 Web Client / Browser-side Hardening

- **CSP ketat**: hindari `unsafe-inline`/`unsafe-eval`; gunakan nonce/hash.
- **Subresource Integrity (SRI)**: hash untuk CDN assets agar tidak dimanipulasi.
- **Cookie security**: `Secure`, `HttpOnly`, `SameSite=Strict/Lax`, domain/path tepat, expiry pendek.
- **Clickjacking**: `X-Frame-Options` + CSP `frame-ancestors`.
- **MIME sniffing**: `X-Content-Type-Options: nosniff`.
- **Referrer control**: `Referrer-Policy` atau `no-referrer`.
- **Permissions-Policy**: batasi camera, mic, geolocation, payment, USB.
- **CORS**: batasi origin; jangan wildcard `*` untuk endpoint sensitif.
- **Input validation**: sanitasi/escape output (UX, bukan keamanan utama — server tetap wajib validasi).
- **Anti-CSRF token** untuk request yang mengubah state.
- **Session management**: regenerasi session ID setelah login, timeout idle/absolute, invalidasi saat logout.
- **Storage**: hindari simpan token sensitif di localStorage/sessionStorage (risk XSS), prefer httpOnly cookie.
- **Third-party scripts**: audit & minimalkan, gunakan SRI, sandbox iframe.
- **Mixed content**: blokir HTTP resources di halaman HTTPS.

## 6. TLS / HTTPS

| Aspek | Rekomendasi | Kenapa |
|---|---|---|
| Minimum TLS | TLS 1.2, lebih baik TLS 1.3 | Protocol lama punya celah |
| Cipher | Hanya cipher modern (ECDHE, GCM, ChaCha20-Poly1305) | Mencegah downgrade attack |
| HSTS | Aktifkan dengan max-age panjang (`max-age=31536000; includeSubDomains; preload`) | Memaksa HTTPS di browser |
| Sertifikat | Let's Encrypt via Certbot, renewal otomatis | Gratis dan umum dipakai |
| Session | Batasi session timeout, pertimbangkan nonaktifkan session tickets | Mengurangi risiko session reuse |
| OCSP Stapling | Aktifkan OCSP stapling | Mempercepat validasi sertifikat dan privasi |
| Redirect | Redirect HTTP → HTTPS (301) | Mencegah akses tidak terenkripsi |
| Key size | RSA 2048+ atau ECDSA P-256/P-384 | Mencegah brute force kunci |
| Cipher order | Server-side cipher preference | Mencegah client memilih cipher lemah |

**Praktik tambahan:**
- Test konfigurasi dengan SSL Labs (grade A target).
- Nonaktifkan TLS compression (CRIME) dan renegotiation.
- Gunakan `ssl_protocols TLSv1.2 TLSv1.3;` di Nginx.
- Simpan private key dengan permission ketat (600) dan jangan commit ke Git.

## 7. WAF: Web Application Firewall

| Komponen | Fungsinya | Catatan |
|---|---|---|
| ModSecurity | WAF engine untuk Apache/Nginx | Perlu tuning agar tidak false positive |
| OWASP CRS | Rule set standar industri | Mulai dari mode `DetectionOnly` |
| Coraza | Alternatif WAF berbasis Go | Ringan dan cocok untuk setup modern |

**Cara pasang (contoh Nginx + ModSecurity):**
1. Install ModSecurity module dan OWASP CRS.
2. Aktifkan di config Nginx: `modsecurity on; modsecurity_rules_file /etc/modsecurity/crs/crs-setup.conf;`
3. Set `SecRuleEngine DetectionOnly` awalnya.
4. Pantau log (`/var/log/modsec_audit.log`) untuk false positive.
5. Tuning rule: exclude rule yang false positive untuk endpoint tertentu.
6. Setelah stabil, ubah ke `SecRuleEngine On` (blocking).

**Yang harus diwaspadai:**
- False positive pada endpoint upload, API, atau form kompleks.
- Performance overhead, monitor latency.
- Update rule secara berkala (CRS release baru).

> **Warning:** Jangan langsung aktifkan WAF mode blocking di production. Rule WAF (terutama OWASP CRS) sering false positive pada traffic legit (form upload, API, query kompleks); jika langsung blocking, user sah bisa terblokir dan service down. Mulai dari `DetectionOnly`, analisis log untuk identifikasi false positive, tuning rule, lalu aktifkan blocking secara bertahap.

## 8. Database Hardening

| Aspek | Yang dilakukan | Kenapa |
|---|---|---|
| Secure installation | Jalankan secure installation bawaan database | Hapus anonymous user, test database, dan remote root |
| Least privilege | Buat user aplikasi dengan hak terbatas: SELECT, INSERT, UPDATE, DELETE | Jika bocor, dampaknya terbatas |
| Bind address | Database hanya listen di `127.0.0.1` | Database tidak bisa diakses dari luar |
| Password | Gunakan password kuat, PostgreSQL mendukung SCRAM-SHA-256 | Mencegah brute force |
| Remote access | Nonaktifkan remote login untuk root database | Root dari luar sangat berbahaya |
| Backup | Backup rutin dan tes restore | Hardening tidak melindungi dari human error atau kerusakan disk |
| Encryption at rest | Aktifkan TDE (jika didukung) atau LUKS pada volume data | Melindungi data jika disk dicuri |
| Audit logging | Aktifkan query log untuk operasi sensitif (DDL, DML pada tabel penting) | Deteksi akses tidak sah dan memenuhi compliance |
| Connection security | Gunakan TLS untuk koneksi database (bahkan localhost jika multi-tenant) | Mencegah sniffing credential/data |
| Query monitoring | Monitor query lambat dan anomali (pg_stat_statements, slow query log) | Deteksi abuse atau injeksi yang lolos WAF |
| Backup encryption | Enkripsi backup (GPG/LUKS), simpan offsite, uji restore | Mencegah kebocoran data dari backup yang dicuri |
| Network isolation | Jangan expose port DB ke publik, gunakan firewall/VPN untuk akses admin | Mengurangi attack surface |

**Catatan praktis:**
- Pisahkan user DB per aplikasi, jangan gunakan root untuk app.
- Rotasi credential DB secara berkala.
- Batasi jumlah koneksi maksimum (connection pool) untuk cegah DoS.
- Nonaktifkan fitur DB yang tidak dipakai (xp_cmdshell, LOAD DATA LOCAL, dll).

## 9. Runtime Hardening

| Runtime | Pengaturan penting | Tujuan |
|---|---|---|
| PHP-FPM | Jalankan sebagai `www-data`; batasi `pm.max_children`; matikan fungsi berbahaya; `expose_php Off` | Mengurangi resource abuse dan information leak |
| Node.js | Jalankan sebagai user non-root via systemd, gunakan PM2 atau service manager | Isolasi process dan auto-restart |
| Python | Gunakan virtual environment, jalankan Gunicorn/uWSGI sebagai user biasa | Isolasi dependency dan privilege |
| Java | Setel JVM memory limit, jalankan sebagai user biasa | Mencegah memory exhaustion |
| .NET | Jalankan Kestrel sebagai user non-root, gunakan reverse proxy di depannya | Isolasi process dan kontrol akses |

## 10. Logging dan Monitoring

| Komponen | Fungsinya | Kenapa |
|---|---|---|
| `auditd` | Mencatat perubahan file sensitif dan akses | Deteksi aktivitas aneh |
| `journald` | Logging sistem yang persisten | Investigasi insiden |
| `logrotate` | Rotasi log agar disk tidak penuh | Menjaga ketersediaan |
| Fail2ban | Blokir IP setelah gagal login berulang | Proteksi SSH dan login service |
| Baseline | Catat kondisi normal: port, user, service, log | Tanpa baseline, sulit tahu mana yang aneh |

## 11. Backup dan Recovery

| Aspek | Yang dilakukan | Kenapa |
|---|---|---|
| Database backup | Backup rutin dan otomatis | Data aplikasi adalah aset utama |
| Configuration backup | Backup Nginx/Apache, systemd, firewall, dan WAF config | Mempercepat rebuild server |
| Restore test | Uji restore secara berkala | Backup yang belum dites belum terbukti bisa dipakai |
| Recovery runbook | Tulis langkah pemulihan | Saat insiden, kamu tidak harus menebak dari nol |
| Retensi | Tentukan berapa lama backup disimpan | Menyeimbangkan biaya storage dan kebutuhan recovery |

> **Important:** Backup yang tersimpan di server yang sama tetap berisiko. Simpan minimal satu salinan di tempat terpisah.

## 12. Incident Response

| Tahap | Yang dilakukan |
|---|---|
| Deteksi | Cek log SSH, web server, WAF, database, dan `auditd` |
| Containment | Blokir IP, matikan service terinfeksi, atau isolasi VM |
| Investigasi | Cari waktu pertama, akun yang dipakai, file yang berubah, dan request mencurigakan |
| Pemulihan | Restore dari backup bersih, rotasi credential, patch celah |
| Evaluasi | Catat penyebab dan perbaiki hardening yang kurang |

Incident response tidak harus kompleks untuk lab. Yang penting kamu tahu: **apa yang dilihat, apa yang dilakukan, dan bagaimana memulihkan server.**

## 13. Verifikasi Hardening

Checklist setelah hardening:

- [ ] Hanya port 22, 80, 443 yang terbuka
- [ ] Database hanya listen di `127.0.0.1`
- [ ] SSH root login ditolak
- [ ] Password auth SSH ditolak
- [ ] TLS configuration diverifikasi dengan OpenSSL atau testssl.sh
- [ ] Security headers ada di response
- [ ] WAF `DetectionOnly` mencatat request uji
- [ ] Fail2ban aktif dan aturan ban sudah diuji di lab
- [ ] Audit log mencatat perubahan file sensitif
- [ ] Backup database berjalan
- [ ] Restore backup sudah pernah diuji
- [ ] Tidak ada secret di repository atau file world-readable

## 14. Kesalahan Umum

1. **Buka port database ke publik** — target paling mudah.
2. **Root login SSH aktif** — target brute force.
3. **Tidak update** — CVE lama yang sebenarnya sudah ada patch.
4. **WAF langsung blocking tanpa tuning** — false positive memblokir user asli.
5. **Tidak ada backup** — hardening tidak melindungi dari human error.
6. **Log tidak dimonitor** — serangan tidak terdeteksi.
7. **Secret masuk Git** — credential bocor bersama repository.
8. **Backup tidak pernah dites** — saat dibutuhkan, ternyata tidak bisa dipulihkan.

## 15. End-to-End: Dari OS Sampai Database dan Runtime

Bagian ini melengkapi hardening agar tidak hanya berhenti di web server, tetapi mencakup seluruh stack.

### IDS/IPS

| Komponen | Fungsi | Contoh |
|---|---|---|
| IDS | Deteksi intrusi jaringan | Suricata, Snort |
| IPS | Blokir intrusi secara aktif | Suricata inline mode |

Pasang Suricata di host atau di depan server. Gunakan ruleset Emerging Threats. Monitor alert secara rutin.

### File Integrity Monitoring (FIM)

| Komponen | Fungsi | Contoh |
|---|---|---|
| FIM | Deteksi perubahan file sistem | AIDE, Tripwire |

Buat baseline hash file penting (`/etc`, `/usr/bin`, web root). Jalankan cek berkala via cron. Alert jika ada perubahan tak terduga.

### Rate Limiting

| Layer | Cara | Tujuan |
|---|---|---|
| Web server | Nginx `limit_req`, Apache mod_evasive | Batasi request per IP |
| App | Throttle per user/IP di kode | Mencegah brute force dan abuse |

### Secrets Management

| Aspek | Rekomendasi | Kenapa |
|---|---|---|
| Penyimpanan | Vault, SOPS, atau secret manager | Bukan .env plain text |
| Akses | Least privilege, audit log | Mencegah leak |
| Rotasi | Rutin rotasi credential | Mengurangi window of exposure |

### Database Encryption at Rest

| Metode | Deskripsi |
|---|---|
| TDE | Transparent Data Encryption (MySQL/PostgreSQL) |
| LUKS | Enkripsi volume di level OS |

Gunakan LUKS untuk volume data, atau TDE jika database mendukungnya. Enkripsi backup juga wajib.

### Container Hardening (jika pakai Docker/Podman)

| Praktik | Tujuan |
|---|---|
| Drop capabilities | Kurangi privilege container |
| Read-only filesystem | Mencegah modifikasi tak terduga |
| Non-root user | Isolasi privilege |
| Seccomp profile | Batasi syscall |
| Image scanning | Deteksi CVE di image (Trivy) |

### NTP / chrony

Sinkronkan waktu server dengan NTP. Log dan audit bergantung pada timestamp yang akurat. Gunakan `chrony` atau `systemd-timesyncd`.

### Kernel Hardening (sysctl)

| Parameter | Nilai | Tujuan |
|---|---|---|
| `net.ipv4.conf.all.rp_filter` | 1 | Anti-spoofing |
| `net.ipv4.tcp_syncookies` | 1 | Anti-SYN flood |
| `net.ipv4.conf.all.accept_redirects` | 0 | Anti-redirect attack |
| `kernel.randomize_va_space` | 2 | ASLR |

Disable module kernel yang tidak dipakai. Set mount options `noexec`, `nosuid`, `nodev` pada partisi sensitif.

### Dependency Scanning

| Tool | Target | Kapan |
|---|---|---|
| npm audit | Node.js | Saat build/CI |
| pip-audit | Python | Saat build/CI |
| Trivy | Container image | Saat build/CI |

Integrasikan di pipeline. Block deploy jika ada critical finding.

### Centralized Logging / SIEM

Forward log ke Loki, ELK, atau Splunk. Buat alert untuk pola aneh. Retensi minimal 90 hari untuk audit.

### SSH Key Rotation & MFA

Rotasi SSH key secara berkala. Aktifkan MFA (TOTP/PAM) untuk akses admin. Batasi akses SSH ke IP tertentu (AllowUsers + firewall).

### Password Policy & Account Lockout

Gunakan `pam_pwquality` untuk kebijakan password. Aktifkan `faillock` untuk lockout setelah gagal login berulang. Audit akun secara berkala.

### Backup Encryption & Offsite Verification

Enkripsi backup (GPG atau LUKS). Simpan minimal satu salinan offsite. Uji restore secara berkala. Dokumentasikan RTO dan RPO.

## 16. Network, Logging, Monitoring, Backup, dan Incident Response (Mendalam)

### 16.1 Batas keamanan single-tier

Single-tier berarti beberapa komponen berbagi satu OS. Memisahkan proses secara logis tidak sama dengan memisahkan mesin secara keamanan. Jika runtime dibobol, penyerang bisa mencoba mencuri credential DB, menanam file persistence, atau mengirim data keluar. Hardening harus mencakup pencegahan, containment, deteksi, dan recovery.

### 16.2 Network hardening

Bedakan tiga jalur:
- **Ingress** — koneksi dari luar (SSH, HTTP/HTTPS). Batasi sumber, buka hanya port yang perlu.
- **East-west** — komunikasi antarkomponen (runtime ↔ DB via loopback/Unix socket). Batasi hak akses antarproses.
- **Egress** — koneksi keluar (DNS, NTP, update, backup, API). Default-deny egress + allowlist tujuan.

UFW membantu ingress, tetapi tidak otomatis membatasi egress atau mengisolasi proses. Untuk mengurangi lateral movement: akun service terpisah per komponen, DB user khusus app, AppArmor/SELinux, container dengan network policy, atau VM terpisah jika dampak kompromi tinggi.

### 16.3 Logging dan monitoring

Logging = pencatatan kejadian. Monitoring = pemeriksaan untuk menemukan anomali. Alerting = pemberitahuan saat kondisi perlu ditindaklanjuti.

Peta monitoring ujung-ke-ujung:
1. Jalur masuk: SSH, HTTP/HTTPS, firewall, WAF, TLS, auth aplikasi.
2. Eksekusi aplikasi: Nginx/Apache → PHP-FPM/Node/Python.
3. Akses data: runtime → DB → file/backup.
4. Aktivitas OS & egress: proses, user, systemd, cron, file sensitif, DNS, koneksi keluar.
5. Korelasi & respons: kumpulkan log, sinkronkan waktu, korelasikan event, alert, triase.

Yang dipantau per layer: firewall (koneksi masuk/keluar, port, tujuan), SSH/akun OS (login sukses/gagal, user baru), web server/WAF (URL, status, rule), runtime (error, restart, proses anak), database (login, privilege, query sensitif), integritas file (hash, permission, owner), OS (sudo, audit event, cron, kernel), resource (CPU/RAM/disk/latency), backup (status job, ukuran, retensi).

### 16.4 auditd

`auditd` mencatat kejadian sesuai aturan audit. Objek penting: `/etc/ssh/sshd_config`, `/etc/sudoers`, `/etc/passwd`, `/etc/systemd/system/`, cron, `authorized_keys`, config web server/WAF/DB, web root, config firewall, binari kritis.

Siapa yang butuh: admin sistem (perubahan config/user), security analyst (kronologi), incident responder (persistence/escalation), auditor (jejak perubahan).

Batas: aturan yang salah melewatkan aktivitas, terlalu banyak rule membebani disk, perubahan sah (deployment) juga tercatat, log lokal bisa dihapus penyerang root, audit tidak otomatis menjelaskan request HTTP yang memicu.

Bedakan: auditd (aktivitas sesuai rule), journald (pesan OS/app), FIM (perubahan vs baseline), network monitoring (koneksi), SIEM (korelasi & alert).

### 16.5 journald, logrotate, Fail2ban, baseline

- **journald**: kumpulkan pesan sistem/app, persistensi bergantung config & retensi. Pantau SSH, service gagal, kernel, kegagalan resource. Kirim log penting ke sistem terpisah.
- **logrotate**: kelola siklus hidup log (rotasi, kompresi, retensi). Pastikan rotasi tidak menghentikan penulisan log, retensi cukup untuk investigasi.
- **Fail2ban**: baca log, blokir sumber setelah pola (login gagal berulang). Membantu brute force sederhana, tidak mencegah eksploitasi web, credential theft, atau eksfiltrasi. Bisa false positive.
- **Baseline**: catatan kondisi normal (port, user, service, process, hash file, firewall rules, pola login/request/egress, versi). Perbarui via perubahan sah (deployment/patch).

### 16.6 Monitoring yang efektif

Tetapkan kondisi normal lalu alert. Contoh sinyal: SSH login admin dari sumber tidak dikenal (tinggi), user baru/grup admin di luar jadwal (tinggi), file config berubah tanpa deployment (tinggi), proses baru tidak sesuai perilaku app (tinggi), runtime membuka koneksi ke tujuan baru (tinggi jika terkonfirmasi), perubahan privilege DB atau ekspor data besar (tinggi), aturan firewall berubah tanpa persetujuan (tinggi), lonjakan request menyerupai eksploitasi WAF (perlu korelasi), CPU/RAM/disk/latency melonjak (perlu triase), backup gagal/salinan tidak tersedia (tinggi).

WAF hanya melihat trafik yang melewati titik inspeksi, tidak melihat proses lokal, perubahan user/sudo, file yang diubah via SSH, akses DB via loopback, egress non-WAF, perubahan firewall, penghapusan log, perubahan backup. Audit OS juga tidak menggantikan log aplikasi (request sah secara sintaks tapi menyalahgunakan otorisasi).

Log lokal saja tidak cukup: penyerang root bisa menghapus log lokal. Kirim log penting ke sistem terpisah (VM lain dengan hak akses terpisah). CISA merekomendasikan sentralisasi log, alert kejadian berisiko tinggi, perlindungan log dari perubahan tidak sah, retensi jelas.

Tentukan pemilik alert: admin (kesehatan service/config), developer (deployment/error), security analyst (korelasi/containment), pemilik backup (ketersediaan/restore), pemilik layanan (dampak bisnis).

### 16.7 Backup dan recovery

Objek yang wajib: database (data+skema+role+metadata), file aplikasi (versi rilis bersih), upload pengguna, config OS/service, secret/sertifikat (dengan akses/enkripsi sesuai), kunci enkripsi (terpisah dari backup), log/bukti insiden, dokumentasi recovery (versi, dependensi, urutan).

Alur: sumber produksi → backup konsisten (metode sesuai DB engine, catat waktu/versi/status) → enkripsi & transfer (jalur terlindungi, identitas backup khusus) → penyimpanan terpisah (lokasi berbeda, kredensial terpisah, retensi, proteksi penghapusan) → verifikasi & restore test (integritas, restore ke lingkungan terisolasi, uji app+data).

Backup harus terpisah karena penyerang dengan hak tinggi bisa menghapus data produksi sekaligus backup lokal. Gunakan akun backup khusus, hindari hak hapus semua salinan historis, immutable storage, enkripsi + pisahkan kunci, pantau kegagalan & perubahan retensi, uji restore. Pendekatan 3-2-1: 3 salinan, 2 media, 1 offsite. Untuk ransomware, tambah salinan offline/immutable.

RPO (recovery point objective) = kehilangan data yang dapat diterima (rentang waktu). RTO (recovery time objective) = waktu maksimum layanan boleh down. Frekuensi backup tidak otomatis menjamin RPO, backup tidak otomatis menjamin RTO.

Kesulitan recovery: DB & file upload dari waktu berbeda, backup terbaru mungkin sudah berisi data rusak/file berbahaya, secret bocor perlu rotasi, config lama mengembalikan kelemahan, backup terenkripsi tak berguna jika kunci hilang, app gagal saat restore, persistence penyerang ikut kembali. Karena itu restore test di lingkungan terisolasi: verifikasi DB, login app, fungsi bisnis, permission, service, TLS, firewall, monitoring sebelum layanan kembali.

### 16.8 Incident response

Respons cepat (menit pertama): validasi alert (sistem, waktu, akun, proses, indikator), nilai dampak (layanan, data sensitif, akun admin, egress), containment (batasi jalur serangan via kontrol jaringan/isolasi), lindungi bukti (simpan log, timestamp, alert, metadata, catat setiap tindakan), lindungi akses (rencanakan pencabutan sesi, rotasi secret), tentukan eskalasi (root compromise, data theft, ransomware → insiden serius).

Investigasi mendalam — pertanyaan wajib:
- Kapan aktivitas pertama? (log terpusat, auth, web, WAF, audit, DB)
- Titik masuk? (request web, SSH, perubahan app, celah/config lemah)
- Akun apa? (login, user ID, privilege, session, key, sudo)
- Proses apa? (process tree, parent, executable, service, scheduler)
- File apa berubah? (audit event, FIM, hash, metadata, deployment history)
- Data apa diakses? (DB audit, app, file access, volume trafik)
- Apakah data keluar? (flow log, DNS, proxy/firewall log, proses pemilik koneksi)
- Apakah akses masih bertahan? (akun, key, service, cron, config, persistence)
- Apa yang masih dapat dipercaya? (integritas sistem, provenance backup, config, bukti eksternal)

Jika OS dikuasai root: jangan percaya output OS yang dicurigai, isolasi via kontrol jaringan di luar host, pertahankan log terpusat, kumpulkan bukti volatil jika ada prosedur, hindari menjalankan alat sembarangan yang menimpa bukti, pertimbangkan snapshot/image forensik, prioritaskan rebuild dari media bersih, rotasi credential/token/key/secret, periksa akses ke backup & sistem lain.

Containment bukan sekadar blokir IP: jika penyerang pakai akun/sesi sah, akses dari VPN/proxy, eksploitasi lokal, credential DB dicuri, persistence sudah ditanam, atau root diperoleh — blokir IP tidak cukup. Containment bisa: nonaktifkan akun, cabut sesi/key, isolasi VM, batasi egress, hentikan service tertentu, tutup endpoint terdampak.

Recovery & verifikasi sebelum menyatakan selesai: jalur masuk ditutup/dimitigasi, image/paket/file app dari sumber tepercaya, data dipulihkan dari backup yang diperiksa, credential/sesi yang bocor ditangani, user/key/service/scheduler/firewall sesuai baseline, logging/audit/FIM/monitoring aktif, egress & akses DB sesuai kebijakan, app lulus uji fungsi & keamanan, dokumentasi kronologi/dampak/tindakan/pekerjaan lanjutan.

### 16.9 Matriks korelasi (contoh insiden)

Misalnya runtime diduga menjalankan proses tidak semestinya setelah request web:
1. Indikasi awal: WAF & access log → request tidak normal, endpoint, waktu, status.
2. Validasi proses: log runtime & info proses → proses anak, parent, user, waktu mulai.
3. Perubahan sistem: auditd & FIM → file baru, permission, unit service/cron.
4. Perluasan akses: log auth, sudo, DB → akun baru, privilege berubah, akses data sensitif.
5. Komunikasi keluar: firewall, DNS, flow log → tujuan baru, waktu, volume.
6. Containment: firewall eksternal/isolasi host → apakah aktivitas masih berlangsung.
7. Recovery: backup, baseline, image tepercaya → apakah sistem & data dapat dipulihkan aman.
8. Evaluasi: seluruh bukti → jalur masuk, cakupan dampak, kontrol yang gagal.

### 16.10 Kesulitan dan batasan

| Kontrol | Kesulitan utama | Risiko jika tanpa evaluasi |
|---|---|---|
| Egress default-deny | Menyusun allowlist tujuan lengkap & terpelihara | Update/DNS/API/backup gagal |
| auditd | Memilih aturan & mengendalikan volume event | Disk penuh, noise, kejadian penting terlewat |
| FIM | Memperbarui baseline setelah perubahan sah | Alert berlebihan atau perubahan berbahaya dianggap normal |
| SIEM/log terpusat | Biaya storage, parsing, korelasi, pengelolaan alert | Banyak alert tanpa tindak lanjut |
| Fail2ban | Menentukan filter & ambang | False positive, blokir user sah |
| Database auditing | Menentukan operasi yang dicatat | Beban tinggi atau log berisi data sensitif |
| Backup offsite | Kelola identitas, enkripsi, retensi, restore test | Backup tak dapat diakses/didekripsi/dipulihkan |
| Incident response | Seimbangkan containment, preservasi bukti, kontinuitas layanan | Bukti hilang atau kompromi berlanjut |
| Rebuild server | Pastikan image bersih, dependensi tersedia, data konsisten | Penyerang/konfigurasi rentan kembali masuk |

### 16.11 Urutan implementasi yang masuk akal

1. Tetapkan baseline & inventaris (port, service, user, config, dependensi, jalur data, layanan eksternal).
2. Amankan ingress & akses lokal (batasi SSH, tutup port, batasi privilege runtime, lindungi akses DB).
3. Terapkan kebijakan egress (observasi koneksi normal → pembatasan bertahap → uji alur app).
4. Aktifkan logging relevan (auth, web, runtime, DB, OS, firewall, backup).
5. Tambahkan audit & integritas file (objek kritis, aturan audit, baseline, perubahan yang wajib diinvestigasi).
6. Bangun monitoring & alert (aturan berdasarkan skenario risiko, pemilik alert, uji ketersediaan bukti).
7. Pisahkan backup & log penting (lindungi dari penghapusan oleh akun server produksi).
8. Latih incident response (simulasi login mencurigakan, perubahan file, egress tak diharapkan, restore backup di lab).
9. Verifikasi & review ulang (uji kontrol setelah perubahan, catat pengecualian, evaluasi baseline).

### 16.12 Referensi

- [Ubuntu Server — Firewall](https://ubuntu.com/server/docs/firewalls/) — perilaku dan pengelolaan firewall host menggunakan UFW.
- [Linux Audit System — auditd](https://www.linux.org/docs/man5/auditd.html) — peran daemon audit dan pemrosesan catatan audit.
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/use-logging-on-business-systems) — sumber log, alert, sentralisasi, perlindungan log.
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — logging, backup, perlindungan salinan, pemulihan.
- [FBI — Ten Actions to Improve Cyber Resiliency](https://www.fbi.gov/investigate/cyber/ten-actions-to-improve-cyber-resiliency) — perlindungan log dan backup offline/immutable.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — panduan incident response (April 2025).

Kesimpulan utama: pada single-tier, targetnya bukan hanya mencegah akses dari internet. Kamu juga perlu membatasi apa yang dapat dilakukan proses yang sudah dibobol, mengurangi peluang perpindahan akses dan eksfiltrasi, mempertahankan bukti yang dapat dipercaya, serta memastikan sistem bisa dipulihkan tanpa membawa kompromi kembali.

## Kesimpulan

Hardening single-tier stack adalah tentang **mengurangi risiko secara bertahap**. Tidak ada sistem yang 100% aman, tetapi dengan CIS sebagai acuan, firewall, SSH key, TLS modern, WAF, database least-privilege, logging, dan backup yang teruji, server jauh lebih aman daripada default.

Tujuan utamanya bukan hanya membuat aplikasi berjalan.  
Tujuan utamanya adalah memahami setiap lapisan pertahanan, cara memverifikasinya, dan cara memulihkannya saat terjadi masalah.

> **Note:** Hardening adalah proses berkelanjutan. Review konfigurasi secara berkala, update patch keamanan, dan uji ulang backup serta detection.

## Referensi

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — panduan konfigurasi aman per produk. [cisecurity](https://www.cisecurity.org/cis-benchmarks)
- [CIS Benchmarks Overview](https://www.cisecurity.org/cis-benchmarks-overview) — penjelasan benchmark dan pemetaannya ke CIS Controls. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — 18 kontrol keamanan prioritas. [cisecurity](https://www.cisecurity.org/controls/cis-controls-list)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) — hardening untuk host, daemon, image, dan runtime container. [docs.docker](https://docs.docker.com/dhi/explore/security-concepts/cis/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) — relevan jika stack berkembang ke container orchestration. [cisecurity](https://www.cisecurity.org/benchmark/kubernetes)
