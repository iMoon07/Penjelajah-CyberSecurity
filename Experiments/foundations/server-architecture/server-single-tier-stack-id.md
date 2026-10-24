# Server Single-Tier Stack

[🇬🇧 Read in English](server-single-tier-stack-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](server-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](server-single-tier-stack-tl.md)

![Server Single-Tier Stack](single-tier-stack.png)

## Satu Server, Satu Tumpukan

**Server Single-Tier Stack** artinya [web server](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server), [runtime aplikasi](https://en.wikipedia.org/wiki/Runtime\_system), dan [database](https://en.wikipedia.org/wiki/Database) semua berjalan di **satu mesin yang sama**.

Bayangin warung makan satu atap. Kasir, dapur, dan gudang bahan ada di bangunan yang sama. Pesanan langsung diproses di sana tanpa harus dikirim ke bangunan lain.

Semua komponen ini bekerja bersama di satu server agar alurnya lebih mudah dipahami.

## Alurnya Gimana?

Saat ada pengunjung membuka websitemu lewat [browser](https://en.wikipedia.org/wiki/Web\_browser), ini yang terjadi:

1. **Browser** → Mengirim [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) ke server
2. **Web Server** → Menerima dan mengarahkan permintaan ke aplikasi
3. **Runtime Aplikasi** → Menjalankan [logika bisnis](https://en.wikipedia.org/wiki/Business\_logic) aplikasimu (form, login, validasi, dll)
4. **Database** → Mencari, menambah, mengubah, atau menghapus data yang dibutuhkan
5. **Balasan** → Web server mengembalikan [HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) berupa halaman web, file, atau [JSON](https://www.json.org/) ke browser

Semua ini terjadi di **satu mesin yang sama**.

## Komponen Inti

| Komponen | Fungsi | Contoh |
|---|---|---|
| **[Web Server](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server)** | Pintu masuk. Menerima permintaan, mengarahkan, dan mengembalikan respon. | [Nginx](https://nginx.org/), [Apache HTTP Server](https://httpd.apache.org/), [Caddy](https://caddyserver.com/) |
| **[Runtime Aplikasi](https://en.wikipedia.org/wiki/Runtime\_system)** | Otak. Menjalankan kode aplikasimu. | [PHP-FPM](https://www.php.net/manual/en/install.fpm.php), [Node.js](https://nodejs.org/), [Gunicorn](https://gunicorn.org/), [Kestrel (.NET)](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel) |
| **[Database](https://en.wikipedia.org/wiki/Database)** | Gudang data. Menyimpan dan mengelola data aplikasi. | [MariaDB](https://mariadb.org/), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), [SQLite](https://sqlite.org/) |

Bisa ditambah [cache](https://en.wikipedia.org/wiki/Cache\_(computing)) seperti [Redis](https://redis.io/) untuk mempercepat akses data yang sering diminta.

## Kombinasi Stack: LAMP, LEMP, WAMP, WIMP, FAMP & Lainnya

Kombinasi [sistem operasi](https://en.wikipedia.org/wiki/Operating\_system), [web server](https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Web\_mechanics/What\_is\_a\_web\_server), [database](https://en.wikipedia.org/wiki/Database), dan [bahasa pemrograman](https://en.wikipedia.org/wiki/Programming\_language) membentuk sebuah [solution stack](https://en.wikipedia.org/wiki/Solution\_stack). Ini hanya contoh kombinasi yang umum, bukan standar wajib.

| Singkatan | Kepanjangan | Keterangan |
|---|---|---|
| **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)** | *Linux, Apache, MySQL/MariaDB, PHP/Perl/Python* | Stack klasik yang paling umum dipelajari untuk aplikasi web dinamis. |
| **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** | *Linux, Nginx, MySQL/MariaDB, PHP-FPM* | Variasi LAMP dengan [Nginx](https://nginx.org/) sebagai web server dan [PHP-FPM](https://www.php.net/manual/en/install.fpm.php) untuk menjalankan PHP. |
| **[WAMP](https://www.oreilly.com/library/view/learning-php-mysql/9780596157135/ch01.html)** | *Windows, Apache, MySQL/MariaDB, PHP* | Cocok untuk pengembangan lokal di [Windows](https://www.microsoft.com/windows). |
| **[WIMP](https://www.itmedia.co.jp/enterprise/articles/0903/17/news004.html)** | *Windows, IIS, MySQL/MariaDB, PHP* | Menggunakan [IIS](https://www.iis.net/) sebagai pengganti Apache. Perlu diingat, istilah *WIMP* juga punya arti lain di bidang antarmuka pengguna. |
| **[FAMP](https://en.wikipedia.org/wiki/FAMP)** | *FreeBSD, Apache, MySQL/MariaDB, PHP* | Variasi berbasis [FreeBSD](https://www.freebsd.org/). Kurang umum dibanding LAMP/LEMP. |
| **[LAPP](https://www.x386.org/guides/lapp/)** | *Linux, Apache, PostgreSQL, PHP* | Variasi LAMP yang mengganti MySQL/MariaDB dengan [PostgreSQL](https://www.postgresql.org/). |
| **[LEPP](https://lempstack.com/)** | *Linux, Nginx, PostgreSQL, PHP* | Variasi berbasis Nginx dan PostgreSQL. Istilah ini tidak sepopuler LAMP/LEMP dan tidak selalu memiliki definisi baku di semua sumber. Perlu dicatat juga bahwa istilah *WIMP* memiliki arti lain di bidang antarmuka pengguna/komputasi. |

> **Catatan:** MySQL bisa diganti [MariaDB](https://mariadb.org/), PostgreSQL bisa diganti database lain, dan PHP bisa diganti runtime seperti Node.js atau Python sesuai kebutuhan aplikasi.

## Bare Metal, VM, atau Container?

| Cara | Penjelasan | Referensi | Keterangan |
|---|---|---|---|
| **[Bare Metal](https://en.wikipedia.org/wiki/Bare\_machine)** | Sistem operasi berjalan langsung di hardware fisik. | [IBM — Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers) | Memberikan akses langsung ke hardware, dengan performa yang bergantung pada spesifikasi dan konfigurasi. |
| **[Virtual Machine (VM)](https://en.wikipedia.org/wiki/Virtual\_machine)** | Komputer virtual yang berjalan di atas host lewat hypervisor. | [KVM](https://www.linux-kvm.org/), [VirtualBox](https://www.virtualbox.org/), [VMware](https://www.vmware.com/) | **Paling cocok buat belajar**. Bisa di-snapshot, mudah di-reset. |
| **[Container](https://en.wikipedia.org/wiki/Containerization\_(computing))** | Aplikasi diisolasi, tapi tetap memakai kernel host. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) | Sangat ringan, cepat dibuat ulang, hemat resource. |

## Kelebihan, Kekurangan & SPOF

| Aspek | Penjelasan |
|---|---|
| **Kelebihan** | Simpel, murah, gampang dipahami, semua terpusat, ideal buat belajar. |
| **Kekurangan** | Saling berebut resource, konfigurasi bisa campur, skalabilitas terbatas. |
| **[SPOF (Single Point of Failure)](https://en.wikipedia.org/wiki/Single\_point\_of\_failure)** | Kalau mesin ini mati, **web server, runtime aplikasi, dan database ikut mati**. Aplikasi jadi tidak bisa diakses sama sekali. |

## Kapan Cocok & Kapan Harus Pindah

| Kondisi | Status | Keterangan |
|---|---|---|
| **Belajar, latihan, prototipe** | **Cocok** | Cocok untuk memahami hubungan antar-komponen. |
| **Proyek kecil/pribadi** | **Masih cukup** | Aman asal rapi, dipantau, dan di-backup. |
| **Trafik mulai naik signifikan** | **Perlu dipertimbangkan untuk dipisah** | Resource bisa mulai kewalahan, terutama database. |
| **Butuh uptime tinggi / skala besar** | **Perlu dipertimbangkan untuk dipisah** | Single-tier masih bisa dioptimalkan. Pemisahan tier dipertimbangkan berdasarkan kebutuhan ketersediaan, kapasitas, dan arsitektur. |

## Tips Buat Mulai

1. **Fokus ke alurnya** — Kuasai `browser → web server → runtime → database`.
2. **Pilih SATU stack** — Mulai dari **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** atau **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)**. Kuasai satu dulu baru coba yang lain.
3. **Praktek lokal** — Pakai [VM](https://en.wikipedia.org/wiki/Virtual\_machine) atau [container](https://en.wikipedia.org/wiki/Containerization\_(computing)) di laptop kamu, cukup pakai `localhost`.
4. **Ingat SPOF** — Single-Tier simpel buat belajar, bukan solusi buat aplikasi yang wajib selalu online.

**Intinya:** *Single-Tier = semua di satu server. Simpel buat dipelajari, terbatas buat diskalakan. Kuasai yang simpel dulu, baru paham kenapa harus dipisah.*
