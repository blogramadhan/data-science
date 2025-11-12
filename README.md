# Bootcamp Analisis Data - Python, DuckDB & Streamlit

**Durasi:** 2 Hari (16 Jam Total)

## 🎯 Tentang Bootcamp

Bootcamp intensif ini dirancang untuk membekali peserta dengan keterampilan praktis dalam analisis data menggunakan Python, DuckDB sebagai database analitik, dan Streamlit untuk membuat dashboard interaktif. Peserta akan belajar langsung menggunakan **dataset RUP (Rencana Umum Pengadaan) 2025** sebagai studi kasus.

### 🎓 Tujuan Pembelajaran

Setelah menyelesaikan bootcamp ini, peserta akan mampu:

1. **Menguasai Analisis Data dengan Python & Pandas**
   - Melakukan Exploratory Data Analysis (EDA) secara komprehensif
   - Membersihkan dan mentransformasi data mentah menjadi insights
   - Menggunakan Pandas untuk manipulasi data tingkat lanjut

2. **Menggunakan DuckDB untuk Query Analitik**
   - Memahami kelebihan DuckDB untuk analisis data
   - Menulis query SQL kompleks dengan window functions dan CTEs
   - Mengintegrasikan DuckDB dengan workflow Pandas

3. **Membuat Visualisasi Data yang Efektif**
   - Menggunakan Matplotlib & Seaborn untuk visualisasi statistik
   - Membuat grafik interaktif dengan Plotly
   - Menerapkan prinsip data storytelling

4. **Membangun Dashboard Interaktif dengan Streamlit**
   - Membuat aplikasi web analitik tanpa perlu web development expertise
   - Implementasi filter interaktif dan real-time data exploration
   - Deploy dashboard yang siap produksi

5. **Menerapkan Teknik Analisis Lanjutan**
   - Time series analysis dan trend forecasting
   - Statistical hypothesis testing
   - A/B testing fundamentals

### 📈 Hasil Akhir yang Diharapkan

Peserta akan membuat portfolio yang berisi:
- ✅ 7 Jupyter Notebooks dengan analisis lengkap
- ✅ 4 Aplikasi Streamlit interaktif
- ✅ 1 Production-ready Dashboard untuk analisis RUP 2025
- ✅ Pemahaman mendalam tentang workflow analisis data end-to-end

### 📊 Dataset: RUP 2025
- **Topik**: Rencana Umum Pengadaan Barang/Jasa Pemerintah 2025
- **Jumlah Records**: 16,430 paket pengadaan
- **Ukuran File**: ~1.3 MB (format Parquet)
- **Lokasi**: `datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet`

### 🎓 Target Peserta

- Data Analyst yang ingin meningkatkan kemampuan
- Business Analyst yang ingin lebih technical
- Programmer yang ingin masuk ke bidang Data Analytics
- Fresh Graduate yang ingin berkarir di bidang data
- Profesional yang perlu mengolah dan visualisasi data

### ✅ Prerequisites

- Pemahaman dasar programming (Python preferred)
- Familiar dengan konsep database (SQL dasar)
- Laptop dengan minimal 8GB RAM
- Python 3.8+ terinstall

### 🛠️ Tools & Libraries

- Python 3.9+
- Pandas untuk manipulasi data
- NumPy untuk operasi numerik
- DuckDB untuk query analitik
- Streamlit untuk dashboard interaktif
- Plotly untuk visualisasi interaktif
- Matplotlib & Seaborn untuk visualisasi static
- Jupyter Notebook untuk eksplorasi

### 🗓️ Agenda Bootcamp (Ringkas)

#### Hari 1: Fundamental Analisis Data

| Waktu | Sesi | Topik |
|-------|------|-------|
| 08:00 - 12:00 | **Sesi 1** | Python & Pandas untuk Analisis Data |
| 12:00 - 13:00 | **BREAK / ISHOMA** | Istirahat & makan siang |
| 13:00 - 15:00 | **Sesi 2** | DuckDB untuk Query Analitik |
| 15:00 - 15:30 | **BREAK** | Coffee break |
| 15:30 - 17:00 | **Sesi 3** | Visualisasi Data |

#### Hari 2: Analisis Lanjutan & Dashboard

