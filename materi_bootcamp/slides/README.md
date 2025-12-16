# 📊 Slides Presentasi Bootcamp

Folder ini berisi semua materi presentasi untuk Bootcamp Data Science dalam format Markdown (Marp).

## 📁 Struktur Folder

```
slides/
├── *.md                        # Source files (Marp Markdown)
├── pdf/                        # PDF exports
├── ppt/                        # PowerPoint exports
├── convert_slides.sh           # Conversion script
└── README.md                   # This file
```

## 📄 Daftar Slides

| File | Judul | Format |
|------|-------|--------|
| [00_bootcamp_overview.md](00_bootcamp_overview.md) | Bootcamp Overview & Agenda | [PDF](pdf/00_bootcamp_overview.pdf) \| [PPTX](ppt/00_bootcamp_overview.pptx) |
| [01_session1_pandas.md](01_session1_pandas.md) | Sesi 1: Pandas Fundamental | [PDF](pdf/01_session1_pandas.pdf) \| [PPTX](ppt/01_session1_pandas.pptx) |
| [02_session2_duckdb_visualization.md](02_session2_duckdb_visualization.md) | Sesi 2: DuckDB & Visualisasi | [PDF](pdf/02_session2_duckdb_visualization.pdf) \| [PPTX](ppt/02_session2_duckdb_visualization.pptx) |
| [03_session3_streamlit_basics.md](03_session3_streamlit_basics.md) | Sesi 3: Dasar Streamlit | [PDF](pdf/03_session3_streamlit_basics.pdf) \| [PPTX](ppt/03_session3_streamlit_basics.pptx) |
| [04_session4_streamlit_complete.md](04_session4_streamlit_complete.md) | Sesi 4: Dashboard Lengkap | [PDF](pdf/04_session4_streamlit_complete.pdf) \| [PPTX](ppt/04_session4_streamlit_complete.pptx) |

## 🎨 Tentang Marp

Slides ini dibuat menggunakan [Marp (Markdown Presentation Ecosystem)](https://marp.app/), yang memungkinkan pembuatan presentasi dari file Markdown.

### Fitur Marp:
- ✅ Syntax Markdown standar
- ✅ Code syntax highlighting
- ✅ Export ke PDF, PPTX, HTML
- ✅ Custom themes & styling
- ✅ Version control friendly (plain text)

## 🔄 Mengonversi Slides

### Opsi 1: Menggunakan Script (Recommended)

```bash
# Jalankan script konversi otomatis
./convert_slides.sh
```

Script ini akan:
- ✅ Membuat folder `pdf/` dan `ppt/` jika belum ada
- ✅ Mengonversi semua file `.md` ke PDF dan PPTX
- ✅ Menampilkan progress dan ringkasan

### Opsi 2: Manual dengan Marp CLI

```bash
# Install Marp CLI (jika belum)
npm install -g @marp-team/marp-cli

# Convert single file ke PDF
marp 01_session1_pandas.md --pdf -o pdf/01_session1_pandas.pdf

# Convert single file ke PPTX
marp 01_session1_pandas.md --pptx -o ppt/01_session1_pandas.pptx

# Convert semua files sekaligus
marp *.md --pdf --output pdf/
marp *.md --pptx --output ppt/
```

### Opsi 3: Menggunakan Marp VS Code Extension

1. Install [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
2. Buka file `.md`
3. Klik "Export Slide Deck" dari command palette (Ctrl/Cmd+Shift+P)
4. Pilih format: PDF atau PPTX

## ✏️ Mengedit Slides

### Edit dengan VS Code (Recommended)

```bash
# Install Marp extension terlebih dahulu
code 01_session1_pandas.md
```

Dengan Marp extension, Anda akan mendapat:
- ✅ Live preview
- ✅ Syntax highlighting
- ✅ Auto-completion

### Format Markdown Marp

```markdown
---
marp: true
theme: default
paginate: true
---

# Slide Title

Content here...

---

# Next Slide

More content...
```

**Slide separator:** `---` (3 dashes)

## 📊 Ukuran File

| Format | Total Size | Per File (avg) |
|--------|------------|----------------|
| **PDF** | ~1 MB | ~200 KB |
| **PPTX** | ~20 MB | ~4 MB |

## 🎯 Tips Presentasi

### Untuk Instruktur:

1. **Gunakan PPTX untuk presentasi interaktif**
   - Bisa diedit on-the-fly
   - Kompatibel dengan PowerPoint/Google Slides
   - Mendukung animasi

2. **Gunakan PDF untuk distribusi**
   - Ukuran file lebih kecil
   - Kompatibilitas universal
   - Tidak bisa diedit (proteksi konten)

3. **Gunakan Markdown untuk version control**
   - Track changes dengan Git
   - Mudah di-review
   - Collaborative editing

### Untuk Peserta:

- PDF tersedia di folder `pdf/` untuk dibaca offline
- PPTX tersedia jika ingin edit/annotate sendiri
- Source Markdown tersedia untuk referensi kode

## 🚀 Quick Start

```bash
# Clone repository
git clone <repo-url>
cd materi_bootcamp/slides

# View slides dengan Marp CLI
marp --preview 01_session1_pandas.md

# Generate semua exports
./convert_slides.sh
```

## 📝 Maintenance

### Update Slides:

1. Edit file `.md` yang ingin diubah
2. Jalankan conversion script:
   ```bash
   ./convert_slides.sh
   ```
3. Commit changes:
   ```bash
   git add .
   git commit -m "Update slides: [description]"
   ```

### Menambah Slide Baru:

1. Buat file `XX_new_session.md`
2. Gunakan template dari slide existing
3. Jalankan conversion script
4. Update README ini dengan link baru

## 🔗 Resources

- [Marp Official Website](https://marp.app/)
- [Marp CLI Documentation](https://github.com/marp-team/marp-cli)
- [Marp Markdown Syntax](https://marpit.marp.app/markdown)
- [Marp Themes](https://github.com/marp-team/marp-core/tree/main/themes)

---

**Last updated:** 2025-12-16
**Generated with:** Marp CLI
