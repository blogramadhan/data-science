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

## Sesi 1: Python & Pandas untuk Analisis Data (09:00 - 12:00)

**Durasi:** 3 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebook
**Kumpulan Data:** RUP 2025
**Notebook:** `day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb`
**Slides:** `slides/01_session1_pandas.md`

### 🎯 Tujuan Sesi

Peserta akan menguasai teknik Exploratory Data Analysis (EDA) menggunakan Pandas untuk:
- Memahami struktur dan karakteristik dataset
- Mengidentifikasi pola, tren, dan anomali dalam data
- Melakukan data cleaning dan preprocessing
- Membuat insight bisnis dari data pengadaan pemerintah

### 📚 Materi Pembelajaran

#### 1.1 Persiapan Lingkungan (30 menit)
- Persiapan Python & Virtual Environment (uv/venv)
- Instalasi pustaka yang dibutuhkan
- Pengenalan Jupyter Notebook
- Membuka dataset RUP 2025

#### 1.2 Exploratory Data Analysis (EDA) dengan Pandas (150 menit)

**Topik yang Dipelajari:**

**A. Loading dan Inspeksi Data**
- Membaca file Parquet dengan Pandas
- Inspeksi struktur data: `.head()`, `.info()`, `.describe()`, `.shape`
- Memahami kolom-kolom dalam dataset RUP
- Identifikasi tipe data dan missing values

**B. Seleksi & Penyaringan Data**
- Menggunakan `.loc[]` dan `.iloc[]` untuk seleksi data
- Boolean indexing untuk penyaringan
- Query method untuk filter kompleks
- Contoh: Filter paket dengan pagu > 1 miliar

**C. Data Aggregation**
- GroupBy operations untuk agregasi
- Menghitung total pagu per metode pengadaan
- Menghitung jumlah paket per satuan kerja
- Top 10 satker dengan pagu terbesar

**D. Manipulasi Data**
- Sorting data berdasarkan multiple columns
- Menangani missing values (deteksi & treatment)
- Operasi string untuk cleaning
- Operasi date/time

**E. Ringkasan Statistik**
- Statistik deskriptif (mean, median, std, percentiles)
- Analisis distribusi
- Deteksi outlier
- Analisis korelasi antar variabel numerik

**F. Data Visualization dengan Pandas**
- Bar charts untuk categorical data
- Histogram untuk distribusi pagu
- Time series plotting
- Basic styling dan customization

#### 📓 Notebook:
`day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb`

**Praktik yang Dilakukan:**
- Analisis distribusi pagu pengadaan
- Identifikasi satker dengan pengadaan terbanyak
- Analisis metode pengadaan yang paling umum digunakan
- Trend pengumuman pengadaan dari waktu ke waktu
- Identifikasi outliers dan data quality issues

---

## BREAK (12:00 - 13:00)

---

## Sesi 2: DuckDB untuk Query Analitik (13:00 - 15:30)

**Durasi:** 2.5 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebook
**Kumpulan Data:** RUP 2025
**Slides:** `slides/02_session2_duckdb.md`

### Materi Pembelajaran

#### 2.1 Pengenalan DuckDB (30 menit)

**Konsep:**
- Apa itu DuckDB dan mengapa menggunakannya?
- OLAP vs OLTP database
- DuckDB vs Traditional Databases (PostgreSQL, MySQL)
- In-memory analytics & columnar storage
- Use cases: kapan pakai Pandas vs DuckDB

**Setup:**
- Install dan import DuckDB
- Create connection (in-memory vs persistent)
- Basic query execution

#### 2.2 SQL dengan DuckDB (90 menit)

**A. Operasi SQL Dasar**
- SELECT, WHERE, ORDER BY, LIMIT
- DISTINCT untuk unique values
- Agregasi: COUNT, SUM, AVG, MIN, MAX
- GROUP BY dan HAVING
- Penyaringan dengan multiple conditions

**B. Fitur Khusus DuckDB**
- Read Parquet file langsung tanpa loading ke memory
- Query Pandas DataFrame dengan SQL
- Convert hasil query ke DataFrame
- COPY statement untuk export

