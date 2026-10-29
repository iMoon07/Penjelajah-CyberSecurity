# Tindanan Pelayan Satu-Tingkat: Memahami Komponen, Teknologi, dan Pelaksanaan

[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)
[🇬🇧 Read in English](server-single-tier-stack-en.md)
[🇵🇭 Basahin sa Tagalog](server-single-tier-stack-tl.md)

## Satu Pelayan, Satu Tindanan

﷽

![Server Single-Tier Stack: Memahami Komponen, Teknologi, dan Deployment](single-tier-stack.png)

**Tindanan pelayan satu-tingkat** merujuk kepada seni bina di mana [pelayan web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [masa jalan aplikasi](https://en.wikipedia.org/wiki/Runtime_system), dan [pangkalan data](https://en.wikipedia.org/wiki/Database) kesemuanya dijalankan pada **satu mesin yang sama**.

Bayangkan sebuah gerai makan kecil di mana dapur, ruang makan, dan tempat penyimpanan kesemuanya terletak di satu lokasi. Pelanggan membuat pesanan, tukang masak menyediakan hidangan, dan makanan terus dihidangkan. Segala urusan berlaku di tempat yang sama.

Konsep ini serupa dengan **tindanan satu-tingkat**: komponen utama sesebuah aplikasi—iaitu pelayan web, masa jalan aplikasi, dan pangkalan data—disediakan bersama dan dihidangkan kepada pengguna, sama seperti hidangan disediakan dari dapur tersebut.

Namun, bagaimanakah proses ini berlaku apabila pelawat mengakses laman web yang dibina menggunakan tindanan satu-tingkat?

## Aliran Kerja

```mermaid
flowchart TD
    C["🧑‍🦱 Pelanggan<br/>Membuat pesanan"] -->|"1. Pesanan dihantar<br/>sebagai Permintaan HTTP"| P["🧑‍🍳 Pelayan<br/>Menerima pesanan dan mengemudikannya"]
    P -->|"2. Pesanan dihantar<br/>ke dapur"| K["👨‍🍳 Tukang Masak<br/>Menyediakan pesanan"]
    K -->|"3. Mengambil bahan<br/>jika diperlukan"| G["🥫 Pantri<br/>Menyimpan bahan-bahan"]
    G -->|"4. Bahan dihantar<br/>kepada tukang masak"| K
    K -->|"5. Hidangan dihidangkan<br/>kepada pelayan"| P
    P -->|"6. Hidangan dihantar<br/>kepada pelanggan<br/>sebagai Respons HTTP"| C

    subgraph W["Gerai Makan / Satu Lokasi"]
        P
        K
        G
    end
```

## Komponen Teras

Marilah kita mengenali komponen-komponen utama serta peranan masing-masing dalam persekitaran pelayan.

Seperti gerai makan, tidak setiap premis mendedahkan secara terbuka butiran penuh proses di dapurnya. Namun, melalui pengalaman langsung atau dengan mempelajari cara masakan di dapur tersebut, seseorang akan mengetahui dengan tepat bahan dan kaedah yang digunakan.

Begitu juga dalam seni bina pelayan. Berikut merupakan komponen teras yang lazim ditemui dalam tindanan satu-tingkat:

| Komponen | Fungsi |
| --- | --- |
| Sistem Pengendalian (OS) | Asas sistem. Mengurus perkakasan, ingatan, proses, dan sumber pelayan. |
| Klien Web | Aplikasi di pihak pengguna (cth., pelayar web) yang menghantar permintaan HTTP kepada pelayan dan memaparkan respons HTTP. |
| TLS (Transport Layer Security) | Protokol kriptografi yang melindungi komunikasi antara klien web dan pelayan melalui penyulitan, pengesahan pelayan, dan integriti data. SSL ialah pendahulunya yang kini sudah ditamatkan; laman web moden menggunakan TLS melalui HTTPS (biasanya port 443), disyorkan TLS 1.2 atau TLS 1.3. |
| Sijil TLS | Sijil digital daripada *Certificate Authority* (CA) yang dipercayai bagi membuktikan identiti pelayan. Pelayar mengesahkan rantaian kepercayaan, kesesuaian domain, dan tempoh sah; jika sah, sambungan HTTPS dipercayai dan ditandai dengan ikon kunci. |
| Masa Jalan Aplikasi | Melaksanakan kod aplikasi agar dapat diproses oleh pelayan. |
| Rangka Kerja Aplikasi | Menyediakan struktur dan ciri terbina bagi membangunkan aplikasi tanpa perlu membina segala-galanya dari awal. |
| Pangkalan Data | Menyimpan, menyusun, dan mendapatkan semula data yang diperlukan oleh aplikasi. |
| Cache (pilihan) | Menyimpan data yang kerap diakses secara sementara bagi meningkatkan prestasi. |

> *Nota:* Setiap aplikasi mungkin menggunakan gabungan komponen yang berbeza bergantung kepada keperluan. Komponen seperti sistem pengendalian, TLS, pelayan web, masa jalan aplikasi, rangka kerja, pangkalan data, dan cache boleh dipilih atau digantikan dengan alternatif yang sesuai mengikut seni bina yang dipilih.

## Gabungan Tindanan Teknologi

```mermaid
flowchart TD
    A["🍜 Tindanan Teknologi<br/>= Resipi dan bahan-bahan"] --> B{"Pilih bahan mengikut menu"}
    B --> C["🟨 JavaScript / TypeScript<br/>React, Node.js, MongoDB"]
    B --> D["🐘 PHP<br/>Laravel, LAMP, LEMP"]
    B --> E["🐍 Python<br/>Django, FastAPI, Flask"]
    B --> F["🔷 .NET<br/>ASP.NET Core, Blazor"]
    B --> G["☕ Java<br/>Spring Boot, Jakarta EE"]
    B --> H["💎 Ruby<br/>Ruby on Rails"]
    B --> I["🐹 Go<br/>Gin, Echo, Fiber"]
    B --> J["🦀 Rust<br/>Actix, Axum, Rocket"]
    B --> K["📊 Infrastruktur<br/>ELK, Prometheus + Grafana"]
    C --> L["🍽️ Aplikasi Web / API<br/>mengikut keperluan projek"]
    D --> L
    E --> L
    F --> L
    G --> L
    H --> L
    I --> L
    J --> L
    K --> L
```

Tindanan teknologi ibarat resipi beserta bahan-bahannya. Dalam bidang pengkomputeran, pilihan sistem pengendalian, pelayan web, bahasa pengaturcaraan, rangka kerja, dan pangkalan data membentuk susunan tersendiri yang dikenali sebagai [tindanan penyelesaian](https://en.wikipedia.org/wiki/Solution_stack).

Setiap tindanan mempunyai komposisi dan tujuan tersendiri, disesuaikan dengan keperluan aplikasi berkenaan. Berikut adalah beberapa tindanan teknologi yang paling lazim digunakan beserta komponen dan kegunaannya.

### 1. Tindanan JavaScript & TypeScript

Tindanan ini menggunakan JavaScript atau TypeScript bagi membina antara muka pengguna (bahagian hadapan) dan logik pelayan (bahagian belakang). Dengan Node.js, Bun, atau Deno, JavaScript boleh dijalankan di pelayan, justeru membolehkan satu bahasa merangkumi keseluruhan tindanan aplikasi.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [MEAN](https://www.mongodb.com/resources/languages/mean-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [Angular](https://angular.dev/), [Node.js](https://nodejs.org/) | Menggunakan Angular untuk bahagian hadapan SPA, Express.js sebagai rangka kerja bahagian belakang, Node.js sebagai masa jalan, dan MongoDB sebagai pangkalan data NoSQL. Sesuai untuk aplikasi perusahaan yang memerlukan struktur kukuh dan sokongan TypeScript terbina melalui Angular. |
| [MERN](https://www.mongodb.com/resources/languages/mern-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [React](https://react.dev/), [Node.js](https://nodejs.org/) | Menggunakan React untuk bahagian hadapan berasaskan komponen, Express.js untuk API bahagian belakang, Node.js sebagai masa jalan, dan MongoDB sebagai pangkalan data. Sangat popular untuk aplikasi web dan bahagian belakang mudah alih kerana fleksibiliti React serta ekosistem npm yang luas. |
| [MEVN](https://www.mongodb.com/resources/languages/mern-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [Vue.js](https://vuejs.org/), [Node.js](https://nodejs.org/) | Menggunakan Vue.js sebagai rangka kerja hadapan progresif, Express.js untuk bahagian belakang, Node.js sebagai masa jalan, dan MongoDB sebagai pangkalan data. Dikenali ringan, mudah dipelajari, dan mempunyai kereaktifan yang sesuai untuk aplikasi berskala sederhana. |
| [PERN](https://www.digitalocean.com/community/tutorials/how-to-build-a-pern-stack-application) | [PostgreSQL](https://www.postgresql.org/), [Express.js](https://expressjs.com/), [React](https://react.dev/), [Node.js](https://nodejs.org/) | Menggantikan MongoDB dengan PostgreSQL sebagai pangkalan data hubungan (mematuhi ACID), sambil mengekalkan React, Express.js, dan Node.js. Sesuai untuk aplikasi yang menuntut integriti data, pertanyaan kompleks, dan hubungan jadual yang ketat. |
| [Next.js Stack](https://nextjs.org/) | [Next.js](https://nextjs.org/), [React](https://react.dev/), [Node.js](https://nodejs.org/), PostgreSQL atau MySQL | Rangka kerja React yang menyokong Penjanaan Laman Secara Pelayan (SSR), Penjanaan Laman Statik (SSG), dan laluan API dalam satu projek. Sesuai untuk aplikasi berorientasikan SEO, muat turun halaman pantas, dan pembangunan penuh tindanan dalam repositori tunggal. |
| [T3 Stack](https://create.t3.gg/) | [TypeScript](https://www.typescriptlang.org/), [Tailwind CSS](https://tailwindcss.com/), [tRPC](https://trpc.io/), [Next.js](https://nextjs.org/), [Prisma](https://www.prisma.io/), [PostgreSQL](https://www.postgresql.org/) | Tindanan TypeScript penuh yang menguatkuasakan keselamatan jenis hujung ke hujung dari pangkalan data hingga bahagian hadapan. tRPC menghapuskan keperluan untuk membina API REST secara manual, Prisma menyediakan ORM berkeselamatan jenis, dan Tailwind mengendalikan penggayaan. Sesuai untuk pasukan yang mengutamakan keselamatan jenis dan pembangunan pantas. |
| [JAMstack](https://jamstack.org/what-is-jamstack/) | JavaScript, API, Penanda | Pendekatan seni bina yang memisahkan penanda bahagian hadapan daripada bahagian belakang. JavaScript dijalankan di klien, data diperoleh melalui API, dan penanda dibina terlebih dahulu semasa masa binaan. Sesuai untuk laman kandungan, e-dagang statik, serta aplikasi yang memerlukan keselamatan dan kebolehskalaan tinggi tanpa pelayan tradisional. |
| [Bun Stack](https://bun.sh/) | [Bun](https://bun.sh/), [Elysia](https://elysiajs.com/) atau [Hono](https://hono.dev/), SQLite atau PostgreSQL, React atau Vue | Menggunakan Bun sebagai masa jalan JavaScript bagi menggantikan Node.js dengan permulaan lebih pantas dan penggunaan ingatan lebih rendah. Digandingkan dengan rangka kerja ringan seperti Elysia atau Hono serta pangkalan data hubungan. Sesuai untuk mikroperkhidmatan, tanpa pelayan, dan aplikasi sensitif terhadap kependaman atau sumber. Ekosistemnya masih lebih muda berbanding Node.js. |

### 2. Tindanan PHP

Tindanan berasaskan PHP lazim digunakan untuk pembangunan web, biasanya dijalankan di pelayan bersama pelayan web dan pangkalan data hubungan.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Laravel](https://laravel.com/) | [PHP](https://www.php.net/), [Laravel](https://laravel.com/docs), MySQL atau PostgreSQL, Nginx atau Apache | Rangka kerja PHP moden yang menawarkan penghalaan, pengesahan, Eloquent ORM, templat Blade, dan pelbagai ciri lain. Sesuai untuk aplikasi web berskala kecil hingga besar dengan pembangunan tersusun dan dokumentasi luas. |
| [Symfony](https://symfony.com/) | [PHP](https://www.php.net/), [Symfony](https://symfony.com/doc/current/index.html), pelbagai pangkalan data, Nginx atau Apache | Set komponen PHP modular dan boleh digunakan semula, serta menjadi asas kepada banyak rangka kerja lain termasuk Laravel. Sangat fleksibel untuk aplikasi perusahaan berskala besar yang memerlukan kawalan penuh terhadap seni bina. |
| [LAMP](https://cloud.google.com/mysql/lamp) | [Linux](https://www.kernel.org/), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | Tindanan klasik untuk aplikasi web dinamik. Linux sebagai sistem pengendalian, Apache sebagai pelayan web, MySQL/MariaDB sebagai pangkalan data, dan PHP sebagai bahasa pengaturcaraan. Banyak disokong oleh pembekal pengehosan dan mudah dilaksanakan. |
| [LEMP](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-ubuntu-22-04) | [Linux](https://www.kernel.org/), [Nginx](https://nginx.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | Varian LAMP yang menggantikan Apache dengan Nginx. Nginx lebih cekap dalam menangani sambungan serentak dan kandungan statik, menjadikannya sesuai untuk aplikasi bertrafik tinggi atau yang memerlukan prestasi pelayan web lebih baik. |
| [WAMP](https://en.wikipedia.org/wiki/WAMP) | [Windows](https://www.microsoft.com/windows), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | Tindanan berasaskan Windows untuk pembangunan dan pengehosan aplikasi web PHP. Sesuai untuk persekitaran yang menggunakan infrastruktur Microsoft. |
| [WIMP](https://learn.microsoft.com/en-us/iis/) | [Windows](https://www.microsoft.com/windows), [IIS](https://www.iis.net/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | Tindanan berasaskan Windows menggunakan IIS sebagai pelayan web menggantikan Apache. Sesuai untuk organisasi yang berintegrasi dengan ekosistem Microsoft dan ingin menjalankan PHP di Windows Server. |
| [FAMP](https://en.wikipedia.org/wiki/FAMP) | [FreeBSD](https://www.freebsd.org/), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | Varian LAMP menggunakan FreeBSD sebagai sistem pengendalian. Dikenali stabil, selamat, dan cekap dalam rangkaian, sesuai untuk pelayan yang mengutamakan keteguhan sistem pengendalian berasaskan BSD. |
| [XAMPP](https://www.apachefriends.org/) | Pelbagai platform, [Apache](https://httpd.apache.org/), [MariaDB](https://mariadb.org/) or [MySQL](https://mariadb.org/), [PHP](https://www.php.net/), [Perl](https://www.perl.org/) | Pakej pembangunan web serba lengkap yang mudah dipasang di Windows, Linux, dan macOS. Utamanya digunakan untuk pembelajaran dan prototaip tempatan sebelum dilaksanakan ke pelayan pengeluaran. |

### 3. Tindanan Python

Tindanan berasaskan Python untuk pembangunan web, dari rangka kerja mikro hingga rangka kerja penuh yang kaya dengan ciri terbina.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Django](https://www.djangoproject.com/) | [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), PostgreSQL atau MySQL, Nginx atau Apache, Gunicorn | Rangka kerja "lengkap terbina" yang menawarkan panel pentadbir, pengesahan, ORM, dan ciri keselamatan kukuh secara lalai. Sesuai untuk aplikasi web berskala besar yang memerlukan pembangunan pantas dan piawaian keselamatan tinggi. |
| [FastAPI](https://fastapi.tiangolo.com/) | [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), PostgreSQL atau MySQL, Nginx, Uvicorn | Rangka kerja API moden dengan pengesahan data automatik melalui Pydantic dan dokumentasi interaktif Swagger/OpenAPI. Berprestasi tinggi dengan sokongan async, sesuai untuk mikroperkhidmatan dan API pembelajaran mesin. |
| [Flask](https://flask.palletsprojects.com/) | [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/), pelbagai pangkalan data, Nginx atau Apache, Gunicorn | Rangka kerja mikro ringan dan fleksibel yang memberi kawalan penuh kepada pembangun tanpa mengenakan struktur tetap. Sesuai untuk aplikasi kecil, prototaip, atau perkhidmatan yang memerlukan penyesuaian maksimum. |
| [Pyramid](https://trypyramid.com/) | [Python](https://www.python.org/), [Pyramid](https://trypyramid.com/), pelbagai pangkalan data | Rangka kerja fleksibel yang boleh diskalakan dari aplikasi kecil hingga besar. Membolehkan pembangun memilih komponen mengikut keperluan dan sesuai untuk projek yang berkembang secara beransur-ansur. |

### 4. Tindanan .NET

Berasaskan bahasa C# dan ekosistem .NET, tindanan ini digunakan untuk membina aplikasi web, API, dan perkhidmatan bahagian belakang.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | [C#](https://learn.microsoft.com/en-us/dotnet/csharp/), [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/), SQL Server atau PostgreSQL, IIS atau Nginx | Rangka kerja berprestasi tinggi dan merentas platform dari Microsoft untuk membina aplikasi web, API REST, dan perkhidmatan bahagian belakang. Berjalan pada Windows, Linux, dan macOS, sesuai untuk persekitaran perusahaan dalam ekosistem Microsoft. |
| [Blazor Stack](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor) | [C#](https://learn.microsoft.com/en-us/dotnet/csharp/), [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor), [.NET](https://dotnet.microsoft.com/), SQL Server atau PostgreSQL | Membolehkan antara muka web interaktif menggunakan C# berbanding JavaScript, melalui Blazor WebAssembly (sebelah klien) atau Blazor Server (sebelah pelayan). Sesuai untuk pasukan .NET yang ingin membina bahagian hadapan kaya tanpa bergantung sepenuhnya kepada JavaScript. |

### 5. Tindanan Java

Tindanan berasaskan Java, lazim digunakan untuk sistem bahagian belakang berskala dan aplikasi bertaraf perusahaan.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Java-Spring](https://spring.io/projects/spring-boot) | [Java](https://dev.java/), [Spring Boot](https://spring.io/projects/spring-boot), pelbagai pangkalan data, Tomcat | Rangka kerja Java paling popular untuk membina bahagian belakang dan mikroperkhidmatan. Spring Boot memudahkan konfigurasi serta menyediakan ciri sedia pengeluaran seperti semakan kesihatan, metrik, dan konfigurasi luaran. |
| [Jakarta EE](https://jakarta.ee/) | [Java](https://dev.java/), [Jakarta EE](https://jakarta.ee/), pelbagai pangkalan data, pelayan aplikasi | Piawaian Java perusahaan terbuka untuk aplikasi berskala besar, merangkumi web, Enterprise Bean, dan pemesejan. Lazim digunakan dalam sektor perbankan, telekomunikasi, dan sektor awam yang memerlukan piawaian terbuka. |
| [Quarkus](https://quarkus.io/) | [Java](https://dev.java/), [Quarkus](https://quarkus.io/), pelbagai pangkalan data | Rangka kerja Java dioptimumkan untuk Kubernetes dan persekitaran tanpa pelayan, menawarkan permulaan pantas dan penggunaan ingatan rendah. Sesuai untuk mikroperkhidmatan asli awan, terutamanya apabila dikompilasi ke imej asli GraalVM. |

### 6. Tindanan Ruby

Tindanan berpusatkan Ruby, dikenali dengan konvensyen kuat dan penekanan terhadap pembangunan web pantas.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Ruby on Rails](https://rubyonrails.org/) | [Ruby](https://www.ruby-lang.org/), [Rails](https://guides.rubyonrails.org/getting_started.html), PostgreSQL atau MySQL, Puma atau Unicorn | Rangka kerja penuh tindanan yang mengikut prinsip "Konvensyen berbanding Konfigurasi". Menyediakan migrasi pangkalan data, pembinaan rangka, saluran aset, dan pelbagai ciri lain secara lalai. Sesuai untuk syarikat pemula dan MVP yang memerlukan pembangunan pada kelajuan tinggi. |
| [Sinatra](https://sinatrarb.com/) | [Ruby](https://www.ruby-lang.org/), [Sinatra](https://sinatrarb.com/), pelbagai pangkalan data | Rangka kerja mikro Ruby yang minimal dan ringan. Sesuai untuk membina perkhidmatan ringkas, API kecil, atau aplikasi yang tidak memerlukan struktur penuh Rails. |

### 7. Tindanan Go

Tindanan berasaskan Go (Golang), direka untuk bahagian belakang, API, dan mikroperkhidmatan berprestasi tinggi.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Gin](https://gin-gonic.com/) | [Go](https://go.dev/), [Gin](https://gin-gonic.com/), pelbagai pangkalan data | Rangka kerja web Go yang pantas dan ringan, serupa dengan Express.js. Sesuai untuk membina API REST dan mikroperkhidmatan dengan prestasi tinggi serta kompilasi pantas. |
| [Echo](https://echo.labstack.com/) | [Go](https://go.dev/), [Echo](https://echo.labstack.com/), pelbagai pangkalan data | Rangka kerja Go berprestasi tinggi dengan ciri lengkap seperti perantara, penghalaan, dan pengesahan. Dikenali cekap dari segi penggunaan ingatan dan sesuai untuk aplikasi berkelajuan tinggi. |
| [Fiber](https://docs.gofiber.io/) | [Go](https://go.dev/), [Fiber](https://docs.gofiber.io/), pelbagai pangkalan data | Diilhamkan oleh Express.js dan dibina di atas Fasthttp, Fiber sangat pantas dan ringan. Sesuai untuk mikroperkhidmatan dan aplikasi yang memerlukan kependaman rendah serta penggunaan sumber minimum. |
| [Perpustakaan Piawai Go](https://go.dev/) | [Go](https://go.dev/), `net/http`, pelbagai pangkalan data | Pendekatan tanpa rangka kerja luaran menggunakan perpustakaan piawai terbina dalam Go. Menawarkan kawalan maksimum, pergantungan minimum, dan sesuai untuk aplikasi ringan tanpa beban rangka kerja. |

### 8. Tindanan Rust

Tindanan berasaskan Rust, mengutamakan keselamatan ingatan, keserentakan, dan prestasi peringkat sistem.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Actix Web](https://actix.rs/) | [Rust](https://www.rust-lang.org/), [Actix Web](https://actix.rs/), pelbagai pangkalan data | Salah satu rangka kerja web Rust terpantas, dibina berdasarkan model pelakon. Sesuai untuk aplikasi yang memerlukan keselamatan ingatan, keserentakan tinggi, dan prestasi maksimum tanpa pengumpul sampah. |
| [Axum](https://github.com/tokio-rs/axum) | [Rust](https://www.rust-lang.org/), [Axum](https://github.com/tokio-rs/axum), [Tokio](https://tokio.rs/), pelbagai pangkalan data | Rangka kerja web modular dan berkeselamatan jenis dari ekosistem Tokio. Memanfaatkan async/await terbina dalam Rust dan sesuai untuk membina API async yang cekap serta mudah diselenggara. |
| [Rocket](https://rocket.rs/) | [Rust](https://www.rust-lang.org/), [Rocket](https://rocket.rs/), pelbagai pangkalan data | Rangka kerja Rust mesra pembangun yang mengutamakan kebolehgunaan. Menawarkan ciri seperti templat, pengendalian borang, dan integrasi pangkalan data dengan sintaks deklaratif yang bersih. |

### 9. Infrastruktur dan Kebolehcerapan

Tindanan yang menggabungkan sistem pengendalian, pelayan web, pangkalan data, atau alatan sokongan untuk pengurusan infrastruktur dan kebolehcerapan aplikasi.

| Tindanan | Komponen Utama | Keterangan |
| --- | --- | --- |
| [Wazuh](https://wazuh.com/) | [Wazuh Server](https://documentation.wazuh.com/current/) (pengurus, pengindeks, papan pemuka), [Wazuh Agent](https://documentation.wazuh.com/current/), [Elasticsearch](https://www.elastic.co/elasticsearch) atau [OpenSearch](https://opensearch.org/) (pilihan), [Kibana](https://www.elastic.co/kibana) atau [Wazuh Dashboard](https://documentation.wazuh.com/current/) (pilihan) | Platform sumber terbuka untuk pengesanan pencerobohan, pemantauan keselamatan (XDR/SIEM), analisis log, pemantauan integriti fail, dan tindak balas terhadap ancaman. Sesuai untuk pemantauan keselamatan berpusat merentas pelayan dan titik akhir. |
| [Tindanan Elastic (ELK)](https://www.elastic.co/elastic-stack) | [Elasticsearch](https://www.elastic.co/elasticsearch), [Logstash](https://www.elastic.co/logstash), [Kibana](https://www.elastic.co/kibana) | Digunakan untuk mengumpul, mencari, menganalisis, dan memvisualisasikan log serta metrik sistem. Sesuai untuk pemantauan, penyelesaian masalah, dan Pengurusan Maklumat Keselamatan dan Acara (SIEM). |
| [Prometheus + Grafana](https://prometheus.io/) | [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), pengeksport pelbagai | Tindanan pemantauan sumber terbuka yang mengumpul metrik siri masa dari sistem dan aplikasi, kemudian memvisualisasikannya melalui papan pemuka Grafana. Sesuai untuk pemantauan infrastruktur dan amaran. |
| [Tindanan TICK](https://docs.influxdata.com/influxdb/v2/get-started/) | [Telegraf](https://docs.influxdata.com/telegraf/), [InfluxDB](https://www.influxdata.com/products/influxdb/), [Chronograf](https://docs.influxdata.com/chronograf/), [Kapacitor](https://docs.influxdata.com/kapacitor/) | Tindanan untuk mengumpul, menyimpan, memvisualisasikan, dan memproses data siri masa. Lazim digunakan untuk pemantauan infrastruktur, IoT, dan penjejakan metrik aplikasi dari semasa ke semasa. |

> *Nota:* Memilih bahan yang betul menghasilkan hidangan lazat yang menarik pelanggan kembali. Namun, setiap pilihan melibatkan pertukaran—begitu juga dengan tindanan teknologi. Senarai ini bukanlah lengkap atau wajib; komponen dalam sesuatu tindanan boleh digantikan bagi memenuhi keperluan tertentu.

## Di Mana Untuk Menjalankan Tindanan?

Setelah memilih tindanan teknologi, langkah seterusnya ialah menentukan *di mana* ia akan dijalankan dan bagaimana infrastrukturnya diurus. Ini dikenali sebagai **persekitaran pelaksanaan**.

```mermaid
flowchart TD
    A["🍜 Tindanan sedia<br/>resipi + bahan-bahan + alatan"] --> B{"📍 Di mana untuk dijalankan?"}
    B --> C["🏠 Logam Kosong (Bare Metal)<br/>Bina gerai sendiri"]
    B --> D["🛏️ Mesin Maya (VM)<br/>Sewa bilik persendirian"]
    B --> E["🍱 Bekas (Container)<br/>Sewa gerai di medan selera"]
    B --> F["🏪 PaaS<br/>Sertai francais sedia guna"]
    B --> G["🛒 Tanpa Pelayan (Serverless)<br/>Buka gerai hanya apabila ada pesanan"]
    B --> H["🛵 Pengkomputeran Tepi (Edge)<br/>Gerai makanan berhampiran pelanggan"]
    C --> I["🧩 Semua komponen tindanan<br/>berjalan di satu tempat"]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
```

Bayangkan anda telah mengumpul resipi, bahan-bahan, dan alatan untuk membuka gerai makan. Kini anda perlu menentukan lokasi operasi: bina premis sendiri, sewa ruang, kongsi kemudahan bersama peniaga lain, atau buka gerai sementara mengikut keperluan.

Dari sudut pelayan, pilihan ini mempunyai analogi yang serupa:

| Persekitaran | Analogi Gerai Makan | Keterangan | Contoh |
| --- | --- | --- | --- |
| **Logam Kosong / Pelayan Berdedikasi** | Bina gerai di atas tanah milik sendiri. Anda mempunyai kawalan penuh ke atas segala-galanya, dari dinding hingga dapur. | Sistem pengendalian dan aplikasi berjalan terus pada perkakasan fizikal tanpa hipervisor. | [IBM Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers), [OVHcloud Dedicated Server](https://www.ovhcloud.com/en/bare-metal/) |
| **Mesin Maya (VM) - Desktop** | Sewa bilik persendirian di rumah tumpangan. Bilik anda sahaja, boleh ditetapkan semula bila-bila masa jika berlaku masalah. | Komputer maya dengan sistem pengendalian sendiri berjalan pada mesin peribadi anda. | [VirtualBox](https://www.virtualbox.org/), [VMware Workstation](https://www.vmware.com/products/workstation-pro.html), [VMware Fusion](https://www.vmware.com/products/fusion.html) |
| **Platform Virtualisasi Pelayan** | Pemilik rumah tumpangan mengurus berpuluh bilik dari pejabat pusat. | Mengurus pelbagai VM pada pelayan pengeluaran melalui antara muka berpusat. | [VMware vSphere / ESXi](https://www.vmware.com/products/vsphere.html), [Proxmox VE](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) |
| **Bekas (Container)** | Sewa gerai di medan selera. Kongsi kemudahan dapur, tetapi gerai anda diasingkan dan mudah dipindahkan. | Aplikasi berjalan dalam pakej terasing yang berkongsi inti sistem pengendalian hos. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) |
| **PaaS (Platform sebagai Perkhidmatan)** | Buka gerai francais sedia guna. Bawa resipi sahaja, kedai dan utiliti telah disediakan. | Pembekal mengurus infrastruktur; anda hanya perlu muat naik kod. | [Heroku](https://www.heroku.com/), [Render](https://render.com/), [Railway](https://railway.app/) |
| **Tanpa Pelayan / FaaS** | Gerai pop-up di acara. Hanya buka apabila ada pelanggan, tutup apabila sepi, dan bayar mengikut pesanan. | Kod berjalan mengikut permintaan tanpa pelayan yang diurus secara tetap. | [AWS Lambda](https://aws.amazon.com/lambda/), [Azure Functions](https://learn.microsoft.com/azure/azure-functions/), [Cloudflare Workers](https://workers.cloudflare.com/) |
| **Pengehosan Dikongsi** | Gerai di tepi jalan yang dikongsi ramai peniaga. Murah, tetapi sesak dan kawalan terhad. | Berbilang pengguna berkongsi sumber pelayan yang sama. | [cPanel](https://cpanel.net/), [Hostinger](https://www.hostinger.com/) |
| **Pengehosan Diurus** | Sewa kedai dengan pengurus yang mengendalikan operasi harian. | Pembekal mengurus sebahagian besar pengurusan pelayan dan operasinya. | [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) |
| **Pengkomputeran Tepi** | Gerai makanan bergerak berhampiran pelanggan bagi hidangan lebih pantas. | Pemprosesan dijalankan lebih dekat dengan pengguna bagi mengurangkan kependaman. | [Cloudflare Workers](https://workers.cloudflare.com/), [AWS Wavelength](https://aws.amazon.com/wavelength/) |

### Perbezaan Utama

- **VMware Workstation dan Fusion** adalah untuk virtualisasi desktop tempatan, sesuai untuk pembelajaran di rumah.
- **VMware ESXi/vSphere dan Proxmox VE** adalah untuk virtualisasi pelayan pengeluaran, sesuai untuk mengurus berbilang VM pada skala besar.
- **Logam Kosong** merujuk kepada perisian berjalan terus pada perkakasan fizikal. **Pelayan Berdedikasi** merujuk kepada pelayan fizikal yang disewa untuk seorang pelanggan sahaja. Kedua-duanya sering digunakan bersama tetapi tidak sinonim.

### Hubungan dengan Tindanan Satu-Tingkat

Seni bina **satu-tingkat** bermaksud semua komponen tindanan (pelayan web, masa jalan aplikasi, dan pangkalan data) berada di **tempat yang sama**—contohnya, dalam satu VM, satu bekas, atau satu pelayan fizikal.

Namun, satu-tingkat **tidak semestinya** menggunakan VM atau bekas. Ia juga boleh dijalankan pada logam kosong, pelayan berdedikasi, atau bahkan PaaS, asalkan semua komponen kekal dalam persekitaran pelaksanaan tunggal.

Penting untuk membezakan:

- **Persekitaran pelaksanaan** = tempat tindanan dijalankan (VM, bekas, logam kosong, dll.).
- **Seni bina tingkat** = cara komponen aplikasi dibahagikan (satu-tingkat, pelbagai-tingkat, dll.).

Pilihan persekitaran pelaksanaan mempengaruhi kos operasi, fleksibiliti, kebolehskalaan, keselamatan, dan kebolehselenggaraan. Tiada pilihan yang optimum untuk semua kes—segala-galanya bergantung kepada keperluan projek.

## Panduan Memulakan

1. **Fahami aliran aplikasi.** Pelajari bagaimana permintaan bergerak dari pelayar ke pelayan web, dihantar kepada masa jalan aplikasi, dan berinteraksi dengan pangkalan data. Ini membantu dalam penyelesaian masalah kegagalan. Rujukan: [MDN — Bagaimana Web Berfungsi](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/How_the_web_works).
2. **Pilih tindanan mengikut matlamat.** Untuk pembelajaran, pilih teknologi yang anda gemari bagi memastikan konsistensi latihan. Contohnya, LAMP/LEMP untuk PHP, atau MERN untuk JavaScript. Untuk projek serius, pertimbangkan keperluan aplikasi, kepakaran pasukan, dokumentasi, keselamatan, prestasi, kos, dan sokongan jangka panjang.
3. **Mulakan dalam persekitaran tempatan.** Gunakan [VirtualBox](https://www.virtualbox.org/) untuk VM atau [Docker](https://www.docker.com/) untuk bekas. VM mempunyai sistem pengendalian tetamu sendiri, manakala bekas berkongsi inti hos. Kedua-duanya memudahkan eksperimen sebelum dilaksanakan ke pelayan pengeluaran.
4. **Uji setiap komponen.** Pastikan pelayan web menerima permintaan, masa jalan melaksanakan aplikasi, dan pangkalan data boleh membaca serta menulis data. Pengujian berperingkat memudahkan pengenalpastian isu. Rujukan: [Docker — Mulakan](https://docs.docker.com/get-started/).
5. **Pantau sebelum mengoptimumkan.** Jejaki penggunaan CPU, RAM, cakera, masa tindak balas, and log bagi mengenal pasti kesesakan sebelum menambah sumber atau menukar teknologi. Rujukan: [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).
6. **Utamakan keselamatan dari awal.** Hadkan kebenaran akses, lindungi kelayakan, kemas kini pergantungan, dan hanya buka port yang diperlukan. Kesalahan konfigurasi pada satu mesin boleh menjejaskan keseluruhan aplikasi. Rujukan: [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/).
7. **Sediakan sandaran dan uji pemulihan.** Sandarkan pangkalan data, fail aplikasi, dan konfigurasi penting. Uji pemulihan secara berkala bagi memastikan data boleh dikembalikan sekiranya berlaku kegagalan. Rujukan: [PostgreSQL — Sandaran dan Pemulihan](https://www.postgresql.org/docs/current/backup.html).
8. **Dokumentasikan perubahan.** Catat versi perisian, konfigurasi, pergantungan, dan langkah pelaksanaan. Gunakan [Git](https://git-scm.com/) bagi menjejak perubahan kod untuk memudahkan penyelesaian masalah dan kerjasama.
9. **Ketahui had tindanan satu-tingkat.** Jika satu mesin menjadi terbeban atau kebolehsediaan tinggi diperlukan, nilaikan pengoptimuman, redundansi, atau pemisahan komponen merentas tingkat. Satu mesin merupakan Titik Kegagalan Tunggal (Single Point of Failure/SPoF)—satu titik kegagalan yang boleh menghentikan keseluruhan aplikasi. Rujukan: [Red Hat — Apakah Kebolehsediaan Tinggi?](https://www.redhat.com/en/topics/linux/what-is-high-availability).

## Formula Memilih Tindanan dan Persekitaran Pelaksanaan

- **Untuk pembelajaran:** minat peribadi + kemudahan penggunaan + dokumentasi + ketersediaan sumber pembelajaran.
- **Untuk projek baru:** keperluan aplikasi + bilangan dan corak pengguna + kepakaran pasukan + keselamatan + ujian prestasi + kos operasi.
- **Untuk pemindahan tindanan atau pelaksanaan:** isu sistem semasa + faedah pemindahan yang boleh diukur + kos dan risiko + keserasian + impak kepada pengguna + sokongan jangka panjang.

**Intipati:** Pilih tindanan dan persekitaran pelaksanaan berdasarkan keperluan aplikasi, skala pengguna, keupayaan pasukan, keselamatan, kos, dan keputusan ujian. Untuk belajar daripada amalan dunia sebenar, kaji kajian kes kejuruteraan syarikat yang menghadapi cabaran serupa.

### Rujukan Tindanan Dunia Sebenar

Memilih tindanan teknologi boleh membingungkan memandangkan kepelbagaian bahasa, rangka kerja, pangkalan data, dan alatan yang ada. Selain perbandingan ciri, pembelajaran daripada syarikat yang telah membina dan mengendalikan sistem pada skala besar adalah amat berharga:

- [Uber Engineering](https://www.uber.com/blog/tag/engineering/) — Seni bina bahagian belakang dan kebolehskalaan
- [Shopify Engineering](https://shopify.engineering/) — Monolit dan kebolehskalaan pangkalan data
- [Cloudflare Blog](https://blog.cloudflare.com/) — Infrastruktur pelayan dan rangkaian
- [Netflix TechBlog](https://netflixtechblog.medium.com/) — Sistem teragih dan kebolehpercayaan
- [Stripe Engineering](https://stripe.com/blog/engineering) — Bahagian belakang, API, dan konsistensi data
- [Discord Blog](https://discord.com/blog) — Sistem masa nyata dan pengoptimuman prestasi
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) — Seni bina awan dan pelaksanaan

**Petua:** Perhatikan rasional di sebalik pilihan teknologi, masalah yang dihadapi, dan pertukaran yang dipertimbangkan. Jadikan pengalaman mereka sebagai panduan, lalu sesuaikan mengikut keperluan projek anda sendiri.

## Kesimpulan

Tindanan pelayan satu-tingkat ialah seni bina di mana komponen utama aplikasi—pelayan web, masa jalan aplikasi, dan pangkalan data—berjalan pada satu mesin yang sama. Pelayar menghantar permintaan HTTP kepada pelayan, aplikasi memprosesnya dan mengakses pangkalan data jika perlu, dan hasilnya dikembalikan sebagai respons HTTP.

Memahami konsep ini membantu mengenali peranan setiap komponen, memilih tindanan teknologi yang sesuai, dan menentukan persekitaran pelaksanaan yang bersesuaian. Namun, satu mesin mempunyai had sumber dan berisiko menjadi Titik Kegagalan Tunggal (SPoF).

**Akhir kata:** Pilih tindanan dan pelaksanaan berdasarkan keperluan aplikasi, keupayaan pasukan, keselamatan, kos, dan keputusan ujian. Mulakan secara ringkas, dan apabila aplikasi berkembang, nilaikan keperluan pengoptimuman atau pemisahan komponen merentas pelbagai tingkat.
