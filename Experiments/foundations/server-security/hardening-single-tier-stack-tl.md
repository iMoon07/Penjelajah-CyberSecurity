# Hardening Single-Tier Stack

[🇬🇧 Read in English](hardening-single-tier-stack-en.md)
[🇮🇩 Baca dalam Bahasa Indonesia](hardening-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](hardening-single-tier-stack-ms.md)

## Bakit Kailangan I-hardening?

Ang default configuration ay ginawa para tumakbo agad ang application, hindi para maging secure. Sa single-tier architecture, lahat ng component — web server, runtime, database, at file system — ay nasa **isang machine lang**. Maaaring maliit na butas sa isang layer ang magbukas ng daan patungo sa iba pang layer nang hindi kailangang dumaan sa maraming boundary.

Ang layunin dito ay hindi "ilock lahat", kundi **bawasan ang espasyo ng paggalaw ng attacker** kapag may isang layer na nakompromiso. Nakatuon ito sa pagbawas ng access, paghiwalay ng karapatan, pagtuklas ng pagbabago, at pagtiyak na kaya nating makabawi nang hindi muling dinadala ang compromise.

## Threat Model

Bago mag-apply ng settings, unawain kung ano ang pinoprotektahan at ang limitasyon nito.

| Aspeto | Paliwanag |
|---|---|
| **Pinoprotektahang asset** | Web service, application data, credentials, configuration files, logs, at backups. |
| **Pangunahing banta** | Pag-exploit ng application vulnerability, brute force login, pagkabulgar ng credentials, lokal na pag-abuso ng karapatan, exfiltration ng data mula sa parehong machine. |
| **Palagay** | Ang web service ay maaaring ma-access mula sa internet. Sa single-tier, ang app, runtime, at database ay nagbabahagi ng isang OS. |
| **Hangganan ng proteksyon** | Mababawasan natin ang attack surface, makakahadlang sa lateral movement, at mapapalakas ang detection. Ngunit kung buong machine ay nakontrol na may root rights, walang single-host setting na makakagarantiya ng absolute security. |
| **Labis sa saklaw** | Perimeter network security labas ng host, hypervisor-level attacks, o compromise ng account na nagpapatakbo ng machine. |

## Attack Surface & Daloy ng Access

Sa single-tier, ang paggalaw ng attacker ay maaaring sumunod sa mga magkakaugnay na landas.

| Landas | Paliwanag | Nota ng Hardening |
|---|---|---|
| **Ingress (mula sa labas)** | Pasok sa pamamagitan ng bukas na port, karaniwang `80`/`443`. SSH lamang kung talagang kailangan. | Default deny; payagan lamang ang kailangang port. Hadlangan ang SSH sa trusted admin networks. |
| **East-West (sa pagitan ng component)** | Komunikasyon sa pagitan ng mga proseso sa parehong machine, karaniwang via `127.0.0.1` o Unix socket. | Huwag hayaang makinig ang database sa `0.0.0.0`. Ihiwalay ang user/service bawat component. I-apply ang least privilege. |
| **Egress (papalabas)** | Koneksyon mula sa server papunta sa labas (updates, DNS, API, atbp.). | Obserbahan muna ang normal na pattern, saka bawasan nang paunti-unti. Huwag balewalain dahil "kailangan ng server lumabas". |

> **Mahalaga:** Ang port `443` ay maaaring bukas dahil kailangan, ngunit dahil kinakailangang bukas ito, tiyakin na ang application sa likod nito ay secure, may limitadong karapatan, at pinangangasiwaan.

## Mga Pangunahing Prinsipyo ng Hardening

Bawat control ay dapat sumagot sa tatlong tanong: *Ano ang ginagawa? Bakit bumababa ang risk? Ano ang hangganan?*

| Prinsipyo | Paggamit | Hangganan |
|---|---|---|
| **Bawasan ang attack surface** | I-disable ang unused services; buksan lamang ang kailangang port. | Hindi maaaring isara ang port na talagang kailangan ng application. |
| **Least privilege** | Patakbuhin bawat service bilang hiwalay na user na may pinakamababang karapatan. | Dapat sapat pa rin para gumana ang app. Kailangan i-test. |
| **Isolation** | Ihiwalay ang process rights, file ownership, at systemd limits. | Sa isang machine, ang isolation ay logical. Ang compromise na may sapat na access ay maaaring lumampas sa pagitan ng component. |
| **Defense in depth** | Pagsamahin ang firewall, permissions, app validation, logging, at backup. | Kung may isang layer na bumagsak, ang iba ay maaaring magpabagal o magdetekta. Hindi garantiya. |
| **Detection & verification** | Baseline, bantayan ang pagbabago, subukan ang controls nang regular. | Kung walang follow-up, ang logs ay arkibo lang. |
| **Handa makabawi** | Ihiwalay ang backup, subukan ang restore, dokumentuhin ang incident response. | Ang backup na hindi pa nate-test ang restore ay katumbas ng walang backup. |

