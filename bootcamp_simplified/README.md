# 🎓 Bootcamp Analisis Data - Versi Sederhana

**Edisi Fundamental selama 2 Hari**

Folder ini berisi materi bootcamp yang dipadatkan supaya fokus pada konsep dasar dan selesai dalam durasi bootcamp singkat.

## 📋 Struktur Materi

### Hari 1: Dasar Analisis Data

#### ⏰ Sesi 1: Pandas Fundamental (120 menit)
**File:** `day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb`

**Topik:**
- Muat & eksplorasi data
- Seleksi kolom & baris
- Filtering dengan boolean indexing
- GroupBy & agregasi
- Missing values
- Statistik ringkasan

**Output:** Peserta dapat menjalankan operasi dasar Pandas untuk analisis data

---

#### ⏰ Sesi 2: DuckDB & Visualisasi (120 menit)
**File:**
- `day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb`
- `day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb`

**Topik DuckDB (60 menit):**
- Setup DuckDB
- Query SQL dasar (SELECT, WHERE, ORDER BY)
- Fungsi agregasi (SUM, COUNT, AVG)
- GROUP BY & HAVING
- Ekspor hasil

**Topik Visualisasi (60 menit):**
- Bar chart & pie chart
- Line chart untuk tren
- Integrasi Plotly dengan Pandas

**Output:** Peserta dapat menjalankan query SQL dan membuat visualisasi dasar

---

### Hari 2: Dashboard Streamlit (Full Day)

#### ⏰ Sesi 3: Dasar Streamlit (120 menit)
**File:** `day2/session3_streamlit_basics/app_part1.py`

**Topik:**
- Setup aplikasi Streamlit
- Layout (kolom, container)
- Widgets (selectbox, slider, checkbox)
- Metrics & kartu KPI
- Tabel data

**Output:** Aplikasi Streamlit dasar dengan widgets interaktif

---

#### ⏰ Sesi 4: Dashboard Streamlit Lengkap (120 menit)
**File:** `day2/session4_streamlit_complete/app_complete.py`

**Topik:**
- Tabs & layout multi-section
- Integrasi Plotly charts
- Filtering & interaktivitas
- Caching untuk performa
- Ekspor data (CSV/Excel)
- Deploy ke Streamlit Cloud

**Output:** Dashboard RUP lengkap yang siap produksi

---

## 🚀 Cara Menggunakan

### 1. Siapkan Environment

```bash
# Clone repo (jika belum)
git clone <repo-url>
cd data-science/bootcamp_simplified

# Install dependencies
pip install pandas plotly streamlit duckdb pyarrow
```

### 2. Jalankan Notebooks (Hari 1)

```bash
# Sesi 1-3: buka di Jupyter
jupyter notebook

# Atau gunakan VS Code dengan ekstensi Jupyter
```

### 3. Jalankan Streamlit App (Hari 2)

```bash
cd day2/session4_streamlit
streamlit run app_simple.py
```

Dashboard terbuka di browser pada `http://localhost:8501`

---

## 📊 Dataset

**Dataset:** RUP Paket Penyedia Terumumkan 2025  
**Lokasi:** `../datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet`  
**Ukuran:** ~16.430 baris, 48 kolom  
**Format:** Parquet (efisien & terkompresi)

**Kolom penting:**
- `nama_paket`: Nama paket pengadaan
- `pagu`: Nilai pagu (Rupiah)
- `metode_pengadaan`: Tender, E-Purchasing, dll
- `jenis_pengadaan`: Barang, Jasa, Konstruksi, dll
- `nama_satker`: Satuan Kerja
- `status_pdn`, `status_ukm`, `status_pradipa`: Status khusus
- `tgl_pengumuman_paket`: Tanggal pengumuman

---

## ⚡ Perbedaan dengan Versi Lengkap

| Aspek | Versi Lengkap | Versi Sederhana |
|-------|---------------|-----------------|
| **Durasi** | 3-4 hari | 2 hari (8 jam efektif) |
| **Fokus** | Komprehensif & advance | Fundamental & praktis |
| **Pandas** | 69 sel, semua fitur | 20 sel, operasi inti |
| **DuckDB** | Query lanjutan, join | Query dasar, agregasi |
| **Visualisasi** | Matplotlib + Seaborn + Plotly | Plotly saja |
| **Streamlit** | Multi-halaman, kompleks | **2 sesi progresif** (dasar → lengkap) |
| **Topik lanjut** | Statistik, time series | ❌ Dihilangkan |
| **Porsi Streamlit** | 25% | **50% (full day 2)** |

---

## 🎯 Learning Outcomes

Setelah menyelesaikan bootcamp versi sederhana, peserta mampu:

✅ Memuat dan mengeksplorasi data dengan Pandas  
✅ Melakukan filtering, grouping, dan agregasi  
✅ Menulis query SQL dengan DuckDB  
✅ Membuat visualisasi interaktif dengan Plotly  
✅ Membangun dashboard sederhana dengan Streamlit  
✅ Deploy dashboard ke Streamlit Cloud

---

## 📚 Materi Tambahan (Opsional)

Jika waktu memungkinkan, tambah topik:

- **Data Cleaning:** Tangani duplikat, outlier, tipe data
- **Time Series:** Resampling, rolling windows
- **Chart Lanjutan:** Scatter, heatmap, treemap
- **Streamlit Lanjutan:** Multi-halaman, session state, forms

Materi lengkap ada di folder `../day1` dan `../day2`.

---

## 🔗 Sumber Belajar

- **Pandas Docs:** https://pandas.pydata.org/docs/
- **DuckDB Docs:** https://duckdb.org/docs/
- **Plotly Docs:** https://plotly.com/python/
- **Streamlit Docs:** https://docs.streamlit.io/
- **Streamlit Cloud:** https://streamlit.io/cloud

---

## 💡 Tips untuk Instruktur

1. **Sesi 1-3:** Fokus hands-on, biarkan peserta mencoba sendiri  
2. **Sesi 4:** Live coding dashboard step-by-step  
3. **Break:** 15 menit setiap 90 menit  
4. **Q&A:** 15-30 menit di akhir tiap sesi  
5. **Latihan:** Gunakan “Latihan Mandiri” di akhir notebook

---

## 📝 Lisensi

Materi bootcamp ini disiapkan untuk kebutuhan edukasi.

---

**Selamat belajar! 🚀**
