# Hardening Single-Tier Stack

[🇮🇩 Read in Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](hardening-single-tier-stack-tl.md)

## Why Harden?

Default configurations are built so applications run immediately, not so they are secure. In a single-tier architecture, all components — web server, runtime, database, and file system — live on **one machine**. A small flaw in one layer can open a path to another without crossing many boundaries.

The goal here is not to "lock everything down", but to **reduce an attacker's room to move** if one layer is compromised. Focus on limiting access, separating privileges, detecting changes, and ensuring we can recover without reintroducing compromise.

## Threat Model

Before applying settings, understand what we protect and its limits.

| Aspect | Explanation |
|---|---|
| **Protected assets** | Web service, application data, credentials, configuration files, logs, and backups. |
| **Main threats** | Application vulnerability exploitation, login brute force, credential leaks, local privilege misuse, data exfiltration from the same machine. |
| **Assumptions** | Web service is reachable from the internet. In single-tier, app, runtime, and database share one OS. |
| **Protection limits** | We can reduce attack surface, limit lateral movement, and strengthen detection. But if the whole machine is fully controlled with root rights, no single-host setting guarantees absolute security. |
| **Out of scope** | Perimeter network security outside the host, hypervisor-level attacks, compromise of the account running the machine. |

## Attack Surface & Access Flow

In single-tier, an attacker's movement can follow interlinked paths.

| Path | Explanation | Hardening note |
|---|---|---|
| **Ingress (from outside)** | Entry through open ports, usually `80`/`443`. SSH only if truly needed. | Default deny; allow only needed ports. Restrict SSH to trusted admin networks. |
| **East-West (between components)** | Communication between processes on the same machine, usually via `127.0.0.1` or Unix socket. | Do not let the database listen on `0.0.0.0`. Separate users/services per component. Apply least privilege. |
| **Egress (outbound)** | Connections from the server outward (updates, DNS, APIs, etc.). | Observe normal patterns first, then restrict gradually. Do not ignore it because "the server needs outbound". |

> **Important:** Port `443` may be open because it is needed, but precisely because it must be open, make sure the application behind it is secure, permission-limited, and monitored.

## Core Hardening Principles

Every control should answer three questions: *What is done? Why does risk decrease? What is the limit?*

| Principle | Application | Limit |
|---|---|---|
| **Reduce attack surface** | Disable unused services; open only needed ports. | Cannot close ports the application genuinely needs. |
| **Least privilege** | Run each service as a separate user with minimal rights. | Minimal rights must still be enough for the app to function. Needs testing. |
| **Isolation** | Separate process rights, file ownership, systemd limits. | On one machine, isolation is logical. A compromise with enough access can still cross components. |
| **Defense in depth** | Combine firewall, permissions, app validation, logging, backups. | If one layer fails, others can slow down or detect. Not a guarantee. |
| **Detection & verification** | Baseline, monitor changes, test controls regularly. | Without follow-up, logs are just archives. |
| **Be recoverable** | Separate backups, test restores, document incident response. | An untested backup is as good as no backup. |

## Reference Standard: CIS

[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) are a reference, not an absolute target.

- **Level 1**: Practical baseline, suitable for gradual rollout on most single-tier setups.
- **Level 2**: Stricter; use only if truly needed and tested in a lab.
- **Compliance ≠ Security**: Scores depend on profile, benchmark version, and documented exceptions. What matters is understanding the reason behind each control, not just checking every box.

## OS, Attack Surface & Network

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Update & patch** | *What:* Apply security updates. *Why:* Close known flaws. *Limit:* Patches need testing; zero-days remain. | Routine updates; prioritize components exposed to the network. |
| **Host firewall** | *What:* Default deny incoming; allow only needed ports. *Why:* Reduce ingress paths. *Limit:* Does not protect against exploitation through ports that must stay open (80/443). | SSH can be restricted to VPN/admin network. HTTP can redirect to HTTPS. |
| **SSH hardening** | *What:* Use keys; disable root login & password auth. *Why:* Reduce brute force. *Limit:* A leaked key still works if not revoked. | Restrict `AllowUsers` when possible. |
| **Kernel & mount options** | *What:* Apply relevant sysctl; consider `noexec/nosuid/nodev` on sensitive partitions. *Why:* Limit dangerous execution/movement. *Limit:* Can break apps if applied untested. Match to mount function. | Test in a lab first. |

