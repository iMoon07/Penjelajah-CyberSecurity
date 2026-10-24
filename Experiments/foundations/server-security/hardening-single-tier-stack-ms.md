# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

## Mengapa Perlu Dihardening?

Konfigurasi lalai dibina supaya aplikasi boleh terus berjalan, bukan supaya selamat. Dalam seni bina *single-tier*, semua komponen — pelayan web, runtime, pangkalan data, dan sistem fail — berada dalam **satu mesin yang sama**. Kecacatan kecil pada satu lapisan boleh membuka jalan ke lapisan lain tanpa menembusi banyak sempadan.

Tujuan *hardening* di sini bukan "mengunci segala-galanya", tetapi **mengurangkan ruang gerak penyerang** jika suatu lapisan dikompromi. Fokus ialah mengehadkan akses, mengasingkan hak, mengesan perubahan, dan memastikan kita boleh memulihkan sistem tanpa membawa kompromi balik.

## Model Ancaman

Sebelum menerapkan tetapan, fahami apa yang kita lindungi dan batasannya.

| Aspek | Penjelasan |
|---|---|
| **Aset dilindungi** | Perkhidmatan web, data aplikasi, kelayakan, fail konfigurasi, log, dan salinan *backup*. |
| **Ancaman utama** | Eksploitasi kecacatan aplikasi, *brute force* log masuk, kebocoran kelayakan, penyalahgunaan hak tempatan, eksfiltrasi data dari mesin yang sama. |
| **Andaian** | Perkhidmatan web boleh dicapai dari internet. Dalam *single-tier*, aplikasi, runtime, dan pangkalan data berkongsi satu OS. |
| **Batas perlindungan** | Kita boleh mengurangkan *attack surface*, mengehadkan pergerakan lateral, dan mengukuhkan pengesanan. Tetapi jika satu mesin dikuasai sepenuhnya dengan hak *root*, tiada tetapan hos tunggal yang menjamin keselamatan mutlak. |
| **Luar skop** | Keselamatan rangkaian perimeter luar hos, serangan peringkat hypervisor, atau kompromi terhadap akaun *provider* yang menjalankan mesin. |

## Attack Surface & Aliran Akses

Dalam *single-tier*, pergerakan penyerang boleh mengikut laluan yang saling berkait.

| Laluan | Penjelasan | Nota Hardening |
|---|---|---|
| **Ingress (dari luar)** | Masuk melalui port terbuka, biasanya `80`/`443`. SSH hanya dibuka jika benar-benar diperlukan. | *Default deny*; izinkan hanya port diperlukan. Hadkan SSH ke rangkaian/admin dipercayai. |
| **East-West (antar komponen)** | Komunikasi antara proses dalam mesin yang sama, biasanya melalui `127.0.0.1` atau *Unix socket*. | Jangan biar pangkalan data mendengar `0.0.0.0`. Asingkan pengguna/perkhidmatan setiap komponen. Terapkan *least privilege*. |
| **Egress (keluar)** | Sambungan dari pelayan ke luar (kemas kini, DNS, API, dll). | Perhatikan pola normal dahulu, kemudian hadkan secara berperingkat. Jangan abaikan kerana "pelayan perlukan keluar". |

> **Penting:** Port `443` boleh dibuka kerana diperlukan, tetapi kerana ia wajib dibuka, pastikan aplikasi di belakangnya selamat, hadkan haknya, dan dipantau.

## Prinsip Asas Hardening

Setiap kawalan harus menjawab tiga soalan: *Apa yang dilakukan? Mengapa risiko berkurang? Apa batasnya?*

| Prinsip | Penerapan | Batas |
|---|---|---|
| **Kurangkan attack surface** | Matikan perkhidmatan tak digunakan; buka hanya port diperlukan. | Tidak boleh tutup port yang memang diperlukan aplikasi. |
| **Least privilege** | Jalankan setiap perkhidmatan dengan pengguna berasingan dan hak minimum. | Hak minimum mesti masih cukup untuk aplikasi berfungsi. Perlu diuji. |
| **Pengasingan** | Asingkan hak proses, pemilikan fail, had systemd. | Dalam satu mesin, pengasingan bersifat logik. Kompromi dengan akses cukup masih boleh melintasi komponen. |
| **Defense in depth** | Gabungkan firewall, hak, pengesahan aplikasi, logging, backup. | Jika satu lapisan gagal, lapisan lain boleh melambatkan atau mengesan. Bukan jaminan. |
| **Pengesanan & pengesahan** | Baseline, pantau perubahan, uji kawalan secara berkala. | Tanpa susulan, log hanya jadi arkib. |
| **Sedia pulih** | Asingkan backup, uji restore, dokumentasikan respons insiden. | Backup yang tak diuji restore sama seperti tiada backup. |

