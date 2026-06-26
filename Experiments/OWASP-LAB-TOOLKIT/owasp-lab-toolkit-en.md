# Build Your Own Web Security Lab with OWASP Lab Toolkit

[🇮🇩 Baca dalam Bahasa Indonesia](owasp-lab-toolkit-id.md)

Welcome to Penjelajah CyberSecurity! This is the first article on my blog, where I'll be documenting my learning journey through offensive security, defensive security, and everything in between. I'll be sharing lab setups, hands-on experiments, and technical write-ups that I hope other learners will also find useful.

If you're building a local security lab, this toolkit might save you quite a bit of time. The toolkit automates most of the setup process, allowing you to deploy several intentionally vulnerable web applications with just a few commands.

This project bundles together several well-known intentionally vulnerable web applications into a single installation toolkit, providing a perfect "hacking dojo" for cybersecurity training.

Here are the vulnerable apps and supporting tools currently integrated into the OWASP Lab Toolkit:

- OWASP Juice Shop - [owasp.org/www-project-juice-shop](https://owasp.org/www-project-juice-shop/)
- OWASP Mutillidae II - [owasp.org/www-project-mutillidae-ii](https://owasp.org/www-project-mutillidae-ii/)
- OWASP WebGoat & WebWolf - [owasp.org/www-project-webgoat](https://owasp.org/www-project-webgoat/)
- DVWA (Damn Vulnerable Web App) - [github.com/digininja/DVWA](https://github.com/digininja/DVWA)
- bWAPP (buggy web application) - [itsecgames.com](http://www.itsecgames.com/)
- XVWA (Xtreme Vulnerable Web Application) - [github.com/s4n7h0/xvwa](https://github.com/s4n7h0/xvwa)
- VWA (Vulnerable Web Application) - [github.com/hummingbirdscyber/Vulnerable-Web-Application](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

### Prerequisites

What do you need to get this lab up and running?

- VMware Workstation Pro (VirtualBox works too)
- Ubuntu 24.04 LTS (Currently, the toolkit only supports Ubuntu/Debian-based systems. Support for other OS will be added in future updates)
- Minimum Specs: 2GB RAM - 1 vCPU - 20GB Disk Space
- Notepad (To edit the hosts file if you are on Windows)
- The OWASP Lab Toolkit - https://github.com/iMoon07/OWASP-Lab-Toolkit

### Installation & Setup Guide

The installation process is seamless because everything is automated via a bash script. Follow these steps:

#### 1. Clone the Repository

Open the terminal on your Ubuntu Server and run the following commands to download the toolkit:
```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

#### 2. Run the Installer

Execute the main script with `sudo` privileges. This process will take a few minutes as it automatically installs all necessary dependencies (Web Server, Database, Node.js, Java) and clones the applications.
```bash
sudo ./install-owasp-lab.sh
```

#### 3. Configure the Hosts File

To access the labs using clean local domains (e.g., `dvwa.owasp.hacking`), you need to route those domains to your Ubuntu Server's IP address.
- On Windows, open **Notepad** as an *Administrator*.
- Open the file located at: `C:\Windows\System32\drivers\etc\hosts`.
- Add the following line at the very bottom (Replace `[IP_ADDRESS]` with your Ubuntu Server's actual IP):
```text
[IP_ADDRESS] dvwa.owasp.hacking bwapp.owasp.hacking juiceshop.owasp.hacking
```

![Windows Hosts File Configuration](Input%20Hosts.png)

#### 4. Verify Lab Status

To ensure all services are running properly (HTTP 200 OK), use the built-in health checker script:
```bash
sudo ./check-owasp-lab.sh
```
Select option `1` to check HTTP connections. Make sure all endpoints return a green `NORMAL` status.

![Endpoints UP Status](Endpoints-UP.png)

### Start Exploring!

Once all statuses are green, open the browser on your host machine and start hacking!

![Application Overview](Overview.png)

Happy hacking and stay safe!

If you find this toolkit helpful for your cybersecurity journey, don't hesitate to drop by my GitHub and leave a ⭐ (Star)!

If you run into any installation issues, encounter errors, or want to request other vulnerable apps for future updates, feel free to drop a comment in the discussion section below. Let's learn together! 👇