## Pamantayang Sanggunian: CIS

Ang [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) ay maaaring maging sanggunian, hindi absolute target.

- **Level 1**: Praktikal na baseline, angkop sa unti-unting paglalapat sa karamihan ng single-tier setup.
- **Level 2**: Mas mahigpit; gamitin lamang kung talagang kailangan at nate-test sa lab.
- **Compliance ≠ Security**: Ang score ay nakadepende sa profile, bersyon ng benchmark, at naka-dokumentong exception. Ang mahalaga ay unawain ang dahilan ng bawat control, hindi lamang pag-check ng bawat punto.

## OS, Attack Surface & Network

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Update & patch** | *Ano:* Mag-apply ng security updates. *Bakit:* Isara ang kilalang butas. *Hangganan:* Kailangan i-test ang patch; zero-day nananatili. | Regular updates; bigyang-prioridad ang exposed component. |
| **Host firewall** | *Ano:* Default deny incoming; payagan lamang ang kailangang port. *Bakit:* Bawasan ang ingress path. *Hangganan:* Hindi nagpoprotekta sa exploitation sa pamamagitan ng port na kailangang bukas (80/443). | SSH maaaring hadlangan sa VPN/admin network. HTTP maaaring i-redirect sa HTTPS. |
| **SSH hardening** | *Ano:* Gumamit ng key; i-disable ang root login & password auth. *Bakit:* Bawasan ang brute force. *Hangganan:* Ang leaked key ay maaari pa ring gamitin kung hindi ni-revoke. | Hadlangan ang `AllowUsers` kung maaari. |
| **Kernel & mount options** | *Ano:* Mag-apply ng relevant sysctl; isaalang-alang ang `noexec/nosuid/nodev` sa sensitive partition. *Bakit:* Hadlangan ang mapanganib na execution/paggalaw. *Hangganan:* Maaaring masira ang app kung inilapat nang walang test. Itugma sa function ng mount. | Subukan sa lab muna. |

## Serbisyo, File, Permissions & Secret

Sa single-tier, ang isolation sa pagitan ng service ay mahalaga dahil lahat ay nagbabahagi ng isang OS.

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Minimisasyon ng serbisyo** | *Ano:* I-disable ang unused service. *Bakit:* Mas kaunting aktibong service = mas maliit na attack surface. *Hangganan:* May supporting service na kailangan para sa tiyak na function. | Mag-inventory muna; huwag i-disable nang walang alam. |
| **Least privilege bawat serbisyo** | *Ano:* Patakbuhin bawat serbisyo bilang hiwalay na user/group. *Bakit:* Hadlangan ang epekto kung may isang serbisyo na nakompromiso. *Hangganan:* Kung kailangan ng app ng malawak na access para gumana, dapat realistic at nate-test ang limit. | Gumamit ng [systemd sandboxing](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html): `User=`, `Group=`, `NoNewPrivileges=`, `ProtectSystem=`, `ProtectHome=`, `ReadOnlyPaths=`, `PrivateTmp=`. |
| **File permissions & ownership** | *Ano:* Magtakda ng mahigpit na ownership/permissions (`600/640`, tamang `chown`). *Bakit:* Maiwasan ang hindi kinakailangang cross-user access. *Hangganan:* Maaaring masira ang app kung mali ang setting. | Fokus sa config, key, log, upload directory. |
| **Pamamahala ng secret** | *Ano:* Huwag ilagay ang credentials sa repo. I-store sa mahigpit na permission file o secret manager. *Bakit:* Bawasan ang risk ng leak. *Hangganan:* Kung nakompromiso ang runtime at mababasa nito ang secret na maa-access niya, maaari pa ring makuha ang secret. | Mag-rotate, hadlangan access, mag-audit, at tiyakin na ang `.env` ay nasa `.gitignore`. |

## Web Server, Browser, TLS & WAF

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Web server hardening** | *Ano:* `server_tokens off`, hadlangan ang method, i-disable ang autoindex, mag-apply ng header sa server side. *Bakit:* Bawasan ang information leak & tiyak na risk. *Hangganan:* Ang header ay tumutulong, ngunit hindi kapalit ng app validation. | Ihiwalay ang responsibilidad: server ang nagtatakda ng header; app pa ring dapat mag-validate ng input, mag-authenticate, mag-authorize, at gumamit ng anti-CSRF. |
| **TLS/HTTPS** | *Ano:* Modern TLS, HSTS, redirect HTTP→HTTPS, OCSP stapling. *Bakit:* I-encrypt ang traffic at iwasan ang downgrade. *Hangganan:* Ang TLS ay nagpoprotekta sa channel, hindi sa app logic o access rights. | I-verify gamit ang `testssl.sh`/SSL Labs. Protektahan ang private key ng mahigpit na permissions. |
| **WAF** | *Ano:* I-filter ang mapanganib na pattern (SQLi/XSS). Magsimula sa DetectionOnly, saka Blocking nang paunti-unti. *Bakit:* Magdagdag ng detection/filter layer. *Hangganan:* Maaaring false positive, hindi nakikitang local/lateral movement, at maaaring malampasan. Kailangang i-tune sa app. | Ang WAF ay nagbabawas ng tsansa ng exploitation ngunit **hindi kapalit** ng secure code. |