**C. Query SQL Lanjutan**
- JOIN operations (INNER, LEFT, RIGHT)
- Subqueries dan nested queries
- CTEs (Common Table Expressions) untuk query kompleks
- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
- CASE WHEN untuk conditional logic
- Aggregate functions dengan OVER clause

**Contoh Query dengan Dataset RUP:**
```sql
-- Top 10 Satker by Total Pagu
-- Running total of pengumuman
-- Ranking paket within kategori
-- Monthly aggregations
-- Penyaringan kompleks dengan multiple conditions
```

#### 2.3 Integrasi Pandas & DuckDB (30 menit)

**Integrasi Alur Kerja:**
- Daftarkan Pandas DataFrame sebagai tabel DuckDB
- Query tabel DuckDB dan dapatkan hasilnya sebagai DataFrame
- Perbandingan performa: Pandas GroupBy vs DuckDB SQL
- Praktik terbaik: kapan pakai Pandas, kapan pakai DuckDB
- Menangani dataset besar secara efisien

#### 📓 Notebook:
`day1/session2_duckdb/notebooks/01_duckdb_intro.ipynb`

**Praktik yang Dilakukan:**
- Query top satker berdasarkan pagu menggunakan SQL
- Hitung running totals dengan window functions
- Analisis pivot: metode pengadaan vs kategori
- Agregasi time series per bulan/kuartal
- Benchmarking performa vs Pandas

---

## BREAK (15:30 - 15:45)

---

## Sesi 3: Visualisasi Data (15:45 - 17:30)

**Durasi:** 1 jam 45 menit
**Format Pembelajaran:** Praktikum dengan Jupyter Notebooks
**Kumpulan Data:** RUP 2025
**Slides:** `slides/03_session3_visualization.md`

### Materi Pembelajaran

#### 3.1 Visualisasi Statis dengan Matplotlib & Seaborn (45 menit)

**Matplotlib Basics:**
- Figure dan Axes architecture
- Plot types: line, bar, scatter, histogram, pie
- Customization: colors, labels, legends, grid
- Subplots untuk multiple charts
- Export ke image files (PNG, PDF)

**Seaborn untuk Statistical Plots:**
- Distribution plots: histplot, kdeplot, boxplot, violinplot
- Categorical plots: barplot, countplot, pointplot
- Relationship plots: scatterplot, regplot
- Heatmaps untuk correlation matrix
- Built-in themes dan color palettes

#### 📓 Notebook:
`day1/session3_visualization/notebooks/01_matplotlib_seaborn.ipynb`

**Praktik yang Dilakukan:**
- Histogram distribusi pagu dengan mean & median lines
- Horizontal bar chart: Top satker by total pagu
- Pie chart: Distribusi metode pengadaan
- Line chart: Trend pengumuman over time
- Box plot & Violin plot: Pagu by metode
- Count plot: Paket per metode
- Heatmap: Correlation matrix
- Subplots: Dashboard dengan multiple charts
- Export visualizations dengan high resolution

#### 3.2 Visualisasi Interaktif dengan Plotly (45 menit)

**Fundamental Plotly:**
- Plotly Express vs Graph Objects
- Grafik interaktif: hover, zoom, pan, select
- Tipe grafik: line, bar, scatter, box, sunburst, treemap
- Subplots dan kustomisasi layout
- Export ke HTML untuk sharing

**Fitur Lanjutan:**
- Tambahkan anotasi dan shapes
- Update layout dan styling
- Multiple traces pada satu grafik
- Desain responsif

#### 📓 Notebook:
`day1/session3_visualization/notebooks/02_plotly_interactive.ipynb`

