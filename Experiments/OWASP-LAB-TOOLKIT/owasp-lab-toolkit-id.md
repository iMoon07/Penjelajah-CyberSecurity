# Build Your Own Hacking Dojo: OWASP Lab Toolkit

[🇬🇧 Read in English](owasp-lab-toolkit-en.md)

﷽

Ini adalah tulisan pertama di blog saya, tempat saya mendokumentasikan eksplorasi, eksperimen, dan pengembangan di bidang cybersecurity.

![Skull](skull.jpg)

Kali ini, saya membagikan **OWASP Lab Toolkit**, sebuah toolkit berbasis Bash untuk menyiapkan lingkungan web application security testing secara otomatis. Toolkit ini mengintegrasikan berbagai aplikasi web yang sengaja dibuat rentan ke dalam satu lab, sehingga proses instalasi dan pengelolaannya lebih praktis.

## Komponen Lab

Toolkit ini mengintegrasikan sejumlah aplikasi dan layanan untuk pengujian keamanan web:

- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [OWASP Mutillidae II](https://owasp.org/www-project-mutillidae-ii/)
- [OWASP WebGoat & WebWolf](https://owasp.org/www-project-webgoat/)
- [DVWA](https://github.com/digininja/DVWA)
- [bWAPP](http://www.itsecgames.com/)
- [XVWA](https://github.com/s4n7h0/xvwa)
- [VWA](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

Selain aplikasi tersebut, toolkit menyediakan layanan pendukung seperti web server dan database, termasuk antarmuka administrasi database sesuai konfigurasi instalasi.

## Persyaratan

- **Virtualisasi:** VMware Workstation Pro atau VirtualBox.
- **Sistem operasi:** Ubuntu Server 24.04 LTS.
- **Spesifikasi minimum yang ditargetkan:** RAM 2 GB, 1 vCPU, dan disk 20 GB.
- **Akses lab:** browser pada mesin klien dan konfigurasi file `hosts`.
- **Toolkit:** [OWASP Lab Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit).

Dukungan sistem operasi saat ini berfokus pada lingkungan Linux berbasis Ubuntu.

## Instalasi dan Konfigurasi

### 1. Clone repositori

Jalankan perintah berikut di terminal Ubuntu Server:

```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

### 2. Jalankan installer

```bash
sudo ./install-owasp-lab.sh
```

Installer akan menyiapkan komponen yang diperlukan dan mengunduh aplikasi sesuai konfigurasi toolkit. Waktu instalasi bergantung pada koneksi internet dan sumber daya mesin.

### 3. Konfigurasi file `hosts`

Agar setiap aplikasi dapat diakses menggunakan domain lokal, arahkan domain-domain lab ke IP Ubuntu Server.

Dalam contoh ini, IP server adalah `10.10.10.2`. Pastikan IP tersebut memang digunakan oleh server dan dapat dijangkau dari mesin klien.

**Linux**

Buka file hosts:

```bash
sudo nano /etc/hosts
```

Tambahkan baris berikut:

```text
10.10.10.2 owasp.hacking
10.10.10.2 mutillidae.owasp.hacking
10.10.10.2 dvwa.owasp.hacking
10.10.10.2 bwapp.owasp.hacking
10.10.10.2 xvwa.owasp.hacking
10.10.10.2 vwa.owasp.hacking
10.10.10.2 adminer.owasp.hacking
10.10.10.2 phpmyadmin.owasp.hacking
10.10.10.2 juiceshop.owasp.hacking
10.10.10.2 webgoat.owasp.hacking
10.10.10.2 webwolf.owasp.hacking
10.10.10.2 tomcat.owasp.hacking
10.10.10.2 upload.owasp.hacking
10.10.10.2 example.owasp.hacking
```

Simpan dengan `Ctrl + O`, tekan `Enter`, lalu keluar menggunakan `Ctrl + X`.

**Windows 10**

1. Cari Notepad, lalu pilih **Run as administrator**.
2. Buka file berikut:

   `C:\Windows\System32\drivers\etc\hosts`

3. Ubah filter berkas menjadi *All Files* jika file `hosts` tidak terlihat.
4. Tambahkan daftar domain yang sama seperti konfigurasi Linux di atas.
5. Simpan file tanpa ekstensi tambahan.

![Konfigurasi File Hosts Windows](Input%20Hosts.png)

**Menambahkan domain baru**

Jika nantinya ada aplikasi baru, tambahkan domainnya dengan format:

```text
10.10.10.2 nama-aplikasi.owasp.hacking
```

Contohnya, jika ingin menambahkan `newlab.owasp.hacking`:

```text
10.10.10.2 newlab.owasp.hacking
```

Simpan perubahan pada file `hosts`. Tidak perlu membuat entri baru jika domain tersebut sudah terdaftar.

> **Catatan:** Daftar `hosts` hanya mengarahkan nama domain ke IP server. Setiap domain tetap harus didukung oleh konfigurasi virtual host, reverse proxy, atau mekanisme routing yang sesuai. Pastikan juga port aplikasi telah dikonfigurasi dengan benar. Domain yang belum tersedia pada server tidak otomatis menjadi aplikasi yang dapat diakses.

### 4. Verifikasi layanan

Setelah instalasi selesai, jalankan health checker:

```bash
sudo ./check-owasp-lab.sh
```

Pilih opsi `1` untuk memeriksa koneksi HTTP. Pastikan endpoint yang diharapkan aktif menunjukkan status normal.

![Status Endpoints UP](Endpoints-UP.png)

## Mulai Eksplorasi

![Overview Aplikasi](Overview.png)

Setelah layanan siap, buka browser dari mesin klien dan akses aplikasi melalui domain yang telah dikonfigurasi. Setiap aplikasi menyediakan lingkungan tersendiri untuk menguji perilaku dan kelemahan keamanan web.

Gunakan lab ini pada lingkungan yang Anda kendalikan, bukan pada sistem pihak lain tanpa izin.

## Penutup

OWASP Lab Toolkit saya kembangkan untuk menyederhanakan proses menyiapkan lingkungan pengujian keamanan aplikasi web. Masukan, laporan bug, dan usulan integrasi aplikasi lainnya sangat terbuka.

Repositori: [iMoon07/OWASP-Lab-Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit)

Jika menemukan kendala instalasi atau ingin mengusulkan pengembangan berikutnya, silakan buka *issue* atau diskusikan melalui kolom komentar.

Selamat bereksperimen.
