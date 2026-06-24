[🇬🇧 English](#english) | [🇮🇩 Bahasa Indonesia](#bahasa-indonesia)

---

<h1 id="english">🇬🇧 Penjelajah-CyberSecurity 📚</h1>

This repository serves as the **Database / Content Backend** for my cybersecurity write-ups, lab explorations, and research. 

> **Where is the actual Website?**
> This repo only contains raw `.md` files. The beautiful website that dynamically reads and displays these files is located here: [imoon07.github.io](https://github.com/iMoon07/imoon07.github.io)

## 🛠️ How This Works (For Fellow Tinkerers)

If you followed the guide from my [Portfolio Engine Repo](https://github.com/iMoon07/imoon07.github.io) and want to replicate this 2-repo setup, here is how you manage the content side of things.

### The "Complicated but Cool" Workflow xD
Because we don't use a traditional CMS dashboard (like WordPress), writing a new article requires a true hacker workflow:

1. **Create Folders:** Organize your topics neatly (e.g., `Architect/`, `Teaming/`).
2. **Write Markdown:** Create your article. (Pro tip: Create an English `-en.md` and Indonesian `-id.md` version if you want bilingual support).
3. **Get the Raw Link:** After pushing your new article to GitHub, click the "Raw" button on your `.md` file to get the `https://raw.githubusercontent.com/...` link.
4. **Link it to the Frontend:** Copy that raw link, jump over to your Frontend Repository, and paste it into the `data.js` file so your website knows it exists!

Is it a bit manual? Yes. Is it cool because you're using Git as a Headless CMS? Absolutely. 😎

## Repository Structure
- **Architect/**: Infrastructure, Lab Setups, and Systems Engineering.
- **Teaming/**: Penetration Testing (Red) & Defensive Strategies (Blue/Purple).
- **Malware/**: Exploit and Malware analysis.

## Legal & Disclaimer
All research, write-ups, and toolkits provided in this repository are for educational and research purposes only. The author is not responsible for any misuse of the information provided.

## License
MIT License - see the LICENSE file for details.

---

<br><br>

<h1 id="bahasa-indonesia">🇮🇩 Penjelajah-CyberSecurity 📚</h1>

Repositori ini berfungsi sebagai **Database / Content Backend** untuk menyimpan semua tulisan, *write-ups*, dokumentasi ngelab, dan *research* Cyber Security gue.

> **Terus Website aslinya di mana?**
> Repo ini *pure* cuma buat nyimpen file mentahan `.md`. Web estetik yang kerjanya ngebaca dan nampilin file-file ini ada di sini: [imoon07.github.io](https://github.com/iMoon07/imoon07.github.io)

## 🛠️ Cara Kerjanya (Buat Sesama Tukang Ngoprek)

Kalau lu udah ngikutin tutorial dari [Repo Mesin Portfolio](https://github.com/iMoon07/imoon07.github.io) gue dan mau niru arsitektur 2-repo ini, di sini adalah tempat lu ngatur kontennya.

### Alur Kerja "Ribet Tapi Keren" xD
Karena kita nggak pakai *Dashboard CMS* manja kayak WordPress, nulis artikel baru di sini butuh *workflow hacker* sejati:

1. **Bikin Folder:** Rapihin topik lu (Contoh: `Architect/`, `Teaming/`).
2. **Nulis Markdown:** Bikin artikel lu. (Pro tip: Bikin dua versi, `-en.md` buat Inggris dan `-id.md` buat Indo kalau mau *support* dua bahasa).
3. **Ambil Link Mentahan (Raw):** Setelah artikel lu di-*push* ke GitHub, klik tombol "Raw" di file `.md` lu buat dapetin link `https://raw.githubusercontent.com/...`
4. **Sambungin ke Frontend:** Copy link *Raw* tadi, balik ke Repositori Frontend lu, dan *paste* ke dalem file `data.js` biar web lu tahu artikel itu eksis!

Manual banget ya? Iya. Tapi keren kan nulis blog berasa lagi ngoding dan pakai Git sebagai *Headless CMS*? Jelas dong. 😎

## Struktur Repositori
Semua dokumentasi dan riset disusun rapi berdasarkan domain Cyber Security:
- **Architect/**: Infrastruktur, Setup Lab, dan Systems Engineering.
- **Teaming/**: Penetration Testing (Red) & Strategi Pertahanan (Blue/Purple).
- **Malware/**: Analisis Exploit dan Malware.

## Disclaimer Hukum
Semua riset, *write-ups*, dan *tools* di repo ini murni untuk tujuan edukasi dan riset (*Educational Purposes Only*). Gue nggak bertanggung jawab kalau ilmu di sini disalahgunakan buat hal yang aneh-aneh.

## Lisensi
Projek ini berlisensi MIT - silakan baca file LICENSE untuk detailnya.