| Waktu | Sesi | Topik |
|-------|------|-------|
| 08:00 - 12:00 | **Sesi 4** | Teknik Analisis Data Lanjutan |
| 12:00 - 13:00 | **BREAK / ISHOMA** | Istirahat & makan siang |
| 13:00 - 15:00 | **Sesi 5** | Dashboard Interaktif dengan Streamlit |
| 15:00 - 15:30 | **BREAK** | Coffee break |
| 15:30 - 17:00 | **Sesi 5 (lanjutan)** | Deployment & Presentasi Dashboard |

---

## 📑 Slides

Seluruh materi presentasi tersedia di folder `slides/`. Gunakan [Marp](https://marp.app/) atau Markdown viewer favorit Anda untuk membukanya.

| File | Fokus Materi | Referensi Praktik |
| ---- | ------------ | ----------------- |
| `slides/00_overview.md` | Agenda bootcamp, struktur hari 1 & 2 | Ikuti sebagai panduan umum sesi |
| `slides/01_session1_pandas.md` | Sesi 1 – Pandas & EDA | Notebook `day1/session1_python_pandas` |
| `slides/02_session2_duckdb.md` | Sesi 2 – DuckDB & SQL analitik | Notebook `day1/session2_duckdb` |
| `slides/03_session3_visualization.md` | Sesi 3 – Visualisasi (Matplotlib/Seaborn/Plotly) | Notebook `day1/session3_visualization` |
| `slides/04_session4_advanced.md` | Sesi 4 – Analisis lanjutan (cleaning, time series, statistik) | Notebook `day2/session4_advanced_analysis` |
| `slides/05_session5_streamlit.md` | Sesi 5 – Dashboard Streamlit | Aplikasi `day2/session5_streamlit/apps` |

---

## 🚀 Memulai

### 1. Persiapan Lingkungan

```bash
# Clone repository
git clone <repository-url>
cd data-science

# Instalasi dependensi dengan uv
uv sync

# Atau dengan pip
pip install pandas numpy duckdb streamlit plotly matplotlib seaborn jupyter openpyxl pyarrow
```

### 2. Jalankan Jupyter Notebook

```bash
uv run jupyter notebook

# Buka notebook: day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb
```

### 3. Jalankan Aplikasi Streamlit

```bash
# LAB 10: Hello Streamlit (Dasar)
uv run streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py

# LAB 11: Komponen Interaktif
uv run streamlit run day2/session5_streamlit/apps/02_components_demo.py

# LAB 12: Penjelajah Data
uv run streamlit run day2/session5_streamlit/apps/03_data_explorer.py

# Dashboard Produksi - Analisis RUP
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

---

## 📁 Struktur Proyek

```
data-science/
├── day1/
│   ├── session1_python_pandas/
│   │   └── notebooks/
│   │       └── 01_exploratory_data_analysis_rup.ipynb  ✅
│   ├── session2_duckdb/
│   │   └── notebooks/
│   │       └── 01_duckdb_intro.ipynb  ✅
│   └── session3_visualization/
│       └── notebooks/
│           ├── 01_matplotlib_seaborn.ipynb  ✅
│           └── 02_plotly_interactive.ipynb  ✅
│
├── day2/
│   ├── session4_advanced_analysis/
│   │   └── notebooks/
│   │       ├── 01_data_cleaning.ipynb  ✅
│   │       ├── 02_time_series.ipynb  ✅
│   │       └── 03_statistical_analysis.ipynb  ✅
│   └── session5_streamlit/
│       └── apps/
│           ├── 01_hello_streamlit.py  ✅
│           ├── 02_components_demo.py  ✅
│           ├── 03_data_explorer.py  ✅
│           └── rup_dashboard.py  ✅
│
├── datasets/
│   └── rup/
│       └── RUP-PaketPenyedia-Terumumkan-2025.parquet  ✅
│
├── pyproject.toml  ✅
└── README.md
```

---

# 📚 HARI 1: Fundamental Analisis Data

## Sesi 1: Python & Pandas untuk Analisis Data (08:00 - 12:00)

**Durasi:** 4 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebook
**Kumpulan Data:** RUP 2025
**Notebook:** `day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb`
**Slides:** `slides/01_session1_pandas.md`

### ⏰ Agenda Ringkas
- 08:00 – 08:15 · Kick-off & tujuan sesi
- 08:15 – 09:00 · Persiapan environment & loading data
- 09:00 – 10:00 · EDA fundamentals dengan Pandas
- 10:00 – 11:00 · Data cleaning & handling missing values
- 11:00 – 11:45 · Aggregasi & GroupBy lanjutan
- 11:45 – 12:00 · Visualisasi cepat & wrap-up

### 🎯 Tujuan Sesi

Peserta akan menguasai teknik Exploratory Data Analysis (EDA) menggunakan Pandas untuk:
- Memahami struktur dan karakteristik dataset
- Mengidentifikasi pola, tren, dan anomali dalam data
- Melakukan data cleaning dan preprocessing
- Membuat insight bisnis dari data pengadaan pemerintah

### 📚 Materi Pembelajaran

#### 1.1 Kick-off & Setup Lingkungan (08:00 - 09:00)
- Sinkronisasi tujuan sesi, aturan main, dan struktur dataset RUP 2025
- Menyiapkan environment dengan `uv` atau `venv`, instalasi library wajib
- Membuka notebook `01_exploratory_data_analysis_rup.ipynb`
- Quick tour data dictionary & pemetaan kebutuhan analisis

#### 1.2 EDA Fundamentals dengan Pandas (09:00 - 10:00)
- Membaca file Parquet dan memahami struktur dengan `.head()`, `.info()`, `.describe()`
- Seleksi kolom/baris via `.loc[]`, `.iloc[]`, serta `query()` untuk filter cepat
- Teknik eksplorasi awal: distribusi, unique values, spotting missing data
- Hands-on: filter paket dengan pagu > 1 miliar & satker tertentu

#### 1.3 Data Cleaning & Quality Checks (10:00 - 11:00)
- Deteksi missing values (`isnull`, visual cues) dan strategi `dropna`/`fillna`
- Normalisasi tipe data (datetime, numerik, kategorikal) serta operasi string
- Penanganan duplikasi, trimming whitespace, dan validasi business rules
- Dokumentasi asumsi & temuan kualitas data sebelum analisis lanjut

#### 1.4 Aggregasi, Visualisasi Cepat & Wrap-up (11:00 - 12:00)
- GroupBy + agregasi untuk pagu per metode, satker, dan kategori
- Statistik deskriptif, deteksi outlier sederhana, dan korelasi cepat
- Visualisasi kilat dengan `DataFrame.plot()` untuk tren & komposisi
- Mini challenge + recap insight sebagai persiapan sesi DuckDB

#### 📓 Notebook:
`day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb`

**Praktik yang Dilakukan:**
- Analisis distribusi pagu pengadaan
- Identifikasi satker dengan pengadaan terbanyak
- Analisis metode pengadaan yang paling umum digunakan
- Trend pengumuman pengadaan dari waktu ke waktu
- Identifikasi outliers dan data quality issues

---

## BREAK / ISHOMA (12:00 - 13:00)

---

## Sesi 2: DuckDB untuk Query Analitik (13:00 - 15:00)

**Durasi:** 2 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebook
**Kumpulan Data:** RUP 2025
**Slides:** `slides/02_session2_duckdb.md`

### ⏰ Agenda Ringkas
- 13:00 – 13:15 · Kick-off DuckDB & setup environment
- 13:15 – 13:45 · DuckDB fundamentals & storage concepts
- 13:45 – 14:15 · SELECT, FILTER, ORDER BY
- 14:15 – 14:45 · Aggregations & window functions
- 14:45 – 15:00 · Integrasi DuckDB + Pandas & wrap-up

### Materi Pembelajaran

#### 2.1 Kick-off DuckDB & Setup (13:00 - 13:15)
- Perbandingan OLAP vs OLTP dan alasan memilih DuckDB untuk analitik lokal
- Instalasi, import, dan membuat koneksi in-memory/persistent
- Demo cepat membaca file Parquet langsung tanpa load penuh ke RAM

#### 2.2 Fundamentals & Storage Concepts (13:15 - 13:45)
- Arsitektur columnar storage, vectorized execution, dan implikasi performa
- Struktur tabel, tipe data, dan cara memetakan dataset RUP
- Praktik terbaik menyusun skema/VIew sementara untuk eksplorasi

#### 2.3 Query Essentials (13:45 - 14:15)
- SELECT, WHERE, ORDER BY, LIMIT, DISTINCT untuk eksplorasi dasar
- Agregasi inti: COUNT, SUM, AVG, MIN, MAX plus GROUP BY/HAVING
- Contoh nyata: Top satker berdasarkan pagu, filter kombinasi kondisi

#### 2.4 Aggregations & Window Functions (14:15 - 14:45)
- Common Table Expressions (CTE) untuk menyusun query modular
- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
- Penggabungan dengan Pandas DataFrame register untuk analisis hibrida
- Benchmark singkat Pandas GroupBy vs DuckDB query

#### 2.5 Integrasi Workflow & Wrap-up (14:45 - 15:00)
- Copy/Export hasil query ke Parquet/CSV
- Mengubah hasil query menjadi DataFrame (`.df()`) untuk visualisasi lanjut
- Checklist kapan memilih DuckDB dibanding Pandas
- Hands-on mini challenge & Q&A menjelang coffee break

#### 📓 Notebook:
`day1/session2_duckdb/notebooks/01_duckdb_intro.ipynb`

**Praktik yang Dilakukan:**
- Query top satker berdasarkan pagu menggunakan SQL
- Hitung running totals dengan window functions
- Analisis pivot: metode pengadaan vs kategori
- Agregasi time series per bulan/kuartal
- Benchmarking performa vs Pandas

---

## Coffee Break (15:00 - 15:30)

---

## Sesi 3: Visualisasi Data (15:30 - 17:00)

**Durasi:** 1 jam 30 menit
**Format Pembelajaran:** Praktikum dengan Jupyter Notebooks
**Kumpulan Data:** RUP 2025
**Slides:** `slides/03_session3_visualization.md`

### ⏰ Agenda Ringkas
- 15:30 – 15:40 · Kick-off & visual story goals
- 15:40 – 16:05 · Matplotlib fundamentals
- 16:05 – 16:30 · Seaborn statistical plots
- 16:30 – 16:50 · Plotly interaktif & dashboard mini
- 16:50 – 17:00 · Data storytelling & Q&A

### Materi Pembelajaran

#### 3.1 Kick-off & Visual Story Goals (15:30 - 15:40)
- Menyelaraskan tujuan sesi, konteks insight RUP, dan alur cerita yang ingin dibangun
- Checklist penilaian kualitas grafik (readability, warna, fokus insight)

#### 3.2 Matplotlib Fundamentals (15:40 - 16:05)
- Struktur Figure/Axes, konfigurasi tema, dan pengaturan ukuran
- Line, bar, scatter, serta histogram untuk highlight tren & distribusi
- Subplots dan anotasi untuk menaruh beberapa grafik dalam satu kanvas
- Export cepat ke PNG/PDF untuk laporan

#### 3.3 Seaborn Statistical Plots (16:05 - 16:30)
- Histogram, box, violin, dan kde plot untuk memotret distribusi pagu
- Categorical plots (countplot/barplot) untuk metode pengadaan dan satker
- Heatmap korelasi dan color palette ramah color-blind
- Styling cepat via `sns.set_theme` dan context manager

#### 📓 Notebook:
`day1/session3_visualization/notebooks/01_matplotlib_seaborn.ipynb`

#### 3.4 Plotly Mini Dashboard (16:30 - 16:50)
- Plotly Express vs Graph Objects dan kapan memakai masing-masing
- Interaktivitas default: hover, zoom, select, range slider
- Sunburst, treemap, bubble chart untuk multi-dimensi insight RUP
- Menyusun mini dashboard multi-tab + export ke HTML standalone

#### 📓 Notebook:
`day1/session3_visualization/notebooks/02_plotly_interactive.ipynb`

#### 3.5 Data Storytelling & Q&A (16:50 - 17:00)
- Prinsip memilih chart (comparison, distribution, relationship, composition, trend)
- Tips warna, hierarki visual, dan menghindari chartjunk
- Checklist final storytelling + sesi tanya jawab menjelang wrap-up

---

## Penutup Hari 1 (17:00 - 17:15)

- Rekap: Pandas, DuckDB, Visualisasi
- Sesi Tanya Jawab
- Pratinjau Hari 2: Analisis Lanjutan & Dashboard Streamlit
- Tugas opsional: Eksplorasi dataset RUP lebih lanjut

---

# 📊 HARI 2: Analisis Lanjutan & Dashboard Interaktif

## Sesi 4: Teknik Analisis Data Lanjutan (08:00 - 12:00)

**Durasi:** 4 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebooks
**Kumpulan Data:** RUP 2025
**Slides:** `slides/04_session4_advanced.md`

### ⏰ Agenda Ringkas
- 08:00 – 08:15 · Kick-off & problem framing
- 08:15 – 09:00 · Data cleaning & transformation
- 09:00 – 09:45 · Feature engineering & outliers
- 09:45 – 10:30 · Time series analysis
- 10:30 – 11:15 · Forecasting mini lab
- 11:15 – 12:00 · Statistical analysis & wrap-up

### Materi Pembelajaran

#### 4.1 Kick-off & Problem Framing (08:00 - 08:15)
- Menetapkan objective analisis lanjutan dan metrik keberhasilan
- Mengidentifikasi tantangan data nyata (missing, outliers, bias)

#### 4.2 Data Cleaning & Transformation (08:15 - 09:00)
- Audit kualitas data: duplicates, missing pattern, tipe data
- Strategi `dropna`, `fillna`, forward/backward fill, interpolation
- Normalisasi/standarisasi, log transform, serta export dataset bersih

#### 4.3 Feature Engineering & Outliers (09:00 - 09:45)
- Deteksi outlier (IQR, Z-score) + treatment (capping, winsorization)
- Encoding kategorikal (label, one-hot, frequency, target)
- Feature engineering tanggal, rasio, dan teks pendek

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/01_data_cleaning.ipynb`

#### 4.4 Time Series Foundations (09:45 - 10:30)
- Parsing tanggal, DateTime indexing, dan resampling multi-granular
- Rolling/expanding windows, EMA/SMA, cumulative metrics
- Growth rate (DoD, MoM, YoY) dan analisis seasonality

#### 4.5 Forecasting Mini Lab (10:30 - 11:15)
- Dekomposisi tren-musiman, moving average forecast, dan baseline modeling
- Kombinasi DuckDB + Pandas untuk pipeline analitik waktu

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/02_time_series.ipynb`

#### 4.6 Statistical Analysis & Experimentation (11:15 - 12:00)
- Statistik deskriptif lanjut (skewness, kurtosis, percentiles)
- Korelasi Pearson & Spearman + heatmap interpretasi
- Pengujian hipotesis (t-test, ANOVA, chi-square) dan dasar A/B testing
- Interpretasi p-value, signifikansi, dan rekomendasi keputusan

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/03_statistical_analysis.ipynb`

---

## BREAK / ISHOMA (12:00 - 13:00)

---

## Sesi 5: Dashboard Interaktif dengan Streamlit (13:00 - 17:00)

**Durasi:** 4 jam (termasuk istirahat)
**Format Pembelajaran:** Praktikum Lab
**Aplikasi:** 4 aplikasi Streamlit
**Slides:** `slides/05_session5_streamlit.md`

### ⏰ Agenda Ringkas
- 13:00 – 13:20 · Kick-off & agenda (`01_hello_streamlit.py`)
- 13:20 – 14:00 · Layout & text components (`01_hello_streamlit.py`)
- 14:00 – 14:45 · Input widgets & session state (`02_components_demo.py`)
- 14:45 – 15:00 · Data display & caching (`02_components_demo.py`)
- 15:00 – 15:30 · **Break / Ishoma**
- 15:30 – 16:15 · Data explorer build & metrics (`03_data_explorer.py`)
- 16:15 – 17:00 · Dashboard architecture, deployment & Q&A (`rup_dashboard.py`)

### 5.1 Kick-off & Dasar-dasar Streamlit - LAB 10 (13:00 - 14:00)

**Aplikasi:** `01_hello_streamlit.py`

**Topik yang Dipelajari:**

**A. Text Elements**
- `st.title()`, `st.header()`, `st.subheader()`
- `st.text()` vs `st.markdown()` vs `st.write()`
- `st.code()` untuk syntax highlighting
- `st.latex()` untuk mathematical expressions
- `st.divider()` untuk separators

**B. Displaying Data**
- `st.dataframe()` - interactive sortable table
- `st.table()` - static table
- `st.metric()` - KPI cards dengan delta
- `st.json()` - formatted JSON display

**C. Status Messages**
- `st.success()`, `st.info()`, `st.warning()`, `st.error()`
- `st.spinner()` untuk loading states
- `st.progress()` untuk progress bars

**D. Basic Charts**
- `st.line_chart()`, `st.bar_chart()`, `st.area_chart()`
- Simple data visualization

**E. Layout**
- `st.columns()` untuk column layout
- `st.container()` untuk grouping
- `st.expander()` untuk collapsible sections
- `st.tabs()` untuk tabbed interface

**Praktik:**
- Buat halaman welcome dengan berbagai text elements
- Tampilkan dataset RUP dengan tabel interaktif
- Tampilkan KPI menggunakan metrik
- Buat grafik sederhana
- Implementasikan layout responsif dengan kolom

---

### 5.2 Komponen Interaktif & Session State - LAB 11 (14:00 - 15:00)

**Aplikasi:** `02_components_demo.py`

**Topik yang Dipelajari:**

**A. Input Widgets**
- Buttons: `st.button()`, `st.download_button()`, `st.link_button()`
- Selection: `st.checkbox()`, `st.toggle()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`
- Sliders: `st.slider()`, `st.select_slider()`
- Text input: `st.text_input()`, `st.text_area()`, `st.number_input()`
- Date & time: `st.date_input()`, `st.time_input()`
- File: `st.file_uploader()`

**B. Formulir**
- `st.form()` untuk batch input submission
- Tombol submit formulir
- Validasi

**C. Session State**
- Memahami model eksekusi Streamlit
- `st.session_state` untuk persist data
- Callbacks dan penanganan event
- Contoh counter
- Contoh keranjang belanja

**D. Sidebar**
- `st.sidebar` untuk navigasi dan filter
- Mengatur kontrol

**Praktik:**
- Bangun penghitung interaktif dengan tombol
- Buat daftar tugas dengan kotak centang
- Implementasikan sistem filter dengan berbagai widget
- Buat formulir pendaftaran
- Pengunggah file dengan pratinjau
- Penyaringan grafik dinamis

---

## Coffee Break (15:00 - 15:30)

---

### 5.3 Penjelajah Data - LAB 12 (15:30 - 16:15)

**Aplikasi:** `03_data_explorer.py`

**Topik yang Dipelajari:**

**A. Alur Kerja Analisis Data Lengkap**
- Unggah file (CSV, Excel, Parquet)
- Pratinjau data dan statistik ringkasan
- Sistem penyaringan interaktif
- Berbagai tab analisis

**B. Integrasi DuckDB**
- `@st.cache_resource` untuk koneksi DuckDB
- `@st.cache_data` untuk caching data
- Pembangunan query SQL dinamis dari filter
- Eksekusi query dan tampilan hasil

**C. Filter Interaktif**
- Filter kategorikal (multiselect)
- Filter numerik (range slider)
- Filter rentang tanggal
- Tombol terapkan filter
- Penyaringan waktu-nyata

**D. Berbagai Tampilan Analisis**
- Tab 1: Analisis Distribusi
  - Histogram untuk kolom numerik
  - Pie chart untuk kolom kategorikal
- Tab 2: Analisis Tren
  - Grafik garis time series
  - Rata-rata bergerak
  - Perhitungan pertumbuhan
- Tab 3: Analisis Hubungan
  - Scatter plots
  - Heatmap korelasi
- Tab 4: Agregasi
  - Operasi groupBy kustom
  - Tabel pivot
  - Statistik ringkasan per grup

**E. Playground SQL**
- Editor query SQL kustom
- Eksekusi query pengguna
- Tampilkan hasil
- Penanganan error

**F. Fungsi Ekspor**
- Unduh data terfilter sebagai CSV
- Unduh ke Excel
- Unduh hasil query

**Praktik:**
- Unggah dataset RUP atau data kustom
- Terapkan berbagai filter
- Jelajahi data dengan berbagai tampilan
- Tulis query SQL kustom
- Ekspor hasil

---

### 5.4 Dashboard Produksi - Analisis RUP (16:15 - 17:00)

**Aplikasi:** `rup_dashboard.py`

**Topik yang Dipelajari:**

**A. Dashboard Siap Produksi**
- Desain UI/UX profesional
- Branding dan styling
- Konfigurasi halaman (`st.set_page_config()`)
- CSS kustom

**B. Pemrosesan Data Kompleks**
- Pipeline pemuatan data
- Strategi caching untuk performa
- Penanganan error
- Validasi data

**C. Visualisasi Lanjutan**
- Berbagai grafik terkoordinasi
- Fitur lanjutan Plotly
- Skema warna kustom
- Desain responsif

**D. KPI dan Metrik**
- Indikator kinerja utama
- Indikator tren dengan delta
- Kartu ringkasan statistik
- Metrik perbandingan

**E. Filter Interaktif**
- Filter sidebar
- Filter bertingkat
- Fungsi reset
- Manajemen status filter

**F. Praktik Terbaik**
- Organisasi kode
- Optimasi performa
- Pertimbangan pengalaman pengguna
- Persiapan deployment

**Praktik:**
- Pelajari struktur dashboard lengkap
- Analisis pola kode
- Pahami optimasi performa
- Pelajari praktik terbaik untuk produksi
- Kustomisasi dashboard

---

## Penutup Hari 2 (17:00 - 17:15)

### Tinjauan & Langkah Selanjutnya

**Poin-poin Penting:**
- Teknik pembersihan dan preprocessing data
- Analisis time series dan statistik
- Membangun dashboard interaktif dengan Streamlit
- Integrasi Pandas + DuckDB + Streamlit

**Sumber Belajar Lebih Lanjut:**
- [Dokumentasi Pandas](https://pandas.pydata.org/docs/)
- [Dokumentasi DuckDB](https://duckdb.org/docs/)
- [Dokumentasi Streamlit](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)

**Langkah Selanjutnya:**
- Berlatih dengan dataset lain
- Bangun dashboard kustom untuk kasus penggunaan sendiri
- Jelajahi fitur-fitur lanjutan Streamlit
- Terapkan dashboard ke Streamlit Cloud

**Sesi Tanya Jawab**

---

## 📚 Sumber Belajar & Materi

### Dokumentasi Resmi
- **Pandas:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- **DuckDB:** [https://duckdb.org/docs/](https://duckdb.org/docs/)
- **Streamlit:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Plotly:** [https://plotly.com/python/](https://plotly.com/python/)
- **Seaborn:** [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- **Matplotlib:** [https://matplotlib.org/](https://matplotlib.org/)

### Lembar Contekan
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Referensi SQL DuckDB](https://duckdb.org/docs/sql/introduction)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Galeri Grafik Python](https://python-graph-gallery.com/)

### Buku yang Direkomendasikan
- **"Python for Data Analysis"** karya Wes McKinney (Pembuat Pandas)
- **"Streamlit for Data Science: Create Interactive Data Apps in Python"** karya Tyler Richards
- **"DuckDB in Action"** karya Mark Needham & Simon Aubury (MotherDuck)

### Platform Pembelajaran Online
- **Kaggle Learn** - Kursus interaktif gratis
- **DataCamp** - Kursus data science praktis
- **Real Python** - Tutorial dan artikel Python
- **Towards Data Science** - Publikasi Medium untuk data science

### Dataset untuk Latihan
- **Kaggle Datasets** - Ribuan dataset untuk latihan
- **UCI Machine Learning Repositori** - Dataset klasik
- **Data.gov** - Data terbuka pemerintah AS
- **Google Dataset Search** - Mesin pencari untuk dataset

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

## 🚀 Langkah Selanjutnya

### Setelah Bootcamp
1. **Bangun portofolio proyek** - Tunjukkan kemampuan Anda
2. **Terapkan dashboard Anda** - Gunakan Streamlit Cloud (gratis)
3. **Berkontribusi ke sumber terbuka** - Belajar dari yang lain
4. **Jelajahi topik lanjutan:**
   - Pembelajaran Mesin dengan scikit-learn
   - Pembelajaran Mendalam dengan TensorFlow/PyTorch
   - Big Data dengan Apache Spark
   - Platform Cloud (AWS, GCP, Azure)

### Pilihan Jalur Karir
- **Data Analyst** - Wawasan bisnis dan pelaporan
- **Business Intelligence** - Dashboard dan visualisasi
- **Data Engineer** - Pipeline data dan infrastruktur
- **Data Scientist** - Pembelajaran mesin dan model prediktif
- **Analytics Engineer** - dbt, SQL, pemodelan data

### Lanjutkan Belajar
- Bergabung dengan komunitas data science (Kaggle, Reddit, Discord)
- Ikuti blog dan newsletter data science
- Hadiri pertemuan dan konferensi
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
