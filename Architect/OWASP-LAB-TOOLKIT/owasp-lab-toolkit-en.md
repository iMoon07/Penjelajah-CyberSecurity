# Build Your Own Hacking Dojo: OWASP Lab Toolkit

[🇮🇩 Baca dalam Bahasa Indonesia](owasp-lab-toolkit-id.md)

Hello Cybersecurity Explorers, how is everyone doing? Nice to meet you, this is my very first post on this blog. Moving forward, this Web Blog will contain my notes as I explore and dive deep into the world of hacking and cybersecurity. I hope this can be useful for all of us to learn and grow together.

I want to share a tool that's quite useful for friends who are currently learning web application pentesting. This tool is the OWASP Lab Toolkit, a tool that makes it easy for us to create a web application lab for hacking and cybersecurity learning.

I built this tool using several famous references and resources that are used in the Cyber Security Industry as training grounds (I call it *like a dojo hacking*).

Here are the vulnerable apps (*vulnerable apps*) and supporting *tools* that I integrated into the OWASP Lab Toolkit:

- OWASP Juice Shop - [owasp.org/www-project-juice-shop](https://owasp.org/www-project-juice-shop/)
- OWASP Mutillidae II - [itsecgames.com](http://itsecgames.com/)
- OWASP WebGoat & WebWolf - [owasp.org/www-project-webgoat](https://owasp.org/www-project-webgoat/)
- DVWA (Damn Vulnerable Web App) - [github.com/digininja/DVWA](https://github.com/digininja/DVWA)
- bWAPP (buggy web application) - [itsecbbq.org/bwapp](http://www.itsecbbq.org/bwapp/)
- XVWA (Xtreme Vulnerable Web Application) - [github.com/s4n7h0/xvwa](https://github.com/s4n7h0/xvwa)
- VWA (Vulnerable Web Application) - [github.com/hummingbirdscyber/Vulnerable-Web-Application](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

So what is required to be able to do labs and practice?

- VMware Workstation Pro (You can also use VirtualBox)
- Operating System Ubuntu 24.04 LTS (Currently the tool still supports the Ubuntu Linux based ecosystem, in the future it will be updated for other OS)
- Specifications RAM 2GB - 1vCPU - Disk 20GB
- Notepad (Used to write the hosts file if on Windows)
- Tools OWASP Lab Toolkit - https://github.com/iMoon07/OWASP-Lab-Toolkit

### Installation & Setup Guide

The installation process is super easy since everything is already automated using a *bash script*. Just follow these steps:

#### 1. Clone the Repository

Open the terminal on your Ubuntu Server machine, then run this command to download the *toolkit*:
```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

#### 2. Run the Installer

Run the main *script* using `sudo` access. This *script* will take a few minutes because it installs all the components (Web Server, Database, Node.js, Java) and clones the applications automatically.
```bash
sudo ./install-owasp-lab.sh
```

#### 3. Configure the Hosts File

So we can access the lab using cool local domains (like `dvwa.owasp.hacking`), we must route those domains to our Ubuntu Server's IP Address.
- On Windows, open **Notepad** as an *Administrator*.
- Open the file at this path: `C:\Windows\System32\drivers\etc\hosts`.
- Add the following line at the very bottom (Replace the IP Address `[IP_ADDRESS]` with your Ubuntu Server's IP):
```text
[IP_ADDRESS] dvwa.owasp.hacking bwapp.owasp.hacking juiceshop.owasp.hacking
```

![Windows Hosts File Configuration](Input%20Hosts.png)

#### 4. Verify Lab Status

To make sure all services are running normally (HTTP 200 OK), use the built-in *health checker script*:
```bash
sudo ./check-owasp-lab.sh
```
Choose option 1 to check HTTP connections. Make sure everything is colored green (NORMAL).

![Endpoints UP Status](Endpoints-UP.png)

### Start Exploring!

Once all the statuses are green, you can directly open the browser on your main machine and start learning *penetration testing*!

![Application Overview](Overview.png)

Enjoy learning and get safe hacking !

Enjoy *labbing* and growing together! If this *toolkit* is deemed useful to accompany your *cybersecurity* journey, don't hesitate to drop by my GitHub and leave a ⭐ (Star)!

If there are any obstacles during installation, getting an *error*, or wanting to *request* other vulnerable apps for the next *update*, you are free to discuss and ask questions in the comments column below. Let's learn together! 👇