## Standard Rujukan: CIS

[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) boleh jadi rujukan, bukan sasaran mutlak.

- **Level 1**: Baseline praktikal, sesuai untuk pelaksanaan berperingkat pada kebanyakan *single-tier*.
- **Level 2**: Lebih ketat; guna hanya jika benar-benar diperlukan dan diuji di makmal.
- **Pematuhan ≠ Keselamatan**: Skor bergantung pada profil, versi *benchmark*, dan pengecualian terdokumentasi. Yang penting ialah memahami sebab setiap kawalan, bukan sekadar menanda semua poin.

## OS, Attack Surface & Rangkaian

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Kemas kini & patch** | *Apa:* Terapkan kemas kini keselamatan. *Mengapa:* Tutup kecacatan diketahui. *Batas:* Patch perlu pengujian; *zero-day* kekal. | Kemas kini rutin; prioritaskan komponen terdedah rangkaian. |
| **Firewall hos** | *Apa:* *Default deny incoming*; izinkan hanya port diperlukan. *Mengapa:* Kurangkan laluan ingress. *Batas:* Tidak melindungi eksploitasi melalui port yang wajib dibuka (80/443). | SSH boleh dihadkan ke VPN/rangkaian admin. HTTP boleh dialihkan ke HTTPS. |
| **SSH hardening** | *Apa:* Guna kunci; nyahaktifkan *root login* & *password auth*. *Mengapa:* Kurangkan *brute force*. *Batas:* Kunci bocor masih boleh diguna jika tak dicabut. | Hadkan `AllowUsers` bila boleh. |
| **Kernel & mount options** | *Apa:* Terapkan sysctl relevan; pertimbangkan `noexec/nosuid/nodev` pada partisi sensitif. *Mengapa:* Hadkan eksekusi/pergerakan berbahaya. *Batas:* Boleh merosakkan aplikasi jika diguna tanpa uji. Sesuaikan dengan fungsi *mount*. | Uji di makmal dahulu. |

## Perkhidmatan, Fail, Hak Akses & Secret

Dalam *single-tier*, pengasingan antara perkhidmatan sangat penting kerana semua berkongsi OS yang sama.

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Minimasi perkhidmatan** | *Apa:* Matikan perkhidmatan tak diguna. *Mengapa:* Semakin sedikit perkhidmatan aktif, semakin kecil *attack surface*. *Batas:* Ada perkhidmatan sokongan yang kadang diperlukan fungsi tertentu. | Inventori dahulu, jangan matikan sembarangan. |
| **Least privilege setiap perkhidmatan** | *Apa:* Jalankan setiap perkhidmatan dengan pengguna/grup berasingan. *Mengapa:* Hadkan kesan jika satu perkhidmatan dikompromi. *Batas:* Jika aplikasi perlukan akses luas untuk berfungsi, had mesti realistik dan diuji. | Guna [systemd sandboxing](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html): `User=`, `Group=`, `NoNewPrivileges=`, `ProtectSystem=`, `ProtectHome=`, `ReadOnlyPaths=`, `PrivateTmp=`. |
| **Hak fail & pemilikan** | *Apa:* Tetapkan pemilikan & izin ketat (`600/640`, `chown` tepat). *Mengapa:* Elak akses lintas-pengguna yang tak perlu. *Batas:* Salah tetapan boleh rosakkan aplikasi. | Fokus ke config, kunci, log, direktori muat naik. |
| **Pengurusan secret** | *Apa:* Jangan letak kelayakan dalam repo. Simpan dalam fail izin ketat atau *secret manager*. *Mengapa:* Kurangkan risiko kebocoran. *Batas:* Jika runtime dikompromi dan boleh baca secret yang boleh diaksesnya, secret masih boleh diambil. | Putar, hadkan akses, audit, dan pastikan `.env` dalam `.gitignore`. |

## Pelayan Web, Pelayar, TLS & WAF

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Hardening pelayan web** | *Apa:* `server_tokens off`, hadkan *method*, nyahaktifkan *autoindex*, terapkan *header* sisi pelayan. *Mengapa:* Kurangkan maklumat & risiko tertentu. *Batas:* Header membantu, tapi bukan pengganti pengesahan aplikasi. | Pisahkan tanggungjawab: *server* tetapkan *header*, aplikasi wajib sahkan input, autentikasi, autorisasi & anti-CSRF. |
| **TLS/HTTPS** | *Apa:* TLS moden, *HSTS*, redirect HTTP→HTTPS, *OCSP stapling*. *Mengapa:* Enkripsi trafik & elak *downgrade*. *Batas:* TLS lindungi saluran, bukan logik aplikasi atau hak akses. | Sahkan dengan `testssl.sh`/SSL Labs. Lindungi *private key* dengan izin ketat. |
| **WAF** | *Apa:* Tapis pola berbahaya (SQLi/XSS). Mula dari *DetectionOnly*, kemudian *Blocking* berperingkat. *Mengapa:* Tambah lapisan pengesanan/tapisan. *Batas:* Boleh *false positive*, tak nampak pergerakan lokal/lateral, dan boleh dipintas. Perlu disuaikan dengan aplikasi. | WAF kurangkan peluang eksploitasi tetapi **bukan pengganti** kod selamat. |

