# Access Control — PortSwigger Web Security Academy

[🇬🇧 Read in English](access-control-en.md)

﷽

## Apa itu access control?

![access-control](images/overview/access-control.png)

Apa itu access control?
Access control adalah penerapan batasan atas siapa atau apa yang berwenang melakukan aksi atau mengakses sumber daya. Dalam konteks aplikasi web, access control bergantung pada autentikasi dan manajemen sesi:

- **Autentikasi** memastikan pengguna adalah orang yang mengklaim dirinya.
- **Manajemen sesi** mengidentifikasi request HTTP berikutnya yang dibuat oleh pengguna yang sama.
- **Access control** menentukan apakah pengguna diizinkan melakukan aksi yang sedang dia coba lakukan.

Broken access control umum terjadi dan seringkali menimbulkan kerentanan keamanan yang kritis. Desain dan manajemen access control adalah masalah yang kompleks dan dinamis, yang menerapkan batasan bisnis, organisasi, dan hukum ke sebuah implementasi teknis. Keputusan desain access control harus dibuat oleh manusia, sehingga potensi kesalahan tinggi.

### Model keamanan access control

Di bagian ini kami menjelaskan apa itu model keamanan access control dan membahas model-model yang paling umum ditemui.

### Apa itu model keamanan access control?

Model keamanan access control adalah definisi formal dari seperangkat aturan access control yang independen dari teknologi atau platform implementasi. Model keamanan access control diimplementasikan di dalam sistem operasi, jaringan, sistem manajemen basis data, serta perangkat lunak back office, aplikasi, dan server web. Berbagai model keamanan access control telah dirancang selama bertahun-tahun untuk mencocokkan kebijakan access control dengan aturan bisnis atau organisasi serta perubahan teknologi.

### Programmatic access control

Dengan programmatic access control, sebuah matriks hak istimewa pengguna disimpan di basis data dan access control diterapkan secara programatik dengan merujuk ke matriks ini. Pendekatan ini dapat mencakup role atau grup atau pengguna individual, koleksi atau workflow proses, dan bisa sangat granular.

### Discretionary access control (DAC)

Dengan discretionary access control, akses ke sumber daya atau fungsi dibatasi berdasarkan pengguna atau kelompok pengguna. Pemilik sumber daya atau fungsi memiliki kemampuan untuk menetapkan atau mendelegasikan izin akses ke pengguna. Model ini sangat granular dengan hak akses yang didefinisikan ke sumber daya atau fungsi individual dan pengguna. Akibatnya model ini bisa menjadi sangat kompleks untuk dirancang dan dikelola.

### Mandatory access control (MAC)

Mandatory access control adalah sistem access control yang dikendalikan secara terpusat, di mana akses ke suatu objek (file atau sumber daya lain) oleh suatu subjek dibatasi. Secara signifikan, berbeda dengan DAC, pengguna dan pemilik sumber daya tidak memiliki kemampuan untuk mendelegasikan atau memodifikasi hak akses atas sumber daya mereka. Model ini sering dikaitkan dengan sistem berbasis clearance militer.

### Role-based access control (RBAC)

Dengan role-based access control, role bernama didefinisikan yang kepadanya hak istimewa access control ditetapkan. Pengguna kemudian ditetapkan ke satu atau beberapa role. RBAC memberikan manajemen yang lebih baik dibanding model access control lain, dan jika dirancang dengan benar, cukup granular untuk memberikan access control yang dapat dikelola di aplikasi kompleks. Contohnya, purchase clerk mungkin didefinisikan sebagai role dengan izin akses untuk sebagian tugas purchase clerk. RBAC paling efektif ketika ada cukup role untuk menerapkan access control dengan benar, tetapi tidak terlalu banyak sampai membuat model terlalu kompleks dan sulit dikelola.

### Vertical access controls

Vertical access controls adalah mekanisme yang membatasi akses ke fungsi sensitif hanya untuk tipe pengguna tertentu.

Dengan vertical access controls, tipe pengguna berbeda memiliki akses ke fungsi aplikasi yang berbeda. Contohnya, administrator mungkin bisa memodifikasi atau menghapus akun pengguna mana pun, sedangkan pengguna biasa tidak punya akses ke aksi tersebut. Vertical access controls bisa jadi implementasi yang lebih halus dari model keamanan yang dirancang untuk menegakkan kebijakan bisnis seperti separation of duties dan least privilege.

