# Dataset RUP (Rencana Umum Pengadaan) 2025

## Tentang Dataset

Dataset ini berisi informasi **Rencana Umum Pengadaan (RUP) Paket Penyedia yang Terumumkan untuk tahun anggaran 2025**.

### Apa itu RUP?

RUP adalah daftar rencana pengadaan barang/jasa yang akan dilaksanakan oleh Kementerian/Lembaga/Pemerintah Daerah (K/L/PD) selama 1 (satu) tahun anggaran yang berpedoman pada Rencana Kerja dan Anggaran.

## Informasi Dataset

- **Filename**: `RUP-PaketPenyedia-Terumumkan-2025.parquet`
- **Format**: Apache Parquet
- **Total Records**: 16,430 paket pengadaan
- **Total Kolom**: 48 kolom
- **Size**: ~1.3 MB (compressed)

## Struktur Data

### Kolom Utama

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `tahun_anggaran` | integer | Tahun anggaran pengadaan |
| `kd_klpd` | string | Kode K/L/PD |
| `nama_klpd` | string | Nama K/L/PD |
| `jenis_klpd` | string | Jenis K/L/PD (Kementerian/Lembaga/Pemda) |
| `kd_satker` | integer | Kode Satuan Kerja |
| `nama_satker` | string | Nama Satuan Kerja |
| `kd_rup` | string | Kode RUP unik |
| `nama_paket` | string | Nama paket pengadaan |
| `pagu` | float | Nilai pagu pengadaan (Rupiah) |
| `metode_pengadaan` | string | Metode pengadaan yang digunakan |
| `jenis_pengadaan` | string | Jenis pengadaan (Barang/Jasa/Konstruksi) |
| `status_pradipa` | string | Status PRADIPA (Ya/Tidak) |
| `status_pdn` | string | Status Produk Dalam Negeri |
| `status_ukm` | string | Status untuk UKM |
| `status_konsolidasi` | string | Status konsolidasi paket |
| `volume_pekerjaan` | string | Volume pekerjaan |
| `uraian_pekerjaan` | string | Uraian detail pekerjaan |
| `spesifikasi_pekerjaan` | string | Spesifikasi teknis |
| `tgl_awal_pemilihan` | datetime | Tanggal awal pemilihan penyedia |
| `tgl_akhir_pemilihan` | datetime | Tanggal akhir pemilihan penyedia |
| `tgl_awal_kontrak` | datetime | Tanggal mulai kontrak |
| `tgl_akhir_kontrak` | datetime | Tanggal berakhir kontrak |
| `tgl_buat_paket` | datetime | Tanggal pembuatan paket |
| `tgl_pengumuman_paket` | datetime | Tanggal pengumuman paket |
| `nip_ppk` | string | NIP Pejabat Pembuat Komitmen |
| `nama_ppk` | string | Nama PPK |
| `status_aktif_rup` | string | Status aktif RUP |
| `status_umumkan_rup` | string | Status pengumuman RUP |

## Statistik Dataset

### Overview
- **Total Pagu**: ~Rp XX Triliun
- **Rata-rata Pagu per Paket**: ~Rp XX Miliar
- **Jumlah K/L/PD**: XX instansi
- **Jumlah Satker**: XX satuan kerja

### Distribusi Status
- **PDN (Produk Dalam Negeri)**: XX% paket
- **UKM (Usaha Kecil Menengah)**: XX% paket
- **PRADIPA**: XX% paket

## Use Cases

Dataset ini dapat digunakan untuk berbagai analisis, antara lain:

1. **Analisis Spending**: Menganalisis pola belanja pemerintah
2. **Transparansi Pengadaan**: Monitoring transparansi proses pengadaan
3. **Analisis Kompetisi**: Melihat tingkat kompetisi per metode pengadaan
4. **Partisipasi UKM**: Mengukur partisipasi UKM dalam pengadaan
5. **Penggunaan PDN**: Analisis penggunaan produk dalam negeri
6. **Efisiensi Pengadaan**: Mengevaluasi efisiensi waktu dan biaya
7. **Prediksi Trend**: Forecasting trend pengadaan
8. **Regional Analysis**: Analisis per wilayah/instansi

