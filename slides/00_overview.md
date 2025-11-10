---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Bootcamp Analisis Data - Python, DuckDB & Streamlit'
footer: '© 2024 | Data Science Bootcamp'
---

<style>
section {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
  color: #1f77b4;
  border-bottom: 3px solid #1f77b4;
  padding-bottom: 10px;
}
h2 {
  color: #2c5aa0;
}
code {
  background-color: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
}
pre {
  background-color: #2d2d2d;
  color: #f8f8f2;
  padding: 15px;
  border-radius: 5px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
ul {
  line-height: 1.8;
}
</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# 📊 Bootcamp Analisis Data
## Python, DuckDB & Streamlit

### Pembelajaran Praktis dengan Dataset Real

**Durasi:** 2 Hari (16 Jam Total)

---

# 👋 Selamat Datang!

## Tentang Bootcamp

Bootcamp intensif ini dirancang untuk membekali Anda dengan keterampilan praktis dalam:

- 🐍 **Python & Pandas** untuk manipulasi dan analisis data
- 🦆 **DuckDB** untuk query analitik yang powerful
- 📈 **Visualisasi Data** dengan Matplotlib, Seaborn, dan Plotly
- 🚀 **Streamlit** untuk membuat dashboard interaktif

**Pembelajaran berbasis praktik** menggunakan dataset real: **RUP 2025**

---

# 📊 Dataset: RUP 2025

## Rencana Umum Pengadaan Barang/Jasa Pemerintah

<div class="columns">

<div>

### Karakteristik Dataset
- **Records:** 16,430 paket
- **Size:** ~1.3 MB (Parquet)
- **Tahun:** 2025
- **Source:** Data Pengadaan Pemerintah

</div>

<div>

### Kolom Utama
- Nama paket & kode RUP
- Pagu anggaran
- Metode pengadaan
- Satuan kerja
- Timeline pengadaan
- Lokasi dan kategori

</div>

</div>

**Real-world data = Real-world skills!** 🎯

---

# 🎯 Tujuan Pembelajaran

Setelah bootcamp ini, Anda akan mampu:

### 1. Analisis Data dengan Python & Pandas
- ✅ Exploratory Data Analysis (EDA) komprehensif
- ✅ Data cleaning dan transformasi
- ✅ Manipulasi data tingkat lanjut

### 2. Query Analitik dengan DuckDB
- ✅ SQL query kompleks (CTEs, Window Functions)
- ✅ Integrasi dengan Pandas
- ✅ Performance optimization

---

# 🎯 Tujuan Pembelajaran (lanjutan)

### 3. Visualisasi Data yang Efektif
- ✅ Static charts (Matplotlib/Seaborn)
- ✅ Interactive charts (Plotly)
- ✅ Data storytelling principles

### 4. Dashboard Interaktif dengan Streamlit
- ✅ Aplikasi web tanpa web development
- ✅ Filter interaktif & data exploration
- ✅ Production-ready dashboard

### 5. Teknik Analisis Lanjutan
- ✅ Time series analysis
- ✅ Statistical testing
- ✅ A/B testing fundamentals

---

# 👥 Target Peserta

Bootcamp ini cocok untuk:

- 📊 **Data Analyst** yang ingin upgrade skills
- 💼 **Business Analyst** yang ingin lebih technical
- 💻 **Programmer** yang ingin masuk ke Data Analytics
- 🎓 **Fresh Graduate** yang ingin berkarir di bidang data
- 👔 **Profesional** yang perlu mengolah & visualisasi data

---

# ✅ Prerequisites

## Yang Perlu Anda Siapkan:

### Pengetahuan
- ✅ Pemahaman dasar programming (Python preferred)
- ✅ Familiar dengan konsep database & SQL dasar
- ✅ Mindset analitis dan problem-solving

### Hardware & Software
- ✅ Laptop dengan minimal **8GB RAM**
- ✅ **Python 3.8+** terinstall
- ✅ Text editor (VS Code recommended)
- ✅ Git untuk version control

---

# 🛠️ Tools & Libraries

<div class="columns">

<div>

### Core Tools
- **Python 3.9+**
- **Jupyter Notebook**
- **uv** (package manager)
- **Git**

### Data Processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **DuckDB** - Analytical queries

</div>

<div>

### Visualization
- **Plotly** - Interactive charts
- **Matplotlib** - Static plots
- **Seaborn** - Statistical viz

### Dashboard
- **Streamlit** - Web apps
- **Altair** - Declarative viz

</div>

</div>

---

# 📈 Hasil Akhir yang Diharapkan

## Portfolio Anda akan berisi:

- ✅ **7 Jupyter Notebooks** dengan analisis lengkap
  - EDA, DuckDB, Visualization, Data Cleaning, Time Series, Statistical Analysis

- ✅ **4 Aplikasi Streamlit** interaktif
  - Hello Streamlit, Components Demo, Data Explorer, RUP Dashboard

- ✅ **1 Production-Ready Dashboard**
  - Analisis komprehensif RUP 2025

- ✅ **Pemahaman mendalam** workflow analisis data end-to-end

---

# 📅 Agenda Bootcamp

## Hari 1: Fundamental Analisis Data (8 Jam)

| Waktu | Sesi | Topik |
|-------|------|-------|
| 09:00 - 12:00 | **Sesi 1** | Python & Pandas untuk Analisis Data |
| 12:00 - 13:00 | **BREAK** | Istirahat & Makan Siang |
| 13:00 - 15:30 | **Sesi 2** | DuckDB untuk Query Analitik |
| 15:30 - 15:45 | **BREAK** | Coffee Break |
| 15:45 - 17:30 | **Sesi 3** | Visualisasi Data |

---

# 📅 Agenda Bootcamp

## Hari 2: Analisis Lanjutan & Dashboard (8 Jam)

| Waktu | Sesi | Topik |
|-------|------|-------|
| 09:00 - 12:00 | **Sesi 4** | Teknik Analisis Data Lanjutan |
| 12:00 - 13:00 | **BREAK** | Istirahat & Makan Siang |
| 13:00 - 17:30 | **Sesi 5** | Dashboard Interaktif dengan Streamlit |

*(Termasuk coffee break 15 menit)*

---

# 🗂️ Struktur Project

```
data-science/
├── day1/
│   ├── session1_python_pandas/
│   │   └── notebooks/01_exploratory_data_analysis_rup.ipynb
│   ├── session2_duckdb/
│   │   └── notebooks/01_duckdb_intro.ipynb
│   └── session3_visualization/
│       └── notebooks/
│           ├── 01_matplotlib_seaborn.ipynb
│           └── 02_plotly_interactive.ipynb
├── day2/
│   ├── session4_advanced_analysis/
│   │   └── notebooks/ (3 notebooks)
│   └── session5_streamlit/
│       └── apps/ (4 aplikasi)
└── datasets/rup/
```

---

# 🚀 Setup Environment

## Quick Start

```bash
# 1. Clone repository
git clone <repository-url>
cd data-science

# 2. Install dependencies dengan uv
uv sync

# 3. Jalankan Jupyter Notebook
uv run jupyter notebook

# 4. Jalankan Streamlit App (nanti di hari 2)
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

---

# 🚀 Setup Environment (Alternative)

## Menggunakan pip

```bash
# 1. Buat virtual environment
python -m venv .venv

# 2. Aktivasi virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3. Install dependencies
pip install pandas numpy duckdb streamlit plotly \
            matplotlib seaborn jupyter openpyxl pyarrow

# 4. Jalankan Jupyter
jupyter notebook
```

---

# 📚 Metode Pembelajaran

## Hands-On Learning

Bootcamp ini menggunakan pendekatan **learning by doing**:

1. 🎓 **Teori Singkat** (20%)
   - Konsep fundamental
   - Best practices

2. 💻 **Live Coding** (30%)
   - Demonstrasi instruktur
   - Follow along

3. 🔨 **Praktikum** (50%)
   - Hands-on exercises
   - Real-world problems
   - Build your own solutions

---

# 💡 Tips untuk Sukses

## Maximize Your Learning

- ✅ **Ikuti semua hands-on exercises**
  - Jangan hanya menonton, code bersama!

- ✅ **Bertanya jika ada yang tidak jelas**
  - No question is a stupid question

- ✅ **Eksperimen dengan kode**
  - Coba variasi, break things, learn from errors

- ✅ **Catat key insights**
  - Documentation for future reference

- ✅ **Kolaborasi dengan peserta lain**
  - Learn from peers, share knowledge

---

# 📖 Sumber Belajar

## Dokumentasi Resmi

- **Pandas:** https://pandas.pydata.org/docs/
- **DuckDB:** https://duckdb.org/docs/
- **Streamlit:** https://docs.streamlit.io/
- **Plotly:** https://plotly.com/python/

## Cheat Sheets

- Pandas Cheat Sheet
- DuckDB SQL Reference
- Streamlit Cheat Sheet
- Python Graph Gallery

---

# 🎯 Learning Outcomes - Detail

<div class="columns">

<div>

## HARI 1

### Sesi 1: Pandas
- Data loading & inspection
- Filtering & selection
- GroupBy & aggregation
- Missing values handling
- Statistical summary

### Sesi 2: DuckDB
- SQL fundamentals
- Window functions
- CTEs & subqueries
- Pandas integration

</div>

<div>

## HARI 2

### Sesi 3: Visualization
- Matplotlib basics
- Seaborn statistical plots
- Plotly interactivity
- Chart selection guide

### Sesi 4: Advanced
- Data cleaning techniques
- Time series analysis
- Statistical testing

### Sesi 5: Streamlit
- Interactive components
- Dashboard building
- Production deployment

</div>

</div>

---

# 🏆 Apa yang Membuat Bootcamp Ini Berbeda?

## Unique Value Propositions

1. **Dataset Real-World** 🌍
   - Bukan toy dataset, tapi data pengadaan pemerintah asli

2. **End-to-End Workflow** 🔄
   - Dari raw data → insights → dashboard produksi

3. **Modern Tech Stack** ⚡
   - DuckDB untuk performa, Streamlit untuk simplicity

4. **Production-Ready Skills** 🚀
   - Bukan hanya tutorial, tapi skills untuk kerja

5. **Portfolio Building** 📁
   - 7 notebooks + 4 apps = portfolio yang impressive

---

# 🎬 Next Steps

## Persiapan Sebelum Mulai

### ✅ Checklist Pre-Bootcamp

- [ ] Install Python 3.8+
- [ ] Install VS Code atau editor favorit
- [ ] Install Git
- [ ] Clone repository
- [ ] Setup virtual environment
- [ ] Install dependencies (`uv sync` atau `pip install`)
- [ ] Test dengan `jupyter notebook`
- [ ] Download/verify dataset RUP 2025

**Siap? Mari kita mulai! 🚀**

---

# ❓ FAQ - Frequently Asked Questions

**Q: Apakah saya harus sudah mahir Python?**
A: Tidak perlu mahir, tapi sebaiknya sudah familiar dengan basic syntax

**Q: Apakah perlu background statistik?**
A: Tidak wajib, konsep statistik akan dijelaskan dari dasar

**Q: Apakah bisa menggunakan dataset sendiri?**
A: Ya! Setelah paham workflow dengan RUP, bisa pakai dataset lain

**Q: Bagaimana jika tertinggal?**
A: Semua materi ada di notebook, bisa di-review nanti

**Q: Apakah ada sertifikat?**
A: Yang penting adalah skills dan portfolio yang dihasilkan!

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 🎉 Ready to Start?

## Mari Mulai Perjalanan Data Analytics Anda!

### Hari 1 - Sesi 1
### Python & Pandas untuk Analisis Data

**Let's dive in!** 💪

---

# 📞 Support & Resources

## Bantuan Selama Bootcamp

- 💬 **Tanya Instruktur** - Jangan ragu bertanya
- 👥 **Diskusi Grup** - Kolaborasi dengan peserta lain
- 📚 **Dokumentasi** - Referensi selalu tersedia
- 💻 **Repository** - Semua kode ada di Git

## Setelah Bootcamp

- 📧 Email support
- 🐛 GitHub Issues untuk bug/pertanyaan
- 💬 Komunitas Discord/Slack (jika ada)
- 📖 Akses ke materi selamanya

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Thank You! 🙏

**Good Luck & Happy Learning!**

*Questions before we start?*
