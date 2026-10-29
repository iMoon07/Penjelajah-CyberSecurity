# Cara Setup Burpsuite Community di Browser

[🇬🇧 Read in English](Setup-Burpsuite-Community-en.md)

﷽

Pertama pastikan mempunyai Tools Burpsuite, jika pengguna Operating System Linux distro Kali Linux secara khusus langsung ada dan disediakan.

Lalu membutuhkan extension, dan pemilihan browser yang tepat dan nyaman.

## Prasyarat install:

- Burpsuite Community
- Foxxy Proxy Extension
- Browser (Firefox)

## Demonstrasi

![burpsuite](burpsuitetools.png)

Buka burpsuite

![foxyproxy](foxyproxy.png)

Pasang Extesion di browser Firefox

![setting-foxyproxy](setting.png)

Setting interface di foxy proxy

- Title: Burpsuite hosts
- hostname: `127.0.0.1` 
- port: `8080`

![alamatburp](alamatburp.png)

Pastikan alamat hosts sama secara default.


![pengujian local](pengujian-web-local.png)

Pengujian proxy intercept dan pencegatan lalu lintas target web local.


![testing web lain bermasalah](testing-web-lain-bermasalah.png)


Jika ingin menguji Web domain yang memiliki jaringan publik maka perlu melakukan konfigurasi selanjutnya.

![cara ambil dan download](caradownload-cert-burp.png)

Pertama ambil dan download cert di http://burp


![download-burpcert](download-burpcert.png)

Setelah selesai download lanjut ke pengaturan.


![pengaturan](kepengaturan-firefox.png)

pilih setting

![](import-cert-burp-ke-browser.png)

cari disearch keyword "cert" dan view lalu import certificate


![izin email domain](izin-trust-cert.png)

Trust CA untuk identifikasi website, dan emails users

![import cert ke burp](format-der-untuk-import-cert-browser-ke-burp.png)

import certificate yang dari browser ke burpsuite format in `DER`

![pilih lokasi export ca](import-cert-ke-burp-yang-berasal-dari-browser.png)


pilih lokasi cert yang barusan di download lalu import

![berhasil](berhasil-import-cert-dari-burp.png)

berhasil import cert dari browser ke burpsuite.

![pengujian web domain luar](pengujian-web-public.png)

Disini misalnya mengujungi github.com mengaktifkan dan tanpa mengaktifkan intecept atau cegat lalu lintas, http tersebut dapat tertangkap oleh burpsuite.


## Referensi

* Burpsuite Community
  https://portswigger.net/burp/communitydownload

* Burpsuite Documentation
  https://portswigger.net/burp/documentation/desktop/
