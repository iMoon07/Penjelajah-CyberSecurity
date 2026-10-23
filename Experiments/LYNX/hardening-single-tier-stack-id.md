# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)

Ini membahas **hardening single-tier stack**. Artinya, semua layer—web server, runtime, database, cache—berada di satu mesin, dan kita akan mengamankannya dari dasar tanpa harus membahas instalasi dari nol.

![Hardening single tier stack](linux-exposure-network-experiment.png)

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

> **Warning:** Jangan hardening di production langsung. Selalu uji di lab atau VM dulu.

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

> **Note:** CIS bukan berarti harus diterapkan 100%. Pilih level sesuai kebutuhan lab atau production, lalu dokumentasikan apa yang diterapkan dan apa yang sengaja dilewati.

## 3. Sistem Operasi

| Aspek | Yang dilakukan | Kenapa penting |
|---|---|---|
| Update dan patch | Rutin perbarui OS dan paket | Menutup celah yang sudah diketahui |
| User dan privilege | Jangan login root; buat user biasa dengan sudo | Mengurangi dampak jika akun bocor |
| SSH | Nonaktifkan root login dan password auth; pakai SSH key | SSH adalah pintu masuk utama server |
| Firewall host | Default deny incoming; buka hanya 22, 80, 443 | Mengurangi exposure port |
| Auto patch | Aktifkan unattended upgrades untuk patch keamanan | Menjaga sistem tetap aman tanpa intervensi manual |
| Service minimization | Matikan service yang tidak dipakai | Semakin sedikit service, semakin kecil attack surface |
| Kernel parameter | Terapkan sysctl hardening yang relevan | Mengurangi risiko network-level abuse |

> **Important:** Jangan buka port database (3306, 5432) ke publik. Database harus hanya bisa diakses dari localhost atau jaringan internal.

## 4. Service, File, dan Secret

| Aspek | Yang dilakukan | Kenapa |
|---|---|---|
| Service minim | Hapus atau disable service yang tidak dipakai | Mengurangi jalur masuk dan beban server |
| File permission | Batasi permission config, log, dan file sensitif | Mencegah akses tidak perlu |
| Umask | Gunakan default permission yang ketat | File baru tidak langsung terbuka untuk semua user |
| SELinux/AppArmor | Aktifkan sesuai distro | Membatasi perilaku service jika terkena compromise |
| Secret | Jangan taruh password atau API key di repo atau file world-readable | Mencegah credential leak |
| Environment variable | Simpan secret di file dengan permission ketat atau secret manager | Mengurangi risiko kebocoran konfigurasi |

> **Warning:** File `.env`, database credential, SSH key, dan backup tidak boleh masuk ke Git. Gunakan `.gitignore` sejak awal.

## 5. Web Server Hardening

| Web server | Pengaturan penting | Tujuan |
|---|---|---|
| Nginx | `server_tokens off`, security headers, batasi method HTTP, nonaktifkan autoindex | Menyembunyikan versi dan membatasi request berbahaya |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers | Menyembunyikan informasi server dan menolak method berbahaya |
| Caddy | Header security, reverse proxy dengan TLS otomatis | Konfigurasi sederhana dengan default yang aman |

Security headers yang sebaiknya ada:

- `X-Frame-Options: SAMEORIGIN` — mencegah clickjacking
- `X-Content-Type-Options: nosniff` — mencegah MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin` — kontrol referrer
- `Permissions-Policy` — batasi akses fitur browser

## 6. TLS / HTTPS

| Aspek | Rekomendasi | Kenapa |
|---|---|---|
| Minimum TLS | TLS 1.2, lebih baik TLS 1.3 | Protocol lama punya celah |
| Cipher | Hanya cipher modern, misalnya ECDHE dan GCM | Mencegah downgrade attack |
| HSTS | Aktifkan dengan `max-age` panjang | Memaksa HTTPS di browser |
| Sertifikat | Let's Encrypt via Certbot, renewal otomatis | Gratis dan umum dipakai |
| Session | Batasi session timeout dan pertimbangkan menonaktifkan session tickets | Mengurangi risiko session reuse |

## 7. WAF: Web Application Firewall

| Komponen | Fungsinya | Catatan |
|---|---|---|
| ModSecurity | WAF engine untuk Apache/Nginx | Perlu tuning agar tidak false positive |
| OWASP CRS | Rule set standar industri | Mulai dari mode `DetectionOnly` |
| Coraza | Alternatif WAF berbasis Go | Ringan dan cocok untuk setup modern |

> **Warning:** Jangan langsung aktifkan WAF mode blocking di production. Mulai dari `DetectionOnly`, analisis log, lalu aktifkan secara bertahap.

## 8. Database Hardening

| Aspek | Yang dilakukan | Kenapa |
|---|---|---|
| Secure installation | Jalankan secure installation bawaan database | Hapus anonymous user, test database, dan remote root |
| Least privilege | Buat user aplikasi dengan hak terbatas: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Jika bocor, dampaknya terbatas |
| Bind address | Database hanya listen di `127.0.0.1` | Database tidak bisa diakses dari luar |
| Password | Gunakan password kuat; PostgreSQL mendukung SCRAM-SHA-256 | Mencegah brute force |
| Remote access | Nonaktifkan remote login untuk root database | Root dari luar sangat berbahaya |
| Backup | Backup rutin dan tes restore | Hardening tidak melindungi dari human error atau kerusakan disk |

## 9. Runtime Hardening

| Runtime | Pengaturan penting | Tujuan |
|---|---|---|
| PHP-FPM | Jalankan sebagai `www-data`; batasi `pm.max_children`; matikan fungsi berbahaya; `expose_php Off` | Mengurangi resource abuse dan information leak |
| Node.js | Jalankan sebagai user non-root via systemd; gunakan PM2 atau service manager | Isolasi process dan auto-restart |
| Python | Gunakan virtual environment; jalankan Gunicorn/uWSGI sebagai user biasa | Isolasi dependency dan privilege |
| Java | Setel JVM memory limit; jalankan sebagai user biasa | Mencegah memory exhaustion |
| .NET | Jalankan Kestrel sebagai user non-root; gunakan reverse proxy di depannya | Isolasi process dan kontrol akses |

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
