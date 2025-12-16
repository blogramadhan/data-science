# 🎓 Bootcamp Data Science
## Python, DuckDB & Streamlit

**Bootcamp 2 Hari: Dari Data Analyst ke Dashboard Builder**

**Oleh: Kurnia Ramadhan, ST., M.Eng**
**Tahun: 2025**

---

## 🎯 Tentang Bootcamp

Bootcamp intensif ini dirancang untuk membekali peserta dengan keterampilan praktis dalam analisis data menggunakan Python, DuckDB sebagai database analitik, dan Streamlit untuk membuat dashboard interaktif. Peserta akan belajar langsung menggunakan **dataset RUP (Rencana Umum Pengadaan) 2025** sebagai studi kasus.

### 📊 Dataset: RUP 2025

**RUP Paket Penyedia Terumumkan 2025**

- 📦 **16,430** paket pengadaan
- 💰 Total pagu **~2 Triliun** rupiah
- 🏢 Ratusan satuan kerja
- 📅 Data sepanjang 2024-2025
- 📍 **Lokasi:** `datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet`

**Kasus penggunaan:** Analisis & monitoring pengadaan pemerintah

### 🎓 Hasil Pembelajaran

Setelah menyelesaikan bootcamp ini, peserta akan mampu:

✅ Menganalisis data dengan **Pandas**
✅ Menulis query SQL dengan **DuckDB**
✅ Membuat visualisasi dengan **Plotly**
✅ Membangun dashboard dengan **Streamlit**
✅ Melakukan deploy dashboard ke cloud

### 📈 Output Akhir

Di akhir bootcamp, peserta akan memiliki:

1. 📓 3 notebook Jupyter (Pandas, DuckDB, Visualisasi)
2. 📱 2 aplikasi Streamlit (Basic & Complete)
3. 🚀 1 dashboard ter-deploy (Streamlit Cloud)
4. 📚 Dokumentasi lengkap
5. 💼 Portofolio pribadi

### 🎓 Target Peserta

- Data Analyst yang ingin meningkatkan kemampuan
- Business Analyst yang ingin lebih technical
- Programmer yang ingin masuk ke bidang Data Analytics
- Fresh Graduate yang ingin berkarir di bidang data
- Profesional yang perlu mengolah dan visualisasi data

### ✅ Prasyarat

**Basic Python:**
- Variabel, fungsi, loops
- List, dictionary
- Dasar pandas (lebih baik jika sudah pernah)

**Tools:**
- Python 3.9+
- Text editor / VS Code
- Browser
- Laptop dengan minimal 8GB RAM

**Mindset:**
- Siap belajar
- Tidak takut error!

### 🛠️ Teknologi

| Tool | Kegunaan | Sesi |
|------|---------|------|
| **Pandas** | Manipulasi data | Hari 1 - S1 |
| **DuckDB** | Analitik SQL | Hari 1 - S2 |
| **Plotly** | Visualisasi interaktif | Hari 1 - S2 |
| **Streamlit** | Dashboard web | Hari 2 - S3, S4 |

---

## 🗓️ Agenda Bootcamp

### Hari 1: Dasar Data Science

| Waktu | Sesi | Topik |
|-------|------|-------|
| 08:00 - 10:00 | **Sesi 1** | Pandas Fundamental (120 menit) |
| 10:00 - 10:15 | **BREAK** | Coffee break |
| 10:15 - 12:00 | **Sesi 2** | DuckDB Fundamental (105 menit) |
| 12:00 - 13:00 | **BREAK / ISHOMA** | Istirahat & makan siang |
| 13:00 - 15:00 | **Sesi 2 (lanjutan)** | Visualisasi Fundamental (120 menit) |
| 15:00 - 15:45 | **Review** | Review & Pratinjau Hari 2 |

### Hari 2: Dashboard Streamlit

| Waktu | Sesi | Topik |
|-------|------|-------|
| 08:00 - 10:00 | **Sesi 3** | Dasar Streamlit (120 menit) |
| 10:00 - 10:15 | **BREAK** | Coffee break |
| 10:15 - 11:30 | **Sesi 4** | Dashboard Lengkap - Bagian 1 (75 menit) |
| 11:30 - 13:00 | **BREAK / ISHOMA** | Istirahat & makan siang |
| 13:00 - 14:45 | **Sesi 4 (lanjutan)** | Dashboard Lengkap - Bagian 2 & Deploy (105 menit) |
| 14:45 - 15:45 | **Penutupan** | Review, Tanya Jawab & Penutupan |

