# The Hidden Cost of AI-Generated Code: Understanding and Managing Technical Debt

[🇮🇩 Baca dalam Bahasa Indonesia](hidden-cost-ai-generated-code-id.md)
[🇬🇧 Read in English](hidden-cost-ai-generated-code-en.md)
[🇲🇾 Baca dalam Bahasa Melayu](hidden-cost-ai-generated-code-ms.md)

Ito ay tungkol sa **nakatagong gastos ng code na gawa ng AI**: maaaring pabilisin ng AI ang paglikha ng software, ngunit ang paggawa ng software at ang pagpapanatili nito ay dalawang magkaibang problema.

![Hidden cost of AI-generated code](hidden-cost-ai-generated-code.png)

Layunin:
- Paano binabago ng AI ang gastos sa paggawa ng software
- Pagkakaiba ng pagsulat ng code at pagpapanatili nito
- Gastos sa pag-unawa, beripikasyon, at pagbabago
- Paano nakikilala at pinaprioridad ang technical debt
- Kung tunay bang nakakatipid ang AI o iniilipat lamang nito

## 1. Pinabilis ng AI ang Paglikha ng Code

Maaaring gawin ng AI (tulad ng Copilot, ChatGPT, Claude):

- Magsulat ng kumpletong function o module sa loob ng ilang segundo
- Gumawa ng boilerplate code
- Magbigay ng halimbawa ng implementasyon
- Pabilisin ang prototyping

Resulta: **bumaba nang malaki ang creation cost**. Ang code na dati ay tumatagal ng oras, ngayon ay tumatagal ng minuto.

## 2. Pagsulat ng Code ≠ Pagpapanatili ng Code

Ngunit may malaking pagkakaiba:

- **Pagsulat ng code**: paggawa ng isang bagay na tumatakbo.
- **Pagpapanatili ng code**: pag-unawa, pagbabago, beripikasyon, at pagtatanggol ng pangmatagalang konsekwensya.

Ang code na tumatakbo ay hindi nangangahulugang:

- Madaling maunawaan
- Madaling mabago
- Madaling masuri
- Ligtas

## 3. Mga Gastos na Madalas Nakatago

### Gastos sa pag-unawa (Understanding cost)

- Gaano katagal ang kailangan para maunawaan ang daloy ng code na gawa ng AI?
- May katuturan ba ang lohika ng implementasyon?
- Maipapaliwanag ba ang mga desisyon sa disenyo?

### Gastos sa beripikasyon (Verification cost)

- Tama ba ang code?
- May mga edge case na hindi tinutugunan?
- May mga kerentanan sa seguridad?

### Gastos sa pagpapanatili (Maintenance cost)

- Ano ang mangyayari kung magbabago ang mga pangangailangan?
- Paano hinahawakan ang mga bug?
- Paano ina-update ang mga dependency?

### Gastos sa pagbabago (Change cost)

- Gaano kahirap baguhin ang code nang hindi sinisira ang ibang bahagi?
- May mga hindi kinakailangang abstraksyon ba?

## 4. Technical Debt at AI

Hindi awtomatikong lumilitaw ang technical debt dahil gawa ng AI ang code. Maaaring manggaling ang technical debt sa:

- Mahinang desisyon sa disenyo
- Kakulangan ng oras
- Kakulangan ng pagsusuri
- Pagbabago ng pangangailangan ng negosyo

Gayunpaman, maaaring **pabilisin ng AI ang pag-accumulate ng utang** kung:

- Tinatanggap ang code nang walang pag-unawa
- Tinatanggap ang code nang walang beripikasyon
- Dinadagdag ang hindi kinakailangang abstraksyon
- Ipinakikilala ang hindi kinakailangang dependency

## 5. Pamamahala ng Technical Debt

Mga estratehiya para pamahalaan ang technical debt:

1. **Regular na audit** — periodicong suriin ang code na gawa ng AI.
2. **Pagsusuri** — siguraduhing may sapat na mga test.
3. **Dokumentasyon** — itala ang mga desisyon sa disenyo at mga palagay.
4. **Refactoring** — ayusin ang code na hindi malinaw o hindi episyente.
5. **Beripikasyon** — huwag basta-basta magtiwala sa output ng AI.

## 6. Konklusyon

Pinabilis ng AI ang paglikha ng code, ngunit hindi awtomatikong nabawasan ang gastos sa pag-unawa at pagpapanatili. LLM (tulad ng GPT-4, Claude, Gemini) at mga AI tool (Copilot, Cursor, atbp.) ay hindi lamang generator ng code; sila ay bahagi ng sistema ng pag-unlad na nangangailangan ng konteksto, direksyon, at pangangasiwa.

Para epektibong pamahalaan ang output ng LLM:

- **Konteksto**: Magbigay ng sapat na konteksto sa LLM—arkitektura, kumbensyon ng koponan, tunay na data, at mga limitasyon ng produksyon—hindi lamang lokal na prompt.
- **Direksyon**: Magtakda ng malinaw na layunin. Mas mahusay ang LLM sa mga tiyak na instruksyon at tinukoy na mga hangganan.
- **Sistema ng pangangasiwa**: Bumuo ng pipeline ng beripikasyon—review batay sa risk, automated tests, CI/CD guardrails, at dokumentasyon ng desisyon (ADR).
- **Modelo at tool**: Pumili ng mga modelo at tool na angkop sa pangangailangan. Hindi laging mas mabuti ang mas malaking modelo; mas epektibo ang mga tool na naka-integrate sa konteksto ng proyekto (tulad ng Cursor na may codebase awareness) kaysa sa generic na chatbot.

Ang pangunahing tanong ay hindi "kaya ba ng LLM magsulat ng code?", kundi "naiintindihan, dinidirekta, at tinatanggap pa rin ba natin ang responsibilidad para sa code na ginawa ng LLM at AI tool?"

> **Tandaan:** Hindi kaaway ang technical debt, ngunit dapat itong pamahalaan. Ang code na hindi naiintindihan ay utang na nag-iipon. Ang LLM at AI tool ay mga kasangkapan, hindi kapalit ng engineering judgment.

## Mga Sanggunian

- [IBM — Technical Debt](https://www.ibm.com/ph-en/think/topics/technical-debt)
- [Martin Fowler — Technical Debt](https://martinfowler.com/bliki/TechnicalDebt.html)
- [OWASP — Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Google — Software Engineering at Google](https://abseil.io/resources/swe-book)