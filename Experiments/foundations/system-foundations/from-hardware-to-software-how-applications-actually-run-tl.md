# Mula sa Hardware Hanggang sa Software: Paano Talagang Gumagana ang mga Aplikasyon

[🇮🇩 Baca dalam Bahasa Indonesia](from-hardware-to-software-how-applications-actually-run-id.md)  
[🇬🇧 Read in English](from-hardware-to-software-how-applications-actually-run-en.md)  
[🇲🇾 Baca dalam Bahasa Melayu](from-hardware-to-software-how-applications-actually-run-ms.md)

![Mula sa Hardware Hanggang sa Software: Paano Talagang Gumagana ang mga Aplikasyon](from-hardware-to-software.png)

## Simpleng Tanong: Paano Gumagana ang Isang File?

Naisip mo na ba kung paano kapag nag-click ka ng application, biglang lumalabas ang window sa screen mo?

Nag-click tayo ng icon. Pagkalipas ng ilang sandali, puwede nang pindutin ang mga button, mag-type ng text, at lumabas ang mga larawan. Ang nakikita lang natin ay ang interface. Ngunit marami nang pangyayari sa likod ng eksena bago ito mangyari.

Ipapaliwanag ng artikulong ito ang proseso sa konseptwal na paraan. Hindi ito para maging hardware engineer, bagkus para magkaroon ka ng malawak na pang-unawa kung paano talaga gumagana ang mga aplikasyon.

## Program vs Proseso: Ano ang Pagkakaiba?

Bago tayo magpatuloy, mahalagang maunawaan ang pagkakaiba ng dalawa:

- **Program** — Isang file na naka-imbak sa disk (halimbawa: `firefox`, `chrome.exe`, o binary ng app). Koleksyon lamang ito ng mga instruction sa anyong data. Kapag hindi pa ito pinapatakbo, ito ay "di-aktibo" — puro code lamang.
- **Proseso** — Isang program na kasalukuyang pinapagana. Sa sandaling i-click mo ito at magsimula nang tumakbo ang application, ito ay gagawing proseso ng operating system. Ang proseso ay may sariling memory space, kasalukuyang estado, mga bukas na file, at mga nakalaang resources.

**Simpleng analohiya:** Ang program ay katulad ng recipe na nakasulat sa cookbook. Ang proseso naman ay katulad ng lutong ulam na aktwal nang niluluto sa kusina. Ang recipe ay puwede manatili sa istante magpakailanman, ngunit ang ulam ay nabubuo lamang kapag nagsimula na tayong magluto.

## Mga Layer ng Kompyuter: Hardware, Operating System, at Aplikasyon

Upang gumana ang isang aplikasyon, tatlong pangunahing layer ang nagtutulungan:

| Layer | Papel | Analohiya |
| --- | --- | --- |
| **Hardware** | Mga pisikal na bahagi: CPU, RAM, storage (SSD/HDD), GPU, at input/output devices. | Mga kagamitan sa kusina: kalan, lamesa, kaldero, at kutsilyo. |
| **Operating System (OS)** | Tagapamahala at tagapamagitan. Pinamamahalaan nito ang resources, binibigyan ng access sa hardware, nag-iiskedyul ng mga proseso, at pinoprotektahan ang mga aplikasyon sa isa't isa. | Punong kusinero. Siya ang nagdedesisyon kung sino ang puwedeng gumamit ng kalan, nag-oorganisa ng trabaho, at pumipigil sa kaguluhan. |
| **Aplikasyon (User Space)** | Mga direktang ginagamit natin: browser, text editor, laro, atbp. Hindi direktang nakikipag-usap ang aplikasyon sa hardware — dumadaan ito sa operating system. | Ang recipe at ang ulam na gusto nating lutuin. |

Mahalagang tandaan: **Bihira nang direktang makipag-usap ang mga aplikasyon sa hardware.** Gumagamit ito ng mga *system call* upang humingi ng tulong sa operating system.

## Paglalakbay ng Isang Aplikasyon: Mula sa Click Hanggang sa Screen

Sundan natin ang proseso hakbang-hakbang.

### Hakbang 1: Kahilingan na Patakbuhin ang Program
Nag-click ka ng icon ng aplikasyon. Pipiliin ang executable file na naka-imbak sa disk (halimbawa: `/usr/bin/` o `Program Files/`) upang ito ay patakbuhin.

### Hakbang 2: Gumagawa ang OS ng Proseso
Binabasa ng operating system ang file ng programa at gagawin ang mga sumusunod:

- **Gumawa ng bagong proseso** — Bigyan ito ng natatanging ID (PID).
- **Maglaan ng memory** — Maglaan ng espasyo sa RAM para sa code, data, at pangangailangan ng proseso.
- **I-set up ang konteksto** — Tukuyin kung sinong user ang nagpapatakbo, mga permiso, at mga resources na pinapayagan.

### Hakbang 3: Pag-load Mula sa Disk Papunta sa RAM
Ang mga programa ay naka-imbak sa mas mabagal na media (SSD/HDD). Upang maging mas mabilis ang pagpapatakbo, ilo-load ng OS ang mga kinakailangang bahagi sa **RAM**.

Bakit RAM? Sapagkat mas mabilis na ma-access ng CPU ang RAM kaysa direktang sa disk. Kaya kapag puno na ang RAM o kailangan nang gumamit ng swap, mas bumabagal ang mga aplikasyon.

### Hakbang 4: Pinapagana ng CPU ang mga Instruksyon
Ngayon, ang **CPU** na ang gagawa. Kukunin nito ang mga instruksyon nang paisa-isa mula sa memory, ide-decode, at isasagawa ang mga ito.

