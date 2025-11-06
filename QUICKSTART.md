# 🚀 Quick Start Guide - Analisis RUP 2025

Panduan cepat untuk menjalankan project analisis data RUP 2025.

## Prerequisites

- Python 3.12+ terinstall
- UV package manager ([Install uv](https://github.com/astral-sh/uv))
- Git (optional, untuk clone repository)

## Step 1: Setup Project

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

## Step 2: Verifikasi Instalasi

```bash
# Test import libraries
uv run python -c "import pandas, duckdb, streamlit, plotly; print('✅ All libraries installed!')"
```

## Step 3: Eksplorasi Data dengan Jupyter

### Opsi A: Via Browser (Recommended)

```bash
# Start Jupyter Notebook server
uv run jupyter notebook
```

Browser akan terbuka otomatis. Navigate ke:
```
day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb
```

### Opsi B: Via JupyterLab

```bash
# Install jupyterlab jika belum
uv pip install jupyterlab

# Start JupyterLab
uv run jupyter lab
```

## Step 4: Jalankan Streamlit Dashboard

```bash
# Jalankan dashboard interaktif
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

Dashboard akan terbuka di browser: http://localhost:8501

### Features Dashboard:
- 📊 Overview Data RUP
- 💰 Analisis Pagu
- 🏛️ Analisis K/L/PD
- 📋 Metode & Jenis Pengadaan
- 📅 Timeline Analysis
- 🔍 Interactive Filters
- 📥 Export Data

## Step 5: Eksplorasi Dataset

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

## 📁 File Structure

```
day1/session1_python_pandas/notebooks/
└── 01_exploratory_data_analysis_rup.ipynb    # EDA lengkap dengan visualisasi

day2/session5_streamlit/apps/
└── rup_dashboard.py                           # Dashboard interaktif

datasets/rup/
├── RUP-PaketPenyedia-Terumumkan-2025.parquet # Data source
└── README.md                                  # Dokumentasi dataset
```

## Troubleshooting

### Issue: Module not found

```bash
# Reinstall dependencies
uv sync --refresh
```

### Issue: Jupyter tidak muncul

```bash
# Install jupyter explicitly
uv pip install jupyter notebook

# Jalankan dengan full path
uv run jupyter notebook
```

### Issue: Streamlit error

```bash
# Check streamlit version
uv pip list | grep streamlit

# Reinstall jika perlu
uv pip install --force-reinstall streamlit
```

### Issue: Cannot read parquet file

Pastikan file ada di lokasi yang benar:
```bash
ls -lh datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet
```

### Issue: Port 8501 already in use

```bash
# Gunakan port lain
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py --server.port 8502
```

## 💡 Tips & Tricks

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

## 📊 Sample Analysis Queries

### Query 1: Top 10 Paket Terbesar

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

## 🎓 Learning Path

### Untuk Pemula:
1. Mulai dengan Jupyter notebook untuk memahami data
2. Pelajari basic Pandas operations
3. Coba modifikasi visualisasi
4. Explore dashboard untuk inspiration

### Untuk Intermediate:
1. Tambahkan analisis baru di notebook
2. Buat visualisasi custom dengan Plotly
3. Modifikasi dashboard (add new tabs/features)
4. Eksperimen dengan DuckDB queries

### Untuk Advanced:
1. Implement advanced analytics (time series, clustering)
2. Add machine learning predictions
3. Deploy dashboard ke cloud (Streamlit Cloud)
4. Create automated reporting system

## 📚 Next Steps

1. **Pelajari Documentation**:
   - [datasets/rup/README.md](datasets/rup/README.md) - Detail dataset
   - [README.md](README.md) - Syllabus bootcamp lengkap

2. **Eksperimen**:
   - Modifikasi queries di notebook
   - Tambah filter baru di dashboard
   - Buat visualisasi custom

3. **Build Your Own**:
   - Gunakan dataset lain
   - Buat dashboard untuk use case berbeda
   - Share hasil analisis Anda

## 🆘 Need Help?

- Check documentation di [README.md](README.md)
- Review dataset info di [datasets/rup/README.md](datasets/rup/README.md)
- Search error messages online
- Ask instructor/mentor di bootcamp

---

**Happy Analyzing! 📊🎉**
