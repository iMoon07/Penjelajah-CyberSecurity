# TCP & UDP Proxy Lab — Analisis Traffic FTP

[🇬🇧 Read in English](build-tcp-udp-proxy-lab-en.md)

Lab ini membuat proxy sederhana menggunakan Python untuk meneruskan trafik antara client dan server.

Proxy ditempatkan di tengah komunikasi:

```text
Client → Proxy → Server
```

Tujuannya bukan hanya agar data sampai ke server, tetapi juga agar isi trafik dapat dilihat dalam bentuk hexadecimal dan ASCII.

Melalui lab ini dilakukan tiga hal:

```text
1. Meneruskan trafik TCP.
2. Meneruskan trafik UDP.
3. Menggunakan proxy TCP untuk melihat komunikasi FTP.
```

FTP dipilih sebagai pengujian karena command dan responsnya terlihat jelas, misalnya `USER`, `PASS`, `SYST`, dan `QUIT`.

## Topologi

```text
TCP Client → Kali Proxy (10.10.10.1:9000) → TCP Server (10.10.10.2:9999)

UDP Client → Kali Proxy (10.10.10.1:9000) → UDP Server (10.10.10.2:9997)

FTP Client → Kali Proxy (10.10.10.1:9000) → FTP Server (10.10.10.2:2121)
```

Kali bertindak sebagai proxy.  
`server01` bertindak sebagai server tujuan.

## File

| Mesin | File | Fungsi |
|---|---|---|
| `server01` / `10.10.10.2` | `echo_server.py` | Server TCP untuk test forwarding TCP |
| `server01` / `10.10.10.2` | `udp-server.py` | Server UDP untuk test forwarding UDP |
| Kali / `10.10.10.1` | `proxy.py` | Proxy TCP dan UDP dengan output hex dump |

## Test TCP dan UDP

Testing TCP dan UDP dilakukan lebih dulu untuk memastikan proxy dapat menerima data dari client, meneruskannya ke server, menerima respons server, lalu mengembalikannya ke client.

### Jalankan server UDP

Di `server01`:

![udp](UDP-PROXY.png)

```bash
python3 udp-server.py
```

UDP server berjalan pada:

```text
0.0.0.0:9997
```

### Jalankan server TCP

![TCP](TCP-proxy.png)

Di `server01`:

```bash
python3 echo_server.py
```

TCP server berjalan pada:

```text
0.0.0.0:9999
```

### Jalankan proxy TCP dan UDP

Di Kali:

```bash
python3 proxy.py --mode both --local-host 10.10.10.1 --local-port 9000 --remote-host 10.10.10.2 --remote-tcp-port 9999 --remote-udp-port 9997
```

Proxy menerima koneksi pada:

```text
TCP Proxy: 10.10.10.1:9000
UDP Proxy: 10.10.10.1:9000
```

Lalu meneruskan data ke:

```text
TCP Tujuan: 10.10.10.2:9999
UDP Tujuan: 10.10.10.2:9997
```

### Test TCP

Di terminal Kali lain:

```bash
nc 10.10.10.1 9000
```

Ketik:

```text
Hallo TCP
```

Alur yang terjadi:

![tcp](tcp-testing-proxy.png)

```text
netcat → proxy TCP → echo_server TCP
echo_server TCP → proxy TCP → netcat
```

### Test UDP

Di terminal Kali lain:

```bash
nc -u 10.10.10.1 9000
```

Ketik:

```text
Hallo UDP
```

Alur yang terjadi:

![udp](udp-testing-proxy.png)

```text
netcat UDP → proxy UDP → udp-server
udp-server → proxy UDP → netcat UDP
```

### Hasil yang dilihat di proxy

Proxy menampilkan data dari dua arah:

```text
[TCP CLIENT -> SERVER]
[TCP SERVER -> CLIENT]

[UDP CLIENT -> SERVER]
[UDP SERVER -> CLIENT]
```

Data ditampilkan dalam hexadecimal dan ASCII:

```text
48 61 6C 6C 6F = Hallo
0A = Enter / newline
```

Bagian ini membuktikan bahwa proxy dapat membaca data yang dilewatkan oleh client dan server.

## Testing FTP melalui Proxy

Setelah TCP forwarding bekerja, proxy TCP digunakan untuk melihat komunikasi FTP.

Pada FTP, client tidak langsung terhubung ke FTP server. Client terhubung ke proxy Kali, lalu proxy meneruskan koneksi tersebut ke FTP server di `server01`.

```text
FTP Client → Kali Proxy → FTP Server
```

Tujuan testing FTP adalah melihat command login dan respons server secara langsung melalui output hex dump proxy.

### Jalankan FTP server

Di `server01`:

```bash
python3 -m pyftpdlib -p 2121
```

FTP server berjalan pada:

```text
0.0.0.0:2121
```

### Jalankan proxy untuk FTP

Di Kali:

```bash
python3 proxy.py --mode tcp --local-host 10.10.10.1 --local-port 9000 --remote-host 10.10.10.2 --remote-tcp-port 2121 --receive-first
```

Arti konfigurasi tersebut:

```text
Proxy menerima koneksi FTP pada Kali: 10.10.10.1:9000
Proxy meneruskan koneksi ke FTP server: 10.10.10.2:2121
--receive-first digunakan agar banner FTP dari server diterima lebih dahulu
```

### Connect ke FTP melalui proxy

Di terminal Kali lain:

```bash
nc -C 10.10.10.1 9000
```

Opsi `-C` digunakan agar `nc` mengirim akhir baris sebagai `CRLF`:

```text
CRLF = 0D 0A
```

FTP membutuhkan `CRLF`, bukan hanya `LF`:

```text
LF saja: 0A
CRLF FTP: 0D 0A
```

Ketik command berikut satu per satu:

```text
USER anonymous
PASS test@test.com
SYST
QUIT
```

## Hasil Testing FTP

![ftp](FTP-proxy.png)

![ftp](FTPs-proxy.png)

Client menerima respons dari FTP server:

```text
220 pyftpdlib 2.2.0 ready.
331 Username ok, send password.
230 Login successful.
215 UNIX Type: L8
221 Goodbye.
```

Proxy memperlihatkan komunikasi FTP dua arah:

```text
[TCP SERVER -> CLIENT]
220 pyftpdlib 2.2.0 ready.

[TCP CLIENT -> SERVER]
USER anonymous

[TCP SERVER -> CLIENT]
331 Username ok, send password.

[TCP CLIENT -> SERVER]
PASS test@test.com

[TCP SERVER -> CLIENT]
230 Login successful.
```

Contoh data FTP dalam hexadecimal:

```text
USER anonymous
55 53 45 52 20 61 6E 6F 6E 79 6D 6F 75 73 0D 0A

PASS test@test.com
50 41 53 53 20 74 65 73 74 40 74 65 73 74 2E 63 6F 6D 0D 0A
```

## Yang Dipelajari dari Source Code

Proxy dibuat dengan Python untuk menerima data dari client, menampilkan data dalam hex dump, lalu meneruskannya ke server.

```text
TCP:
client → proxy → server
server → proxy → client

UDP:
client → proxy → server
server → proxy → client
```
## Komponen Source Code

### `echo_server.py`

| Komponen | Fungsi |
|---|---|
| `socket.AF_INET` | Menggunakan alamat IPv4 |
| `socket.SOCK_STREAM` | Membuat echo server TCP |
| `socket.SOCK_DGRAM` | Membuat echo server UDP |
| `bind()` | Menempelkan server ke `0.0.0.0:9999` |
| `listen()` | Menunggu koneksi TCP |
| `accept()` | Menerima koneksi TCP dari client |
| `recv()` | Menerima data TCP |
| `sendall()` | Mengirim respons TCP |
| `recvfrom()` | Menerima data UDP dan alamat client |
| `sendto()` | Mengirim respons UDP |
| `threading.Thread()` | Menjalankan UDP server dan handler TCP secara terpisah |

### `proxy.py`

| Komponen | Fungsi |
|---|---|
| `argparse` | Membaca mode proxy, host, port, dan timeout dari command line |
| `socket.AF_INET` | Menggunakan alamat IPv4 |
| `socket.SOCK_STREAM` | Membuat proxy TCP |
| `socket.SOCK_DGRAM` | Membuat proxy UDP |
| `create_connection()` | Menghubungkan proxy TCP ke remote server |
| `bind()` | Menempelkan proxy ke IP dan port lokal |
| `listen()` | Menunggu koneksi TCP dari client |
| `accept()` | Menerima koneksi TCP dari client |
| `recv()` | Menerima data TCP dari client atau server |
| `sendall()` | Meneruskan data TCP |
| `recvfrom()` | Menerima data UDP dari client |
| `send()` | Mengirim data UDP ke remote server |
| `sendto()` | Mengirim respons UDP kembali ke client |
| `select.select()` | Menunggu data TCP dari sisi client atau server |
| `threading.Thread()` | Menangani koneksi TCP dan request UDP secara terpisah |
| `hexdump()` | Menampilkan payload dalam hexadecimal dan ASCII |
| `--receive-first` | Menerima banner FTP sebelum client mengirim command |

## Kesimpulan

Lab ini melatih cara kerja proxy jaringan: menerima koneksi dari client, meneruskan data ke server, menerima respons server, lalu mengirimkannya kembali ke client.

Testing TCP dan UDP digunakan untuk membuktikan bahwa proxy mendukung dua jenis transport protocol.

Testing FTP digunakan untuk melihat isi komunikasi TCP secara nyata. Proxy berhasil menangkap banner FTP, command `USER`, `PASS`, `SYST`, `QUIT`, serta respons server.

Hal penting yang ditemukan saat testing FTP adalah command FTP harus diakhiri dengan `CRLF` (`0D 0A`). Karena itu digunakan `nc -C`, bukan `nc` biasa.

## Referensi

- [From aw-junaid Black Hat Python Explain & Practice](https://github.com/aw-junaid/Black-Hat-Python/tree/main)
- [My source code network basic](https://github.com/iMoon07/OWASP-Lab-Toolkit/tree/main/network-hacking-basic-code)

---

Terimakasih.
