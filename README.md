[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

<h1 id="english">Penjelajah-CyberSecurity</h1>

This repository serves as the Content Backend (Database) for my cybersecurity lab documentations, write-ups, and research. 

This repository only stores raw Markdown (`.md`) files. The frontend engine that dynamically fetches and renders these files is located at: [imoon07.github.io](https://github.com/iMoon07/imoon07.github.io)

## How It Connects to The Frontend

We use GitHub as a Headless CMS. The workflow is manual, but it guarantees zero backend vulnerabilities.

1. **Write the Article:** Create your Markdown file inside the relevant category folder (e.g., `Architect/`). For bilingual support, create `-en.md` and `-id.md` versions.
2. **Push to GitHub:** Commit and push your files to this repository.
3. **Get the Raw URL:** Navigate to your `.md` file on GitHub and click the "Raw" button. Copy the `https://raw.githubusercontent.com/...` link.
4. **Inject to Frontend:** Open `data.js` in your Frontend repository (`yourusername.github.io`) and create a new JSON object for your article, pasting the Raw URL into the `rawUrl` field.

A bit complicated just for publishing a single post? Yes. But using Git as your database is peak engineering xD.

## Repository Structure
- **Architect/**: Infrastructure, Systems Engineering, and Lab Setups.
- **Teaming/**: Penetration Testing (Red Teaming) and Defense (Blue/Purple Teaming).
- **Malware/**: Exploit Analysis and Malware Reverse Engineering.

## License & Disclaimer
Educational purposes only. MIT License.

---
<br><br>

<h1 id="bahasa-indonesia">Penjelajah-CyberSecurity</h1>

Repositori ini berfungsi sebagai Content Backend (Database) untuk menyimpan seluruh dokumentasi ngelab, write-up, dan riset Cyber Security gue.

Repositori ini murni cuma nyimpen file mentahan Markdown (`.md`). Mesin frontend yang bertugas narik dan nge-render file-file ini ada di sini: [imoon07.github.io](https://github.com/iMoon07/imoon07.github.io)

## Cara Integrasi ke Frontend

Kita pakai GitHub sebagai Headless CMS. Workflow-nya manual, tapi ini ngejamin web lu 100% kebal dari serangan sisi server.

1. **Tulis Artikel:** Bikin file Markdown lu di folder kategori yang pas (misal `Architect/`). Kalau mau bilingual, bikin versi `-en.md` dan `-id.md`.
2. **Push ke GitHub:** Commit dan push file lu ke repositori ini.
3. **Ambil Raw URL:** Buka file `.md` lu di GitHub, klik tombol "Raw". Copy link `https://raw.githubusercontent.com/...` tersebut.
4. **Suntik ke Frontend:** Buka file `data.js` di repositori Frontend lu (`username.github.io`), bikin objek JSON baru, dan paste link Raw tadi ke bagian `rawUrl`.

Agak ribet cuma buat rilis satu artikel doang? Iya. Tapi pamerin kalau lu nulis blog pakai Git sebagai database itu nilai plus tersendiri xD.

## Struktur Repositori
- **Architect/**: Infrastruktur, Systems Engineering, dan Setup Lab.
- **Teaming/**: Penetration Testing (Red Teaming) dan Pertahanan (Blue/Purple Teaming).
- **Malware/**: Analisis Exploit dan Reverse Engineering Malware.

## Lisensi & Disclaimer
Murni untuk edukasi. MIT License.