## Pangkalan Data & Runtime

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Hardening pangkalan data** | *Apa:* *Bind* ke `127.0.0.1`/Unix socket, *least privilege* bagi setiap pengguna aplikasi, nyahaktifkan akses root jauh. *Mengapa:* Hadkan akses rangkaian. *Batas:* Jika aplikasi dikompromi, aplikasi masih boleh akses DB dengan hak pengguna aplikasinya. | Asingkan pengguna setiap aplikasi. Jangan guna pengguna `root` untuk sambungan aplikasi. |
| **Penyulitan pangkalan data** | *Apa:* Pertimbangkan penyulitan *at-rest* (sokongan TDE berbeza ikut enjin/versi/edisi) atau penyulitan volum (LUKS). *Mengapa:* Lindungi data jika cakera dicuri. *Batas:* Tidak lindungi jika mesin hidup & aplikasi/DB boleh dicapai penyerang yang sudah masuk. | Penyulitan *backup* sama penting, kadang lebih kritikal. |
| **Runtime hardening** | *Apa:* Jalankan runtime sebagai non-root, hadkan sumber, minimakan fungsi berbahaya. *Mengapa:* Hadkan kesan RCE. *Batas:* Kompromi runtime dengan akses tempatan masih boleh cuba manfaatkan perkhidmatan tempatan lain dalam mesin yang sama. | Fokus pengasingan setiap perkhidmatan, bukan sekadar "non-root". |

## Logging, Monitoring & Pengesanan

Yang penting bukan "rekod sebanyak mungkin", tetapi **rekod yang boleh ditindaklanjuti**.

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Audit & FIM** | *Apa:* `auditd` untuk perubahan kritikal, *File Integrity Monitoring* untuk fail penting. *Mengapa:* Kesan perubahan tak sah. *Batas:* Perlukan *baseline* yang dijaga. Perubahan sah (deploy) boleh timbulkan bunyi bila tak diurus. | Fokus ke `/etc`, config web/DB, kunci, direktori kritikal. |
| **Log berpusat & perlindungan log** | *Apa:* Kumpul log relevan, jaga integriti log. *Mengapa:* Jika penyerang dapat akses *root*, log tempatan boleh dipadam. *Batas:* Perlukan saluran berasingan yang lebih terlindung. | Pertimbangkan hantar log ke sistem berasingan dengan hak akses berbeza. |
| **Pengesanan berasaskan anomali** | *Apa:* Pantau log masuk mencurigakan, pengguna baru, proses tak biasa, sambungan keluar tak wajar, perubahan hak. *Mengapa:* Banyak serangan tak tinggalkan tanda "exploit" jelas. *Batas:* Perlukan masa untuk kenal pola normal. *Alert* tanpa pemilik & laluan susulan sia-sia. | Tetapkan pemilik *alert* dan cara eskalasi ringkas. |

## Backup, Recovery & Respons Insiden

Dalam *single-tier*, pemisahan *backup* jauh lebih penting dari yang kebanyakan fikir.

| Kawalan | Apa / Mengapa / Batasnya | Nota |
|---|---|---|
| **Backup terasing** | *Apa:* Simpan salinan luar mesin (lokasi/kelayakan berbeza). *Mengapa:* Akaun produksi boleh diguna padam backup tempatan. *Batas:* Jika kunci penyulitan backup disimpan dalam mesin yang sama, boleh ikut terkunci/dicuri. | Asingkan pengurusan kunci. Guna akaun *backup* khusus dengan hak minimum. |
| **Uji restore** | *Apa:* Uji *restore* ke persekitaran terasing secara berkala. *Mengapa:* Buktikan backup benar-benar boleh dipulihkan. *Batas:* Persekitaran uji mesti cukup serupa untuk dedahkan masalah keserasian. | **Peraturan praktikal:** Backup yang tak pernah diuji restore sama seperti tiada backup. |
| **Respons insiden ringkas** | *Apa:* Aliran *Deteksi → Pembendungan → Siasatan → Pemulihan → Penilaian*. *Mengapa:* Elak panik & elak re-kompromi. *Batas:* Pada *root compromise*, jangan percaya output tempatan. Prioritikan pengasingan, lindungi bukti berpusat, dan putuskan rebuild dari sumber dipercayai. | Fokus putaran kelayakan, penutupan laluan masuk, pengesahan baseline, dokumentasi kronologi. |

