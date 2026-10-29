# How to Setup Burpsuite Community in Browser

[🇮🇩 Read in Bahasa Indonesia](Setup-Burpsuite-Community-id.md)

﷽

First, make sure you have Burpsuite installed. If you are using Kali Linux, it is typically pre-installed.

Then, you will need an extension and a suitable, comfortable browser.

## Prerequisites:

- Burpsuite Community
- FoxyProxy Extension
- Browser (Firefox)

## Demonstration

![burpsuite](burpsuitetools.png)

Open burpsuite

![foxyproxy](foxyproxy.png)

Install the extension in Firefox browser

![setting-foxyproxy](setting.png)

Set the interface in foxy proxy

- Title: Burpsuite hosts
- hostname: `127.0.0.1`
- port: `8080`

![alamatburp](alamatburp.png)

Make sure the host address is the same by default.

![pengujian local](pengujian-web-local.png)

Testing proxy intercept and blocking local web traffic.

![testing web lain bermasalah](testing-web-lain-bermasalah.png)

If you want to test a web domain with a public network, further configuration is required.

![cara ambil dan download](caradownload-cert-burp.png)

First, retrieve and download the certificate from http://burp

![download-burpcert](download-burpcert.png)

After downloading, proceed to the settings.

![pengaturan](kepengaturan-firefox.png)

Select settings

![](import-cert-burp-ke-browser.png)

Search for the keyword "cert" and view, then import certificate

![izin email domain](izin-trust-cert.png)

Trust CA for website identification and email users

![import cert ke burp](format-der-untuk-import-cert-browser-ke-burp.png)

Import the certificate from browser to burpsuite in `DER` format

![pilih lokasi export ca](import-cert-ke-burp-yang-berasal-dari-browser.png)

Select the location of the recently downloaded certificate, then import

![berhasil](berhasil-import-cert-dari-burp.png)

Successfully imported the certificate from browser to burpsuite.

![pengujian web domain luar](pengujian-web-public.png)

Here, for example, testing github.com with and without intercept or blocking traffic, the http can be captured by burpsuite.

## References

* Burpsuite Community
  https://portswigger.net/burp/communitydownload

* Burpsuite Documentation
  https://portswigger.net/burp/documentation/desktop/