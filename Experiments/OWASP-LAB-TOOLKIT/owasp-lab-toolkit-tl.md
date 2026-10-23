# Build Your Own Hacking Dojo: OWASP Lab Toolkit

[🇬🇧 Read in English](owasp-lab-toolkit-en.md)  
[🇮🇩 Baca dalam Bahasa Indonesia](owasp-lab-toolkit-id.md)  
[🇲🇾 Baca dalam Bahasa Melayu](owasp-lab-toolkit-ms.md)

Ito ang unang artikulo sa blog ko, kung saan dinodokumento ko ang mga exploration, experiment, at development ko sa field ng cybersecurity.

![Skull](skull.jpg)

Sa pagkakataong ito, ibinabahagi ko ang **OWASP Lab Toolkit**, isang Bash-based toolkit para awtomatikong i-set up ang web application security testing environment. Isinasama ng toolkit ang iba’t ibang intentionally vulnerable web applications sa isang lab, para mas praktikal ang installation at management.

## Mga Lab Component

Isinasama ng toolkit ang ilang application at service para sa web security testing:

- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [OWASP Mutillidae II](https://owasp.org/www-project-mutillidae-ii/)
- [OWASP WebGoat & WebWolf](https://owasp.org/www-project-webgoat/)
- [DVWA](https://github.com/digininja/DVWA)
- [bWAPP](http://www.itsecgames.com/)
- [XVWA](https://github.com/s4n7h0/xvwa)
- [VWA](https://github.com/hummingbirdscyber/Vulnerable-Web-Application)

Bukod sa mga application na ito, nagbibigay din ang toolkit ng supporting services tulad ng web server at database, kabilang ang database administration interface depende sa installation configuration.

## Mga Requirement

- **Virtualization:** VMware Workstation Pro o VirtualBox.
- **Operating system:** Ubuntu Server 24.04 LTS.
- **Target minimum specs:** 2 GB RAM, 1 vCPU, at 20 GB disk.
- **Lab access:** browser sa client machine at configuration ng `hosts` file.
- **Toolkit:** [OWASP Lab Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit).

Sa kasalukuyan, nakafocus ang operating system support sa Ubuntu-based Linux environments.

## Installation at Configuration

### 1. I-clone ang repository

Patakbuhin ang mga sumusunod na command sa Ubuntu Server terminal:

```bash
git clone https://github.com/iMoon07/OWASP-Lab-Toolkit.git
cd OWASP-Lab-Toolkit
chmod +x *.sh
```

### 2. Patakbuhin ang installer

```bash
sudo ./install-owasp-lab.sh
```

Ise-set up ng installer ang mga kinakailangang component at ida-download ang mga application base sa toolkit configuration. Depende sa internet connection at machine resources ang oras ng installation.

### 3. I-configure ang `hosts` file

Para ma-access ang bawat application gamit ang local domain, i-point ang lab domains sa IP ng Ubuntu Server.

Sa halimbawang ito, `10.10.10.2` ang IP ng server. Siguraduhing ginagamit nga ng server ang IP na iyon at accessible ito mula sa client machine.

**Linux**

Buksan ang hosts file:

```bash
sudo nano /etc/hosts
```

Idagdag ang mga sumusunod na linya:

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

I-save gamit ang `Ctrl + O`, pindutin ang `Enter`, pagkatapos ay lumabas gamit ang `Ctrl + X`.

**Windows 10**

1. Hanapin ang Notepad, pagkatapos ay piliin ang **Run as administrator**.
2. Buksan ang sumusunod na file:

   `C:\Windows\System32\drivers\etc\hosts`

3. Palitan ang file filter ng *All Files* kung hindi nakikita ang `hosts` file.
4. Idagdag ang parehong domain list mula sa Linux configuration sa itaas.
5. I-save ang file nang walang karagdagang extension.

![Windows Hosts File Configuration](Input%20Hosts.png)

**Pagdaragdag ng bagong domain**

Kung may bagong application sa hinaharap, idagdag ang domain nito gamit ang format:

```text
10.10.10.2 application-name.owasp.hacking
```

Halimbawa, kung gusto mong magdagdag ng `newlab.owasp.hacking`:

```text
10.10.10.2 newlab.owasp.hacking
```

I-save ang mga pagbabago sa `hosts` file. Hindi na kailangang gumawa ng bagong entry kung naka-register na ang domain.

> **Note:** Ang `hosts` list ay nagpo-point lamang ng domain name sa server IP. Kailangan pa ring suportahan ng bawat domain ang tamang virtual host configuration, reverse proxy, o routing mechanism. Siguraduhin ding naka-configure nang tama ang application port. Ang domain na wala pa sa server ay hindi awtomatikong magiging accessible na application.

### 4. I-verify ang mga service

Pagkatapos ng installation, patakbuhin ang health checker:

```bash
sudo ./check-owasp-lab.sh
```

Piliin ang option `1` para i-check ang HTTP connection. Siguraduhing normal ang status ng mga expected active endpoints.

![Endpoints UP Status](Endpoints-UP.png)

## Simulan ang Exploration

![Application Overview](Overview.png)

Kapag handa na ang mga service, buksan ang browser mula sa client machine at i-access ang mga application gamit ang mga na-configure na domain. May sariling environment ang bawat application para subukan ang behavior at web security vulnerabilities.

Gamitin ang lab na ito sa environment na kontrolado mo, hindi sa sistema ng ibang tao nang walang pahintulot.

## Pangwakas

Binuo ko ang OWASP Lab Toolkit para gawing mas simple ang pag-set up ng web application security testing environment. Malugod na tinatanggap ang feedback, bug reports, at mga suhestiyon para sa iba pang application integrations.

Repository: [iMoon07/OWASP-Lab-Toolkit](https://github.com/iMoon07/OWASP-Lab-Toolkit)

Kung nakatagpo ka ng installation issue o may gusto kang i-suggest na susunod na development, mag-open ng *issue* o mag-discuss sa comments section.

Happy experimenting.