Isipin ang CPU bilang isang kusinero na nakatayo lamang sa "prep counter" (RAM). Hindi ito palaging babalik sa pantry (disk) para sa bawat sangkap. Ang pantry ay para sa pangmatagalang imbakan, ang prep counter naman ay para sa aktibong gawain.

### Hakbang 5: Pakikipag-ugnayan sa Pamamagitan ng System Call
Kapag ang isang aplikasyon ay nangangailangan ng bagay na lampas sa saklaw nito — tulad ng pagbukas ng file, pagkonekta sa internet, o pagguhit sa screen — hihingi ito ng tulong sa OS sa pamamagitan ng *system call*.

Mga halimbawa:
- **Pagbukas ng file** → Hihingi ang aplikasyon sa OS na basahin ang file mula sa disk.
- **Pagpapakita ng window** → Hihingi ang aplikasyon sa OS (sa pamamagitan ng window manager) na magpakita ng bagay sa screen.
- **Pag-save ng data** → Hihingi ang aplikasyon sa OS na isulat ang data sa storage.

Susuriin ng OS ang mga permiso at ipapasa ang kahilingan sa tamang hardware.

### Hakbang 6: Lumalabas ang Resulta sa Screen
Matapos ang lahat ng hakbang na ito, ang hiniling mo ay makikita na sa screen. Lalabas ang button, magre-render ang webpage, o ipapakita ang error message.

Ang lahat ng ito ay maaaring mangyari sa loob lamang ng milisegundo, kahit na may dose-dosenang maliliit na hakbang na nadaanan.

## Bakit Kailangan Natin ng Operating System?

Kung direktang makikipag-usap ang mga aplikasyon sa hardware, tila mas epektibo ito. Ngunit sa realidad, magiging magulo ito nang husto.

May mga dahilan kung bakit mahalaga ang OS:

- **Abstraction** — Hindi kailangang malaman ng mga aplikasyon ang eksaktong specs ng RAM, uri ng SSD, o GPU driver mo. Nagbibigay ang OS ng pare-parehong interface.
- **Pamamahala ng resources** — Kapag sabay-sabay na humingi ng CPU time ang sampung aplikasyon, ipamamahagi ito ng OS nang patas upang pantay-pantay na makapagpatakbo ang lahat.
- **Isolation** — Hindi dapat malayang mabasa ng proseso ng isang aplikasyon ang memory ng ibang aplikasyon. Mahalaga ito sa estabilidad at seguridad.
- **Seguridad at permiso** — Tinutukoy ng OS kung anong mga file ang puwedeng i-access ng isang aplikasyon, saan ito puwedeng kumonekta, at ano ang hindi pinapayagan.
- **Kahusayan** — Matalinong inaayos ng OS kung ano ang kailangang i-load, ano ang puwedeng ipagpaliban, at paano pinakamahusay na gamitin ang mga limitadong resources.

Kung wala ang OS, kailangang maunawaan ng bawat aplikasyon ang lahat ng hardware sa mundo. Sa tulong ng OS, sapat na na maunawaan ng aplikasyon ang OS mismo.

## Maikling Pagtanaw sa Memory Hierarchy

Bago tayo lumipat sa susunod na artikulo, heto ang simpleng larawan ng hierarchy ng memory:

| Komponente | Bilis | Laki | Layunin |
| --- | --- | --- | --- |
| **Registers** | Pinakamabilis | Napakaliit (bytes) | Nagtatago ng data na direktang pinoproseso ng CPU sa sandaling iyon. |
| **CPU Cache (L1/L2/L3)** | Napakabilis | Maliit | Nagtatago ng madalas gamitin na data/instruksyon upang hindi na kailangang palaging pumunta sa RAM ang CPU. |
| **RAM (Main Memory)** | Mabilis | Katamtaman–Malaki (GB) | Nagtatago ng code, variables, at data para sa mga aktibong proseso. |
| **Storage (SSD/HDD)** | Mas mabagal | Napakalaki (GB–TB) | Pangmatagalang imbakan ng mga programa, file, at data. |

Simpleng tuntunin: **Kapag mas malapit sa CPU, mas mabilis at mas maliit. Kapag mas malayo, mas mabagal ngunit mas malaki.**

## Konklusyon

Sa madaling salita: **Ang program ay hindi proseso.** Ang program ay isang file na nakaupo lamang sa disk. Ang proseso naman ay ang program na binuhay sa RAM at isinasagawa ng CPU.

Ganito ang daloy: *click → gumagawa ang OS ng proseso → ilo-load sa RAM → isinasagawa ng CPU ang mga instruksyon → humingi ng tulong sa OS kung kinakailangan → lumalabas ang resulta sa screen*.

Ang pinakamahalagang maunawaan dito ay hindi ang detalye ng bawat chip, kundi ang malawak na larawan: hindi direktang hawak ng mga aplikasyon ang hardware. Ang operating system ang nagsisilbing tulay, ang RAM ang nagsisilbing "workbench", at ang CPU ang nagsasagawa ng aktwal na trabaho.

Ang pag-unawa sa mental model na ito ang magpapadali sa iyo na maunawaan ang mga susunod na paksa tulad ng memory, *system call*, at performance ng mga aplikasyon.

## Mga Sanggunian

- Silberschatz, A. et al. *Operating System Concepts* (10th Edition) — Mga konsepto ng proseso, pamamahala ng memory, at tungkulin ng OS.
- Bryant, R. E. & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective (CS:APP)* — Napakaganda para sa pag-unawa sa ugnayan ng hardware at software sa konseptwal na paraan.
- Tanenbaum, A. S. & Bos, H. *Modern Operating Systems* (5th Edition) — Malinaw at sistematikong paliwanag kung paano nagiging tulay ang OS sa pagitan ng mga aplikasyon at hardware.