**Praktik yang Dilakukan:**
- Bar chart interaktif: Top satker dengan hover tooltips
- Histogram dengan interaktivitas
- Scatter plot: Bubble chart dengan dimensi size & color
- Box plot: Perbandingan distribusi interaktif
- Sunburst chart: Visualisasi hierarkis
- Treemap: Persegi panjang proporsional berdasarkan metode
- Time series: Line chart dengan range slider
- Graph Objects kustom dengan anotasi
- Perbandingan berbagai traces
- Layout dashboard dengan subplots
- Ekspor grafik interaktif sebagai file HTML standalone

#### 3.3 Data Storytelling (15 menit)

**Prinsip:**
- Memilih tipe grafik yang tepat untuk data
- Teori warna dan aksesibilitas (ramah buta warna)
- Praktik terbaik grafik (hindari chartjunk)
- Prinsip desain dashboard
- Kesalahan visualisasi umum

**Panduan Pemilihan Grafik:**
- Perbandingan → Bar chart
- Distribusi → Histogram, Box plot
- Hubungan → Scatter plot
- Komposisi → Pie chart, Treemap
- Tren → Line chart

---

## Penutup Hari 1 (17:30 - 17:45)

- Rekap: Pandas, DuckDB, Visualisasi
- Sesi Tanya Jawab
- Pratinjau Hari 2: Analisis Lanjutan & Dashboard Streamlit
- Tugas opsional: Eksplorasi dataset RUP lebih lanjut

---

# 📊 HARI 2: Analisis Lanjutan & Dashboard Interaktif

## Sesi 4: Teknik Analisis Data Lanjutan (09:00 - 12:00)

**Durasi:** 3 jam
**Format Pembelajaran:** Praktikum dengan Jupyter Notebooks
**Kumpulan Data:** RUP 2025
**Slides:** `slides/04_session4_advanced.md`

### Materi Pembelajaran

#### 4.1 Pembersihan & Transformasi Data (60 menit)

**A. Menangani Missing Data**
- Deteksi: `.isnull()`, `.isna()`, `.info()`
- Strategi:
  - Drop: `dropna()`
  - Fill: `fillna()` dengan value/mean/median
  - Forward/Backward fill: `ffill()`, `bfill()`
  - Interpolasi
- Praktik terbaik untuk missing data

**B. Menangani Outliers**
- Metode deteksi:
  - IQR (Interquartile Range) method
  - Z-score method
  - Visualisasi dengan box plots
- Strategi treatment:
  - Hapus outliers
  - Winsorization (capping)
  - Transformasi (log, sqrt)
- Kapan outliers adalah data valid vs error

**C. Encoding Categorical Variables**
- Label Encoding untuk ordinal data
- One-Hot Encoding untuk nominal data
- Target Encoding
- Frequency Encoding

**D. Feature Engineering**
- Ekstraksi fitur date/time (year, month, quarter, day of week)
- Binning variabel kontinyu
- Membuat fitur rasio
- Feature engineering teks (panjang, jumlah kata)

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/01_data_cleaning.ipynb`

**Praktik yang Dilakukan:**
- Data quality assessment (missing values, duplicates, dtypes)
- Missing values detection dan visualization
- Multiple strategies: drop, fill, impute
- Outlier detection: IQR method & Z-score
- Outlier treatment: Capping/Winsorization
- Data transformation: Log, normalization, standardization
- Label encoding untuk ordinal data
- One-hot encoding untuk nominal data
- Frequency encoding untuk high cardinality
- Feature engineering tanggal (year, month, quarter, weekend, etc.)
- Binning: Buat kategorikal dari kontinyu
- Fitur teks: Panjang, jumlah kata
- Ekspor dataset yang telah dibersihkan

#### 4.2 Analisis Time Series (60 menit)

**A. Operasi DateTime**
- Parsing dates dengan `pd.to_datetime()`
- DateTime indexing
- Resampling: daily, weekly, monthly, quarterly
- Penanganan time zones

**B. Time Series Aggregations**
- Rolling windows: moving average, moving sum
- Expanding windows
- Cumulative calculations: cumsum, cumprod
- Lead and lag operations

**C. Analisis Tren**
- Perhitungan pertumbuhan: MoM, YoY, QoQ
- Deteksi tren
- Analisis seasonality dengan decomposition
- Konsep forecasting sederhana

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/02_time_series.ipynb`