### Horizontal access controls

Horizontal access controls adalah mekanisme yang membatasi akses ke sumber daya hanya untuk pengguna tertentu.

Dengan horizontal access controls, pengguna berbeda memiliki akses ke sebagian sumber daya dari tipe yang sama. Contohnya, aplikasi perbankan akan mengizinkan pengguna melihat transaksi dan melakukan pembayaran dari akun mereka sendiri, tetapi bukan akun pengguna lain.

### Context-dependent access controls

Context-dependent access control membatasi akses ke fungsi dan sumber daya berdasarkan keadaan aplikasi atau interaksi pengguna dengannya.

Context-dependent access controls mencegah pengguna melakukan aksi dalam urutan yang salah. Contohnya, situs ritel mungkin mencegah pengguna memodifikasi isi keranjang belanja mereka setelah mereka melakukan pembayaran.

## Contoh broken access controls

Kerentanan broken access control ada ketika pengguna bisa mengakses sumber daya atau melakukan aksi yang seharusnya tidak bisa mereka lakukan.

### Vertical privilege escalation

Jika pengguna bisa mendapatkan akses ke fungsi yang tidak diizinkan untuk mereka akses, maka ini adalah vertical privilege escalation. Contohnya, jika pengguna non-administratif bisa mendapatkan akses ke halaman admin di mana mereka bisa menghapus akun pengguna, maka ini adalah vertical privilege escalation.

#### Unprotected functionality

Pada tingkat paling dasar, vertical privilege escalation muncul ketika aplikasi tidak menerapkan perlindungan apa pun untuk fungsi sensitif. Contohnya, fungsi administratif mungkin ditautkan dari halaman sambutan administrator tetapi tidak dari halaman sambutan pengguna. Namun, pengguna mungkin bisa mengakses fungsi administratif dengan menjelajah ke URL admin yang relevan.

Contohnya, sebuah situs mungkin menempatkan fungsi sensitif di URL berikut:

```
https://insecure-website.com/admin
```
Ini mungkin bisa diakses oleh pengguna mana pun, bukan hanya pengguna administratif yang punya tautan ke fungsi itu di antarmuka pengguna mereka. Dalam beberapa kasus, URL administratif mungkin diungkap di lokasi lain, seperti file `robots.txt`:

```
https://insecure-website.com/robots.txt
```
Bahkan jika URL tidak diungkap di mana pun, penyerang mungkin bisa memakai wordlist untuk brute-force lokasi fungsi sensitif.

##### Lab: Unprotected admin functionality

Lab ini punya admin panel yang tidak terlindungi.

<details>
<summary>Lab details, screenshots & walkthrough 0.1</summary>

Selesaikan lab dengan menghapus pengguna `carlos`.

**Screenshots:**

![Halaman lab — Unprotected admin functionality (belum solved)](images/lab-0.1-unprotected-admin-functionality/01-lab-page.png)

![Burp HTTP history — GET /robots.txt](images/lab-0.1-unprotected-admin-functionality/02-burp-proxy.png)

![Burp Repeater — robots.txt membocorkan /administrator-panel](images/lab-0.1-unprotected-admin-functionality/03-burp-robots.png)

![Burp Repeater — GET /administrator-panel menampilkan Users](images/lab-0.1-unprotected-admin-functionality/04-burp-admin-panel.png)

![Burp Repeater — GET /administrator-panel/delete?username=carlos](images/lab-0.1-unprotected-admin-functionality/05-burp-delete.png)

![Lab solved — 'User deleted successfully!'](images/lab-0.1-unprotected-admin-functionality/06-solved.png)

##### Tutorial

1. Buka robots.txt
2. Lihat respons dan dapatkan administrator-panel
3. Buka panel, coba hapus pengguna `carlos`
4. Berhasil, lab solved

##### Reference

<details>
<summary>1. Broken Access Control - Lab #1 Unprotected admin functionality — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=qJ8mtm_G40E
Purpose: Lab ini punya admin panel yang tidak terlindungi. Untuk menyelesaikan lab, kami mengeksploitasi kerentanan access control untuk mengakses admin panel dan menghapus pengguna carlos.

</details>

