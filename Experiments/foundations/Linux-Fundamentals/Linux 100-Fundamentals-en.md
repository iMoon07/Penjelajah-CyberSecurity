# Linux 100-Fundamentals from TCM Security

Now i want to share here learning practical Linux from TCM Security Academy.

## What is Linux?

Linux is a open-source operating system that serves as the fondation for various distributions (or "distros") like Ubuntu, Fedora, and Debian. Here's what makes Linux unique:

- Kernel-based
- Open-source
- Multi-platform
- Customizable
- Community-driven
- Security and Stable

## Why Learn Linux?

- Beyond to basics
  - Pentester (Active Directory, Web/Mobile/Api, Wireless/IOT, etc)
- Hacking Basics
  - Flow Post Exploitation
- Security deffend
  - Investigation and audit about a configuration landing
- Foundational Skills
  - Basic IT/OT Skills like a (Network, Linux Operating System, Coding/Automation scripting for programmer, and fast to work for security and Developer)
- Industry Standard
- Career Opportunities
- Security and stability
- Customizable
- Efficient for hardware resource

## What We'll Cover

This course is meant to be a crash course, which is why it's marked level 100. By the end of this course, you'll be comfortable with the core basics of Linux, including the following topics:

- Linux Distributions
- How to install Linux
- Exploring Linux
- Sudo
- Navigating the File System
- Users & Privileges
- Common Network Commands
- Viewing, Creating, & Editing Files
- Starting & Stopping services
- Installing and Updating Tools
- Scripting with bash

## Introduction

### Linux Distribution

- [List of Linux Distributions](https://en.wikipedia.org/wiki/List_of_Linux_distributions)

- [DistroWatch](https://distrowatch.com/)

- [Ubuntu](https://ubuntu.com/)

- [Kali](https://www.kali.org/)

- [CentOS](https://www.centos.org/)

## Setting Up Our Lab

### Installing VMWare

[Download VMWare](https://broadcom.com)

### Installing Linux

[Download Kali](https://www.kali.org/get-kali/#kali-virtual-machines)

[Download 7zip](https://www.7-zip.org/download.html)

## Introduction To Linux

### Exploring Linux

Kali Linux is a specialized Linux distribution designed for digital forensics, penetration testing, and ethical hacking purposes. It is a powerfull and widely used operating system used by cybersecurity professionals, researchers, and enthusiasts.

Kali Linux is based on Debian Linux. It provides a comprehensive set of pre-installed tools and software packages specifically tailored for various security testing and hacking purposes.

The main goal of Kali Linux is to provide a robust and all-in-one platform for performing security assesments, vulnerability analysis, network scanning, password cracking, wireless security testing, and much more. It includes tools for web application testing, reverse engineering, exploit development, and secure communication as well.

Kali Linux is designed with security in mind and comes with features like full disk encryption, secure shell access, and regular updates to ensure a secure and up-to-date environment for its users.

While Kali Linux is a powerful tool for security professionals, it is important to use it responsibly and within legal boundaries. Ethical Hacking and security testing should always be performed with proper authorization and adherence to applicable and regulations.

### Sudo Overview

The `sudo` command in Linux allows a user with appropriate privileges to execute commands as a superuser or another user. It is commonly used to perform administrative tasks that require elevated privileges. Here's an example of how `sudo` is used:

Let's say you want to install a software package using the `apt` package manager, but it requires administrative privileges. You can use `sudo` to execute the `apt` command with elevated privileges. Here's the command:

`sudo apt isntall <package_name>`

For instance, if you want to install package named "nginx" on an Ubuntu system, you can use the following command:

`sudo apt install nginx`

After running this command, you will be prompted to enter your passwor. Once you provide the correct password, the command will be executed with superuser privileges, allowing you to install the "nginx" package on the system.

Please note that the availability and configuration of `sudo` can vary depending on the Linux distribution and the user's privileges. Additionally, the `sudo` command can be used for various other administrative tasks, such as editing system files, managing services, and executing critical commands.

### Navigating the File System

Here are explanations and examples of the commands mentioned in this video:

`pwd` (Print Working Directory)
  - Explanation: Displays the current working directory
  - Example: Running `pwd` in the terminal would show the absolute path of the current diretory such as `"/home/user/documents"`

`cd` (Change Directory)
  - Explanation: Allows you to change the current working directory.
  - Example: Running `cd /home/user/documents` would change the directory to `"/home/user/documents"`.

`cd ..` (Change to parent Directory):
  - Explanation: Moves up one level in the directory hierarchy.
  - Example: Running `cd ..` in `"home/user/documents"` would move to the `"/home/user"` directory.

`ls` (List Directory Contens):
  - Explanation: Lists the files and directories in the current directory.
  - Example: Running `ls` would display the files and directories in the current directory.

`ls -la` (List Detailed Directory Contents):
  - Explanation: Lists detailed information about files and directories, including hidden files.
  - Example: Running `ls -la` would display a detailed list of files and directories, including hidden files, in the current directory.

