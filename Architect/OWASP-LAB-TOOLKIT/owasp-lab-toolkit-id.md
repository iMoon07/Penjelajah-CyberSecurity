# Build Your Own Hacking Dojo: OWASP Lab Toolkit

[🇬🇧 Read in English](owasp-lab-toolkit-en.md)

Hallo sobat Penjelajah CyberSecurity, apakabar semuanya salam kenal ya ini merupakan tulisan pertama saya di blog ini. Web Blog ini nantinya akan berisi catatan-catatan saya saat explorasi dan eksplorasi saya secara dalam dunia hacking dan cybersecurity. Semoga bermanfaat untuk kita semua dalam belajar dan berkembang bersama.

Saya ingin berbagi sebuah tools yang lumayan bermanfaat bagi temen-temen yang sedang belajar web application pentesting. Tools ini adalah OWASP Lab Toolkit, sebuah tools yang memudahkan kita dalam membuat lab web application untuk belajar hacking dan cybersecurity.

Saya membangun tools ini dengan menggunakan beberapa referensi dan resource terkenal yang di gunakan di Industri Cyber Security sebagai tempat latihan (saya menyebut like a dojo hacking).

Berikut adalah *resource* aplikasi rentan (*vulnerable apps*) dan *tools* pendukung yang saya integrasikan ke dalam OWASP Lab Toolkit:

- OWASP Juice Shop - [owasp.org/www-project-juice-shop](https://owasp.org/www-project-juice-shop/)
- OWASP Mutillidae II - [itsecgames.com](http://itsecgames.com/)
- OWASP WebGoat & WebWolf - [owasp.org/www-project-webgoat](https://owasp.org/www-project-webgoat/)
- DVWA (Damn Vulnerable Web App) - [github.com/digininja/DVWA](https://github.com/digininja/DVWA)
- bWAPP (buggy web application) - [itsecbbq.org/bwapp](http://www.itsecbbq.org/bwapp/)
- XVWA (Xtreme Vulnerable Web Application) - [github.com/s4n7h0/xvwa](https://github.com/s4n7h0/xvwa)
- VWA (Vulnerable Web Application) - [github.com/hummingbirdscyber/Vulnerable-Web-Application](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

Jadi diperlukan apa saja untuk bisa ngelabs dan latihan?

- VMware Workstation Pro (Bisa juga menggunakan VirtualBox)
- Operating System Ubuntu 24.04 LTS (Saat ini tools masih support di ekosistem Linux based Ubuntu, kedepannya akan di update untuk OS lain)
- Spesifikasi Ram 2GB - 1vCPU - Disk 20GB
- Notepad (Digunakan untuk menulis hosts file jika di Windows)
- Tools OWASP Lab Toolkit - https://github.com/imoon07/OWASP-Lab-Toolkit

### Cara Instalasi & Setup OWASP Lab Toolkit

Proses instalasinya sangat mudah karena semuanya sudah diotomatisasi menggunakan *bash script*. Ikuti langkah-langkah berikut:

#### 1. Clone Repositori

Buka terminal di mesin Ubuntu Server kalian, lalu jalankan perintah ini untuk mengunduh *toolkit*:
```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

#### 2. Jalankan Installer

Jalankan *script* utama menggunakan akses `sudo`. *Script* ini akan memakan waktu beberapa menit karena menginstal seluruh komponen (Web Server, Database, Node.js, Java) dan mengkloning aplikasinya secara otomatis.
```bash
sudo ./install-owasp-lab.sh
```

#### 3. Konfigurasi File Hosts

Agar kita bisa mengakses lab menggunakan domain lokal yang keren (seperti `dvwa.owasp.hacking`), kita wajib mengarahkan domain tersebut ke IP Address Ubuntu Server kita.
- Di Windows, buka **Notepad** sebagai *Administrator*.
- Buka file di path ini: `C:\Windows\System32\drivers\etc\hosts`.
- Tambahkan baris berikut di bagian paling bawah (Ganti IP Address `[IP_ADDRESS]` dengan IP Ubuntu Server kalian):
```text
[IP_ADDRESS] dvwa.owasp.hacking bwapp.owasp.hacking juiceshop.owasp.hacking
```

![Konfigurasi File Hosts Windows](Input%20Hosts.png)

#### 4. Verifikasi Status Lab

Untuk memastikan semua layanan berjalan normal (HTTP 200 OK), gunakan *script health checker* bawaan:
```bash
sudo ./check-owasp-lab.sh
```
Pilih opsi 1 untuk mengecek koneksi HTTP. Pastikan semuanya berwarna hijau (NORMAL).

![Status Endpoints UP](Endpoints-UP.png)

### Mulai Eksplorasi!

Setelah semua statusnya hijau, kalian bisa langsung membuka browser di mesin utama dan mulai belajar *penetration testing*!

![Overview Aplikasi](Overview.png)

Enjoy learning and get safe hacking !

Selamat *ngelabs* dan berkembang bersama! Jika *toolkit* ini dirasa bermanfaat untuk menemani perjalanan *cybersecurity* kalian, jangan ragu untuk mampir ke GitHub saya dan tinggalkan jejak ⭐ (Star)!

Kalau ada kendala saat instalasi, dapet *error*, atau mau *request* aplikasi rentan lain buat *update* selanjutnya, kalian bebas diskusi dan tanya-tanya di kolom komentar di bawah ini ya. Mari kita belajar bareng! 👇
