# Book Thumbnail Prompt Template
## Reusable "Analog Technical Archive" Series

Template prompt untuk generate thumbnail buku/e-book di koleksi `Penjelajah-CyberSecurity/e-books/`.
Pakai file ini sebagai basis: ganti bagian `[...]` sesuai isi buku, lalu kirim ke image generator
(ChatGPT/DALL·E, Midjourney, Firefly, Gemini, dsb.).

---

## 1. Cara Pakai

1. Baca buku (ekstrak teks): `python3 ai-tools/read_pdf.py <file.pdf> --format md -o buku.md`
2. Tentukan **fokus visual** + **2–3 simbol pendukung** dari isi buku (jangan mengarang).
3. Salin blok `PROMPT` di bawah ke image generator.
4. Simpan hasil di `<folder-buku>/images/overview/<slug>.png` + catat prompt yang dipakai.

---

## 2. Aturan Visual (Global Identity)

- Canvas: 16:9, 1920×1080 (atau 1280×720 untuk ringan).
- Gaya: editorial flat-vector + ilustrasi teknis, garis bersih, hierarki jelas.
- Palet dasar: ink-navy `#0B1220`, kertas hangat `#F5EFE6`, aksen `#33FF99` / `#FFB000`.
- Varian terang (opsional): latar kertas `#F5EFE6`, tinta navy `#0B1220`, aksen oranye.
- Tekstur: grid halus / blueprint, scanline tipis, grain kertas — seperti sampul manual teknis lama.
- Tipografi: sans-serif tebal untuk judul; monospace untuk keterangan teknis kecil.
- Safe area 10% untuk judul; judul harus terbaca pada 320 px lebar.

---

## 3. Struktur Prompt (Wajib)

1. **Tema** — 2–3 kalimat inti buku (hasil baca, bukan tebakan).
2. **Subjek utama** — 1 fokus + era + lokasi + pencahayaan.
3. **Simbol pendukung** — 2–3 elemen teknis yang benar-benar ada di buku.
4. **Mood** — 1 frasa emosi (mis. "reverent, heroic, nocturnal").
5. **Title treatment** — judul utama + subjudul + posisi.
6. **Negative prompt** — yang harus dihindari.
7. **Teknis** — rasio, resolusi, detail, larangan teks asal.

---

## 4. PROMPT (Template — Isi Bagian `[...]`)

```
Create a book thumbnail (16:9, 1920×1080) for the book "[JUDUL BUKU]" by [PENULIS].

ART DIRECTION — "Analog Technical Archive":
- Editorial flat-vector illustration with a subtle blueprint grid on deep ink-navy
  background (#0B1220), warm paper-white accents (#F5EFE6).
- Accent colors: [WARNA AKSEN 1] for [FUNGSI], [WARNA AKSEN 2] for [FUNGSI],
  muted steel blue for machinery.
- Soft vignette, faint scanline texture, slight paper grain — like a printed
  technical manual cover from [ERA].
- Clean bold sans-serif for the title, monospaced for small technical captions.

MAIN SUBJECT (center-left):
[DESKRIPSI SUBJEK UTAMA: siapa/apa, di mana, kapan, pencahayaan, komposisi.
 Contoh: "A 1959 MIT research lab at night. A huge vintage minicomputer console:
 rows of steel toggle switches, blinking amber indicator lamps, a round CRT
 glowing green, a teleprinter feeding a long strip of punched paper tape..." ]

SUPPORTING SYMBOLS (subtle, not crowded):
- [SIMBOL 1 — mis. faint binary digits drifting in the light beam]
- [SIMBOL 2 — mis. paper-tape strip with visible hole patterns]
- [SIMBOL 3 — mis. ghosted blueprint lines hinting at the origin story]
- Optional: [SIMBOL 4 — mis. a tiny green blip pattern on the CRT]

MOOD: [EMOSI: mis. reverent, heroic, nocturnal, quietly revolutionary —
 "the birth of a culture", not a cyberpunk action scene.]

TITLE TREATMENT:
- Main title "[JUDUL]" in large bold white letters, [POSISI: upper-left / top-center],
  sitting on a subtle accent-colored brush-stroke band.
- Subtitle "[SUBJUDUL]" in smaller white sans-serif beneath.
- Keep text inside a safe area (10% margin), legible at 320 px wide.

NEGATIVE PROMPT:
[DAFTAR LARANGAN — mis. neon cyberpunk city, hooded hacker, green matrix rain,
skull, glowing padlock, stock-photo businessman, realistic portrait of any real
person, brand logos or trademarks, gibberish text, random code symbols, 3D render,
plastic gloss, overcrowded composition, watermark.]

TECHNICAL:
aspect 16:9, 1920×1080, high detail, sharp vector edges, cinematic lighting,
no text except the title block described above.
```

---

## 5. Contoh Isian (Hackers — Steven Levy)

File contoh hasil isian: `hackers-heroes-of-the-computer-revolution/prompt-thumb.md`

---

## 6. Tips Kualitas

- **Akurasi dulu, dekorasi belakangan.** Semua simbol harus ada di buku.
- **Jangan** pakai klise: neon cyberpunk, hulu/hoodie, matrix rain, tengkorak, gembok.
- **Jangan** pakai wajah realistis orang terkenal / logo merek.
- **Satu fokus** per thumbnail; jangan padat.
- Untuk seri buku: pertahankan palet & layout judul yang sama, variasikan subjek + diagram.
- Simpan prompt yang dipakai di file buku agar bisa direproduksi.