## Services, Files, Permissions & Secrets

In single-tier, isolation between services matters because everything shares one OS.

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Service minimization** | *What:* Disable unused services. *Why:* Fewer active services = smaller attack surface. *Limit:* Some supporting services are needed for certain functions. | Inventory first; do not disable blindly. |
| **Least privilege per service** | *What:* Run each service under a separate user/group. *Why:* Limit impact if one service is compromised. *Limit:* If the app needs broad access to function, restrictions must stay realistic and tested. | Use [systemd sandboxing](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html): `User=`, `Group=`, `NoNewPrivileges=`, `ProtectSystem=`, `ProtectHome=`, `ReadOnlyPaths=`, `PrivateTmp=`. |
| **File permissions & ownership** | *What:* Set strict ownership/permissions (`600/640`, correct `chown`). *Why:* Prevent unnecessary cross-user access. *Limit:* Misconfiguration can break the app. | Focus on config, keys, logs, upload directories. |
| **Secret management** | *What:* Do not put credentials in the repo. Store in tightly permissioned files or a secret manager. *Why:* Reduce leak risk. *Limit:* If the runtime is compromised and can read secrets it has access to, those secrets can still be taken. | Rotate, restrict access, audit, and ensure `.env` is in `.gitignore`. |

## Web Server, Browser, TLS & WAF

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Web server hardening** | *What:* `server_tokens off`, limit methods, disable autoindex, apply headers server-side. *Why:* Reduce information leakage & certain risks. *Limit:* Headers help but do not replace app validation. | Split responsibility: server sets headers; app still must validate input, authenticate, authorize, and use anti-CSRF. |
| **TLS/HTTPS** | *What:* Modern TLS, HSTS, HTTP→HTTPS redirect, OCSP stapling. *Why:* Encrypt traffic and prevent downgrade. *Limit:* TLS protects the channel, not app logic or access rights. | Verify with `testssl.sh`/SSL Labs. Protect private keys with strict permissions. |
| **WAF** | *What:* Filter dangerous patterns (SQLi/XSS). Start in DetectionOnly, move to Blocking gradually. *Why:* Adds a detection/filter layer. *Limit:* Can false-positive, cannot see local/lateral movement, and can be bypassed. Must be tuned to the app. | WAF reduces exploitation chances but is **not a replacement** for secure code. |

## Database & Runtime

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Database hardening** | *What:* Bind to `127.0.0.1`/Unix socket, least privilege per app user, disable remote root access. *Why:* Limit network access. *Limit:* If the app is compromised, it can still access the DB with the app user's rights. | Separate users per app. Never use the `root` user for app connections. |
| **Database encryption** | *What:* Consider at-rest encryption (TDE support varies by engine/version/edition) or volume encryption (LUKS). *Why:* Protect data if the disk is stolen. *Limit:* Does not protect if the machine is live and the app/DB is reachable by an attacker who is already in. | Encrypting backups is equally important, sometimes more crucial. |
| **Runtime hardening** | *What:* Run runtime as non-root, limit resources, minimize dangerous functions. *Why:* Limit RCE impact. *Limit:* A compromised runtime with local access can still try to exploit other local services on the same machine. | Focus on isolation per service, not just "non-root". |

## Logging, Monitoring & Detection

What matters is not "log as much as possible", but **log what can be acted on**.

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Audit & FIM** | *What:* `auditd` for critical changes, File Integrity Monitoring for important files. *Why:* Detect unauthorized changes. *Limit:* Needs a maintained baseline. Legitimate changes (deploys) create noise if unmanaged. | Focus on `/etc`, web/DB config, keys, and critical directories. |
| **Centralized logs & log protection** | *What:* Collect relevant logs, protect log integrity. *Why:* If an attacker gains root, local logs can be deleted. *Limit:* Needs a more protected separate channel. | Consider shipping logs to a separate system with different access rights. |
| **Anomaly-based detection** | *What:* Monitor suspicious logins, new users, unusual processes, abnormal outbound connections, privilege changes. *Why:* Many attacks leave no clear "exploit" sign. *Limit:* Takes time to learn normal patterns. Alerts without an owner & follow-up path are useless. | Assign alert owners and a simple escalation path. |