<details>
<summary>2. Portswigger - Access Control - Lab #1 Unprotected admin functionality — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=XF-SNuSyVNo
Purpose: Halo Hackers, di video Unprotected admin functionality ini kamu akan melihat cara mengeksploitasi, menemukan, dan mencari informasi sensitif berdasarkan alur logika aplikasi untuk bocor yang berpotensi jadi serangan dari Burp Suite di lab dari Web Security Academy powered by Portswigger.

</details>

</details>

#### Unprotected functionality - Lanjutan

Dalam beberapa kasus, fungsi sensitif disembunyikan dengan memberinya URL yang kurang dapat diprediksi. Ini contoh dari yang disebut "security by obscurity". Namun, menyembunyikan fungsi sensitif tidak memberikan access control yang efektif karena pengguna mungkin menemukan URL yang diobfuskasi itu dengan berbagai cara.

Bayangkan aplikasi yang menempatkan fungsi administratif di URL berikut:

```
https://insecure-website.com/administrator-panel-yb556
```
Ini mungkin tidak langsung bisa ditebak penyerang. Namun, aplikasi mungkin tetap membocorkan URL itu ke pengguna. URL mungkin diungkap di JavaScript yang membangun antarmuka pengguna berdasarkan role pengguna:

```html
<script>
	var isAdmin = false;
	if (isAdmin) {
		...
		var adminPanelTag = document.createElement('a');
		adminPanelTag.setAttribute('href', 'https://insecure-website.com/administrator-panel-yb556');
		adminPanelTag.innerText = 'Admin panel';
		...
	}
</script>
```
Script ini menambahkan tautan ke UI pengguna jika mereka admin. Namun, script yang berisi URL itu terlihat oleh semua pengguna terlepas dari role mereka.

##### Lab: Unprotected admin functionality with unpredictable URL

Lab ini punya admin panel yang tidak terlindungi. Lokasinya tidak dapat diprediksi, tetapi lokasinya diungkap di suatu tempat dalam aplikasi.

<details>
<summary>Lab details, screenshots & walkthrough 0.2</summary>

Selesaikan lab dengan mengakses admin panel, lalu menggunakannya untuk menghapus pengguna `carlos`.

**Screenshots:**

![Halaman lab — admin panel dengan URL tak dapat diprediksi](images/lab-0.2-unprotected-admin-unpredictable-url/01-lab-page.png)

![View source — JS membocorkan URL admin panel (var isAdmin)](images/lab-0.2-unprotected-admin-unpredictable-url/02-js-source.png)

![Admin panel — Users wiener & carlos](images/lab-0.2-unprotected-admin-unpredictable-url/03-admin-panel.png)

![Lab solved — 'User deleted successfully!'](images/lab-0.2-unprotected-admin-unpredictable-url/04-solved.png)

##### Tutorial

1. Buka /login, lihat source code
2. Lihat kode javascript

```javascript
<!--LAB_HEADER_END-->
        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                            <script>
var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-jufne8');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}
</script>
```
3. Buka /admin-*

##### Reference

<details>
<summary>3. Broken Access Control - Lab#2 Unprotected admin functionality with unpredictable URL | Short Version — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=7Jve11VySNU
Purpose: Lab ini punya admin panel yang tidak terlindungi. Lokasinya tidak dapat diprediksi, tetapi lokasinya diungkap di suatu tempat dalam aplikasi. Untuk menyelesaikan lab, kami mengakses admin panel dan menggunakannya untuk menghapus pengguna carlos.

</details>

<details>
<summary>4. Unprotected admin functionality with unpredictable URL — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=mml8SlN2Or4
Purpose: Video ini menunjukkan solusi lab "Unprotected admin functionality with unpredictable URL" dari Web Security Academy (Portswigger)

</details>

</details>

#### Parameter-based access control methods

Sebagian aplikasi menentukan hak akses atau role pengguna saat login, lalu menyimpan informasi itu di lokasi yang dapat dikontrol pengguna.

Ini bisa berupa:

- Hidden field.
- Cookie.
- Parameter query string yang telah ditetapkan.

Aplikasi membuat keputusan access control berdasarkan nilai yang dikirim. Contohnya:

```
https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1
```
Pendekatan ini tidak aman karena pengguna bisa memodifikasi nilai dan mengakses fungsi yang tidak berwenang mereka akses, seperti fungsi administratif.

##### Lab: User role controlled by request parameter

Lab ini punya admin panel di /admin, yang mengidentifikasi administrator memakai cookie yang bisa dipalsukan.

<details>
<summary>Lab details, screenshots & walkthrough 0.3</summary>

