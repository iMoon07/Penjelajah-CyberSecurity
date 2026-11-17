# Thumbnail Prompt — Hackers: Heroes of the Computer Revolution

Buku: `Hackers Heroes of the Computer Revolution.pdf` (Steven Levy, edisi 2010, 520 hlm)
Sumber isi: `hackers-heroes-of-the-computer-revolution-en.md` (ekstraksi teks penuh, 520/520 halaman)
Template: `../prompt-thumb-template.md`

Fokus visual yang dipilih (dari isi buku):
- **Subjek utama:** laboratorium riset MIT, malam hari, akhir 1950-an — konsol TX-0/PDP-1.
- **Simbol pendukung:** kertas pita berlubang, CRT hijau, jejak bip *Spacewar*, garis blueprint rel model (TMRC).
- **Mood:** khidmat, heroik, malam, revolusioner — kelahiran sebuah budaya, bukan adegan aksi cyberpunk.

---

## Prompt (siap tempel)

```
Create a book thumbnail (16:9, 1920×1080) for the classic book "Hackers: Heroes of
the Computer Revolution" by Steven Levy.

ART DIRECTION — "Analog Technical Archive":
- Editorial flat-vector illustration with a subtle blueprint grid on deep ink-navy
  background (#0B1220), warm paper-white accents (#F5EFE6).
- Accent colors: phosphor green (#33FF99) for the CRT glow, amber (#FFB000) for lamp
  highlights and the title brush-stroke, muted steel blue for the machinery.
- Soft vignette, faint scanline texture, slight paper grain — like a printed cover of
  a 1960s technical manual.
- Clean bold sans-serif for the title, monospaced for small technical captions.

MAIN SUBJECT (center-left):
A 1959 MIT research lab at night. A huge vintage minicomputer console of the PDP-1
era: rows of steel toggle switches, blinking amber indicator lamps, a round smoke-gray
CRT glowing phosphor green, and a Flexowriter teleprinter feeding a long strip of
punched paper tape that curls across the foreground. A single desk lamp casts a warm
pool of light while the room falls into deep navy shadow. The silhouette of one young
hacker in a short-sleeve shirt leans in, one hand on a switch, face lit only by the CRT.

SUPPORTING SYMBOLS (subtle, not crowded):
- Faint binary digits (0/1) drifting like dust in the light beam.
- A paper-tape strip with clearly visible hole patterns, curling like a ribbon.
- Ghosted background blueprint lines of a circuit board and a model-railroad track,
  hinting at the Tech Model Railroad Club origin of the story.
- A tiny distant green blip pattern on the CRT screen suggesting a Spacewar dogfight.

MOOD: reverent, heroic, nocturnal, quietly revolutionary — the birth of a hacker
culture, not a cyberpunk action scene.

TITLE TREATMENT:
- Main title "HACKERS" in large bold white letters at the top-center, sitting on a
  subtle amber brush-stroke band.
- Subtitle "Heroes of the Computer Revolution" in smaller white sans-serif beneath.
- Keep text inside a safe area (10% margin), legible at 320 px wide.

NEGATIVE PROMPT:
neon cyberpunk city, hooded hacker, green matrix rain, skull, glowing padlock,
stock-photo businessman, realistic portrait of any real person, brand logos or
trademarks, gibberish text, random code symbols, 3D render, plastic gloss,
overcrowded composition, watermark.

TECHNICAL:
aspect 16:9, 1920×1080, high detail, sharp vector edges, cinematic lighting,
no text except the title block described above.
```

---

## Varian (opsional)

**A. Versi terang "Blueprint":**
```
Same composition, but light theme: warm paper background (#F5EFE6) with a faint
navy blueprint grid, ink-navy machinery lines, amber and teal accents. Flat vector
technical illustration, no dark vignette. Same title treatment in navy + orange.
```

**B. Versi "Cover klasik" (potrait-ish crop untuk sampul):**
```
Vertical 4:5 crop centered on the CRT and the hacker's silhouette, title at the top
in bold white on amber band, more shadow and negative space, poster-like.
```

---

## Catatan Reproduksi

- Prompt ini menghasilkan ilustrasi **orijinal** (bukan foto), aman untuk blog/portofolio.
- Simpan output di `images/overview/hackers-heroes-of-the-computer-revolution.png`
  (samakan dengan pola `Port-Swigger/.../images/overview/*.png`).
- Kalau ingin seragam dengan koleksi PortSwigger (navy + oranye, grid putih), ubah
  palet & layout ke `Port-Swigger/prompt-thumb.md`.