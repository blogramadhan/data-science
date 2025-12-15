# 📝 Changelog - Bootcamp Simplified

## Version 2.0 - Streamlit Full Day (Latest)

**Tanggal:** December 15, 2024

### 🎯 Major Changes

#### Restrukturisasi Jadwal
- **Day 1:** Data Analysis Fundamentals (4 jam)
  - Session 1: Pandas (120 menit) ← lebih panjang
  - Session 2: DuckDB + Visualization (120 menit) ← digabung

- **Day 2:** Streamlit Dashboard Full Day (4 jam) ← NEW!
  - Session 3: Streamlit Basics (120 menit) ← NEW
  - Session 4: Dashboard Complete (120 menit) ← NEW

#### Perubahan Konten

1. **Session 1: Pandas** (120 menit)
   - Tidak ada perubahan konten
   - Durasi diperpanjang dari 90 → 120 menit

2. **Session 2: DuckDB + Visualization** (120 menit)
   - DuckDB: 60 menit (reduced from 90)
   - Visualization: 60 menit (reduced from 90)
   - Kombinasi 2 session dalam 1 slot

3. **Session 3: Streamlit Basics** (120 menit) ← **NEW**
   - **File:** `day2/session3_streamlit_basics/app_part1.py`
   - **Fokus:**
     - Layout fundamentals (columns, containers, expanders)
     - Semua widgets (text_input, selectbox, multiselect, slider, checkbox, radio)
     - Metrics & KPI cards
     - Data table
     - Buttons & actions
     - Progress bar & status messages
   - **Output:** Aplikasi interaktif dengan filtering lengkap

4. **Session 4: Dashboard Complete** (120 menit) ← **NEW**
   - **File:** `day2/session4_streamlit_complete/app_complete.py`
   - **Fokus:**
     - Tabs untuk multi-section layout
     - Integrasi Plotly charts (pie, bar, line, scatter)
     - Advanced filtering dengan DuckDB-style
     - Caching (@st.cache_data)
     - Export (CSV dengan timestamp)
     - Deploy instructions
   - **Output:** Production-ready dashboard

### 📊 Distribusi Waktu

| Topik | Version 1.0 | Version 2.0 | Change |
|-------|-------------|-------------|--------|
| Pandas | 90 min (11%) | 120 min (15%) | +30 min |
| DuckDB | 90 min (11%) | 60 min (7.5%) | -30 min |
| Visualization | 90 min (11%) | 60 min (7.5%) | -30 min |
| Streamlit | 180 min (22%) | **240 min (30%)** | **+60 min** |
| **Total Streamlit** | 22% | **50% (full day 2)** | **+128%** |

### 🎓 Keunggulan Version 2.0

✅ **Lebih Banyak Hands-on Streamlit**
- Full day 2 dedicated untuk Streamlit
- 2 aplikasi berbeda (progressive learning)
- Dari basics → production-ready

✅ **Progressive Learning**
- Session 3: Fokus pada widgets & layout
- Session 4: Fokus pada charts & advanced features
- Step-by-step, tidak overwhelming

✅ **Realistic untuk Bootcamp**
- Day 1: Data analysis basics (cukup untuk foundation)
- Day 2: Full focus pada building dashboard
- Peserta pulang dengan 2 dashboard

✅ **Production-Ready Output**
- Session 4 dashboard siap deploy
- Include caching, export, dan best practices
- Ready untuk portfolio

### 📁 New File Structure

```
bootcamp_simplified/
├── day1/
│   ├── session1_pandas_basics/        # 120 min
│   ├── session2_duckdb_basics/        # 60 min
│   └── session3_visualization_basics/ # 60 min
│
└── day2/
    ├── session3_streamlit_basics/     # 120 min ← NEW!
    │   └── app_part1.py
    └── session4_streamlit_complete/   # 120 min ← NEW!
        └── app_complete.py
```

### 🔄 Migration from Version 1.0

Jika Anda menggunakan version 1.0:

1. **Tidak perlu perubahan** untuk Day 1 notebooks
2. **Day 2:** Gunakan 2 file baru:
   - `session3_streamlit_basics/app_part1.py` (basics)
   - `session4_streamlit_complete/app_complete.py` (complete)
3. **Old file:** `session4_streamlit/app_simple.py` → archived

### 📌 Breaking Changes

- ❌ Removed: `day2/session4_streamlit/app_simple.py`
- ✅ Added: `day2/session3_streamlit_basics/app_part1.py`
- ✅ Added: `day2/session4_streamlit_complete/app_complete.py`

---

## Version 1.0 - Initial Release

**Tanggal:** December 15, 2024

### Features

- 4 sessions: Pandas, DuckDB, Visualization, Streamlit
- Equal time distribution (90 min each for day 1)
- Single Streamlit app (simplified)

### File Structure

```
bootcamp_simplified/
├── day1/
│   ├── session1_pandas_basics/
│   ├── session2_duckdb_basics/
│   └── session3_visualization_basics/
└── day2/
    └── session4_streamlit/
        └── app_simple.py
```

---

## Comparison Summary

| Aspect | V1.0 | V2.0 |
|--------|------|------|
| Day 1 Sessions | 3 x 90 min | 1 x 120 min + 1 x 120 min (combined) |
| Day 2 Sessions | 1 x 180 min | 2 x 120 min |
| Streamlit Apps | 1 app | 2 apps (progressive) |
| Streamlit Time | 180 min (22%) | 240 min (50%) |
| Focus | Balanced | Streamlit-heavy |
| Output | 1 simple dashboard | 2 dashboards (basic + complete) |

---

**Recommendation:** Use Version 2.0 for bootcamps yang fokus pada dashboard building dan deployment.
