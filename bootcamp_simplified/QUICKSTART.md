# 🚀 Quick Start Guide

Panduan cepat untuk memulai bootcamp.

## ⚡ Setup Cepat (5 menit)

### 1. Install Dependencies

```bash
# Navigasi ke folder bootcamp_simplified
cd bootcamp_simplified

# Install semua package yang dibutuhkan
pip install -r requirements.txt
```

### 2. Verifikasi Installation

```bash
# Test Python & packages
python -c "import pandas, duckdb, plotly, streamlit; print('✅ All packages installed!')"
```

### 3. Mulai Belajar!

#### Untuk Day 1 (Notebooks):

```bash
# Jalankan Jupyter
jupyter notebook

# Buka file ini secara berurutan:
# Session 1 (120 menit):
#   1. day1/session1_pandas_basics/notebooks/01_pandas_fundamental.ipynb
#
# Session 2 (120 menit):
#   2. day1/session2_duckdb_basics/notebooks/02_duckdb_fundamental.ipynb (60 menit)
#   3. day1/session3_visualization_basics/notebooks/03_visualization_fundamental.ipynb (60 menit)
```

#### Untuk Day 2 (Streamlit - Full Day):

```bash
# Session 3: Streamlit Basics (120 menit)
cd day2/session3_streamlit_basics
streamlit run app_part1.py

# Session 4: Dashboard Complete (120 menit)
cd day2/session4_streamlit_complete
streamlit run app_complete.py

# Dashboard akan terbuka di browser
# URL: http://localhost:8501
```

---

## 📁 Struktur Folder

```
bootcamp_simplified/
├── README.md                          # Dokumentasi lengkap
├── QUICKSTART.md                      # Panduan ini
├── requirements.txt                   # Dependencies
│
├── day1/                              # Hari 1: Data Analysis (4 jam)
│   ├── session1_pandas_basics/        # 120 menit
│   │   └── notebooks/
│   │       └── 01_pandas_fundamental.ipynb
│   ├── session2_duckdb_basics/        # 60 menit
│   │   └── notebooks/
│   │       └── 02_duckdb_fundamental.ipynb
│   └── session3_visualization_basics/ # 60 menit
│       └── notebooks/
│           └── 03_visualization_fundamental.ipynb
│
└── day2/                              # Hari 2: Streamlit Full Day (4 jam)
    ├── session3_streamlit_basics/     # 120 menit
    │   └── app_part1.py
    └── session4_streamlit_complete/   # 120 menit
        └── app_complete.py
```

---

## 📊 Dataset

Dataset RUP sudah tersedia di:
```
../datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet
```

Jika dataset tidak ditemukan, pastikan struktur folder benar.

---

## ⏱️ Jadwal Bootcamp

### Day 1: Data Analysis Fundamentals (4 jam)
- **09:00 - 11:00** Session 1: Pandas Fundamental (120 menit)
  - Load & explore data
  - Seleksi & filtering
  - GroupBy & agregasi
- **11:00 - 11:15** Break ☕
- **11:15 - 13:15** Session 2: DuckDB & Visualization (120 menit)
  - SQL queries (60 menit)
  - Plotly charts (60 menit)
- **13:15 - 14:15** Lunch 🍱
- **14:15 - 14:45** Review & Q&A Day 1
- **14:45 - 15:00** Preview Day 2

### Day 2: Streamlit Dashboard Full Day (4 jam)
- **09:00 - 11:00** Session 3: Streamlit Basics (120 menit)
  - Setup & Layout
  - Widgets (selectbox, slider, checkbox, radio)
  - Metrics & KPI cards
  - Data table
  - Buttons & actions
  - **File:** `day2/session3_streamlit_basics/app_part1.py`
- **11:00 - 11:15** Break ☕
- **11:15 - 13:15** Session 4: Dashboard Complete (120 menit)
  - Tabs & multi-section layout
  - Plotly chart integration
  - Advanced filtering
  - Caching & performance
  - Export (CSV/Excel)
  - **File:** `day2/session4_streamlit_complete/app_complete.py`
- **13:15 - 14:15** Lunch 🍱
- **14:15 - 15:00** Deploy to Streamlit Cloud
  - GitHub setup
  - Deploy configuration
  - Testing & troubleshooting
- **15:00 - 15:30** Final Q&A & Closing

---

## 🆘 Troubleshooting

### Problem: Jupyter tidak bisa dibuka
```bash
# Install jupyter jika belum
pip install jupyter

# Atau gunakan VS Code dengan Jupyter extension
code .
```

### Problem: Dataset not found
```bash
# Cek path dataset
ls ../datasets/rup/

# Jika tidak ada, sesuaikan path di notebooks/app
```

### Problem: Streamlit error
```bash
# Pastikan di folder yang benar
cd day2/session4_streamlit

# Jalankan dengan full path
streamlit run app_simple.py
```

### Problem: Import error
```bash
# Reinstall package yang error
pip install --upgrade <package-name>

# Atau reinstall semua
pip install -r requirements.txt --force-reinstall
```

---

## 💡 Tips

1. **Save your work:** Notebooks auto-save, tapi lebih baik `Ctrl+S` berkala
2. **Clear output:** Jika notebook lambat, `Cell > All Output > Clear`
3. **Restart kernel:** Jika ada error aneh, `Kernel > Restart & Clear Output`
4. **Documentation:** Tekan `Shift+Tab` di function untuk lihat docs
5. **Shortcuts:** `Shift+Enter` untuk run cell, `Esc` untuk command mode

---

## 📚 Resources

- **Cheat Sheets:**
  - [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  - [SQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)

- **Documentation:**
  - [Pandas](https://pandas.pydata.org/docs/)
  - [DuckDB](https://duckdb.org/docs/)
  - [Plotly](https://plotly.com/python/)
  - [Streamlit](https://docs.streamlit.io/)

---

**Selamat Belajar! 🎉**

Jika ada pertanyaan, jangan ragu untuk bertanya!