**Praktik yang Dilakukan:**
- Parse dates dan DateTime indexing
- Extract date components (year, month, quarter, day of week, etc.)
- Resampling: Daily, Weekly, Monthly, Quarterly aggregations
- Simple Moving Average (SMA) - 7d, 14d, 30d
- Exponential Moving Average (EMA)
- Statistik rolling: sum, std, min, max
- Perhitungan kumulatif: cumsum, cumprod
- Perhitungan tingkat pertumbuhan: DoD, WoW, MoM, YoY
- Analisis seasonality: Pola bulanan & hari dalam seminggu
- Dekomposisi musiman (trend, seasonal, residual)
- Visualisasi berbagai granularitas waktu
- Dasar-dasar forecasting time series

#### 4.3 Analisis Statistik (60 menit)

**A. Statistik Deskriptif**
- Tendensi sentral: mean, median, mode
- Dispersi: variance, std dev, range, IQR
- Percentiles dan quantiles
- Skewness dan kurtosis

**B. Analisis Korelasi**
- Korelasi Pearson (hubungan linear)
- Korelasi Spearman (hubungan monotonik)
- Visualisasi matriks korelasi
- Kausalitas vs korelasi

**C. Analisis Distribusi**
- Analisis histogram
- Pengujian distribusi normal
- Q-Q plots
- Penyesuaian distribusi

**D. Dasar-dasar Pengujian Hipotesis**
- Hipotesis null vs hipotesis alternatif
- Interpretasi nilai P
- T-test untuk membandingkan dua grup
- Chi-square test untuk data kategorikal
- ANOVA untuk membandingkan beberapa grup

**E. Fundamental A/B Testing**
- Merancang A/B test
- Perhitungan ukuran sampel
- Signifikansi statistik
- Menginterpretasikan hasil

#### 📓 Notebook:
`day2/session4_advanced_analysis/notebooks/03_statistical_analysis.ipynb`

**Praktik yang Dilakukan:**
- **Statistik Deskriptif:**
  - Tendensi sentral: Mean, median, mode dengan visualisasi
  - Dispersi: Variance, std dev, range, CV
  - Percentiles & Quartiles (box plots)
  - Ukuran bentuk: Skewness & Kurtosis
- **Analisis Korelasi:**
  - Korelasi Pearson (hubungan linear)
  - Korelasi Spearman (hubungan monotonik)
  - Heatmap matriks korelasi
  - Pengujian signifikansi statistik
- **Analisis Distribusi:**
  - Tes normalitas: Shapiro-Wilk, D'Agostino-Pearson
  - Q-Q plots untuk penilaian visual
  - Histogram dengan curve fitting
- **Pengujian Hipotesis:**
  - Independent T-test: Bandingkan 2 grup
  - ANOVA: Bandingkan beberapa grup
  - Chi-square test: Independensi kategorikal
  - Interpretasi nilai P & tingkat signifikansi
- **A/B Testing:**
  - Perbandingan tingkat konversi
  - Pengujian signifikansi statistik
  - Perhitungan lift
  - Penentuan pemenang

---

## BREAK (12:00 - 13:00)

---

## Sesi 5: Dashboard Interaktif dengan Streamlit (13:00 - 17:30)

**Durasi:** 4.5 jam (termasuk istirahat)
**Format Pembelajaran:** Praktikum Lab
**Aplikasi:** 4 aplikasi Streamlit
**Slides:** `slides/05_session5_streamlit.md`

### 5.1 Dasar-dasar Streamlit - LAB 10 (13:00 - 14:00)

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

### 5.2 Komponen Interaktif - LAB 11 (14:00 - 15:15)

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

## BREAK (15:15 - 15:30)

---

### 5.3 Penjelajah Data - LAB 12 (15:30 - 16:45)

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

### 5.4 Dashboard Produksi - Analisis RUP (16:45 - 17:30)

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

## Penutup Hari 2 (17:30 - 17:45)

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