Selesaikan lab dengan mengakses admin panel dan menggunakannya untuk menghapus pengguna `carlos`.

Kamu bisa login ke akun sendiri memakai kredensial berikut:
`wiener:peter`

**Screenshots:**

![Halaman login — login sebagai wiener](images/lab-0.3-user-role-request-parameter/01-login.png)

![Burp HTTP history — my-account dengan cookie Admin=false](images/lab-0.3-user-role-request-parameter/02-burp-proxy.png)

![GET /admin dengan Admin=false — 'Admin interface only available'](images/lab-0.3-user-role-request-parameter/03-admin-denied.png)

![Burp Repeater — ubah cookie jadi Admin=true](images/lab-0.3-user-role-request-parameter/04-burp-repeater.png)

![Burp Repeater — kirim ulang request dengan Admin=true](images/lab-0.3-user-role-request-parameter/05-burp-repeater-2.png)

![Burp — dialog 'Show response in browser'](images/lab-0.3-user-role-request-parameter/06-response-browser.png)

![Browser — 'Admin interface only available if logged in as an administrator'](images/lab-0.3-user-role-request-parameter/07-admin-denied-2.png)

![Admin panel — GET /admin 200, daftar Users](images/lab-0.3-user-role-request-parameter/08-admin-panel.png)

![Percobaan hapus carlos — Admin=false 401](images/lab-0.3-user-role-request-parameter/09-burp-request.png)

![Lab solved — hapus carlos dengan Admin=true](images/lab-0.3-user-role-request-parameter/10-solved.png)

##### Tutorial

1. Login sebagai `wiener:peter`
2. Coba lihat parameter `admin=false`
3. Ubah nilai jadi `admin=true`
4. Buka admin panel
5. Hapus pengguna `carlos`
6. Berhasil, lab solved

##### Reference

<details>
<summary>5. Broken Access Control - Lab #3 User role controlled by request parameter — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=e_jsPdEeSto
Purpose: Lab ini punya admin panel di /admin, yang mengidentifikasi administrator memakai cookie yang bisa dipalsukan. Untuk menyelesaikan lab, kami mengakses admin panel dan menggunakannya untuk menghapus pengguna carlos.

</details>

</details>

##### Lab: User role can be modified in user profile

Lab ini punya admin panel di `/admin`. Hanya bisa diakses pengguna yang login dengan `roleid` 2.

<details>
<summary>Lab details, screenshots & walkthrough 0.4</summary>

Selesaikan lab dengan mengakses admin panel dan menggunakannya untuk menghapus pengguna `carlos`.
Kamu bisa login ke akun sendiri memakai kredensial berikut:
`wiener:peter`

**Screenshots:**

![Halaman login — login sebagai wiener](images/lab-0.4-user-role-modifiable-profile/01-login.png)

![Burp HTTP history — GET /admin mengembalikan 401](images/lab-0.4-user-role-modifiable-profile/02-burp-proxy.png)

![Burp HTTP history — alur login & my-account](images/lab-0.4-user-role-modifiable-profile/03-burp-history.png)

![Burp Repeater — POST /my-account/change-email dengan roleid:1](images/lab-0.4-user-role-modifiable-profile/04-change-email.png)

![Admin panel — Users wiener & carlos](images/lab-0.4-user-role-modifiable-profile/05-admin-panel.png)

![Lab solved — 'User deleted successfully!'](images/lab-0.4-user-role-modifiable-profile/06-solved.png)

![Burp Repeater — change-email dengan roleid:2 (privilege escalation)](images/lab-0.4-user-role-modifiable-profile/07-burp-request.png)

##### Tutorial

1. Login sebagai `wiener:peter`
2. Coba cari my-account
3. Ubah email untuk melihat parameter
4. Coba buka parameter json di profil my-account
5. Lihat respons dan tambahkan `roleId=1` lalu ubah roleId administratif jadi `roleId=2`
6. Buka admin panel
7. Hapus pengguna carlos
8. Berhasil, lab solved

##### Reference

<details>
<summary>6. Broken Access Control - Lab #4 User role can be modified in user profile — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=jjfe7WRN76o
Purpose: Lab ini punya admin panel di /admin. Hanya bisa diakses pengguna yang login dengan roleid 2. Untuk menyelesaikan lab, kami mengakses admin panel dan menggunakannya untuk menghapus pengguna carlos.

