# Dari Perangkat Keras ke Perangkat Lunak: Bagaimana Aplikasi Benar-Benar Berjalan

[🇬🇧 Read in English](from-hardware-to-software-how-applications-actually-run-en.md)  
[🇲🇾 Baca dalam Bahasa Melayu](from-hardware-to-software-how-applications-actually-run-ms.md)  
[🇵🇭 Basahin sa Tagalog](from-hardware-to-software-how-applications-actually-run-tl.md)

![Dari Perangkat Keras ke Perangkat Lunak: Bagaimana Aplikasi Benar-Benar Berjalan](from-hardware-to-software.png)

## Pertanyaan Sederhana: Gimana Caranya File Bisa Berjalan?

Pernah kepikiran nggak, gimana caranya ketika kamu klik sebuah aplikasi, tiba-tiba ada jendela yang muncul di layarmu?

Kita klik sebuah ikon. Beberapa detik kemudian, tombol bisa ditekan, teks bisa diketik, gambar bisa muncul. Yang keliatan cuma antarmukanya aja. Padahal yang terjadi di balik layar jauh lebih banyak dari yang kita sadari.

Artikel ini bakal ngobrolin alurnya secara konseptual. Bukan buat jadi insinyur hardware, tapi buat punya gambaran besar tentang gimana aplikasi beneran bisa jalan.

## Program vs Proses: Bedanya Apa?

Sebelum lanjut, ada dua istilah yang wajib dibedain.

- **Program** — Berupa file yang tersimpan di disk (mis. `firefox`, `chrome.exe`, atau `app`). Ia cuma kumpulan instruksi dalam bentuk data. Kalau belum dijalanin, program itu "mati", cuma berisi kode.
- **Proses** — Program yang sedang dieksekusi. Begitu kamu klik dan aplikasinya jalan, sistem operasi bakal mengubah program jadi proses. Proses ini punya memori sendiri, status saat ini, file yang dibuka, dan sumber daya yang dipakainya.

**Analogi simpel:** Program itu resep masakan yang tertulis di buku. Proses itu masakan yang sedang dimasak di dapur. Resep bisa ada di rak selamanya, tapi masakan baru ada pas kita mulai masak.

## Lapisan Komputer: Hardware, Sistem Operasi, dan Aplikasi

Agar sebuah aplikasi bisa jalan, ada tiga lapisan utama yang saling bekerja sama.

| Lapisan | Peran | Analogi |
| --- | --- | --- |
| **Hardware** | Bagian fisik. CPU, RAM, penyimpanan (SSD/HDD), GPU, dan perangkat input/output. | Peralatan dapur: kompor, meja, panci, dan pisau. |
| **Sistem Operasi (OS)** | Pengatur dan penengah. Mengelola sumber daya, memberi akses ke hardware, mengatur proses, serta melindungi satu aplikasi agar nggak mengganggu aplikasi lain. | Kepala dapur. Yang mutusin siapa yang boleh pakai kompor, ngatur urutan, dan mencegah kekacauan. |
| **Aplikasi (User Space)** | Yang kita pakai langsung. Browser, text editor, game, dll. Aplikasi nggak langsung ngobrol ke hardware, ia ngobrol lewat sistem operasi. | Resep & masakan yang mau kita buat. |

Poin penting: **Aplikasi jarang ngobrol langsung ke hardware.** Ia minta izin ke sistem operasi lewat sesuatu yang namanya *system call*.

## Perjalanan Aplikasi: Dari Klik hingga Muncul di Layar

Sekarang, kita ikutin alurnya step by step.

### Langkah 1: Permintaan untuk Menjalankan Program
Ketika kamu klik ikon aplikasinya, sistem operasi **tidak selalu** langsung menciptakan proses baru. Bergantung pada sistem operasi dan aplikasinya, klik tersebut bisa memanggil proses yang sudah ada (misalnya lewat *single instance*), atau bisa membuat satu atau lebih proses baru. Setelah proses terbentuk, barulah sistem operasi memetakan program ke ruang alamat proses dan memuat halaman yang dibutuhkan saat diperlukan.

### Langkah 4: CPU Mengeksekusi Instruksi
Sekarang, **CPU** yang mulai bekerja. Ia akan mengambil instruksi satu per satu dari memori, menerjemahkan, dan menjalankannya.

Bayangin CPU sebagai koki yang cuma bisa baca dari "meja masak" (RAM). Dia nggak akan bolak-balik ke lemari (disk) buat tiap bahan. Lemari dipakai buat nyimpen, meja masak dipakai buat diproses.

### Langkah 5: Berinteraksi Lewat System Call
Saat aplikasi butuh sesuatu yang diluar kemampuannya, misalnya membuka file, konek internet, atau menggambar ke layar, ia bisa meminta bantuan lewat *system call*. Namun, tidak semua urusan tampilan ditangani langsung oleh *system call*. *Window manager*, *graphics stack*, driver grafis, serta API grafis atau *framework* yang dipakai aplikasi turut terlibat untuk merender dan menampilkan antarmuka ke layar. OS tetap berperan lewat *system call* dan manajemen sumber daya, namun interaksi grafis biasanya melalui lapisan tambahan di atasnya.