## Cara Menggunakan

### 1. Load Data dengan Pandas

```python
import pandas as pd

# Load parquet file
df = pd.read_parquet('RUP-PaketPenyedia-Terumumkan-2025.parquet')

# Display info
print(df.info())
print(df.head())
```

### 2. Query dengan DuckDB

```python
import duckdb

# Create connection
conn = duckdb.connect(':memory:')

# Query data
result = conn.execute("""
    SELECT
        nama_klpd,
        COUNT(*) as jumlah_paket,
        SUM(pagu) as total_pagu
    FROM 'RUP-PaketPenyedia-Terumumkan-2025.parquet'
    GROUP BY nama_klpd
    ORDER BY total_pagu DESC
    LIMIT 10
""").df()

print(result)
```

### 3. Analisis dengan Streamlit

Jalankan dashboard interaktif:

```bash
streamlit run ../../day2/session5_streamlit/apps/rup_dashboard.py
```

## Contoh Analisis

### Query 1: Top 10 K/L/PD by Pagu

```sql
SELECT
    nama_klpd,
    COUNT(*) as total_paket,
    SUM(pagu) as total_pagu,
    AVG(pagu) as rata_rata_pagu
FROM rup
GROUP BY nama_klpd
ORDER BY total_pagu DESC
LIMIT 10;
```

### Query 2: Analisis Metode Pengadaan

```sql
SELECT
    metode_pengadaan,
    COUNT(*) as jumlah_paket,
    SUM(pagu) as total_pagu,
    AVG(pagu) as rata_pagu
FROM rup
GROUP BY metode_pengadaan
ORDER BY jumlah_paket DESC;
```

### Query 3: Trend Pengumuman per Bulan

```sql
SELECT
    EXTRACT(MONTH FROM tgl_pengumuman_paket) as bulan,
    COUNT(*) as jumlah_paket,
    SUM(pagu) as total_pagu
FROM rup
WHERE tgl_pengumuman_paket IS NOT NULL
GROUP BY bulan
ORDER BY bulan;
```

## Data Quality Notes

### Missing Values
Beberapa kolom memiliki missing values yang perlu diperhatikan:
- `spesifikasi_pekerjaan`: ~XX% missing
- `alasan_non_ukm`: ~XX% missing
- `alasan_dikecualikan`: ~XX% missing
- `nomor_kontrak`: ~XX% missing (normal untuk paket yang belum kontrak)

### Data Cleaning Recommendations
1. Handle missing values pada kolom penting
2. Konversi kolom tanggal ke datetime
3. Normalisasi nilai pagu (remove outliers jika perlu)
4. Standardisasi nama K/L/PD (ada variasi penulisan)
5. Validasi range tanggal (pastikan logis)

## Catatan Penting

1. **Confidentiality**: Data ini adalah data publik yang telah diumumkan
2. **Updates**: Data di-update secara berkala oleh sumber
3. **Accuracy**: Selalu validasi dengan sumber resmi untuk keputusan penting
4. **Completeness**: Beberapa paket mungkin belum lengkap informasinya

## Sumber Data

- **Portal**: Sistem Informasi Rencana Umum Pengadaan (SIRUP)
- **Website**: https://sirup.lkpp.go.id/
- **Instansi**: Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah (LKPP)

## Lisensi & Penggunaan

Data RUP adalah data terbuka (open data) yang disediakan oleh pemerintah untuk transparansi pengadaan barang/jasa. Penggunaan data untuk:
- ✅ Analisis
- ✅ Penelitian
- ✅ Monitoring
- ✅ Edukasi

## Kontak & Support

Untuk pertanyaan atau masalah terkait dataset:
- Buka issue di repository
- Hubungi instruktur bootcamp
- Referensi: Dokumentasi SIRUP

---

**Last Updated**: 2025-01-06
**Dataset Version**: 1.0
