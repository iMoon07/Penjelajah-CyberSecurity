# SSH Client-Server Experiments with Python Paramiko

[🇮🇩 Baca dalam Bahasa Indonesia](ssh-client-server-python-id.md)

In this experiment, I tried to build and test a simple SSH client and SSH server using Python and Paramiko.
Paramiko is a Python library that implements the SSHv2 protocol. It can be used to create both SSH clients and SSH servers directly in Python programs.

In an SSH connection, Paramiko handles communication between the client and server, including authentication, data exchange through SSH channels, and host keys for server identity. Paramiko also uses the `cryptography` library for the cryptographic functions required by SSH.

This implementation is still intended for lab use. The code is not stable for production use, and the credentials are still hardcoded.

## Lab Topology

The test was conducted using two machines in a lab network. The client runs a Python script with Paramiko to create an SSH connection to the Ubuntu server.

```text
Client: Kali Linux
IP: 10.10.10.1
Role: SSH Client
       |
       | 1. SSH handshake and host key verification
       | 2. Algorithm negotiation and encrypted session creation
       | 3. Username and password authentication
       | 4. SSH channel: command and output
       |
       | SSH encrypted connection
       | Port 22   : OpenSSH Ubuntu
       | Port 2222 : Custom Paramiko SSH server
       |
Server: Ubuntu
IP: 10.10.10.2
Role: SSH Server
```

Before a command is sent, SSH creates an encrypted session between the client and server. The server uses a host key as its identity, while Paramiko uses the `cryptography` library for the cryptographic functions required by SSH.

![enkripsi](enkripsi.png)

This can be seen in the packet capture result. Captured SSH traffic does not display passwords, commands, or server output as plaintext. The data appears as encrypted traffic because the communication between the client and server is protected by the SSH session.

After the encrypted connection and authentication are established, the client can open an SSH channel to send commands and receive output from the server.

The test consists of three parts:

- Running a single command through an SSH client
- Creating an interactive SSH shell session
- Running a simple SSH server on port `2222`

## Single Command Execution

The first test uses `ssh_cmd.py` to connect to the server and run a single command.

![ssh](testing-ssh-cmd.png)

The client successfully connected to `10.10.10.2` on port `22`, ran the `id` command, and received the output from the server.

## Interactive SSH Shell

The second test uses `ssh_rcmd.py`. Unlike the previous script, the connection remains open so multiple commands can be executed in a single SSH session.

![ssh])(testing-interactive-ssh.png)

After the connection is established, commands can be sent through the shell. The server side runs `ssh_server.py` on port `2222`.

When the client connects, the server receives the connection from the client IP address and performs authentication.

The result shows that the client can create an SSH session to the server on port `2222`, pass authentication, send commands, and receive command output through an SSH channel.

## Code Components

| File | Module / Paramiko | Used for |
|---|---|---|
| `ssh_cmd.py` | `getpass` | Requests a password without displaying the input in the terminal |
| `ssh_cmd.py` | `paramiko.SSHClient()` | Creates an SSH client |
| `ssh_cmd.py` | `AutoAddPolicy()` | Accepts the server host key in the lab environment |
| `ssh_cmd.py` | `client.connect()` | Creates a connection to the SSH server |
| `ssh_cmd.py` | `client.exec_command()` | Runs a single command on the server |
| `ssh_cmd.py` | `stdout.read()` | Reads command output from the server |
| `ssh_cmd.py` | `recv_exit_status()` | Reads the command exit status |
| `ssh_rcmd.py` | `getpass` | Requests a password without displaying the input in the terminal |
| `ssh_rcmd.py` | `threading` | Receives server output while waiting for command input |
| `ssh_rcmd.py` | `paramiko.SSHClient()` | Creates an SSH client |
| `ssh_rcmd.py` | `client.connect()` | Creates a connection to the SSH server |
| `ssh_rcmd.py` | `client.invoke_shell()` | Opens an interactive SSH shell |
| `ssh_rcmd.py` | `chan.send()` | Sends commands to the server |
| `ssh_rcmd.py` | `chan.recv()` | Receives output from the server |
| `ssh_server.py` | `socket` | Creates a TCP server on port `2222` |
| `ssh_server.py` | `paramiko.RSAKey()` | Loads the SSH server host key |
| `ssh_server.py` | `paramiko.ServerInterface` | Creates a class to handle the SSH server |
| `ssh_server.py` | `check_auth_password()` | Checks the client username and password |
| `ssh_server.py` | `paramiko.Transport()` | Handles the SSH connection from the client |
| `ssh_server.py` | `transport.start_server()` | Starts the SSH service on the client connection |
| `ssh_server.py` | `transport.accept()` | Accepts an SSH channel from the client |
| `ssh_server.py` | `chan.recv()` | Receives commands from the client |
| `ssh_server.py` | `subprocess.run()` | Runs commands on the server |
| `ssh_server.py` | `chan.send()` | Sends command output back to the client |
| `ssh_server.py` | `threading` | Handles the client session in a separate thread |

## Conclusion

Previously, I experimented with basic client-server communication using Netcat to understand sockets, TCP connections, data transfer, and remote commands. However, commands and output in a standard Netcat connection can appear as plaintext when the traffic is captured on the network.

This experiment follows the **SSH with Paramiko** discussion from *Black Hat Python*. Paramiko is used to build SSH clients and a server: `ssh_cmd.py` runs a single command, `ssh_rcmd.py` creates an interactive shell, and `ssh_server.py` accepts connections, performs authentication, and handles commands from the client.

Paramiko implements SSHv2 and uses the `cryptography` library. The TShark capture shows that after the SSH session is established, commands, passwords, and output are no longer visible as plaintext and instead appear as `Encrypted packet`.

This test focuses on the SSH connection and packet capture, not on firewall, IDS, or network monitoring testing. However, in such environments, the following information may still be visible:

- Client and server IP addresses
- Source and destination ports
- TCP handshake
- SSH banner
- Packet direction, size, count, and duration
- Traffic shown as `Encrypted packet`

SSH can protect the content of communication, but it does not hide the existence of the connection on the network. This experiment provides a foundation for understanding SSH tunneling and pivoting in later stages.

## References

- [Paramiko Documentation](https://docs.paramiko.org/en/stable/)
- [Source Code](https://github.com/iMoon07/OWASP-Lab-Toolkit/tree/main/network-hacking-basic-code)
