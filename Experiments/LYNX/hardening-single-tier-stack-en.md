# Hardening Single-Tier Stack

[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

﷽

This covers **hardening a single-tier stack**: all layers (web server, runtime, database, cache) run on one machine, secured from the ground up—not installation from scratch, but security configuration for each layer.

![Hardening single tier stack](hardening-single-tier-stack.png)

Goals:
- A sensible hardening order
- Reference standards such as CIS
- Security settings per layer
- Verification after hardening
- Common mistakes to avoid

##  Core Hardening Principles

Hardening is not a single button. It is a gradual process:

1. **Minimize attack surface** — open only the ports and services you need.
2. **Least privilege** — every service runs as a user that does not need root.
3. **Defense in depth** — firewall, WAF, TLS, logging, all layered.
4. **Update and patch** — an unpatched system is a target.
5. **Monitoring** — you cannot detect what you cannot see.
6. **Recovery** — hardening does not replace backups and recovery plans.

> **Warning:** Never harden directly in production. Always test in a lab or VM first.

##  Hardening Standard: CIS

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

> **Note:** The CIS Benchmark consists of Level 1 (minimum baseline) and Level 2 (stricter). Compliance scores depend on the benchmark profile, version, and which controls apply to your environment. Applying Level 1 + Level 2 does not mean "100% secure"—compliance is a guide, not a guarantee of absolute security. Choose the appropriate level, document exceptions, evaluate per control, test in the lab, and roll out gradually.

##  Operating System

| Aspect | What to do | Why it matters |
|---|---|---|
| Update and patch | Regularly update OS and packages | Closes known vulnerabilities |
| User and privilege | Don't log in as root, create a regular user with sudo | Limits impact if an account leaks |
| SSH | Disable root login and password auth, use SSH keys | SSH is the main entry point to the server |
| Host firewall | Default deny incoming, allow only ports required for the architecture (e.g., 22, 80, 443) | Reduces port exposure |
| Auto patch | Enable unattended upgrades for security patches | Keeps the system safe without manual intervention |
| Service minimization | Disable unused services | Fewer services means smaller attack surface |
| Kernel parameters | Apply relevant sysctl hardening | Reduces network-level abuse risk |

> **Important:** Never open database ports (3306, 5432) to the public—database access should be limited to `127.0.0.1` or a Unix socket. SSH can be restricted to a VPN/admin network, and HTTP can be used only for redirect to HTTPS. Also consider often-overlooked aspects:
> - **Footprint & installation:** during install, enable disk encryption (LUKS) and separate partitions for `/`, `/var`, `/tmp`, `/home`. Apply mount options `noexec`, `nosuid`, `nodev` only to sensitive partitions as appropriate for their function and always test in a lab (they can break certain applications).
> - **Memory & disk management:** encrypt swap, cap log sizes, rotate logs, and monitor disk usage to avoid denial-of-service from a full disk.
> - **Kernel & service hardening:** apply relevant sysctl parameters, enable SELinux/AppArmor, minimize services, disable unused modules.

##  Services, Files, and Secrets

| Aspect | What to do | Why |
|---|---|---|
| Minimal services | Remove or disable unused services | Every active service is a potential entry point, fewer services means smaller attack surface |
| File permissions | Restrict permissions on config, logs, and sensitive files (chmod 600/640, chown root:root) | Prevents non-privileged users from reading or modifying files containing config or sensitive data |
| Umask | Use strict default permissions (umask 027 or 077) | Newly created files are not world-readable, reducing accidental data leaks |
| SELinux/AppArmor | Enable per distro (enforcing mode) | Limits service behavior if compromised—even if a service is breached, damage is confined to the allowed policy |
| Secrets | Don't put passwords or API keys in repos or world-readable files | Credentials leaked to Git or world-readable files allow unauthorized access |
| Secret storage | Store in tightly permissioned files or a secret manager (Vault, SOPS). Enforce least privilege, rotation, and auditing. | Reduces configuration leak risk, eases rotation, and maintains an audit trail |
| `.gitignore` | Add `.env`, `*.key`, `*.pem`, `backup/` to `.gitignore` from the start | Prevents credentials, SSH keys, and backups from accidentally entering the Git repository |

> **Warning:** `.env` files, database credentials, SSH keys, and backups must not go into Git. Use `.gitignore` from the start, and if already committed, rotate credentials immediately (treat as leaked).

**If already leaked to Git, do this:**
1. **Remove from history** — use `git filter-repo` or BFG Repo-Cleaner to purge the file/secret from all history, then force-push.
2. **Rotate all credentials** — passwords, API keys, SSH keys, tokens that leaked are considered compromised, replace them all.
3. **Revoke old access** — revoke old keys, close active sessions, block suspicious IPs.
4. **Audit** — check access logs to see whether the secret was abused.
5. **Prevention** — add secret scanning (gitleaks, trufflehog) in CI/CD and pre-commit hooks.

##  Web Server & Web Client Hardening

### Web Server (server-side)

| Web server | Key settings | Goal |
|---|---|---|
| Nginx | `server_tokens off`, security headers on the server, restrict HTTP methods, disable autoindex, modern TLS, rate limiting (`limit_req`), WAF (ModSecurity) | Hide version info, limit dangerous requests, protect from abuse/DDoS |
| Apache | `ServerTokens Prod`, `ServerSignature Off`, `TraceEnable Off`, security headers on the server, modern TLS, ModSecurity WAF | Hide server info and reject dangerous methods |
| Caddy | Security headers, reverse proxy with automatic TLS | Simple config with safe defaults |

**Security headers commonly set at the web server:**
- `Strict-Transport-Security (HSTS)` — forces HTTPS (see TLS section)
- `X-Content-Type-Options: nosniff` — prevents MIME sniffing
- `X-Frame-Options: SAMEORIGIN` — prevents clickjacking (can be supplemented/replaced by `Content-Security-Policy: frame-ancestors`)
- `Referrer-Policy: strict-origin-when-cross-origin` — controls referrer leakage
- `Permissions-Policy` — restricts browser feature access
- `Content-Security-Policy (CSP)` — restricts sources for scripts/styles/images to mitigate XSS

> **Note:** Headers reduce certain risks, but they **do not replace** input validation, output encoding, authentication, and authorization. Those remain the application's responsibility.

**Rate limiting & WAF (server-side):**
- Limit requests per IP/user at the web server (`limit_req`, `mod_evasive`).
- Deploy a WAF (ModSecurity/OWASP CRS) to filter SQLi, XSS, and malicious payloads.
- Block repeatedly abusive IPs (fail2ban).

**Reverse proxy / load balancer (if present):**
- Forward `X-Forwarded-For` correctly; do not trust blindly.
- Restrict admin endpoints to specific IPs.
- Enable access and error logging.

### Web Client / Browser-side Hardening

Focus on controls that **cannot be solved by server headers alone**:
- **Strict CSP**: avoid `unsafe-inline`/`unsafe-eval`; use nonce/hash.
- **Subresource Integrity (SRI)**: hash CDN assets to prevent tampering.
- **Cookie security**: `Secure`, `HttpOnly`, `SameSite=Strict/Lax`, correct domain/path, short expiry.
- **Anti-CSRF tokens** for requests that change state.
- **Session management**: regenerate session ID on login, idle/absolute timeouts, invalidate on logout.
- **CORS**: restrict origins strictly; never use wildcard `*` for sensitive endpoints.
- **Storage**: avoid storing sensitive tokens in `localStorage`/`sessionStorage` (XSS risk), prefer `HttpOnly` cookies.
- **Third-party scripts**: audit/minimize, use SRI, sandbox iframes.
- **Mixed content**: block HTTP resources on HTTPS pages.

##  TLS / HTTPS

| Aspect | Recommendation | Why |
|---|---|---|
| Minimum TLS | TLS 1.2, preferably TLS 1.3 | Older protocols have known flaws |
| Ciphers | Only modern ciphers (ECDHE, GCM, ChaCha20-Poly1305) | Prevents downgrade attacks |
| HSTS | Enable with long max-age (`max-age=31536000; includeSubDomains; preload`) | Forces HTTPS in the browser |
| Certificates | Let's Encrypt via Certbot, automatic renewal | Free and widely used |
| Sessions | Limit session timeout, consider disabling session tickets | Reduces session reuse risk |
| OCSP Stapling | Enable OCSP stapling | Speeds up certificate validation and privacy |
| Redirect | Redirect HTTP → HTTPS (301) | Prevents unencrypted access |
| Key size | RSA 2048+ or ECDSA P-256/P-384 | Prevents key brute force |
| Cipher order | Server-side cipher preference | Prevents client from choosing weak ciphers |

**Additional practices:**
- Test configuration with SSL Labs (target grade A).
- Disable TLS compression (CRIME) and renegotiation.
- Use `ssl_protocols TLSv1.2 TLSv1.3;` in Nginx.
- Store private keys with strict permissions (600) and never commit to Git.

##  WAF: Web Application Firewall

| Component | Purpose | Notes |
|---|---|---|
| ModSecurity | WAF engine for Apache/Nginx | Needs tuning to avoid false positives |
| OWASP CRS | Industry-standard rule set | Start in `DetectionOnly` mode |
| Coraza | Go-based alternative WAF | Lightweight, fits modern setups |

**How to deploy (Nginx + ModSecurity example):**
1. Install the ModSecurity module and OWASP CRS.
2. Enable in Nginx config: `modsecurity on; modsecurity_rules_file /etc/modsecurity/crs/crs-setup.conf;`
3. Set `SecRuleEngine DetectionOnly` initially.
4. Monitor logs (`/var/log/modsec_audit.log`) for false positives.
5. Tune rules: exclude rules that false-positive on specific endpoints.
6. Once stable, switch to `SecRuleEngine On` (blocking).

**Watch out for:**
- False positives on upload, API, or complex form endpoints.
- Performance overhead, monitor latency.
- Update rules regularly (new CRS releases).

> **Warning:** Do not enable WAF blocking mode directly in production. WAF rules (especially OWASP CRS) often false-positive on legitimate traffic (form uploads, APIs, complex queries); if blocking is enabled immediately, legitimate users may be blocked and the service can go down. Start in `DetectionOnly`, analyze logs to identify false positives, tune rules, then enable blocking gradually.

##  Database Hardening

| Aspect | What to do | Why |
|---|---|---|
| Secure installation | Run the database's built-in secure installation | Removes anonymous users, test database, remote root |
| Least privilege | Create an app user with limited rights: `SELECT`, `INSERT`, `UPDATE`, `DELETE` | If leaked, impact is limited |
| Bind address | Database only listens on `127.0.0.1` or Unix socket | Database unreachable from outside |
| Password | Use strong passwords, PostgreSQL supports SCRAM-SHA-256 | Prevents brute force |
| Remote access | Disable remote login for database root | Remote root is extremely dangerous |
| Backup | Regular backups and restore tests | Hardening does not protect against human error or disk failure |
| Encryption at rest | Enable TDE *if supported* by the engine/version/edition, else use LUKS on data volumes + encrypted backups | Protects data if disk is stolen; TDE support varies by MySQL/MariaDB/PostgreSQL |
| Audit logging | Enable query logging for sensitive operations (DDL, DML on key tables) | Detects unauthorized access and meets compliance |
| Connection security | Use TLS for database connections (even localhost in multi-tenant setups) | Prevents credential/data sniffing |
| Query monitoring | Monitor slow queries and anomalies (pg_stat_statements, slow query log) | Detects abuse or injection that bypassed the WAF |
| Backup encryption | Encrypt backups (GPG/LUKS), store offsite, test restores | Prevents data leaks from stolen backups |
| Network isolation | Never expose DB ports publicly, use firewall/VPN for admin access | Reduces attack surface |

**Practical notes:**
- Separate DB users per app, never use root for the app.
- Rotate DB credentials periodically.
- Cap max connections (connection pool) to prevent DoS.
- Disable unused DB features (xp_cmdshell, LOAD DATA LOCAL, etc.).

##  Runtime Hardening

| Runtime | Key settings | Goal |
|---|---|---|
| PHP-FPM | Run as `www-data`; limit `pm.max_children`; disable dangerous functions; `expose_php Off` | Reduces resource abuse and information leaks |
| Node.js | Run as non-root via systemd, use PM2 or a service manager | Process isolation and auto-restart |
| Python | Use virtual environments, run Gunicorn/uWSGI as regular user | Dependency isolation and privilege reduction |
| Java | Set JVM memory limits, run as regular user | Prevents memory exhaustion |
| .NET | Run Kestrel as non-root, use a reverse proxy in front | Process isolation and access control |

##  Logging and Monitoring

| Component | Purpose | Why |
|---|---|---|
| `auditd` | Records changes to sensitive files and access | Detects suspicious activity |
| `journald` | Persistent system logging | Incident investigation |
| `logrotate` | Rotates logs so disk doesn't fill | Maintains availability |
| Fail2ban | Blocks IPs after repeated failed logins | Protects SSH and login services |
| Baseline | Record normal state: ports, users, services, logs | Without a baseline, anomalies are hard to spot |

##  Backup and Recovery

| Aspect | What to do | Why |
|---|---|---|
| Database backup | Regular, automated backups | App data is the main asset |
| Configuration backup | Back up Nginx/Apache, systemd, firewall, and WAF config | Speeds up server rebuild |
| Restore test | Test restores periodically | An untested backup is not proven usable |
| Recovery runbook | Write recovery steps | During an incident you don't guess from zero |
| Retention | Define how long backups are kept | Balances storage cost and recovery needs |

> **Important:** Backups stored on the same server are still at risk. Keep at least one copy offsite.

##  Incident Response

| Phase | What to do |
|---|---|
| Detection | Check SSH, web server, WAF, database, and `auditd` logs |
| Containment | Block IPs, stop infected services, or isolate the VM |
| Investigation | Find first time, account used, changed files, suspicious requests |
| Recovery | Restore from clean backup, rotate credentials, patch the hole |
| Review | Record root cause and fix gaps in hardening |

Incident response does not have to be complex for a lab. What matters is knowing: **what you see, what you do, and how to recover the server.**

##  Hardening Verification

Use a `check → execute → verify` approach:

| Control | Check | Execute | Verify |
|---|---|---|---|
| Ports & firewall | List open ports (`ss -tulnp`, `ufw status`) | Apply default deny + allow only required ports | Only approved ports are open |
| DB access | Check bind address | Bind to `127.0.0.1` or Unix socket, deny public access | No DB connections from outside the host |
| SSH | Check sshd config | Disable `PermitRootLogin`, disable password auth, use keys | Root and password auth are rejected |
| TLS | Check cert/cipher | Configure TLS 1.2/1.3, modern ciphers, HSTS, HTTP→HTTPS redirect | Test with `openssl s_client` or testssl.sh (target A) |
| Security headers | Check HTTP response | Set headers at web server | Headers present as configured |
| WAF | Check WAF mode | Start in `DetectionOnly`, tune, move to `Blocking` gradually | Test requests logged, false positives addressed |
| Fail2ban | Check jail status | Enable relevant jails | Tested in lab (ban/unban works) |
| Audit/FIM | Check `auditd`, AIDE/tripwire | Create baseline and audit rules for critical files/configs | Changes are tracked/alerted |
| Egress | Check outbound connections | Observe → apply allowlist/deny gradually as needed | Only allowed destinations reachable |
| Backup & restore | Check backup schedule | Automate, encrypt, separate storage, test restore | Restore in isolated env succeeds and app works |
| Secrets | Check repo/files | Ensure `.env`/keys not committed, strict permissions | Clean scan/history, correct permissions |

##  Common Mistakes

1. **Opening database port to the public** — database must be only on `127.0.0.1` or Unix socket.
2. **SSH root login enabled and password auth allowed** — use SSH keys, disable both.
3. **Not updating** — old CVEs can be exploited even if patches exist.
4. **WAF in blocking mode without tuning** — start in `DetectionOnly`, analyze false positives, enable blocking gradually.
5. **Backups never tested** — backups must be tested via restore in an isolated environment.
6. **Secrets in Git** — use `.gitignore`, a secret manager, and if leaked rotate credentials and clean history.
7. **Assuming headers are enough** — headers reduce risk, but input validation, authentication, and authorization are still required in the application.

##  Detection and Recovery: Boundaries of Hardening on a Single-Tier Stack

### Single-tier security boundary

Single-tier means multiple components share one OS. Logical process separation is not the same as security isolation. If runtime is compromised, attackers may steal DB credentials, plant persistence, or exfiltrate data. Hardening must cover prevention, containment, detection, and recovery.

### Network hardening

Three paths: **Ingress** (external connections — SSH, HTTP/HTTPS: restrict sources, open only needed ports), **East-west** (component-to-component via loopback/Unix socket: restrict inter-process access), **Egress** (outbound DNS, NTP, updates, backups, APIs: default-deny + allowlist).

UFW helps with ingress but does not auto-limit egress or isolate processes. To reduce lateral movement: separate service accounts per component, dedicated DB app user, AppArmor/SELinux, container network policies, or separate VMs if impact is high.

### Logging and monitoring

Logging = recording events. Monitoring = checking for anomalies. Alerting = notifying when action needed.

End-to-end map: (1) entry points (SSH, HTTP/HTTPS, firewall, WAF, TLS, app auth), (2) app execution (web server → runtime), (3) data access (runtime → DB → files/backups), (4) OS & egress activity (processes, users, systemd, cron, sensitive files, DNS, outbound connections), (5) correlation & response (collect logs, sync time, correlate events, alert, triage).

Per-layer monitoring: firewall (connections, ports, destinations), SSH/OS accounts (logins, new users), web server/WAF (URLs, status, rules), runtime (errors, restarts, child processes), database (logins, privileges, sensitive queries), file integrity (hash, permissions, owner), OS (sudo, audit events, cron, kernel), resources (CPU/RAM/disk/latency), backups (job status, size, retention).

### auditd

Records events per audit rules. Key objects: sshd_config, sudoers, passwd/group/shadow, systemd units, cron, authorized_keys, web server/WAF/DB configs, web root, firewall config, critical binaries.

Consumers: sysadmins (config/user changes), security analysts (chronology), incident responders (persistence/escalation), auditors (change trail).

Limits: wrong rules miss activity, too many rules cause disk pressure/noise, legitimate changes (deployments) also logged, root attackers can delete local logs, audit doesn't auto-explain triggering HTTP requests.

Distinguish: auditd (activity per rules), journald (OS/app messages), FIM (change vs baseline), network monitoring (connections), SIEM (correlation & alerts).

### journald, logrotate, Fail2ban, baseline

- **journald**: collects OS/app messages, persistence depends on config/retention. Monitor SSH, failed services, kernel, resource failures. Forward critical logs to separate system.
- **logrotate**: manages log lifecycle (rotation, compression, retention). Ensure rotation doesn't stop log writing, retention long enough for investigation.
- **Fail2ban**: reads logs, blocks sources after patterns (repeated failed logins). Helps simple brute force, does not prevent web exploits, credential theft, exfiltration. Can false-positive.
- **Baseline**: record of normal state (ports, users, services, processes, file hashes, firewall rules, login/request/egress patterns, versions). Update via legitimate changes (deployments/patches).

### Effective monitoring

Set normal conditions then alert. Example signals: SSH admin login from unknown source (high), new OS user/admin group outside change window (high), config file changed without deployment (high), new process not matching app behavior (high), runtime opening connections to new destinations (high if confirmed), DB privilege change or large data export (high), firewall rule change without approval (high), WAF request spike resembling exploitation (needs correlation), CPU/RAM/disk/latency spike (needs triage), backup job failure/unavailable copy (high).

WAF only sees traffic through its inspection point, it doesn't see local processes, user/sudo changes, files changed via SSH, DB access via loopback, non-WAF egress, firewall changes, log deletion, backup changes. OS audit doesn't replace app logs (syntactically valid requests abusing authorization).

Local logs alone insufficient: root attackers can delete local logs. Forward critical logs to a separate system (VM with separate admin rights). CISA recommends centralized logging, high-risk event alerting, log protection from unauthorized changes, clear retention.

Assign alert owners: admin (service health/config), developer (deployment/errors), security analyst (correlation/containment), backup owner (availability/restore), service owner (business impact).

### Backup and recovery

Objects to consider: database (data+schema+roles+metadata), app files (known-clean release version), user uploads, OS/service configs, secrets/certificates (with appropriate access/encryption), encryption keys (separate from backups), logs/evidence, recovery documentation (versions, dependencies, restore order).

Flow: production source → consistent backup (engine-appropriate method, record time/version/status) → encryption & transfer (protected channel, dedicated backup identity) → separate storage (different location, separate credentials, retention, deletion protection) → verification & restore test (integrity, restore to isolated env, test app+data).

Backups must be separate: attackers with high privileges can delete production data AND local backups. Use dedicated backup account, avoid granting production server rights to delete all historical copies, immutable storage, encrypt + separate key management, monitor failures/retention changes, test restores. 3-2-1 approach: 3 copies, 2 media types, 1 offsite. For ransomware, add offline/immutable copies.

RPO (recovery point objective) = acceptable data loss (time window). RTO (recovery time objective) = max downtime allowed. Backup frequency doesn't auto-guarantee RPO, backups don't auto-guarantee RTO if restore is slow.

Recovery difficulties: DB and uploads from different times, latest backup may contain corrupted/malicious data, leaked secrets need rotation not just restore, old configs may reintroduce vulnerabilities, encrypted backups useless if keys lost, app may fail on restore, persistence may be restored. Therefore restore test in isolated environment: verify DB, app login, business functions, permissions, services, TLS, firewall, monitoring before returning to service.

### Incident response

Rapid response (first minutes): validate alert (system, time, account, process, indicator), assess impact (service, sensitive data, admin accounts, egress), containment (limit attack paths via network controls/isolation), protect evidence (save logs, timestamps, alerts, metadata, record every action), protect access (plan session revocation, secret rotation, key replacement via trusted systems), determine escalation (root compromise, data theft, ransomware → serious incident).

Deep investigation — key questions: when did first activity occur? (centralized logs, auth, web, WAF, audit, DB) What was the entry point? (web requests, SSH, app changes, weak config) Which account was used? (login, user ID, privilege, session, key, sudo) What processes ran? (process tree, parent, executable, service, scheduler) What files changed? (audit events, FIM, hash, metadata, deployment history) What data was accessed? (DB audit, app, file access, traffic volume) Did data leave the server? (flow logs, DNS, proxy/firewall logs, owning process) Is access still persistent? (accounts, keys, services, cron, config, other persistence) What can still be trusted? (system integrity, backup provenance, config, external evidence).

If OS is root-compromised: don't trust output from suspicious OS, isolate via external network controls, preserve centrally forwarded logs, collect volatile evidence if procedures exist, avoid running tools that overwrite evidence, consider forensic snapshot/image per platform procedures, prioritize rebuild from clean media/image, rotate credentials/tokens/keys/secrets, check access to backups and other systems using compromised server's identity.

Containment is not just IP blocking: if attacker uses legitimate accounts/sessions, accesses via VPN/proxy, exploits locally, stole DB credentials, planted persistence, or gained root — IP blocking isn't enough. Containment can mean: disable accounts, revoke sessions/keys, isolate VMs, limit egress, stop specific services, close affected endpoints.

Recovery & verification before declaring done: entry point closed/mitigated, images/packages/app files from trusted sources, data restored from verified backup, leaked credentials/sessions handled, users/keys/services/scheduler/firewall match approved baseline, logging/audit/FIM/monitoring active, egress & DB access per policy, app passes functional & security tests, documentation of chronology/impact/actions/follow-ups.

### Correlation matrix (example incident)

Runtime suspected of running unexpected process after web request:
1. Initial indication: WAF & access logs → abnormal request, endpoint, time, status.
2. Process validation: runtime logs & process info → child process, parent, owner, start time.
3. System changes: auditd & FIM → new files, permission changes, service/cron units.
4. Access expansion: auth, sudo, DB logs → new accounts, privilege changes, sensitive data access.
5. Outbound comms: firewall, DNS, flow logs → new destinations, timing, volume.
6. Containment: external firewall/host isolation → is activity still ongoing?
7. Recovery: backups, baseline, trusted image → can system & data be safely restored?
8. Evaluation: all evidence → entry path, impact scope, failed controls.

### Difficulties and limitations

| Control | Main difficulty | Risk if applied without evaluation |
|---|---|---|
| Egress default-deny | Building/maintaining complete destination allowlist | Updates/DNS/APIs/backups fail |
| auditd | Choosing rules, controlling event volume | Disk full, noise, missed events |
| FIM | Updating baseline after legitimate changes | Alert fatigue or malicious changes seen as normal |
| SIEM/centralized logs | Storage cost, parsing, correlation, alert management | Many alerts, no follow-through |
| Fail2ban | Tuning filters and thresholds | False positives, blocking legitimate users |
| DB auditing | Deciding what to log without overhead/data leakage | High load or logs containing sensitive data |
| Offsite backup | Managing identity, encryption, retention, restore tests | Backups inaccessible, undecryptable, or unrestorable |
| Incident response | Balancing containment, evidence preservation, service continuity | Evidence lost or compromise continues |
| Server rebuild | Ensuring clean image, dependencies available, data consistency | Attacker/vulnerable config re-enters |

### Sensible implementation order

1. Establish baseline & inventory (ports, services, users, config, dependencies, data paths, external services).
2. Secure ingress & local access (limit SSH, close unneeded ports, restrict runtime privileges, protect DB access).
3. Apply egress policy (observe normal connections → gradual restriction → test app flows).
4. Enable relevant logging (auth, web, runtime, DB, OS, firewall, backup).
5. Add audit & file integrity (critical objects, audit rules, baseline, changes requiring investigation).
6. Build monitoring & alerts (rules based on risk scenarios, alert owners, test evidence availability).
7. Separate backups & critical logs (protect from deletion by production server accounts).
8. Practice incident response (simulate suspicious logins, file changes, unexpected egress, backup restore in lab).
9. Verify & review (test controls after changes, document exceptions, re-evaluate baseline).

### References

- [Ubuntu Server — Firewall](https://ubuntu.com/server/docs/firewalls/) — host firewall behavior and management with UFW.
- [Linux Audit System — auditd](https://www.linux.org/docs/man5/auditd.html) — audit daemon role and audit record processing.
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/use-logging-on-business-systems) — log sources, alerting, centralization, log protection.
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — logging, backup, copy protection, recovery.
- [FBI — Ten Actions to Improve Cyber Resiliency](https://www.fbi.gov/investigate/cyber/ten-actions-to-improve-cyber-resiliency) — log protection and offline/immutable backups.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — incident response guidance (April 2025).

Key takeaway: on a single-tier stack, the goal is not just preventing internet access. You also need to limit what a compromised process can do, reduce chances of lateral movement and exfiltration, preserve trustworthy evidence, and ensure the system can be recovered without reintroducing compromise.

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
