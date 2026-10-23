# The Hidden Cost of AI-Generated Code: Understanding and Managing Technical Debt

[🇮🇩 Baca dalam Bahasa Indonesia](hidden-cost-ai-generated-code-id.md)
[🇬🇧 Read in English](hidden-cost-ai-generated-code-en.md)
[🇵🇭 Basahin sa Tagalog](hidden-cost-ai-generated-code-tl.md)

﷽

Ini membincangkan **kos tersembunyi kod yang dihasilkan AI**: AI boleh mempercepatkan penciptaan perisian, tetapi membina perisian dan menyelenggaranya adalah dua masalah berbeza.

![Hidden cost of AI-generated code](hidden-cost-ai-generated-code.png)

Tujuannya adalah memahami:
- Bagaimana AI mengubah kos pembinaan perisian
- Perbezaan antara menulis kod dan menyelenggara kod
- Kos pemahaman, pengesahan, dan perubahan
- Bagaimana technical debt dikenal pasti dan diprioritikan
- Sama ada AI benar-benar menjimatkan kos atau sekadar memindahkannya

## 1. AI Mempercepat Penciptaan Kod

AI (seperti Copilot, ChatGPT, Claude) boleh:

- Menulis fungsi atau modul lengkap dalam beberapa saat
- Menjana boilerplate code
- Memberikan contoh implementasi
- Mempercepat prototyping

Hasilnya: **kos penciptaan menurun dengan drastik**. Kod yang sebelumnya mengambil masa berjam-jam kini mengambil minit.

## 2. Menulis Kod ≠ Menyelenggara Kod

Tetapi terdapat perbezaan besar:

- **Menulis kod**: menghasilkan sesuatu yang berjalan.
- **Menyelenggara kod**: memahami, mengubah, mengesahkan, dan menanggung kesan jangka panjang.

Kod yang berjalan tidak semestinya:

- Mudah difahami
- Mudah diubah
- Mudah diuji
- Selamat

## 3. Kos yang Sering Tersembunyi

### Kos pemahaman (Understanding cost)

- Berapa lama masa yang diperlukan untuk memahami aliran kod yang dihasilkan AI?
- Adakah logik implementasinya masuk akal?
- Bolehkah keputusan reka bentuknya dijelaskan?

### Kos pengesahan (Verification cost)

- Adakah kod tersebut betul?
- Adakah terdapat edge case yang tidak ditangani?
- Adakah terdapat kerentanan keselamatan?

### Kos penyelenggaraan (Maintenance cost)

- Apa yang berlaku apabila keperluan berubah?
- Bagaimana bug ditangani?
- Bagaimana dependency dikemas kini?

### Kos perubahan (Change cost)

- Sejauh manakah sukarnya mengubah kod tanpa merosakkan bahagian lain?
- Adakah terdapat abstraksi yang tidak perlu?

## 4. Technical Debt dan AI

Technical debt tidak automatik timbul kerana kod dihasilkan oleh AI. Technical debt boleh datang dari:

- Keputusan reka bentuk yang lemah
- Kekangan masa
- Kekurangan pengujian
- Perubahan keperluan perniagaan

Namun, AI boleh **mempercepat pengumpulan utang** apabila:

- Kod diterima tanpa pemahaman
- Kod diterima tanpa pengesahan
- Abstraksi yang tidak perlu ditambah
- Dependency yang tidak perlu diperkenalkan

## 5. Mengurus Technical Debt

Strategi untuk mengurus utang teknikal:

1. **Audit berkala** — semak semula kod yang dihasilkan AI dari semasa ke semasa.
2. **Pengujian** — pastikan terdapat ujian yang mencukupi.
3. **Dokumentasi** — catatkan keputusan reka bentuk dan andaian.
4. **Refactoring** — perbaiki kod yang tidak jelas atau tidak cekap.
5. **Pengesahan** — jangan percaya output AI tanpa berfikir.

## 10. Kesimpulan

AI menurunkan kos pengeluaran kod, tetapi kos pemahaman, pengesahan, dan tanggungjawab kekal—bahkan boleh meningkat jika output LLM diterima tanpa disiplin kejuruteraan. LLM (seperti GPT-4, Claude, Gemini) dan alat AI (Copilot, Cursor, dll.) bukan sekadar penjana kod; mereka adalah sebahagian daripada sistem pembangunan yang memerlukan konteks, arah, dan pengawasan.

Untuk mengurus output LLM dengan berkesan:

- **Konteks**: Berikan LLM konteks yang mencukupi—arkitektur, konvensi pasukan, data sebenar, dan kekangan produksi—bukan sekadar prompt tempatan.
- **Arah**: Tetapkan matlamat yang jelas. LLM berfungsi lebih baik dengan arahan khusus dan batasan yang ditentukan.
- **Sistem pengawasan**: Bina saluran pengesahan—semakan berasaskan risiko, ujian automatik, guardrails CI/CD, dan dokumentasi keputusan (ADR).
- **Model dan alat**: Pilih model dan alat yang sesuai dengan keperluan. Model yang lebih besar tidak semestinya lebih baik; alat yang bersepadu dengan konteks projek (seperti Cursor dengan codebase awareness) boleh lebih berkesan daripada chatbot generik.

Soalan utamanya bukan "bolehkah LLM menulis kod?", tetapi "adakah kita masih memahami, mengarahkan, dan bertanggungjawab atas kod yang dihasilkan oleh LLM dan alat AI?"

> **Nota:** Technical debt bukan musuh; technical debt yang tidak diurus adalah masalah. Kod yang tidak difahami adalah utang yang terkumpul. LLM dan alat AI adalah alat bantu, bukan pengganti penilaian kejuruteraan.

## Rujukan

- [IBM — Technical Debt](https://www.ibm.com/my-en/think/topics/technical-debt)
- [Martin Fowler — Technical Debt](https://martinfowler.com/bliki/TechnicalDebt.html)
- [OWASP — Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Google — Software Engineering at Google](https://abseil.io/resources/swe-book)