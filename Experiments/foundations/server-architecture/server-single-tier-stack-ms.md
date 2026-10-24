# Tindanan Pelayan Satu-Tingkat (Single-Tier Server Stack)

[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)
[🇬🇧 Read in English](server-single-tier-stack-en.md)
[🇵🇭 Basahin sa Tagalog](server-single-tier-stack-tl.md)

![Tindanan Pelayan Satu-Tingkat](single-tier-stack.png)

## 1. Satu Pelayan, Satu Tindanan

**Tindanan Pelayan Satu-Tingkat (Single-Tier Server Stack)** bermaksud [pelayan web](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server), [masa jalan aplikasi](https://en.wikipedia.org/wiki/Runtime\_system), dan [pangkalan data](https://en.wikipedia.org/wiki/Database) kesemuanya berjalan di **satu mesin yang sama**.

Bayangkan gerai makanan di bawah satu bumbung. Juruwang, dapur dan stor bahan berada di satu bangunan. Pesanan terus diproses di situ.

Kesemua komponen ini bekerjasama di satu pelayan bagi memudahkan pemahaman.

## 2. Bagaimana Ia Berfungsi?

Apabila seseorang melayari laman web anda menggunakan [pelayar web](https://en.wikipedia.org/wiki/Web\_browser), begini alirannya:

1. **Pelayar** → Menghantar [permintaan HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) ke pelayan
2. **Pelayan Web** → Menerima dan mengarahkan permintaan kepada aplikasi
3. **Masa Jalan Aplikasi** → Menjalankan [logik perniagaan](https://en.wikipedia.org/wiki/Business\_logic) aplikasi (borang, log masuk, pengesahan, dll.)
4. **Pangkalan Data** → Mengambil, menambah, mengemas kini atau memadam data yang diperlukan
5. **Respons** → Pelayan web menghantar [respons HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) (HTML, JSON atau fail) kembali ke pelayar

Kesemua ini berlaku di **satu mesin yang sama**.

## 3. Komponen Utama

| Komponen | Fungsi | Contoh |
|---|---|---|
| **[Pelayan Web](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server)** | Pintu masuk. Menerima permintaan, mengarahkan dan membalas respons. | [Nginx](https://nginx.org/), [Apache HTTP Server](https://httpd.apache.org/), [Caddy](https://caddyserver.com/) |
| **[Masa Jalan Aplikasi](https://en.wikipedia.org/wiki/Runtime\_system)** | Otak. Menjalankan kod aplikasi anda. | [PHP-FPM](https://www.php.net/manual/en/install.fpm.php), [Node.js](https://nodejs.org/), [Gunicorn](https://gunicorn.org/), [Kestrel (.NET)](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel) |
| **[Pangkalan Data](https://en.wikipedia.org/wiki/Database)** | Stor data. Menyimpan dan mengurus data aplikasi. | [MariaDB](https://mariadb.org/), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), [SQLite](https://sqlite.org/) |

Boleh ditambah [cache](https://en.wikipedia.org/wiki/Cache\_(computing)) seperti [Redis](https://redis.io/) bagi mempercepat capaian data yang kerap diminta.

## Gabungan Tindanan: LAMP, LEMP, WAMP, WIMP, FAMP & Lain-lain

Gabungan [tindanan web](https://en.wikipedia.org/wiki/Solution\_stack) ([sistem pengendalian](https://en.wikipedia.org/wiki/Operating\_system), pelayan web, pangkalan data dan bahasa pengaturcaraan) membentuk stack. Ini hanyalah contoh biasa, bukan piawaian wajib.

| Singkatan | Bentuk Penuh | Keterangan |
|---|---|---|
| **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)** | *Linux, Apache, MySQL/MariaDB, PHP/Perl/Python* | Tindanan klasik, paling sesuai untuk pemula. |
| **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** | *Linux, Nginx, MySQL/MariaDB, PHP-FPM* | Variasi LAMP menggunakan [Nginx](https://nginx.org/) dengan [PHP-FPM](https://www.php.net/manual/en/install.fpm.php). |
| **[WAMP](https://www.oreilly.com/library/view/learning-php-mysql/9780596157135/ch01.html)** | *Windows, Apache, MySQL/MariaDB, PHP* | Sesuai untuk pembangunan tempatan pada [Windows](https://www.microsoft.com/windows). |
| **[WIMP](https://www.itmedia.co.jp/enterprise/articles/0903/17/news004.html)** | *Windows, IIS, MySQL/MariaDB, PHP* | Menggunakan [IIS](https://www.iis.net/) berbanding Apache. Perlu diingat, "WIMP" turut mempunyai maksud lain dalam bidang antara muka pengguna. |
| **[FAMP](https://en.wikipedia.org/wiki/FAMP)** | *FreeBSD, Apache, MySQL/MariaDB, PHP* | Berasaskan [FreeBSD](https://www.freebsd.org/). Kurang biasa untuk pemula. |
| **[LAPP](https://www.x386.org/guides/lapp/)** | *Linux, Apache, PostgreSQL, PHP* | Variasi LAMP yang menukar MySQL/MariaDB kepada [PostgreSQL](https://www.postgresql.org/). |
| **[LEPP](https://lempstack.com/)** | *Linux, Nginx, PostgreSQL, PHP* | Variasi Nginx + PostgreSQL. Singkatan ini kurang biasa berbanding LAMP/LEMP dan tidak mempunyai definisi baku yang universal. Perlu diingat, "WIMP" turut mempunyai maksud lain dalam konteks UI/komputasi. |

> **Nota:** MySQL boleh digantikan dengan [MariaDB](https://mariadb.org/), pangkalan data lain boleh digunakan, dan PHP boleh digantikan dengan runtime seperti [Node.js](https://nodejs.org/) atau [Python](https://www.python.org/).

## Bare Metal, VM atau Kontena?

| Kaedah | Penjelasan | Rujukan | Catatan |
|---|---|---|---|
| **[Bare Metal](https://en.wikipedia.org/wiki/Bare\_machine)** | Berjalan terus pada perkakasan fizikal. | [IBM — Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers) | Memberi akses terus kepada perkakasan, prestasinya bergantung pada spesifikasi dan konfigurasi. |
| **[Mesin Maya (VM)](https://en.wikipedia.org/wiki/Virtual\_machine)** | Komputer maya di atas hos melalui hypervisor. | [KVM](https://www.linux-kvm.org/), [VirtualBox](https://www.virtualbox.org/), [VMware](https://www.vmware.com/) | **Paling sesuai untuk belajar**. Boleh snapshot dan tetapkan semula dengan mudah. |
| **[Kontena](https://en.wikipedia.org/wiki/Containerization\_(computing))** | Pengasingan aplikasi tanpa perlu OS penuh. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) | Ringan, pantas, jimat sumber. Sesuai untuk makmal tempatan. |

## Kelebihan, Kekurangan & SPOF

| Aspek | Penjelasan |
|---|---|
| **Kelebihan** | Mudah, kos rendah, ringkas, semua terpusat, ideal untuk belajar. |
| **Kekurangan** | Berkongsi sumber, konfigurasi boleh bercampur, skalabiliti terhad. |
| **[SPOF (Single Point of Failure)](https://en.wikipedia.org/wiki/Single\_point\_of\_failure)** | Jika mesin ini rosak, **pelayan web, masa jalan aplikasi dan pangkalan data turut terjejas**. Aplikasi tidak boleh diakses. |

## Bila Sesuai & Bila Perlu Beralih

| Keadaan | Penilaian | Nota |
|---|---|---|
| **Belajar, latihan, prototaip** | **Sangat sesuai** | Sesuai untuk memahami perkaitan antara komponen. |
| **Projek peribadi kecil** | **Masih mencukupi** | Elok jika kemas, dipantau dan disandarkan. |
| **Trafik semakin bertambah** | **Perlu pertimbangkan** | Sumber boleh mula tidak mencukupi, terutamanya pangkalan data. |
| **Perlu masa aktif tinggi / berskala besar** | **Perlu dipertimbangkan untuk beralih** | Tindanan satu-tingkat masih boleh dioptimumkan. Pengasingan lapisan perlu dipertimbangkan berdasarkan keperluan ketersediaan, kapasiti dan senibina. |

## Tips Untuk Bermula

1. **Fokus pada aliran** — Kuasai `pelayar → pelayan web → masa jalan aplikasi → pangkalan data`.
2. **Pilih SATU tindanan** — Mulakan dengan **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** atau **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)**. Kuasai satu dahulu.
3. **Latihan secara tempatan** — Guna [VM](https://en.wikipedia.org/wiki/Virtual\_machine) atau [kontena](https://en.wikipedia.org/wiki/Containerization\_(computing)) di komputer anda, gunakan `localhost`.
4. **Ingat SPOF** — Sesuai untuk belajar, bukan untuk aplikasi yang perlu sentiasa aktif.

**Intinya:** *Satu pelayan, semua komponen. Ringkas untuk dipelajari, terhad untuk diskalakan. Kuasai ini dahulu bagi memahami kenapa perlu mengasingkan komponen kelak.*