### Langkah 6: Hasil Muncul di Layar
Setelah melewati seluruh proses di atas, akhirnya apa yang kamu minta bisa terlihat. Tombol muncul, halaman web ter-render, atau pesan error ditampilkan ke layarmu.

Semua ini bisa terjadi dalam hitungan milidetik, padahal ada puluhan hingga ribuan langkah kecil yang dilalui.

## Peran Penting: Mengapa Kita Butuh Sistem Operasi?

Kalo aplikasinya bisa langsung ngobrol ke hardware, kedengerannya efisien. Tapi di dunia nyata, ini bakal jadi bencana.

Sistem operasi ada buat alasan ini:

- **Abstraksi** — Aplikasi nggak perlu tau spek RAM, tipe SSD, atau driver GPU kamu. OS yang nyediain antarmuka yang seragam.
- **Manajemen sumber daya** — Kalau 10 aplikasi minta akses CPU bersamaan, OS yang bagi-bagi waktunya biar semuanya kebagian.
- **Isolasi** — Proses satu aplikasi nggak boleh seenaknya baca memori aplikasi lain. Ini penting buat stabilitas dan keamanan.
- **Keamanan & izin** — OS yang nentuin aplikasi boleh akses file apa, boleh konek kemana, atau nggak.
- **Efisiensi** — OS pintar mengatur mana yang harus dimuat, mana yang bisa ditunda, dan gimana memanfaatkan sumber daya sebaik mungkin.

Tanpa OS, tiap aplikasi harus "kenal" semua hardware di dunia. Dengan OS, aplikasi cukup "kenal" OS aja.

## Pengantar Singkat: Stack Memori

Sebelum kita masuk lebih dalam di artikel selanjutnya, ada baiknya tau gambaran hierarki memori secara simpel.

| Komponen | Kecepatan | Kapasitas | Fungsi |
| --- | --- | --- | --- |
| **Register** | Paling cepat | Sangat kecil, terdiri dari sejumlah register CPU | Tempat CPU nyimpen data yang lagi diproses langsung. |
| **CPU Cache (L1/L2/L3)** | Sangat cepat | Kecil | Buffer buat data/instruksi yang sering dipake biar CPU nggak bolak-balik ke RAM. |
| **RAM (Main Memory)** | Cepat | Sedang-Besar (GB) | Tempat proses nyimpen kode, variabel, dan data yang lagi aktif dipakai. |
| **Penyimpanan (SSD/HDD)** | Lebih lambat | Sangat besar (GB-TB) | Penyimpanan permanen buat program, file, dan data kamu. |

Aturannya simpel: **Semakin dekat ke CPU, semakin cepat, tapi semakin kecil kapasitasnya. Semakin jauh, semakin lambat, tapi semakin besar.**

## Kesimpulan

Singkatnya: **Program bukan proses**. Program itu file yang diam di disk. Proses itu program yang "hidup" di RAM dan dijalankan CPU.

Alurnya kurang lebih begini: *klik → OS buat proses → muat ke RAM → CPU eksekusi instruksi → minta bantuan OS kalo perlu → hasil tampil di layar*.

Yang paling penting buat dipahami disini bukan detail teknis tiap chip, tapi **gambaran besar**: aplikasi nggak langsung pegang hardware. Ada sistem operasi yang jadi jembatan, ada RAM yang jadi "meja kerja", dan ada CPU yang jadi "yang mengerjakan".

Paham mental model ini bakal bikin kamu jauh lebih gampang nangkap topik-topik fundamental selanjutnya, kayak memori, *system call*, atau kenapa aplikasi bisa terasa lemot.

## Referensi

- Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating System Concepts* (10th Edition). Wiley — Referensi untuk memahami proses, manajemen memori, penjadwalan CPU, dan peran sistem operasi.  
  [Official Publisher Page — Wiley](https://www.wiley.com/en-us/shop/general-end-user-computing/operating-system-concepts-10th-edition-p-9781119800361) · [Book Resources](https://codex.cs.yale.edu/avi/os-book/OS10/index.html)

- Bryant, R. E., & O’Hallaron, D. R. *Computer Systems: A Programmer’s Perspective (CS:APP)* (3rd Edition). Pearson / Carnegie Mellon University — Membahas bagaimana program dijalankan, hubungan perangkat lunak dengan perangkat keras, representasi instruksi, hierarki memori, dan manajemen memori.  
  [Official Book Website — Carnegie Mellon University](https://csapp.cs.cmu.edu/3e/perspective.html) · [Publisher Page — Pearson](https://www.pearson.com/en-us/subject-catalog/p/computer-systems-a-programmers-perspective/P200000003479/9780138105396)

- Tanenbaum, A. S., & Bos, H. *Modern Operating Systems* (5th Edition). Pearson — Referensi mengenai proses, thread, manajemen memori, sistem berkas, input/output, serta bagaimana sistem operasi mengelola sumber daya komputer.  
  [Official Publisher Page — Pearson](https://www.pearson.com/en-us/subject-catalog/p/modern-operating-systems/P200000003295/9780137618934)