---

## 📑 Slides

Seluruh materi presentasi tersedia di folder [materi_bootcamp/slides/](materi_bootcamp/slides/). Gunakan [Marp](https://marp.app/) atau Markdown viewer favorit Anda untuk membukanya.

| File | Fokus Materi | Referensi Praktik |
| ---- | ------------ | ----------------- |
| [00_bootcamp_overview.md](materi_bootcamp/slides/00_bootcamp_overview.md) | Agenda bootcamp, struktur hari 1 & 2 | Ikuti sebagai panduan umum sesi |
| [01_session1_pandas.md](materi_bootcamp/slides/01_session1_pandas.md) | Sesi 1 – Pandas Fundamental | Notebook [01_pandas_fundamental.ipynb](materi_bootcamp/day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb) |
| [02_session2_duckdb_visualization.md](materi_bootcamp/slides/02_session2_duckdb_visualization.md) | Sesi 2 – DuckDB & Visualisasi | Notebook [02_duckdb_fundamental.ipynb](materi_bootcamp/day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb) & [03_visualization_fundamental.ipynb](materi_bootcamp/day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb) |
| [03_session3_streamlit_basics.md](materi_bootcamp/slides/03_session3_streamlit_basics.md) | Sesi 3 – Dasar Streamlit | Aplikasi [app_part1.py](materi_bootcamp/day2/session3_streamlit_basics/app_part1.py) |
| [04_session4_streamlit_complete.md](materi_bootcamp/slides/04_session4_streamlit_complete.md) | Sesi 4 – Dashboard Lengkap | Aplikasi [app_complete.py](materi_bootcamp/day2/session4_streamlit_complete/app_complete.py) |

---

## 🚀 Memulai

### 1. Persiapan Lingkungan

```bash
# Clone repository
git clone <repository-url>
cd data-science

# Instalasi dependensi dengan uv (recommended)
uv sync

# Atau dengan pip
pip install pandas duckdb plotly streamlit jupyter
```

### 2. Verifikasi Instalasi

```bash
# Verifikasi semua library terinstall
python -c "import pandas, duckdb, plotly, streamlit; print('✅ Semua library berhasil terinstall!')"
```

### 3. Jalankan Jupyter Notebook (Hari 1)

```bash
# Dengan uv
uv run jupyter notebook

# Atau langsung
jupyter notebook

# Buka notebook di folder materi_bootcamp/day1/
```

**Notebook yang tersedia:**
- [01_pandas_fundamental.ipynb](materi_bootcamp/day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb) - Sesi 1
- [02_duckdb_fundamental.ipynb](materi_bootcamp/day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb) - Sesi 2
- [03_visualization_fundamental.ipynb](materi_bootcamp/day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb) - Sesi 2

### 4. Jalankan Aplikasi Streamlit (Hari 2)

```bash
# Sesi 3: Dasar Streamlit
uv run streamlit run materi_bootcamp/day2/session3_streamlit_basics/app_part1.py
# Atau
streamlit run materi_bootcamp/day2/session3_streamlit_basics/app_part1.py

# Sesi 4: Dashboard Lengkap
uv run streamlit run materi_bootcamp/day2/session4_streamlit_complete/app_complete.py
# Atau
streamlit run materi_bootcamp/day2/session4_streamlit_complete/app_complete.py
```

---

## 📁 Struktur Proyek

```
data-science/
├── materi_bootcamp/
│   ├── slides/                              # 📑 Slides presentasi (Marp format)
│   │   ├── 00_bootcamp_overview.md          # Overview & agenda bootcamp
│   │   ├── 01_session1_pandas.md            # Sesi 1: Pandas Fundamental
│   │   ├── 02_session2_duckdb_visualization.md  # Sesi 2: DuckDB & Visualisasi
│   │   ├── 03_session3_streamlit_basics.md  # Sesi 3: Dasar Streamlit
│   │   └── 04_session4_streamlit_complete.md    # Sesi 4: Dashboard Lengkap
│   │
│   ├── day1/                                # 📊 Hari 1: Dasar Data Science
│   │   ├── session1_pandas_basics/
│   │   │   └── notebooks/
│   │   │       └── 01_pandas_fundamental.ipynb  ✅
│   │   ├── session2_duckdb_basics/
│   │   │   └── notebooks/
│   │   │       └── 02_duckdb_fundamental.ipynb  ✅
│   │   └── session3_visualization_basics/
│   │       └── notebooks/
│   │           └── 03_visualization_fundamental.ipynb  ✅
│   │
│   └── day2/                                # 📱 Hari 2: Dashboard Streamlit
│       ├── session3_streamlit_basics/
│       │   └── app_part1.py  ✅
│       └── session4_streamlit_complete/
│           └── app_complete.py  ✅
│
├── datasets/
│   └── rup/
│       └── RUP-PaketPenyedia-Terumumkan-2025.parquet  ✅
│
├── pyproject.toml  ✅
└── README.md
```

---

## 📚 Ringkasan Materi Per Sesi

### 📊 HARI 1: Dasar Data Science

#### Sesi 1: Pandas Fundamental (08:00 - 10:00)

**Durasi:** 120 menit
**Notebook:** [01_pandas_fundamental.ipynb](materi_bootcamp/day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb)
**Slides:** [01_session1_pandas.md](materi_bootcamp/slides/01_session1_pandas.md)

**Objektif:**
- ✅ Memuat & mengeksplorasi data dengan Pandas
- ✅ Menyeleksi kolom & baris
- ✅ Memfilter data dengan boolean indexing
- ✅ Melakukan agregasi dengan `groupby`
- ✅ Menangani missing values
- ✅ Membuat statistik ringkasan

**Materi:**
1. **Memuat Data** - Parquet, CSV, Excel
2. **Eksplorasi Data** - `head()`, `info()`, `describe()`
3. **Seleksi Data** - `.loc[]`, `.iloc[]`
4. **Filter Data** - Boolean indexing, query kompleks
5. **Agregasi Data** - `groupby()`, agregasi functions
6. **Missing Values** - `isnull()`, `dropna()`, `fillna()`

**Praktik:**
- Analisis data RUP 2025
- Eksplorasi pagu pengadaan per satker
- Analisis metode pengadaan

---

#### Sesi 2: DuckDB & Visualisasi (10:15 - 15:00)

**Durasi:** 105 menit (DuckDB) + 120 menit (Visualisasi)
**Notebook:**
- [02_duckdb_fundamental.ipynb](materi_bootcamp/day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb)
- [03_visualization_fundamental.ipynb](materi_bootcamp/day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb)

**Slides:** [02_session2_duckdb_visualization.md](materi_bootcamp/slides/02_session2_duckdb_visualization.md)

##### Bagian A: DuckDB Fundamental

**Objektif:**
- ✅ Setup DuckDB & koneksi
- ✅ Query dasar SQL
- ✅ Agregasi & window functions
- ✅ Integrasi DuckDB + Pandas

**Materi:**
1. **Setup DuckDB** - In-memory database, register DataFrame
2. **Query Dasar** - SELECT, WHERE, ORDER BY, LIMIT
3. **Agregasi** - COUNT, SUM, AVG, GROUP BY
4. **Window Functions** - ROW_NUMBER, RANK, LAG, LEAD
5. **Integrasi Pandas** - Convert hasil query ke DataFrame
6. **Best Practices** - Kapan pakai DuckDB vs Pandas

**Praktik:**
- Query top satker berdasarkan pagu
- Analisis pivot metode pengadaan
- Running totals dengan window functions

##### Bagian B: Visualisasi Fundamental

**Objektif:**
- ✅ Membuat visualisasi dengan Plotly
- ✅ Chart interaktif (bar, line, pie, scatter)
- ✅ Customization & styling
- ✅ Export hasil visualisasi

**Materi:**
1. **Plotly Express** - Quick plotting
2. **Chart Types** - Bar, line, pie, scatter, histogram
3. **Interaktivity** - Hover, zoom, filter
4. **Customization** - Colors, labels, layout
5. **Export** - Save to HTML/PNG

**Praktik:**
- Visualisasi distribusi pagu
- Chart metode pengadaan
- Time series analisis
- Multi-chart dashboard mini

---

### 📱 HARI 2: Dashboard Streamlit

#### Sesi 3: Dasar Streamlit (08:00 - 10:00)

**Durasi:** 120 menit
**Aplikasi:** [app_part1.py](materi_bootcamp/day2/session3_streamlit_basics/app_part1.py)
**Slides:** [03_session3_streamlit_basics.md](materi_bootcamp/slides/03_session3_streamlit_basics.md)

**Objektif:**
- ✅ Setup aplikasi Streamlit
- ✅ Membuat layout dengan columns & containers
- ✅ Memakai widgets interaktif
- ✅ Menampilkan metrics & KPI
- ✅ Menampilkan data table
- ✅ Mengelola input pengguna

**Materi:**
1. **Setup & Hello World** - `st.write()`, `st.title()`
2. **Text Elements** - Headers, markdown, code
3. **Data Display** - `st.dataframe()`, `st.table()`, `st.metric()`
4. **Layout** - `st.columns()`, `st.container()`, `st.tabs()`
5. **Input Widgets** - Buttons, sliders, selectbox, multiselect
6. **Charts** - `st.line_chart()`, `st.bar_chart()`

**Praktik:**
- Aplikasi hello world
- Layout responsif
- Dashboard sederhana dengan metrics
- Interactive filters

---

#### Sesi 4: Dashboard Lengkap (10:15 - 14:45)

**Durasi:** 75 menit + 105 menit
**Aplikasi:** [app_complete.py](materi_bootcamp/day2/session4_streamlit_complete/app_complete.py)
**Slides:** [04_session4_streamlit_complete.md](materi_bootcamp/slides/04_session4_streamlit_complete.md)

**Objektif:**
- ✅ Membangun dashboard production-ready
- ✅ Integrasi Pandas + DuckDB + Plotly
- ✅ Advanced filtering & interactivity
- ✅ Caching untuk performa
- ✅ Deploy ke Streamlit Cloud

**Materi:**
1. **Dashboard Architecture** - Page config, sidebar, main area
2. **Data Loading** - `@st.cache_data` untuk optimasi
3. **Advanced Filters** - Multi-select, date range, numeric range
4. **Interactive Charts** - Plotly integration, linked charts
5. **KPI Metrics** - Cards, delta indicators
6. **Export Features** - Download CSV, Excel
7. **Deployment** - Streamlit Cloud setup & deploy

**Praktik:**
- Dashboard RUP lengkap
- Multi-page filtering
- Real-time data exploration
- Export & sharing
- Deploy to cloud

---

## 🐛 Pemecahan Masalah

### Masalah Instalasi

**Masalah:** `pip install` gagal
```bash
# Solusi: Upgrade pip
python -m pip install --upgrade pip setuptools wheel
```

**Masalah:** Error import DuckDB
```bash
# Solusi: Install ulang DuckDB
pip uninstall duckdb
pip install duckdb --no-cache-dir
```

**Masalah:** Jupyter tidak bisa dijalankan
```bash
# Solusi: Install ulang Jupyter
pip install --upgrade jupyter notebook
```

### Masalah Streamlit

**Masalah:** Streamlit tidak bisa dijalankan
```bash
# Cek ketersediaan port
streamlit run app.py --server.port 8502
```

**Masalah:** Module tidak ditemukan di Streamlit
```bash
# Jalankan dengan interpreter Python yang benar
python -m streamlit run app.py
```

**Masalah:** Batas ukuran upload file
```toml
# Buat file .streamlit/config.toml
[server]
maxUploadSize = 1000  # MB
```

### Masalah Memuat Data

**Masalah:** File Parquet tidak bisa dibaca
```bash
# Install pyarrow
pip install pyarrow
```

**Masalah:** Error memori dengan dataset besar
```python
# Gunakan DuckDB untuk query file besar
import duckdb
df = duckdb.query("SELECT * FROM 'large_file.parquet' LIMIT 10000").df()
```

---

## 💡 Tips & Praktik Terbaik

### Untuk Belajar Efektif
1. **Latihan, latihan, latihan** - Kerjakan semua lab
2. **Eksperimen dengan dataset lain** - Jangan hanya RUP
3. **Bangun proyek sendiri** - Terapkan ke kasus penggunaan pribadi
4. **Bergabung dengan komunitas** - Stack Overflow, Reddit, Discord
5. **Baca dokumentasi** - Dokumentasi adalah teman terbaik
6. **Kontrol versi** - Gunakan Git untuk melacak progres

### Untuk Development
1. **Gunakan virtual environment** - Isolasi dependensi
2. **Tulis kode yang bersih** - Ikuti panduan gaya PEP 8
3. **Beri komentar pada kode** - Jelaskan "mengapa", bukan "apa"
4. **Uji secara bertahap** - Jangan menulis terlalu banyak sebelum diuji
5. **Cache operasi mahal** - Gunakan `@st.cache_data` di Streamlit
6. **Tangani error dengan baik** - Selalu gunakan blok try-except

### Untuk Dashboard Produksi
1. **Optimalkan performa** - Cache data, gunakan query efisien
2. **Desain untuk pengguna** - Pikirkan pengalaman pengguna
3. **Responsif mobile** - Uji di berbagai ukuran layar
4. **Penanganan error** - Tampilkan pesan error yang ramah
5. **Tambahkan loading states** - Gunakan spinner dan progress bar
6. **Dokumentasi** - README untuk instruksi setup

---

## 📚 Sumber Belajar & Materi

### Dokumentasi Resmi
- **Pandas:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- **DuckDB:** [https://duckdb.org/docs/](https://duckdb.org/docs/)
- **Streamlit:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Plotly:** [https://plotly.com/python/](https://plotly.com/python/)

### Lembar Contekan
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Referensi SQL DuckDB](https://duckdb.org/docs/sql/introduction)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Galeri Grafik Python](https://python-graph-gallery.com/)

### Platform Pembelajaran Online
- **Kaggle Learn** - Kursus interaktif gratis
- **DataCamp** - Kursus data science praktis
- **Real Python** - Tutorial dan artikel Python
- **Towards Data Science** - Publikasi Medium untuk data science

### Dataset untuk Latihan
- **Kaggle Datasets** - Ribuan dataset untuk latihan
- **UCI Machine Learning Repository** - Dataset klasik
- **Data.gov** - Data terbuka pemerintah
- **Google Dataset Search** - Mesin pencari untuk dataset

---

## 🚀 Langkah Selanjutnya

### Setelah Bootcamp
1. **Bangun portofolio proyek** - Tunjukkan kemampuan Anda
2. **Deploy dashboard Anda** - Gunakan Streamlit Cloud (gratis)
3. **Berkontribusi ke open source** - Belajar dari yang lain
4. **Jelajahi topik lanjutan:**
   - Machine Learning dengan scikit-learn
   - Deep Learning dengan TensorFlow/PyTorch
   - Big Data dengan Apache Spark
   - Platform Cloud (AWS, GCP, Azure)

### Pilihan Jalur Karir
- **Data Analyst** - Business insights dan pelaporan
- **Business Intelligence** - Dashboard dan visualisasi
- **Data Engineer** - Pipeline data dan infrastruktur
- **Data Scientist** - Machine learning dan model prediktif
- **Analytics Engineer** - dbt, SQL, pemodelan data

### Lanjutkan Belajar
- Bergabung dengan komunitas data science (Kaggle, Reddit, Discord)
- Ikuti blog dan newsletter data science
- Hadiri meetup dan konferensi
- Bangun proyek pribadi dan portofolio
- Jalin relasi dengan profesional di industri

---

## 📞 Dukungan & Kontak

**Untuk pertanyaan atau dukungan:**
- Email: kurnia@ramadhan.me

**Umpan Balik:**
Kami sangat menghargai umpan balik Anda untuk meningkatkan materi bootcamp ini. Silakan kirim umpan balik melalui email.

---

## 📄 Lisensi

Materi bootcamp ini dibuat untuk keperluan edukasi dan dapat digunakan secara bebas untuk pembelajaran.

---

## 🙏 Penghargaan

Terima kasih kepada:
- Komunitas open source Python, Pandas, DuckDB, dan Streamlit
- Semua kontributor dan pengelola pustaka yang digunakan
- Peserta bootcamp yang memberikan umpan balik

---

**Selamat Belajar! Selamat Coding! 🎉**

*Terakhir diperbarui: 2025*
