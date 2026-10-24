# Basic Network Tracing: TCP dan UDP

[🇬🇧 Read in English](trace-network-basic-en.md)

Di sini saya berlatih melakukan tracing komunikasi TCP dan UDP antara Kali (`10.10.10.1`) sebagai client dan Ubuntu (`10.10.10.2`) sebagai server.

Ini adalah lanjutan dari tulisan sebelumnya tentang [`Socket Programming Experiments with Python`](https://imoon07.github.io/read.html?post=network-hacking-basic)

- `strace` digunakan di Ubuntu untuk melihat system call jaringan yang dipanggil oleh proses server.
- `tshark` digunakan di Kali untuk melihat paket yang dikirim dan diterima melalui jaringan.
- `tcp-client.py` dan `udp-client.py` digunakan sebagai client untuk menguji server TCP dan UDP.
- `netcat.py` digunakan dalam lab untuk menguji koneksi TCP interaktif pada server.

Tracing membantu saya melihat proses program, system call, dan paket jaringan saat client dan server berkomunikasi. Dengan ini, saya dapat memastikan server membuka port, menerima data, dan mengirim respons.

Latihan ini membangun alur troubleshooting untuk menentukan masalah pada client, jaringan, socket/kernel, atau logika server, serta menganalisis koneksi abnormal, reset, dan kegagalan respons.

---

## Trace TCP Server–Client

Ubuntu:
```bash
strace -f -e trace=%network python3 tcp-server.py
```
Kali:
```bash
sudo tshark -i vmnet1 -f "tcp port 9998"
python3 tcp-client.py
```
![trace-tcp](trace-tcp.png)

```bash
strace server:
socket()                         membuat TCP socket
bind(0.0.0.0:9998)               memakai port TCP 9998
listen()                         menunggu koneksi
accept4(10.10.10.1:54958)        menerima koneksi dari Kali
recvfrom("AAABBBCCC") = 9        menerima 9 byte payload
sendto("ACK") = 3                mengirim respons 3 byte
```

| Frame | Arah | Flag / Data | Keterangan |
|---:|---|---|---|
| 1 | Kali → Ubuntu | `SYN` | Client meminta koneksi |
| 2 | Ubuntu → Kali | `SYN, ACK` | Server menerima koneksi |
| 3 | Kali → Ubuntu | `ACK` | Handshake selesai |
| 4 | Kali → Ubuntu | `PSH, ACK`, `Len=9` | Client mengirim `AAABBBCCC` |
| 5 | Ubuntu → Kali | `ACK` | Server mengakui data client |
| 6 | Ubuntu → Kali | `PSH, ACK`, `Len=3` | Server mengirim `ACK` |
| 7 | Kali → Ubuntu | `ACK` | Client mengakui respons server |
| 8 | Kali → Ubuntu | `FIN, ACK` | Client memulai penutupan koneksi |
| 9 | Ubuntu → Kali | `FIN, ACK` | Server menutup koneksi |
| 10 | Kali → Ubuntu | `ACK` | Koneksi ditutup normal |

```text
TCP:
SYN → SYN, ACK → ACK → AAABBBCCC → ACK → FIN → FIN → ACK
```

Koneksi TCP berhasil, client mengirim `AAABBBCCC`, server membalas `ACK`, lalu koneksi ditutup normal.

---

## Trace UDP Server–Client

Ubuntu (`10.10.10.2`) menjalankan UDP server dan `strace`. Kali (`10.10.10.1`) menjalankan `tshark` serta `udp-client.py`.

Ubuntu:

```bash
strace -f -e trace=%network python3 udp-server.py
```

Kali:

```bash
sudo tshark -i vmnet1 -f "udp port 9997"
python3 udp-client.py
```

![trace-udp](trace-udp.png)

```bash
strace server:
socket(AF_INET, SOCK_DGRAM, ...)                  membuat UDP socket
bind(0.0.0.0:9997)                                memakai port UDP 9997
recvfrom(... "AAABBBCCC" ..., 10.10.10.1:57877) = 9
                                                   menerima payload 9 byte dari Kali
sendto(... "ACK" ..., 10.10.10.1:57877) = 3       mengirim respons 3 byte ke Kali
```

| Frame | Arah | Port | Protokol / Data | Keterangan |
|---:|---|---|---|---|
| 1 | Kali `10.10.10.1` → Ubuntu `10.10.10.2` | `57877 → 9997` | UDP, `Len=9`, `AAABBBCCC` | Client mengirim datagram UDP 9 byte ke server |
| 2 | Ubuntu `10.10.10.2` → Kali `10.10.10.1` | `9997 → 57877` | UDP, `Len=3`, `ACK` | Server membalas datagram UDP 3 byte ke client |

```bash
UDP:
AAABBBCCC → ACK
```

UDP tidak memakai `listen()`, `accept()`, handshake, atau proses penutupan koneksi seperti TCP. Client langsung mengirim datagram `AAABBBCCC`, server menerimanya melalui `recvfrom()`, lalu membalas `ACK` melalui `sendto()`.

## Trace Netcat TCP Interactive Command

Ubuntu (`10.10.10.2`) menjalankan listener `netcat.py` dengan `strace`. Kali (`10.10.10.1`) menjalankan client dan `tshark`.

Ubuntu:

```bash
strace -f -e trace=%network python3 netcat.py -l -p 5555 -c
```

Kali:

```bash
sudo tshark -i vmnet1 -f "tcp port 5555"
python3 netcat.py -t 10.10.10.2 -p 5555
```

![net-cat-py-dettach-cmd](netcat-py-dettach-cmd.png)

### Saat client terhubung

```text
strace server:
socket(AF_INET, SOCK_STREAM, ...) = 3
setsockopt(... SO_REUSEADDR ...) = 0
bind(0.0.0.0:5555) = 0
listen(3, 5) = 0
accept4(... 10.10.10.1:54016 ...) = 4
sendto(4, "xyz: #> ", 8, ...) = 8
recvfrom(4, ...
```

| Frame | Arah | Flag / Data | Keterangan |
|---:|---|---|---|
| 1 | Kali `10.10.10.1:54016` → Ubuntu `10.10.10.2:5555` | `SYN` | Client meminta koneksi |
| 2 | Ubuntu → Kali | `SYN, ACK` | Server menerima koneksi |
| 3 | Kali → Ubuntu | `ACK` | TCP handshake selesai |
| 4 | Ubuntu → Kali | `PSH, ACK`, `Len=8` | Server mengirim prompt `xyz: #> ` |
| 5 | Kali → Ubuntu | `ACK` | Client mengakui prompt server |

### Saat client menjalankan `id`

```text
Client:
xyz: #> 
> id

![netcat-cmd-run-id](netcat-cmd-run-id.png)

Server strace:
recvfrom(4, "id\n", 4096, 0, NULL, NULL) = 3
sendto(4, "uid=1000(moon) gid=1000(moon) ...", 103, ...) = 103
sendto(4, "xyz: #> ", 8, ...) = 8
```

| Frame | Arah | Flag / Data | Keterangan |
|---:|---|---|---|
| 6 | Kali → Ubuntu | `PSH, ACK`, `Len=3` | Client mengirim perintah `id\n` |
| 7 | Ubuntu → Kali | `ACK` | Server mengakui 3 byte perintah |
| 8 | Ubuntu → Kali | `PSH, ACK`, `Len=103` | Server mengirim output perintah `id` |
| 9 | Kali → Ubuntu | `ACK` | Client mengakui output perintah |
| 10 | Ubuntu → Kali | `PSH, ACK`, `Len=8` | Server mengirim prompt `xyz: #> ` kembali |
| 11 | Kali → Ubuntu | `ACK` | Client mengakui prompt baru |
| 12 | Kali → Ubuntu | `RST, ACK` | Client dihentikan dengan `Ctrl+C`; koneksi di-reset |

```text
Alur:
TCP handshake → prompt server → id\n → output id → prompt baru → Ctrl+C → RST
```

Perintah `id` dijalankan di Ubuntu oleh user `moon`, terlihat dari output:

```text
uid=1000(moon) gid=1000(moon)
```

`ECONNRESET` di sisi server muncul karena client Kali dihentikan menggunakan `Ctrl+C`, sehingga koneksi TCP di-reset.

---

Terimakasih.