</details>

<details>
<summary>7. User role can be modified in user profile — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=4AXJpx7F9YY
Purpose: Video ini menunjukkan solusi lab "User role can be modified in user profile" dari Web Security Academy (Portswigger)

</details>

</details>

#### Broken access control resulting from platform misconfiguration

Sebagian aplikasi menerapkan access control di layer platform. Mereka melakukannya dengan membatasi akses ke URL dan metode HTTP tertentu berdasarkan role pengguna. Contohnya, aplikasi mungkin mengonfigurasi aturan sebagai berikut:

```
DENY: POST, /admin/deleteUser, managers
```
Aturan ini menolak akses ke metode `POST` pada URL `/admin/deleteUser`, untuk pengguna di grup managers. Berbagai hal bisa salah dalam situasi ini, yang mengarah ke bypass access control.

Sebagian framework aplikasi mendukung berbagai header HTTP non-standar yang bisa dipakai untuk menimpa URL di request asli, seperti `X-Original-URL` dan `X-Rewrite-URL`. Jika situs memakai kontrol front-end yang ketat untuk membatasi akses berdasarkan URL, tetapi aplikasi mengizinkan URL ditimpa via header request, maka mungkin bisa melewati access control memakai request seperti berikut:

```
POST / HTTP/1.1
X-Original-URL: /admin/deleteUser
```

##### Lab: URL-based access control can be circumvented

Situs ini punya admin panel tanpa autentikasi di `/admin`, tetapi sistem front-end dikonfigurasi untuk memblokir akses eksternal ke path itu. Namun, aplikasi back-end dibangun di atas framework yang mendukung header `X-Original-URL`.

<details>
<summary>Lab details, screenshots & walkthrough 0.5</summary>

Untuk menyelesaikan lab, akses admin panel dan hapus pengguna `carlos`.

**Screenshots:**

![Burp Repeater — bypass X-Original-URL: /admin](images/lab-0.5-url-based-access-control-bypass/01-burp-repeater.png)

![Body respons — 'access denied'](images/lab-0.5-url-based-access-control-bypass/02-access-denied.png)

![Body respons — 'access denied' (ulangan)](images/lab-0.5-url-based-access-control-bypass/03-access-denied-2.png)

![Admin panel — Users wiener & carlos (bypass berhasil)](images/lab-0.5-url-based-access-control-bypass/04-admin-panel.png)

![Lab solved — 'Congratulations, you solved the lab!'](images/lab-0.5-url-based-access-control-bypass/05-solved.png)

##### Tutorial

1. Buka admin panel
2. Pasang `X-Original-Url: /admin`
3. Jika berhasil, coba hapus pengguna `carlos`.

```
GET /?username=carlos
X-Original-Url: /admin/delete
```
4. Pengguna berhasil dihapus
5. Berhasil, lab solved.

##### Reference

<details>
<summary>7. Broken Access Control - Lab #5 URL-based access control can be circumvented — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=AwvQrdE1Wtc
Purpose: Di video ini, kami membahas Lab #5 pada modul Access Control Vulnerabilities dari Web Security Academy. Situs ini punya admin panel tanpa autentikasi di /admin, tetapi sistem front-end dikonfigurasi untuk memblokir akses eksternal ke path itu. Namun, aplikasi back-end dibangun di atas framework yang mendukung header X-Original-URL. Untuk menyelesaikan lab, kami mengakses admin panel dan menghapus pengguna carlos.

</details>

<details>
<summary>8. URL based access control can be circumvented — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=Rj0B12Vsh_E
Purpose: Video ini menunjukkan solusi lab "URL based access control can be circumvented" dari Web Security Academy (Portswigger)

</details>

</details>

##### Lab: Method-based access control can be circumvented

#### Broken access control resulting from URL-matching discrepancies

### Horizontal privilege escalation

##### Lab: User ID controlled by request parameter

##### Lab: User ID controlled by request parameter, with unpredictable user IDs

##### Lab: User ID controlled by request parameter with data leakage in redirect

#### Horizontal to vertical privilege escalation

##### Lab: User ID controlled by request parameter with password disclosure

### Insecure direct object references

##### Lab: Insecure direct object references

### Access control vulnerabilities in multi-step processes

##### Lab: Multi-step process with no access control on one step

### Referer-based access control

##### Lab: Referer-based access control

### Location-based access control

## Cara mencegah kerentanan access control