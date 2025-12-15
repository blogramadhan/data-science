# 📝 Catatan Perubahan - Bootcamp Simplified

## Versi 2.0 - Streamlit Full Day (Terbaru)

**Tanggal:** 15 Desember 2024

### 🎯 Perubahan Utama

#### Restrukturisasi Jadwal
- **Hari 1:** Dasar Analisis Data (4 jam)  
  - Sesi 1: Pandas (120 menit) ← durasi lebih panjang  
  - Sesi 2: DuckDB + Visualisasi (120 menit) ← digabung

- **Hari 2:** Dashboard Streamlit Full Day (4 jam) ← BARU  
  - Sesi 3: Dasar Streamlit (120 menit) ← BARU  
  - Sesi 4: Dashboard Lengkap (120 menit) ← BARU

#### Pembaruan Konten

1. **Sesi 1: Pandas** (120 menit)  
   - Konten tetap  
   - Durasi dari 90 → 120 menit

2. **Sesi 2: DuckDB + Visualisasi** (120 menit)  
   - DuckDB: 60 menit (dari 90)  
   - Visualisasi: 60 menit (dari 90)  
   - Dua sesi digabung menjadi satu slot

3. **Sesi 3: Dasar Streamlit** (120 menit) ← **BARU**  
   - **File:** `day2/session3_streamlit_basics/app_part1.py`  
   - **Fokus:** layout (columns, containers, expanders), semua widget (text_input, selectbox, multiselect, slider, checkbox, radio), metrics & KPI, data table, tombol & aksi, progress/status  
   - **Output:** Aplikasi interaktif dengan filtering lengkap

4. **Sesi 4: Dashboard Lengkap** (120 menit) ← **BARU**  
   - **File:** `day2/session4_streamlit_complete/app_complete.py`  
   - **Fokus:** tabs multi-section, integrasi chart Plotly (pie, bar, line, scatter), filtering ala DuckDB, caching (@st.cache_data), ekspor CSV dengan timestamp, panduan deploy  
   - **Output:** Dashboard siap produksi

### 📊 Distribusi Waktu

| Topik | Versi 1.0 | Versi 2.0 | Perubahan |
|-------|-----------|-----------|-----------|
| Pandas | 90 menit (11%) | 120 menit (15%) | +30 menit |
| DuckDB | 90 menit (11%) | 60 menit (7,5%) | -30 menit |
| Visualisasi | 90 menit (11%) | 60 menit (7,5%) | -30 menit |
| Streamlit | 180 menit (22%) | **240 menit (30%)** | **+60 menit** |
| **Total Streamlit** | 22% | **50% (full day 2)** | **+128%** |

### 🎓 Keunggulan Versi 2.0

✅ **Lebih banyak praktik Streamlit**  
- Hari kedua penuh untuk Streamlit  
- 2 aplikasi berbeda (pembelajaran progresif)  
- Dari dasar → siap produksi  

✅ **Progressive learning**  
- Sesi 3: Fokus widget & layout  
- Sesi 4: Fokus chart & fitur lanjut  
- Step-by-step, tidak overwhelming  

✅ **Realistis untuk bootcamp**  
- Hari 1: Fondasi analisis data  
- Hari 2: Full fokus membangun dashboard  
- Peserta pulang dengan 2 dashboard  

✅ **Output siap produksi**  
- Dashboard Sesi 4 siap deploy  
- Sudah termasuk caching, ekspor, best practice  
- Cocok untuk portofolio

### 📁 Struktur File Baru

```
bootcamp_simplified/
├── day1/
│   ├── session1_pandas_basics/        # 120 menit
│   ├── session2_duckdb_basics/        # 60 menit
│   └── session3_visualization_basics/ # 60 menit
│
└── day2/
    ├── session3_streamlit_basics/     # 120 menit ← BARU!
    │   └── app_part1.py
    └── session4_streamlit_complete/   # 120 menit ← BARU!
        └── app_complete.py
```

### 🔄 Migrasi dari Versi 1.0

Jika Anda masih memakai versi 1.0:

1. **Tidak ada perubahan** untuk notebook Hari 1  
2. **Hari 2:** Gunakan 2 file baru:  
   - `session3_streamlit_basics/app_part1.py` (dasar)  
   - `session4_streamlit_complete/app_complete.py` (lengkap)  
3. **File lama:** `session4_streamlit/app_simple.py` → diarsipkan

### 📌 Breaking Changes

- ❌ Dihapus: `day2/session4_streamlit/app_simple.py`  
- ✅ Ditambah: `day2/session3_streamlit_basics/app_part1.py`  
- ✅ Ditambah: `day2/session4_streamlit_complete/app_complete.py`

---

## Versi 1.0 - Rilis Awal

**Tanggal:** 15 Desember 2024

### Fitur

- 4 sesi: Pandas, DuckDB, Visualisasi, Streamlit  
- Distribusi waktu seimbang (90 menit per sesi hari 1)  
- Satu aplikasi Streamlit (simplified)

### Struktur File

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

## Ringkasan Perbandingan

| Aspek | Versi 1.0 | Versi 2.0 |
|-------|-----------|-----------|
| Sesi Hari 1 | 3 x 90 menit | 1 x 120 menit + 1 x 120 menit (digabung) |
| Sesi Hari 2 | 1 x 180 menit | 2 x 120 menit |
| Aplikasi Streamlit | 1 aplikasi | 2 aplikasi (progresif) |
| Waktu Streamlit | 180 menit (22%) | 240 menit (50%) |
| Fokus | Seimbang | Lebih berat ke Streamlit |
| Output | 1 dashboard sederhana | 2 dashboard (basic + complete) |

---

**Rekomendasi:** Gunakan Versi 2.0 untuk bootcamp yang menekankan pembuatan dashboard dan deployment.
