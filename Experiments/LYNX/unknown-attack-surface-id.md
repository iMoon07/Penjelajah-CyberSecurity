# Unknown Attack Surface

[🇬🇧 Read in English](unknown-attack-surface-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](unknown-attack-surface-ms.md)
[🇵🇭 Basahin sa Tagalog](unknown-attack-surface-tl.md)

Ini membahas **Unknown Attack Surface**: batas antara attack surface yang kamu ketahui dan yang belum kamu sadari. Bukan soal tools, tetapi soal blind spot, dependency, interaksi sistem, dan asumsi yang belum diperiksa.

![Unknown attack surface](unknown-attack-surface.png)

Tujuannya adalah memahami:
- Apa itu attack surface yang diketahui vs yang tidak diketahui
- Mengapa blind spot muncul
- Bagaimana dependency dan interaksi sistem memperluas risiko
- Bagaimana asumsi yang belum diperiksa menjadi celah
- Cara menemukan dan mengurangi attack surface yang tersembunyi

## 1. Attack Surface yang Diketahui

Attack surface yang diketahui adalah permukaan yang kamu sadari dan bisa kamu kontrol:

- Port yang terbuka (22, 80, 443)
- Endpoint publik (login, API, admin panel)
- Service yang berjalan (web server, database, cache)
- User dan akun yang ada
- Fitur aplikasi yang diekspos

Ini adalah hal-hal yang biasanya muncul di scan, audit, atau checklist keamanan. Kamu tahu mereka ada, dan kamu bisa mengamankannya.

## 2. Attack Surface yang Tidak Diketahui (Blind Spots)

Blind spot adalah bagian sistem yang tidak kamu sadari keberadaannya atau dampaknya:

- Dependency transitif yang jarang diperiksa
- File konfigurasi lama yang masih aktif
- Endpoint tersembunyi atau debug yang lupa dimatikan
- Service yang berjalan tanpa dokumentasi
- Akun atau token yang sudah tidak dipakai tapi masih valid
- Fitur framework yang aktif secara default

Blind spot tidak selalu terlihat dari luar. Sering kali mereka muncul dari akumulasi keputusan kecil yang tidak pernah ditinjau ulang.

## 3. Dependency dan Interaksi Sistem

Sistem modern jarang berdiri sendiri. Setiap komponen bergantung pada komponen lain:

- Runtime bergantung pada OS dan library
- Aplikasi bergantung pada runtime dan database
- Database bergantung pada OS dan storage
- WAF bergantung pada web server
- Backup bergantung pada jaringan dan storage eksternal

Risiko muncul bukan hanya dari satu komponen, tetapi dari **interaksi antarkomponen**. Sebuah celah kecil di satu layer bisa menjadi jalur masuk ke layer lain jika interaksi tidak diperiksa.

Contoh:
- Runtime yang dibobol bisa mencuri credential database
- WAF yang salah konfigurasi bisa membuka endpoint internal
- Backup yang tidak dienkripsi bisa membocorkan data sensitif

## 4. Asumsi yang Belum Diperiksa

Banyak attack surface muncul dari asumsi yang tidak pernah diverifikasi:

- "Jaringan internal aman, jadi tidak perlu firewall antar host"
- "Database hanya diakses oleh aplikasi, jadi tidak perlu audit query"
- "User admin sudah dipercaya, jadi tidak perlu MFA"
- "Backup tersimpan di server yang sama, jadi pasti aman"
- "Dependency yang populer pasti aman"

Asumsi ini sering kali benar sebagian, tetapi tidak pernah diuji. Ketika asumsi salah, attack surface muncul tanpa disadari.

## 5. Cara Menemukan Attack Surface yang Tersembunyi

Langkah praktis untuk menemukan blind spot:

1. **Inventarisasi** — buat daftar semua komponen, service, port, user, dan dependency.
2. **Audit konfigurasi** — cek file config, environment variable, dan setting default.
3. **Scan dependency** — gunakan SCA untuk menemukan CVE di library yang dipakai.
4. **Review endpoint** — cek route, API, dan fitur yang diekspos.
5. **Cek akun dan token** — pastikan tidak ada akun atau token yang tidak dipakai.
6. **Test dari sudut pandang penyerang** — coba akses resource yang seharusnya tidak bisa diakses.

## 6. Mengurangi Unknown Attack Surface

Prinsip untuk mengurangi risiko:

- **Minimize** — hapus service, fitur, dan dependency yang tidak dipakai.
- **Isolate** — pisahkan komponen agar kompromi satu tidak menyebar.
- **Monitor** — pantau aktivitas yang tidak biasa.
- **Verify** — jangan percaya asumsi, uji dan buktikan.
- **Document** — catat semua komponen dan konfigurasi agar bisa ditinjau.

## 7. Kesimpulan

Attack surface yang tidak diketahui sering lebih berbahaya daripada yang diketahui, karena kamu tidak bisa mengamankan sesuatu yang tidak kamu sadari.

Tujuan utamanya bukan hanya menemukan celah yang ada, tetapi memahami sistem secara menyeluruh sehingga blind spot bisa ditemukan sebelum dieksploitasi.

> **Note:** Attack surface yang tidak diketahui tidak bisa dihilangkan sepenuhnya, tetapi bisa diminimalkan dengan inventarisasi, audit, dan verifikasi yang rutin.

## Referensi

- [OWASP Attack Surface Analysis](https://owasp.org/www-community/Attack_Surface_Analysis_Cheat_Sheet) — panduan analisis attack surface.
- [NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — kontrol keamanan dan manajemen risiko.
- [CISA — Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — katalog CVE yang aktif dieksploitasi.