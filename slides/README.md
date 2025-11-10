# Slides Bootcamp Analisis Data

Folder ini berisi materi presentasi untuk Bootcamp Analisis Data - Python, DuckDB & Streamlit.

## 📋 Daftar Slide

### Hari 1: Fundamental Analisis Data
1. **00_overview.md** - Overview & Pengenalan Bootcamp
2. **01_session1_pandas.md** - Sesi 1: Python & Pandas untuk Analisis Data
3. **02_session2_duckdb.md** - Sesi 2: DuckDB untuk Query Analitik
4. **03_session3_visualization.md** - Sesi 3: Visualisasi Data

### Hari 2: Analisis Lanjutan & Dashboard
5. **04_session4_advanced.md** - Sesi 4: Teknik Analisis Data Lanjutan
6. **05_session5_streamlit.md** - Sesi 5: Dashboard Interaktif dengan Streamlit

## 🚀 Cara Menggunakan Slide

### Opsi 1: Marp (Direkomendasikan)

Slide ini dibuat dalam format Marp Markdown dan dapat dikonversi ke berbagai format.

#### Instalasi Marp CLI

```bash
# Instalasi dengan npm
npm install -g @marp-team/marp-cli

# Atau gunakan Docker
docker pull marp/marp-cli
```

#### Membuka Slide sebagai Presentasi HTML

```bash
# Konversi satu file ke HTML
marp 00_overview.md -o 00_overview.html

# Konversi semua slide sekaligus
marp *.md

# Preview dengan live reload
marp -p 00_overview.md
```

#### Export ke PDF

```bash
# Export ke PDF (memerlukan Chrome/Chromium)
marp 00_overview.md --pdf

# Export semua slide ke PDF
marp *.md --pdf
```

#### Export ke PowerPoint

```bash
# Export ke PPTX
marp 00_overview.md --pptx

# Export semua slide
marp *.md --pptx
```

### Opsi 2: VS Code Extension

1. Install ekstensi "Marp for VS Code" di Visual Studio Code
2. Buka file `.md` di VS Code
3. Klik ikon Marp di toolbar atau tekan `Ctrl+Shift+V` untuk preview
4. Gunakan tombol export untuk konversi ke HTML/PDF/PPTX

### Opsi 3: Reveal.js

Slide ini juga kompatibel dengan Reveal.js:

```bash
# Clone reveal.js
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start

# Copy file markdown ke folder reveal.js dan edit index.html
```

### Opsi 4: Markdown Viewer (Sederhana)

Untuk preview sederhana, buka file markdown dengan:
- GitHub/GitLab (otomatis render)
- VS Code (built-in markdown preview)
- Typora, Mark Text, atau Obsidian

## 🎨 Tema dan Styling

Slide menggunakan tema kustom dengan:
- Header biru (#1f77b4) untuk konsistensi dengan dashboard
- Code highlighting dengan syntax warna
- Layout responsif untuk berbagai ukuran layar
- Font yang mudah dibaca untuk presentasi

## 📊 Struktur Slide

Setiap file slide mengikuti struktur:
1. **Slide Judul** - Judul sesi dan informasi dasar
2. **Tujuan Pembelajaran** - Apa yang akan dipelajari
3. **Konten Utama** - Materi pembelajaran dengan contoh
4. **Praktikum** - Hands-on exercises
5. **Ringkasan** - Key takeaways
6. **Q&A** - Sesi tanya jawab

## 💡 Tips Presentasi

1. **Durasi**: Setiap slide dirancang untuk presentasi 1.5-2 jam
2. **Interaktif**: Gunakan live coding untuk demonstrasi
3. **Praktikum**: Alokasikan waktu untuk hands-on practice
4. **Break**: Jangan lupa istirahat setiap 1-1.5 jam
5. **Q&A**: Sediakan waktu untuk diskusi dan pertanyaan

## 🔧 Customization

Untuk mengubah tema atau styling:
1. Edit bagian frontmatter di awal setiap file
2. Tambahkan custom CSS di bagian `<style>`
3. Gunakan direktif Marp seperti `<!-- _class: lead -->` untuk layout khusus

## 📝 Lisensi

Materi presentasi ini dibuat untuk keperluan edukasi dan dapat digunakan secara bebas untuk pembelajaran.