## Database & Runtime

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Database hardening** | *Ano:* I-bind sa `127.0.0.1`/Unix socket, least privilege bawat app user, i-disable ang remote root access. *Bakit:* Hadlangan ang network access. *Hangganan:* Kung nakompromiso ang app, maaari pa rin itong ma-access ang DB gamit ang karapatan ng app user. | Ihiwalay ang user bawat app. Huwag gumamit ng `root` user para sa app connection. |
| **Database encryption** | *Ano:* Isaalang-alang ang at-rest encryption (nag-iiba ang TDE support ayon sa engine/version/edition) o volume encryption (LUKS). *Bakit:* Protektahan ang data kung ninakaw ang disk. *Hangganan:* Hindi nagpoprotekta kung live ang machine at maaabot ng attacker na nasa loob na ang app/DB. | Ang pag-encrypt ng backup ay kasinghalaga, minsan mas kritikal. |
| **Runtime hardening** | *Ano:* Patakbuhin ang runtime bilang non-root, hadlangan ang resource, bawasan ang dangerous function. *Bakit:* Hadlangan ang epekto ng RCE. *Hangganan:* Ang compromised runtime na may lokal na access ay maaaring subukang samantalahin ang iba pang lokal na serbisyo sa parehong machine. | Fokus sa isolation bawat serbisyo, hindi lamang "non-root". |

## Logging, Monitoring & Detection

Ang mahalaga ay hindi "mag-log ng karamihan", kundi **mag-log ng kayang aksyunan**.

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Audit & FIM** | *Ano:* `auditd` para sa critical changes, File Integrity Monitoring para sa importanteng file. *Bakit:* Tuklasin ang hindi awtorisadong pagbabago. *Hangganan:* Kailangan ng pinangangalagaang baseline. Ang legitimate changes (deploy) ay maaaring magdulot ng noise kung hindi inaasikaso. | Fokus sa `/etc`, web/DB config, key, at critical directory. |
| **Centralized logs & log protection** | *Ano:* Kolektahin ang relevant logs, protektahan ang integrity ng log. *Bakit:* Kung nakakuha ng root access ang attacker, maaaring tanggalin ang lokal na log. *Hangganan:* Kailangan ng mas protektadong hiwalay na channel. | Isaalang-alang ang pagpapadala ng log sa hiwalay na sistema na may ibang access rights. |
| **Anomaly-based detection** | *Ano:* Bantayan ang suspicious login, bagong user, hindi karaniwang proseso, abnormal outbound connection, privilege changes. *Bakit:* Maraming atake ang walang malinaw na "exploit" na senyales. *Hangganan:* Kailangan ng panahon para makilala ang normal na pattern. Ang alert na walang may-ari at follow-up path ay walang silbi. | Magtakda ng may-ari ng alert at simpleng escalation path. |

## Backup, Recovery & Incident Response

Sa single-tier, ang paghiwalay ng backup ay mas mahalaga kaysa sa iniisip ng karamihan.

