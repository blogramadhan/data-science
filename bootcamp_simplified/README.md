# 🎓 Bootcamp Data Analysis - Simplified Version

**Versi Sederhana & Fundamental untuk Bootcamp 2 Hari**

Folder ini berisi materi bootcamp yang telah disederhanakan agar lebih fokus pada konsep fundamental dan dapat diselesaikan dalam waktu bootcamp yang terbatas.

## 📋 Struktur Materi

### Day 1: Data Analysis Fundamentals

#### ⏰ Session 1: Pandas Fundamental (120 menit)
**File:** `day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb`

**Topik:**
- Load & explore data
- Seleksi data (columns & rows)
- Filtering dengan boolean indexing
- GroupBy & agregasi
- Missing values
- Summary statistics

**Output:** Peserta dapat melakukan operasi dasar Pandas untuk analisis data

---

#### ⏰ Session 2: DuckDB & Visualization (120 menit)
**File:**
- `day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb`
- `day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb`

**Topik DuckDB (60 menit):**
- Setup DuckDB
- SQL queries dasar (SELECT, WHERE, ORDER BY)
- Aggregate functions (SUM, COUNT, AVG)
- GROUP BY & HAVING
- Export results

**Topik Visualization (60 menit):**
- Bar chart & Pie chart
- Line chart untuk trend
- Integrasi Plotly dengan Pandas

**Output:** Peserta dapat menjalankan SQL query dan membuat visualisasi dasar

---

### Day 2: Streamlit Dashboard (Full Day)

#### ⏰ Session 3: Streamlit Basics (120 menit)
**File:** `day2/session3_streamlit_basics/app_part1.py`

**Topik:**
- Setup Streamlit app
- Layout (columns, containers)
- Widgets (selectbox, slider, checkbox)
- Metrics & KPI cards
- Data table

**Output:** Aplikasi Streamlit dasar dengan widgets interaktif

---

#### ⏰ Session 4: Streamlit Dashboard Complete (120 menit)
**File:** `day2/session4_streamlit_complete/app_complete.py`

**Topik:**
- Tabs & multi-section layout
- Integrasi dengan Plotly charts
- Filtering & interaktivitas
- Caching untuk performance
- Export data (CSV/Excel)
- Deploy ke Streamlit Cloud

**Output:** Dashboard RUP lengkap yang siap production

---

## 🚀 Cara Menggunakan

### 1. Setup Environment

```bash
# Clone repo (jika belum)
git clone <repo-url>
cd data-science/bootcamp_simplified

# Install dependencies
pip install pandas plotly streamlit duckdb pyarrow
```

### 2. Jalankan Notebooks (Day 1)

```bash
# Session 1-3: Buka di Jupyter
jupyter notebook

# Atau gunakan VS Code dengan Jupyter extension
```

### 3. Jalankan Streamlit App (Day 2)

```bash
cd day2/session4_streamlit
streamlit run app_simple.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

---

## 📊 Dataset

**Dataset:** RUP Paket Penyedia Terumumkan 2025
**Lokasi:** `../datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet`
**Size:** ~16,430 rows, 48 columns
**Format:** Parquet (efficient & compressed)

**Kolom Penting:**
- `nama_paket`: Nama paket pengadaan
- `pagu`: Nilai pagu (Rupiah)
- `metode_pengadaan`: Tender, E-Purchasing, dll
- `jenis_pengadaan`: Barang, Jasa, Konstruksi, dll
- `nama_satker`: Satuan Kerja
- `status_pdn`, `status_ukm`, `status_pradipa`: Status khusus
- `tgl_pengumuman_paket`: Tanggal pengumuman

---

## ⚡ Perbedaan dengan Versi Lengkap

| Aspek | Versi Lengkap | Versi Simplified |
|-------|---------------|------------------|
| **Durasi** | 3-4 hari | 2 hari (8 jam efektif) |
| **Fokus** | Comprehensive & advanced | Fundamental & praktis |
| **Pandas** | 69 cells, semua fitur | 20 cells, operasi inti |
| **DuckDB** | Advanced queries, joins | Basic queries, agregasi |
| **Visualization** | Matplotlib + Seaborn + Plotly | Plotly only |
| **Streamlit** | Multi-page, complex | **2 sessions progressif** (basics → complete) |
| **Advanced Topics** | Statistical analysis, time series | ❌ Dihapus |
| **Waktu Streamlit** | 25% dari total | **50% dari total (full day 2)** |

---

## 🎯 Learning Outcomes

Setelah menyelesaikan bootcamp simplified, peserta akan dapat:

✅ Memuat dan mengeksplorasi data dengan Pandas
✅ Melakukan filtering, grouping, dan agregasi
✅ Menulis SQL queries dengan DuckDB
✅ Membuat visualisasi interaktif dengan Plotly
✅ Membangun dashboard sederhana dengan Streamlit
✅ Deploy dashboard ke Streamlit Cloud

---

## 📚 Materi Tambahan (Opsional)

Jika waktu tersedia, topik ini bisa ditambahkan:

- **Data Cleaning:** Handle duplicates, outliers, data types
- **Time Series:** Resampling, rolling windows
- **Advanced Charts:** Scatter plots, heatmaps, treemaps
- **Streamlit Advanced:** Multi-page apps, session state, forms

Materi lengkap tersedia di folder `../day1` dan `../day2`

---

## 🔗 Resources

- **Pandas Docs:** https://pandas.pydata.org/docs/
- **DuckDB Docs:** https://duckdb.org/docs/
- **Plotly Docs:** https://plotly.com/python/
- **Streamlit Docs:** https://docs.streamlit.io/
- **Streamlit Cloud:** https://streamlit.io/cloud

---

## 💡 Tips untuk Instruktur

1. **Session 1-3:** Fokus pada hands-on, biarkan peserta coding sendiri
2. **Session 4:** Live coding dashboard step-by-step
3. **Breaks:** 15 menit setiap 90 menit
4. **Q&A:** Alokasikan 15-30 menit di akhir setiap session
5. **Practice:** Gunakan "Latihan Mandiri" di akhir setiap notebook

---

## 📝 License

Materi bootcamp ini dibuat untuk keperluan edukasi.

---

**Happy Learning! 🚀**