## Backup, Recovery & Incident Response

In single-tier, separating backups matters far more than most people think.

| Control | What / Why / Limit | Notes |
|---|---|---|
| **Separated backups** | *What:* Store copies outside the machine (different location/credentials). *Why:* Production accounts can be used to delete local backups. *Limit:* If backup encryption keys are stored on the same machine, they can be locked/deleted along with it. | Separate key management. Use a dedicated backup account with minimal rights. |
| **Restore test** | *What:* Test restores into an isolated environment regularly. *Why:* Proves backups are truly recoverable. *Limit:* The test environment must be similar enough to reveal compatibility issues. | **Practical rule:** A backup that has never been restore-tested is as good as no backup. |
| **Simple incident response** | *What:* Flow: Detect → Contain → Investigate → Recover → Evaluate. *Why:* Avoid panic and prevent re-compromise. *Limit:* On root compromise, do not trust local output. Prioritize isolation, protect centralized evidence, and decide to rebuild from a trusted source. | Focus on credential rotation, closing entry paths, verifying baseline, documenting chronology. |

## Hardening Verification

Split by function for realism.

### Preventive (preventing)

| Check | Verify |
|---|---|
| Only needed ports open | `ss -tulnp` / firewall status |
| DB only on `127.0.0.1` or Unix socket | DB config + test connection from outside host |
| SSH uses keys; root/password auth disabled | `sshd_config` + login test |
| Services run as separate users | `ps aux` / systemd units |
| Secrets not in repo and tightly permissioned | File audit & `.gitignore` |

### Detective (detecting)

| Check | Verify |
|---|---|
| `auditd` active for critical files/config | Audit rules & logs appear |
| File Integrity Monitoring running | Baseline exists & changes detected |
| Relevant logging active & centrally accessible | Log flow works, retention sufficient |
| Alerts have owners & follow-up paths | Simple alert owner list exists |

### Recovery (recovering)

| Check | Verify |
|---|---|
| Backups separated from production machine | Location, credentials, permissions separated |
| Restore test succeeded at least once | Recorded date + result in isolated environment |
| Isolation & credential rotation plan exists | Short document usable during panic |
| Can return to a trusted baseline | Rebuild/recovery path documented |

## Common Mistakes & Single-Tier Limits

| Common mistake | Why dangerous | How to avoid |
|---|---|---|
| **Opening DB port to public** | Directly expands attack surface | Only `127.0.0.1`/Unix socket + strict firewall |
| **SSH root + password auth** | Favorite brute-force target | SSH keys, disable both, restrict access |
| **Relying on headers/WAF only** | Assuming the protection layer is enough | Headers & WAF help, but validation, auth, authorization remain mandatory in the app |
| **"Closed from outside" = safe** | Ignoring local & east-west access | Remember: if runtime/app is compromised, it can use local access |
| **Untested backups** | Fail when truly needed | Schedule periodic restore tests; separate copies & keys |
| **Over-applying `noexec/nosuid/nodev`** | Can break apps without reason | Apply per partition by function; always test in lab |
| **Logs only stored, never acted on** | Detection becomes useless | Assign alert owners + escalation path |

**Single-tier hardening limit:** You can slow down, limit, and detect attacks. You **cannot** eliminate the SPOF risk through configuration alone. If one machine is fully compromised, what you can do is **limit the damage, protect the evidence, and recover from a trusted source**.

## Conclusion

Single-tier hardening is about **reducing room to move, not making the system invincible**. Start from understanding the threat model & attack surface, apply least privilege + isolation, separate preventive/detective/recovery, and most importantly: **test what you apply**.

Configuration can be correct yet still have limits. What distinguishes mature hardening is the ability to answer: *"If this fails, what can still be prevented, detected, or recovered?"*

## References

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — Secure configuration reference per product
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — Security control priorities
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — Incident response guidance
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/resources-tools/resources/use-logging-business-systems) — Log management, detection & protection
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware) — Separated backups, copy protection & recovery
- [systemd.exec Manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) — Per-service sandboxing options