| Control | Ano / Bakit / Hangganan | Nota |
|---|---|---|
| **Hiwalay na backup** | *Ano:* I-store ang kopya sa labas ng machine (iba't ibang lokasyon/kredensyal). *Bakit:* Maaaring gamitin ang production account para tanggalin ang lokal na backup. *Hangganan:* Kung naka-store ang backup encryption key sa parehong machine, maaari itong mabura/makawala. | Ihiwalay ang pamamahala ng key. Gumamit ng dedicated backup account na may minimum rights. |
| **Restore test** | *Ano:* Subukan ang restore sa isolated environment nang regular. *Bakit:* Patunayan na talagang maaaring mabawi ang backup. *Hangganan:* Dapat sapat na katulad ang test environment para mailantad ang compatibility issue. | **Praktikal na tuntunin:** Ang backup na hindi pa nate-test ang restore ay katumbas ng walang backup. |
| **Simpleng incident response** | *Ano:* Daloy: Detect → Contain → Investigate → Recover → Evaluate. *Bakit:* Iwasan ang panic at iwasan ang re-compromise. *Hangganan:* Sa root compromise, huwag magtiwala sa lokal na output. Bigyang-prioridad ang isolation, protektahan ang centralized evidence, at magpasya kung mag-rebuild mula sa trusted source. | Fokus sa credential rotation, pagsasara ng entry path, pag-verify ng baseline, at dokumentasyon ng kronolohiya. |

## Pag-verify ng Hardening

Ihiwalay ayon sa function para mas realistic.

### Preventive (pag-iwas)

| Check | Verify |
|---|---|
| Tanging kailangang port ang bukas | `ss -tulnp` / firewall status |
| DB lamang sa `127.0.0.1` o Unix socket | DB config + test connection mula sa labas ng host |
| SSH gumagamit ng key; root/password auth naka-disable | `sshd_config` + login test |
| Serbisyo tumatakbo bilang hiwalay na user | `ps aux` / systemd units |
| Secret hindi nasa repo at may mahigpit na permissions | File audit & `.gitignore` |

### Detective (pagtuklas)

| Check | Verify |
|---|---|
| `auditd` aktibo para sa critical file/config | Audit rules & logs lumilitaw |
| File Integrity Monitoring tumatakbo | May baseline at natutuklasan ang pagbabago |
| Relevant logging aktibo at centrally accessible | Gumagana ang log flow, sapat ang retention |
| May may-ari at follow-up path ang alert | May simpleng alert owner list |

### Recovery (pagbawi)

| Check | Verify |
|---|---|
| Backup hiwalay mula sa production machine | Lokasyon, kredensyal, permissions hiwalay |
| Restore test nagtagumpay nang hindi bababa sa isang beses | Naitala ang petsa + resulta sa isolated environment |
| May plan para sa isolation & credential rotation | Maikling dokumento na magagamit sa panic |
| Kaya bumalik sa trusted baseline | Naidokumento ang rebuild/recovery path |

## Mga Karaniwang Pagkakamali & Hangganan ng Single-Tier Hardening

| Karaniwang pagkakamali | Bakit mapanganib | Paano iwasan |
|---|---|---|
| **Pagbubukas ng DB port sa publiko** | Direktang nagpapalawak ng attack surface | Lamang `127.0.0.1`/Unix socket + mahigpit na firewall |
| **SSH root + password auth** | Paboritong target ng brute force | SSH key, i-disable ang dalawa, hadlangan access |
| **Pag-asa lamang sa header/WAF** | Pag-aakalang sapat na ang protection layer | Ang header & WAF ay tumutulong, ngunit validation, auth, authorization ay mananatiling mandatory sa app |
| **"Sarado mula sa labas" = ligtas** | Pagbalewala sa lokal at east-west access | Tandaan: kung nakompromiso ang runtime/app, maaari itong gumamit ng local access |
| **Hindi nate-test na backup** | Bigo kapag tunay na kailangan | Mag-iskedyul ng periodic restore tests; ihiwalay ang kopya at key |
| **Sobrang pag-apply ng `noexec/nosuid/nodev`** | Maaaring masira ang app nang walang dahilan | I-apply bawat partition ayon sa function; laging subukan sa lab |
| **Log na nakaimbak lamang, hindi aksyunan** | Nagiging walang silbi ang detection | Magtakda ng alert owner + escalation path |

**Hangganan ng single-tier hardening:** Mababawasan mo ang bilis, mahahadlangan mo, at madedetekta mo ang atake. **Hindi mo maaalis** ang risk ng SPOF sa pamamagitan lamang ng configuration. Kung buong machine ay ganap na nakompromiso, ang magagawa mo ay **limitahan ang pinsala, protektahan ang ebidensya, at makabawi mula sa trusted source**.

## Konklusyon

Ang single-tier hardening ay tungkol sa **pagbawas ng espasyo ng paggalaw, hindi paggawa ng hindi matalong sistema**. Magsimula sa pag-unawa sa threat model & attack surface, mag-apply ng least privilege + isolation, ihiwalay ang preventive/detective/recovery, at pinakamahalaga: **subukan ang inilapat mo**.

Ang configuration ay maaaring tama, ngunit may hangganan pa rin. Ang nagtatangi sa mature hardening ay ang kakayahang sumagot: *"Kung bumagsak ito, ano pa ang maaaring maiwasan, madetekta, o mabawi?"*

## Mga Sanggunian

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — Sanggunian ng secure configuration bawat produkto
- [CIS Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — Prayoridad ng security control
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — Gabay sa incident response
- [CISA — Use Logging on Business Systems](https://www.cisa.gov/resources-tools/resources/use-logging-business-systems) — Pamamahala ng log, detection & protection
- [CISA — Stop Ransomware Guide](https://www.cisa.gov/stopransomware) — Hiwalay na backup, protection ng kopya at recovery
- [systemd.exec Manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) — Mga opsyon ng sandboxing bawat service unit
