# Socket Programming Experiments with Python

Last night, I read **Black Hat Python, 2nd Edition** by Justin Seitz and Tim Arnold. In the early part of the book, I found a discussion about network programming: TCP, UDP, sockets, and a simple Netcat implementation using Python.

![books](books.png)

I am trying to get into programming. Network programming feels interesting as a starting point for me to practice what is in the book by writing one program as a server, another program as a client, and allowing both of them to send data to each other through an IP address and port.

I use Python as an initial step to understand sockets and network communication. After understanding the basics better, I want to try the same concepts using C.

## Lab

| Machine | IP | Role |
| :-- | :-- | :-- |
| Kali Linux | `10.10.10.1` | Client |
| Ubuntu Server01 | `10.10.10.2` | Server |

```text
Kali Linux  →  TCP / UDP  →  Ubuntu Server01
10.10.10.1                   10.10.10.2
```

## Experiments

| File | Function |
| :-- | :-- |
| `tcp-client.py` | TCP client |
| `tcp-server.py` | TCP server |
| `udp-client.py` | UDP client |
| `udp-server.py` | UDP server |
| `netcat.py` | Netcat from the book source code |

## What I Learned

| Section | TCP | UDP |
| :-- | :-- | :-- |
| Socket type | `socket.SOCK_STREAM` | `socket.SOCK_DGRAM` |
| Client flow | `connect() → send() → recv()` | `sendto() → recvfrom()` |
| Server flow | `bind() → listen() → accept() → recv()` | `bind() → recvfrom() → sendto()` |
| Connection | Must establish a connection first | Does not need to establish a persistent connection |
| Data | Byte stream | Datagram / packet data |

---

The book suggests why practicing basic network hacking is important, because it can help me perform better when conducting penetration testing by understanding the flow of how programs and servers work. Understanding server requests and responses is something that I have not explored much yet.

I also explored several important Python network socket syntaxes, such as the difference between TCP and UDP protocols. I can also see the difference from the code side, such as:

![tcp](tcp.png)

![udp](udp.png)

- for UDP `server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
- for TCP `server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`

- TCP establishes a connection first, then sends and receives data.
- UDP sends data directly to the destination without establishing a connection first.


At the moment, I have not yet seen the packet side while it is running.

Okay

Then, the Netcat program is not fully developed yet. I am still trying to explore the network side and create space such as:

![netcat](netcat-python.png)

- TCP connection between client and server.
- Sending and receiving data using send() and recv().
- Server mode using bind(), listen(), and accept().
- A simple command shell and program option configuration using argparse.

Next, I want to run this source code while capturing traffic with `tcpdump` or Wireshark, so I can see the relationship between:

```text
Python source
→ socket
→ TCP / UDP packet
→ network traffic
```

All experiments were conducted in a local lab.