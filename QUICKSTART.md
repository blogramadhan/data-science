# 🚀 Panduan Memulai Cepat - Analisis RUP 2025

Panduan cepat untuk menjalankan project analisis data RUP 2025.

## Prasyarat

- Python 3.12+ terinstall
- UV package manager ([Install uv](https://github.com/astral-sh/uv))
- Git (opsional, untuk clone repository)

## Langkah 1: Setup Project

```bash
# Jika belum di folder project
cd /home/rizko/coding/python/project/data-science

# Install dependencies dengan uv
uv sync
```

Output yang diharapkan:
```
✅ Resolved 133 packages
✅ Installed 129 packages
```

## Langkah 2: Verifikasi Instalasi

```bash
# Test import libraries
uv run python -c "import pandas, duckdb, streamlit, plotly; print('✅ Semua library berhasil diinstall!')"
```

## Langkah 3: Eksplorasi Data dengan Jupyter

### Opsi A: Via Browser (Direkomendasikan)

```bash
# Jalankan Jupyter Notebook server
uv run jupyter notebook
```

Browser akan terbuka otomatis. Navigasi ke:
```
day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb
```

### Opsi B: Via JupyterLab

```bash
# Install jupyterlab jika belum
uv pip install jupyterlab

# Jalankan JupyterLab
uv run jupyter lab
```

## Langkah 4: Jalankan Streamlit Dashboard

```bash
# Jalankan dashboard interaktif
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

Dashboard akan terbuka di browser: http://localhost:8501

### Fitur Dashboard:
- 📊 Overview Data RUP
- 💰 Analisis Pagu
- 🏛️ Analisis K/L/PD
- 📋 Metode & Jenis Pengadaan
- 📅 Analisis Timeline
- 🔍 Filter Interaktif
- 📥 Ekspor Data

## Langkah 5: Eksplorasi Dataset

### Cek Data dengan Python

```bash
uv run python
```

Kemudian di Python shell:

```python
import pandas as pd

# Load data
df = pd.read_parquet('datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet')

# Basic info
print(f"Total records: {len(df):,}")
print(f"Total columns: {len(df.columns)}")
print(f"Total pagu: Rp {df['pagu'].sum() / 1e12:.2f} Triliun")

# Top 5 K/L/PD
print("\nTop 5 K/L/PD by Pagu:")
top_klpd = df.groupby('nama_klpd')['pagu'].sum().sort_values(ascending=False).head()
print(top_klpd / 1e9)  # dalam Miliar
```

### Query dengan DuckDB

```python
import duckdb

conn = duckdb.connect(':memory:')

# Query langsung dari file parquet
result = conn.execute("""
    SELECT
        nama_klpd,
        COUNT(*) as jumlah_paket,
        SUM(pagu) / 1e9 as total_pagu_miliar
    FROM 'datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet'
    GROUP BY nama_klpd
    ORDER BY total_pagu_miliar DESC
    LIMIT 10
""").df()

print(result)
```

## 📁 Struktur File

```
day1/session1_python_pandas/notebooks/
└── 01_exploratory_data_analysis_rup.ipynb    # EDA lengkap dengan visualisasi

day2/session5_streamlit/apps/
└── rup_dashboard.py                           # Dashboard interaktif

datasets/rup/
├── RUP-PaketPenyedia-Terumumkan-2025.parquet # Sumber data
└── README.md                                  # Dokumentasi dataset
```

## Pemecahan Masalah

### Masalah: Module tidak ditemukan

```bash
# Reinstall dependencies
uv sync --refresh
```

### Masalah: Jupyter tidak muncul

```bash
# Install jupyter secara eksplisit
uv pip install jupyter notebook

# Jalankan dengan full path
uv run jupyter notebook
```

### Masalah: Error Streamlit

```bash
# Cek versi streamlit
uv pip list | grep streamlit

# Reinstall jika perlu
uv pip install --force-reinstall streamlit
```

### Masalah: Tidak bisa membaca file parquet

Pastikan file ada di lokasi yang benar:
```bash
ls -lh datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet
```

### Masalah: Port 8501 sudah digunakan

```bash
# Gunakan port lain
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py --server.port 8502
```

## 💡 Tips & Trik

### 1. Auto-reload di Streamlit

Setiap kali Anda save file `rup_dashboard.py`, Streamlit akan auto-reload!

### 2. Jupyter Keyboard Shortcuts

- `Shift + Enter`: Run cell dan pindah ke cell berikutnya
- `Ctrl + Enter`: Run cell tanpa pindah
- `A`: Insert cell di atas
- `B`: Insert cell di bawah
- `DD`: Delete cell

### 3. Filter Data di Dashboard

Gunakan sidebar di kiri untuk:
- Filter metode pengadaan
- Filter jenis pengadaan
- Filter K/L/PD
- Range pagu
- Status PDN/UKM/PRADIPA

### 4. Export Data

Di dashboard, klik tombol "Export Filtered Data (CSV)" di sidebar untuk download data yang sudah difilter.

## 📊 Contoh Query Analisis

### Query 1: 10 Paket Terbesar

```sql
SELECT
    nama_paket,
    nama_klpd,
    pagu / 1e9 as pagu_miliar,
    metode_pengadaan
FROM 'datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet'
ORDER BY pagu DESC
LIMIT 10;
```

### Query 2: Analisis PDN & UKM

```sql
SELECT
    status_pdn,
    status_ukm,
    COUNT(*) as jumlah_paket,
    SUM(pagu) / 1e12 as total_pagu_triliun
FROM 'datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet'
GROUP BY status_pdn, status_ukm
ORDER BY total_pagu_triliun DESC;
```

### Query 3: Trend per Bulan

```sql
SELECT
    strftime(tgl_pengumuman_paket, '%Y-%m') as bulan,
    COUNT(*) as jumlah_paket,
    SUM(pagu) / 1e9 as total_pagu_miliar
FROM 'datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet'
WHERE tgl_pengumuman_paket IS NOT NULL
GROUP BY bulan
ORDER BY bulan;
```

## 🎓 Jalur Pembelajaran

### Untuk Pemula:
1. Mulai dengan Jupyter notebook untuk memahami data
2. Pelajari operasi dasar Pandas
3. Coba modifikasi visualisasi
4. Eksplorasi dashboard untuk inspirasi

### Untuk Intermediate:
1. Tambahkan analisis baru di notebook
2. Buat visualisasi custom dengan Plotly
3. Modifikasi dashboard (tambah tab/fitur baru)
4. Eksperimen dengan query DuckDB

### Untuk Advanced:
1. Implementasikan analitik lanjutan (time series, clustering)
2. Tambahkan prediksi machine learning
3. Deploy dashboard ke cloud (Streamlit Cloud)
4. Buat sistem pelaporan otomatis

## 📚 Langkah Selanjutnya

1. **Pelajari Dokumentasi**:
   - [datasets/rup/README.md](datasets/rup/README.md) - Detail dataset
   - [README.md](README.md) - Syllabus bootcamp lengkap

2. **Eksperimen**:
   - Modifikasi query di notebook
   - Tambah filter baru di dashboard
   - Buat visualisasi custom

3. **Bangun Sendiri**:
   - Gunakan dataset lain
   - Buat dashboard untuk kasus penggunaan berbeda
   - Bagikan hasil analisis Anda

## 🆘 Butuh Bantuan?

- Cek dokumentasi di [README.md](README.md)
- Review info dataset di [datasets/rup/README.md](datasets/rup/README.md)
- Cari pesan error secara online
- Tanya instruktur/mentor di bootcamp

---

**Selamat Menganalisis! 📊🎉**
