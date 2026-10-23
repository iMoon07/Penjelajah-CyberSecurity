# Hardening Single-Tier Stack

[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

This covers **hardening a single-tier stack**. That means all layers—web server, runtime, database, cache—live on one machine, secured from the ground up without covering installation from scratch.

![Hardening single tier stack](linux-exposure-network-experiment.png)

Goals:
- A sensible hardening order
- Reference standards such as CIS
- Security settings per layer
- Verification after hardening
- Common mistakes to avoid

## 1. Core Hardening Principles

Hardening is not a single button. It is a gradual process:

1. **Minimize attack surface** — open only the ports and services you need.
2. **Least privilege** — every service runs as a user that does not need root.
3. **Defense in depth** — firewall, WAF, TLS, logging, all layered.
4. **Update and patch** — an unpatched system is a target.
5. **Monitoring** — you cannot detect what you cannot see.
6. **Recovery** — hardening does not replace backups and recovery plans.

> **Warning:** Never harden directly in production. Always test in a lab or VM first.

## 2. Hardening Standard: CIS

Hardening does not have to be guesswork. There are standards you can use as a reference:

| Standard | Purpose | Relevance for single-tier |
|---|---|---|
| **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** | Secure configuration guides for OS, web servers, databases, Docker, and other products | Concrete reference for securing each layer |
| **[CIS Controls](https://www.cisecurity.org/controls/cis-controls-list)** | 18 prioritized security controls | Big picture: inventory, patching, access control, logging, recovery, incident response |
| **Vendor hardening guides** | Official guides from Debian, Ubuntu, Red Hat, Nginx, MariaDB, PostgreSQL, etc. | Configuration details specific to your distro and software |

Most relevant benchmarks for single-tier:

| Layer | Relevant CIS Benchmark |
|---|---|
| OS | CIS Ubuntu Linux Benchmark, CIS Debian Linux Benchmark, CIS Red Hat Enterprise Linux Benchmark |
| Web server | CIS Nginx Benchmark, CIS Apache HTTP Server Benchmark |
| Database | CIS MariaDB Benchmark, CIS MySQL Benchmark, CIS PostgreSQL Benchmark |
| Container | CIS Docker Benchmark |
| Orchestration | CIS Kubernetes Benchmark, only if the stack grows into Kubernetes |

CIS Benchmarks are secure configuration recommendations developed through security practitioner consensus and available free in PDF for non-commercial use. CIS Controls map those practices into 18 priority controls, from asset inventory to penetration testing. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)

> **Note:** CIS does not mean 100% must be applied. Pick the level that fits your lab or production needs, and document what is applied and what is intentionally skipped.

## 3. Operating System

| Aspect | What to do | Why it matters |
|---|---|---|
| Update and patch | Regularly update OS and packages | Closes known vulnerabilities |
| User and privilege | Don't log in as root; create a regular user with sudo | Limits impact if an account leaks |
| SSH | Disable root login and password auth; use SSH keys | SSH is the main entry point to the server |
| Host firewall | Default deny incoming; open only 22, 80, 443 | Reduces port exposure |
| Auto patch | Enable unattended upgrades for security patches | Keeps the system safe without manual intervention |
| Service minimization | Disable unused services | Fewer services means smaller attack surface |
| Kernel parameters | Apply relevant sysctl hardening | Reduces network-level abuse risk |

> **Important:** Never open database ports (3306, 5432) to the public. The database should only be reachable from localhost or an internal network.

## 4. Services, Files, and Secrets

| Aspect | What to do | Why |
|---|---|---|
| Minimal services | Remove or disable unused services | Reduces entry paths and server load |
| File permissions | Restrict permissions on config, logs, and sensitive files | Prevents unnecessary access |
| Umask | Use strict default permissions | New files are not world-readable by default |
| SELinux/AppArmor | Enable per distro | Limits service behavior if compromised |
| Secrets | Don't put passwords or API keys in repos or world-readable files | Prevents credential leaks |
| Environment variables | Store secrets in tightly permissioned files or a secret manager | Reduces configuration leak risk |

> **Warning:** `.env` files, database credentials, SSH keys, and backups must not go into Git. Use `.gitignore` from the start.

## 5. Web Server Hardening

| Web server | Key settings | Goal |
|---|---|---|
| Nginx | `server_tokens off`, security headers, restrict HTTP methods, disable autoindex | Hide version info and limit dangerous requests |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers | Hide server info and reject dangerous methods |
| Caddy | Security headers, reverse proxy with automatic TLS | Simple config with safe defaults |

Security headers you should have:

- `X-Frame-Options: SAMEORIGIN` — prevents clickjacking
- `X-Content-Type-Options: nosniff` — prevents MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin` — controls referrer leakage
- `Permissions-Policy` — restricts browser feature access

## 6. TLS / HTTPS

| Aspect | Recommendation | Why |
|---|---|---|
| Minimum TLS | TLS 1.2, preferably TLS 1.3 | Older protocols have known flaws |
| Ciphers | Only modern ciphers such as ECDHE and GCM | Prevents downgrade attacks |
| HSTS | Enable with long max-age | Forces HTTPS in the browser |
| Certificates | Let's Encrypt via Certbot, automatic renewal | Free and widely used |
| Sessions | Limit session timeout and consider disabling session tickets | Reduces session reuse risk |

## 7. WAF: Web Application Firewall

| Component | Purpose | Notes |
|---|---|---|
| ModSecurity | WAF engine for Apache/Nginx | Needs tuning to avoid false positives |
| OWASP CRS | Industry-standard rule set | Start in `DetectionOnly` mode |
| Coraza | Go-based alternative WAF | Lightweight, fits modern setups |

> **Warning:** Do not enable WAF blocking mode directly in production. Start in `DetectionOnly`, analyze logs, then enable gradually.

## 8. Database Hardening

| Aspect | What to do | Why |
|---|---|---|
| Secure installation | Run the database's built-in secure installation | Removes anonymous users, test database, remote root |
| Least privilege | Create an app user with limited rights: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | If leaked, impact is limited |
| Bind address | Database only listens on `127.0.0.1` | Database unreachable from outside |
| Password | Use strong passwords; PostgreSQL supports SCRAM-SHA-256 | Prevents brute force |
| Remote access | Disable remote login for database root | Remote root is extremely dangerous |
| Backup | Regular backups and restore tests | Hardening does not protect against human error or disk failure |

## 9. Runtime Hardening

| Runtime | Key settings | Goal |
|---|---|---|
| PHP-FPM | Run as `www-data`; limit `pm.max_children`; disable dangerous functions; `expose_php Off` | Reduces resource abuse and information leaks |
| Node.js | Run as non-root via systemd; use PM2 or a service manager | Process isolation and auto-restart |
| Python | Use virtual environments; run Gunicorn/uWSGI as regular user | Dependency isolation and privilege reduction |
| Java | Set JVM memory limits; run as regular user | Prevents memory exhaustion |
| .NET | Run Kestrel as non-root; use a reverse proxy in front | Process isolation and access control |

## 10. Logging and Monitoring

| Component | Purpose | Why |
|---|---|---|
| `auditd` | Records changes to sensitive files and access | Detects suspicious activity |
| `journald` | Persistent system logging | Incident investigation |
| `logrotate` | Rotates logs so disk doesn't fill | Maintains availability |
| Fail2ban | Blocks IPs after repeated failed logins | Protects SSH and login services |
| Baseline | Record normal state: ports, users, services, logs | Without a baseline, anomalies are hard to spot |

## 11. Backup and Recovery

| Aspect | What to do | Why |
|---|---|---|
| Database backup | Regular, automated backups | App data is the main asset |
| Configuration backup | Back up Nginx/Apache, systemd, firewall, and WAF config | Speeds up server rebuild |
| Restore test | Test restores periodically | An untested backup is not proven usable |
| Recovery runbook | Write recovery steps | During an incident you don't guess from zero |
| Retention | Define how long backups are kept | Balances storage cost and recovery needs |

> **Important:** Backups stored on the same server are still at risk. Keep at least one copy offsite.

## 12. Incident Response

| Phase | What to do |
|---|---|
| Detection | Check SSH, web server, WAF, database, and `auditd` logs |
| Containment | Block IPs, stop infected services, or isolate the VM |
| Investigation | Find first time, account used, changed files, suspicious requests |
| Recovery | Restore from clean backup, rotate credentials, patch the hole |
| Review | Record root cause and fix gaps in hardening |

Incident response does not have to be complex for a lab. What matters is knowing: **what you see, what you do, and how to recover the server.**

## 13. Hardening Verification

Checklist after hardening:

- [ ] Only ports 22, 80, 443 are open
- [ ] Database only listens on `127.0.0.1`
- [ ] SSH root login rejected
- [ ] SSH password auth rejected
- [ ] TLS configuration verified with OpenSSL or testssl.sh
- [ ] Security headers present in responses
- [ ] WAF `DetectionOnly` logs test requests
- [ ] Fail2ban active and ban rules tested in lab
- [ ] Audit log records changes to sensitive files
- [ ] Database backup running
- [ ] Backup restore tested at least once
- [ ] No secrets in repository or world-readable files

## 14. Common Mistakes

1. **Opening database port to the public** — easiest target.
2. **SSH root login enabled** — brute force target.
3. **Not updating** — old CVEs that already have patches.
4. **WAF in blocking mode without tuning** — false positives block real users.
5. **No backups** — hardening doesn't protect against human error.
6. **Logs not monitored** — attacks go undetected.
7. **Secrets in Git** — credentials leak with the repository.
8. **Backups never tested** — when needed, they can't be restored.

## Conclusion

Hardening a single-tier stack is about **reducing risk gradually**. No system is 100% secure, but with CIS as a reference, firewall, SSH keys, modern TLS, WAF, least-privilege database, logging, and tested backups, the server is far safer than the defaults.

The goal is not just to make the app run.  
The goal is to understand each defense layer, how to verify it, and how to recover when something goes wrong.

> **Note:** Hardening is an ongoing process. Review configurations regularly, keep security patches up to date, and re-test backups and detection.

## References

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — secure configuration guides per product. [cisecurity](https://www.cisecurity.org/cis-benchmarks)
- [CIS Benchmarks Overview](https://www.cisecurity.org/cis-benchmarks-overview) — benchmark explanation and mapping to CIS Controls. [cisecurity](https://www.cisecurity.org/cis-benchmarks-overview)
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — 18 prioritized security controls. [cisecurity](https://www.cisecurity.org/controls/cis-controls-list)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) — hardening for host, daemon, image, and container runtime. [docs.docker](https://docs.docker.com/dhi/explore/security-concepts/cis/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) — relevant if the stack grows into container orchestration. [cisecurity](https://www.cisecurity.org/benchmark/kubernetes)
