# Single-Tier Server Stack

[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](server-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](server-single-tier-stack-tl.md)

![Single-Tier Server Stack](single-tier-stack.png)

## One Server, One Stack

A **Single-Tier Server Stack** means the [web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [application runtime](https://en.wikipedia.org/wiki/Runtime_system), and [database](https://en.wikipedia.org/wiki/Database) all run on **a single machine**.

Think of a food stall under one roof. The cashier, kitchen, and storage are all in the same place. Everything is handled right there.

## How Does It Work?

When someone visits your website through a [web browser](https://en.wikipedia.org/wiki/Web_browser), here's what happens:

1. **Browser** → Sends an [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) to the server
2. **Web Server** → Receives and routes the request to your app
3. **Application Runtime** → Runs your app's [business logic](https://en.wikipedia.org/wiki/Business_logic) (forms, login, validation, etc.)
4. **Database** → Fetches, adds, updates, or deletes the required data
5. **Response** → The web server returns an [HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) (HTML, JSON, or files) back to the browser

All of this happens on **one machine**.

## Core Components

| Component | Function | Examples |
|---|---|---|
| **[Web Server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server)** | Entry point. Handles requests and returns responses. | [Nginx](https://nginx.org/), [Apache HTTP Server](https://httpd.apache.org/), [Caddy](https://caddyserver.com/) |
| **[Application Runtime](https://en.wikipedia.org/wiki/Runtime_system)** | Runs your application code. | [PHP-FPM](https://www.php.net/manual/en/install.fpm.php), [Node.js](https://nodejs.org/), [Gunicorn](https://gunicorn.org/), [Kestrel (.NET)](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel) |
| **[Database](https://en.wikipedia.org/wiki/Database)** | Stores and manages your app data. | [MariaDB](https://mariadb.org/), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), [SQLite](https://sqlite.org/) |

You can also add a [cache](https://en.wikipedia.org/wiki/Cache_(computing)) like [Redis](https://redis.io/) to speed up frequently accessed data.

## Common Stacks: LAMP, LEMP, WAMP, WIMP, FAMP & More

A [solution stack](https://en.wikipedia.org/wiki/Solution_stack) is a combination of an [operating system](https://en.wikipedia.org/wiki/Operating_system), web server, database, and [programming language/runtime](https://en.wikipedia.org/wiki/Programming_language). These are common examples, not strict rules.

| Acronym | Full Form | Notes |
|---|---|---|
| **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)** | *Linux, Apache, MySQL/MariaDB, PHP/Perl/Python* | The classic stack for dynamic web apps. |
| **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** | *Linux, Nginx, MySQL/MariaDB, PHP-FPM* | LAMP variant using [Nginx](https://nginx.org/) with [PHP-FPM](https://www.php.net/manual/en/install.fpm.php). |
| **[WAMP](https://www.oreilly.com/library/view/learning-php-mysql/9780596157135/ch01.html)** | *Windows, Apache, MySQL/MariaDB, PHP* | Common for local development on [Windows](https://www.microsoft.com/windows). |
| **[WIMP](https://www.itmedia.co.jp/enterprise/articles/0903/17/news004.html)** | *Windows, IIS, MySQL/MariaDB, PHP* | Uses [IIS](https://www.iis.net/) instead of Apache. Note: "WIMP" also has a separate meaning in UI contexts. |
| **[FAMP](https://en.wikipedia.org/wiki/FAMP)** | *FreeBSD, Apache, MySQL/MariaDB, PHP* | [FreeBSD](https://www.freebsd.org/)-based variant. Less common for beginners. |
| **[LAPP](https://www.x386.org/guides/lapp/)** | *Linux, Apache, PostgreSQL, PHP* | LAMP variant using [PostgreSQL](https://www.postgresql.org/). |
| **[LEPP](https://lempstack.com/)** | *Linux, Nginx, PostgreSQL, PHP* | Nginx + PostgreSQL variant. This acronym is less common than LAMP/LEMP and has no single universally accepted definition. Note: "WIMP" also has a separate meaning in UI/computing contexts. |

> **Note:** You can swap MySQL for [MariaDB](https://mariadb.org/), use a different database, or replace PHP with other runtimes like [Node.js](https://nodejs.org/) or [Python](https://www.python.org/).

## Bare Metal, VM, or Container?

| Method | Explanation | References | Notes |
|---|---|---|---|
| **[Bare Metal](https://en.wikipedia.org/wiki/Bare_machine)** | Runs directly on physical hardware. | [IBM — Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers) | Gives direct access to hardware, with performance depending on specs and configuration. |
| **[Virtual Machine (VM)](https://en.wikipedia.org/wiki/Virtual_machine)** | Runs a full OS inside your machine via a hypervisor. | [KVM](https://www.linux-kvm.org/), [VirtualBox](https://www.virtualbox.org/), [VMware](https://www.vmware.com/) | **Best for learning**. Easy to snapshot and reset. |
| **[Container](https://en.wikipedia.org/wiki/Containerization_(computing))** | Isolates the app while sharing the host kernel. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) | Lightweight, fast, and great for local labs. |

## Pros, Cons & SPOF

| Aspect | Explanation |
|---|---|
| **Pros** | Simple, affordable, easy to understand, all in one place, great for learning. |
| **Cons** | Shared resources, config can get mixed, limited scalability. |
| **[SPOF (Single Point of Failure)](https://en.wikipedia.org/wiki/Single_point_of_failure)** | If this single machine goes down, **the web server, application runtime, and database all go down**. The app becomes unreachable. |

## When to Use It & When to Move On

| Situation | Verdict | Notes |
|---|---|---|
| **Learning, practice, prototyping** | **Ideal** | Suitable for understanding how components connect. |
| **Small personal projects** | **Still fine** | Works if kept tidy, monitored, and backed up. |
| **Growing traffic** | **Consider splitting** | Resources will run tight, especially the database. |
| **High uptime / large scale** | **Consider splitting** | A single-tier setup can still be optimized. Splitting tiers should be considered based on availability, capacity, and architecture needs. |

## Tips to Get Started

1. **Focus on the flow** — Master `browser → web server → runtime → database`.
2. **Pick ONE stack** — Start with **[LEMP](https://make.wordpress.org/hosting/handbook/appendix/server-environment/#lemp-stack)** or **[LAMP](https://cloud.google.com/learn/what-is-a-lamp-stack)**. Learn one well first.
3. **Practice locally** — Use a [VM](https://en.wikipedia.org/wiki/Virtual_machine) or [container](https://en.wikipedia.org/wiki/Containerization_(computing)) on your laptop. Stick to `localhost`.
4. **Remember SPOF** — Great for learning, not for always-on, high-availability apps.

**In short:** *Single-tier = everything on one server. Simple to learn, limited in scale. Master this first to understand why splitting becomes necessary.*