## Pengesahan Hardening

Asingkan mengikut fungsi supaya lebih realistik.

### Pencegahan (mencegah)

| Check | Verify |
|---|---|
| Hanya port diperlukan dibuka | `ss -tulnp` / status firewall |
| DB hanya di `127.0.0.1` atau *Unix socket* | Config DB + uji sambungan dari luar hos |
| SSH guna kunci; root/password auth dinyahaktifkan | `sshd_config` + uji log masuk |
| Perkhidmatan jalan dengan pengguna berasingan | `ps aux` / unit `systemd` |
| Secret tak dalam repo & izin ketat | Audit fail & `.gitignore` |

### Pengesanan (mengesan)

| Check | Verify |
|---|---|
| `auditd` aktif untuk fail/config kritikal | Peraturan audit & log muncul |
| *File Integrity Monitoring* berjalan | *Baseline* ada & perubahan dikesan |
| Logging relevan aktif & boleh diakses berpusat | Aliran log berjalan, retensi cukup |
| *Alert* ada pemilik & laluan susulan | Senarai pemilik *alert* ringkas wujud |

### Pemulihan (memulihkan)

| Check | Verify |
|---|---|
| Backup terasing dari mesin produksi | Lokasi, kelayakan, izin terasing |
| Uji restore pernah berjaya | Tarikh + hasil uji direkod dalam persekitaran terasing |
| Ada rancangan pengasingan & putaran kelayakan | Dokumen ringkas boleh diguna semasa panik |
| Boleh kembali ke baseline dipercayai | Laluan rebuild/pemulihan terdokumentasi |

## Kesilapan Umum & Batas Hardening Single-Tier

| Kesilapan umum | Mengapa berbahaya | Cara elak |
|---|---|---|
| **Buka port DB ke awam** | Terus mengembangkan *attack surface* | Hanya `127.0.0.1`/Unix socket + firewall ketat |
| **SSH root + password auth** | Sasaran kegemaran *brute force* | Kunci SSH, nyahaktifkan kedua-dua, hadkan akses |
| **Bergantung pada header/WAF sahaja** | Menganggap lapisan pelindung cukup | Header & WAF membantu, tapi pengesahan, auth, autorisasi wajib dalam aplikasi |
| **"Tertutup dari luar" = selamat** | Mengabaikan akses tempatan & *east-west* | Ingat: jika runtime/aplikasi dikompromi, ia boleh guna akses tempatan |
| **Backup tak diuji** | Gagal bila benar-benar diperlukan | Jadualkan uji restore berkala; asingkan salinan & kunci |
| **Terlalu umum pada `noexec/nosuid/nodev`** | Boleh rosakkan aplikasi tanpa sebab | Terapkan setiap partisi ikut fungsi, sentiasa uji di makmal |
| **Log cuma disimpan, tak ditindaklanjuti** | Pengesanan jadi sia-sia | Tetapkan pemilik *alert* + laluan eskalasi |

**Batas hardening single-tier:** Anda boleh melambatkan, mengehadkan, dan mengesan serangan. Anda **tidak boleh** menghapus risiko *SPOF* melalui konfigurasi semata. Jika satu mesin sepenuhnya dikompromi, yang boleh anda lakukan ialah **mengehadkan kerosakan, melindungi bukti, dan pulih dari sumber dipercayai**.

## Kesimpulan

Hardening single-tier ialah soal **mengurangkan ruang gerak, bukan membuat sistem kebal**. Mula dari memahami model ancaman & *attack surface*, terapkan *least privilege* + pengasingan, asingkan pencegahan/pengesanan/pemulihan, dan yang paling penting: **uji apa yang anda terapkan**.

Konfigurasi boleh betul, tetapi tetap ada batas. Yang membezakan hardening matang ialah keupayaan menjawab: *"Jika ini gagal, apa yang masih boleh dicegah, dikesan, atau dipulihkan?"*

## Rujukan

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — Rujukan konfigurasi selamat setiap produk
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — Keutamaan kawalan keselamatan
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — Panduan respons insiden
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/resources-tools/resources/use-logging-business-systems) — Pengurusan log, pengesanan & perlindungan log
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware) — Backup terasing, perlindungan salinan & pemulihan
- [systemd.exec Manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) — Pilihan sandboxing setiap unit perkhidmatan
