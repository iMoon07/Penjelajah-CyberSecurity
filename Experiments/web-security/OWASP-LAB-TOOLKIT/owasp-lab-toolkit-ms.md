# Build Your Own Hacking Dojo: OWASP Lab Toolkit

[🇬🇧 Read in English](owasp-lab-toolkit-en.md)  
[🇮🇩 Baca dalam Bahasa Indonesia](owasp-lab-toolkit-id.md)  
[🇵🇭 Basahin sa Tagalog](owasp-lab-toolkit-tl.md)

﷽

Ini ialah tulisan pertama dalam blog saya, tempat saya mendokumentasikan penerokaan, eksperimen, dan pembangunan dalam bidang cybersecurity.

![Skull](skull.jpg)

Kali ini, saya berkongsi **OWASP Lab Toolkit**, sebuah toolkit berasaskan Bash untuk menyediakan persekitaran web application security testing secara automatik. Toolkit ini mengintegrasikan pelbagai aplikasi web yang sengaja dibuat terdedah kepada risiko dalam satu makmal, supaya proses pemasangan dan pengurusannya lebih praktikal.

## Komponen Makmal

Toolkit ini mengintegrasikan beberapa aplikasi dan service untuk pengujian keselamatan web:

- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [OWASP Mutillidae II](https://owasp.org/www-project-mutillidae-ii/)
- [OWASP WebGoat & WebWolf](https://owasp.org/www-project-webgoat/)
- [DVWA](https://github.com/digininja/DVWA)
- [bWAPP](http://www.itsecgames.com/)
- [XVWA](https://github.com/s4n7h0/xvwa)
- [VWA](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

Selain aplikasi tersebut, toolkit menyediakan service sokongan seperti web server dan database, termasuk antara muka pentadbiran database mengikut konfigurasi pemasangan.

## Keperluan

- **Virtualisasi:** VMware Workstation Pro atau VirtualBox.
- **Sistem operasi:** Ubuntu Server 24.04 LTS.
- **Spesifikasi minimum sasaran:** RAM 2 GB, 1 vCPU, dan disk 20 GB.
- **Akses makmal:** browser pada mesin klien dan konfigurasi fail `hosts`.
- **Toolkit:** [OWASP Lab Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit).

Sokongan sistem operasi buat masa ini memfokus kepada persekitaran Linux berasaskan Ubuntu.

## Pemasangan dan Konfigurasi

### 1. Clone repository

Jalankan arahan berikut dalam terminal Ubuntu Server:

```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

### 2. Jalankan installer

```bash
sudo ./install-owasp-lab.sh
```

Installer akan menyediakan komponen yang diperlukan dan memuat turun aplikasi mengikut konfigurasi toolkit. Masa pemasangan bergantung pada sambungan internet dan resource mesin.

### 3. Konfigurasi fail `hosts`

Supaya setiap aplikasi boleh diakses menggunakan domain setempat, arahkan domain-domain makmal kepada IP Ubuntu Server.

Dalam contoh ini, IP server ialah `10.10.10.2`. Pastikan IP tersebut memang digunakan oleh server dan boleh dicapai daripada mesin klien.

**Linux**

Buka fail hosts:

```bash
sudo nano /etc/hosts
```

Tambah baris berikut:

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

Simpan dengan `Ctrl + O`, tekan `Enter`, kemudian keluar menggunakan `Ctrl + X`.

**Windows 10**

1. Cari Notepad, kemudian pilih **Run as administrator**.
2. Buka fail berikut:

   `C:\Windows\System32\drivers\etc\hosts`

3. Tukar penapis fail kepada *All Files* jika fail `hosts` tidak kelihatan.
4. Tambah senarai domain yang sama seperti konfigurasi Linux di atas.
5. Simpan fail tanpa extension tambahan.

![Konfigurasi Fail Hosts Windows](Input%20Hosts.png)

**Menambah domain baharu**

Jika kelak terdapat aplikasi baharu, tambah domainnya dengan format:

```text
10.10.10.2 nama-aplikasi.owasp.hacking
```

Contohnya, jika mahu menambah `newlab.owasp.hacking`:

```text
10.10.10.2 newlab.owasp.hacking
```

Simpan perubahan pada fail `hosts`. Tiada keperluan membuat entri baharu jika domain tersebut sudah didaftarkan.

> **Nota:** Senarai `hosts` hanya mengarahkan nama domain kepada IP server. Setiap domain masih perlu disokong oleh konfigurasi virtual host, reverse proxy, atau mekanisme routing yang sesuai. Pastikan port aplikasi juga telah dikonfigurasikan dengan betul. Domain yang belum tersedia pada server tidak automatik menjadi aplikasi yang boleh diakses.

### 4. Pengesahan service

Selepas pemasangan selesai, jalankan health checker:

```bash
sudo ./check-owasp-lab.sh
```

Pilih opsyen `1` untuk menyemak sambungan HTTP. Pastikan endpoint yang dijangka aktif menunjukkan status normal.

![Status Endpoints UP](Endpoints-UP.png)

## Mula Meneroka

![Overview Aplikasi](Overview.png)

Selepas service sedia, buka browser daripada mesin klien dan akses aplikasi melalui domain yang telah dikonfigurasikan. Setiap aplikasi menyediakan persekitaran tersendiri untuk menguji tingkah laku dan kelemahan keselamatan web.

Gunakan makmal ini dalam persekitaran yang anda kawal, bukan pada sistem pihak lain tanpa kebenaran.

## Penutup

OWASP Lab Toolkit saya bangunkan untuk memudahkan proses menyediakan persekitaran pengujian keselamatan aplikasi web. Maklum balas, laporan bug, dan cadangan integrasi aplikasi lain amat dialu-alukan.

Repository: [iMoon07/OWASP-Lab-Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit)

Jika menemui masalah pemasangan atau mahu mencadangkan pembangunan seterusnya, sila buka *issue* atau bincangkan melalui bahagian komen.

Selamat bereksperimen.
