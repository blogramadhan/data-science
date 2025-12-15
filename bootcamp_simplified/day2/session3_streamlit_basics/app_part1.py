"""
Session 3: Streamlit Basics - Part 1
Dashboard RUP 2025

Fokus: Layout, Widgets, Metrics, Data Table
Durasi: 120 menit
"""

import streamlit as st
import pandas as pd
from pathlib import Path

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Streamlit Basics - RUP 2025",
    page_icon="📊",
    layout="wide"
)

# ========================================
# LOAD DATA
# ========================================
@st.cache_data
def load_data():
    """Load RUP data"""
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    data_path = project_root / 'datasets' / 'rup' / 'RUP-PaketPenyedia-Terumumkan-2025.parquet'

    if not data_path.exists():
        st.error(f"Dataset not found at {data_path}")
        st.stop()

    df = pd.read_parquet(data_path)
    return df

df = load_data()

# ========================================
# HEADER
# ========================================
st.title("📊 Streamlit Basics - Session 3")
st.markdown("Belajar dasar-dasar Streamlit: Layout, Widgets, dan Interaktivitas")

# Info message
st.info("💡 **Tips:** Gunakan sidebar di sebelah kiri untuk mengatur filter data")

st.markdown("---")

# ========================================
# SIDEBAR WIDGETS
# ========================================
st.sidebar.header("🎛️ Widgets & Filters")

# Text input
st.sidebar.subheader("1. Text Input")
search_term = st.sidebar.text_input(
    "Cari nama paket:",
    placeholder="Contoh: Belanja"
)

# Selectbox
st.sidebar.subheader("2. Selectbox")
metode_options = ['Semua'] + sorted(df['metode_pengadaan'].unique().tolist())
selected_metode = st.sidebar.selectbox(
    'Pilih Metode Pengadaan:',
    metode_options
)

# Multiselect
st.sidebar.subheader("3. Multiselect")
jenis_options = sorted(df['jenis_pengadaan'].dropna().unique().tolist())
selected_jenis = st.sidebar.multiselect(
    'Pilih Jenis Pengadaan (bisa lebih dari 1):',
    jenis_options,
    default=jenis_options[:2]  # Default 2 pertama
)

# Slider
st.sidebar.subheader("4. Slider")
pagu_range = st.sidebar.slider(
    'Range Pagu (Miliar Rp):',
    min_value=0.0,
    max_value=100.0,
    value=(0.0, 100.0),
    step=1.0
)

# Checkbox
st.sidebar.subheader("5. Checkbox")
show_only_high_value = st.sidebar.checkbox(
    'Tampilkan hanya paket > 1 Miliar',
    value=False
)

# Radio button
st.sidebar.subheader("6. Radio Button")
sort_by = st.sidebar.radio(
    "Urutkan berdasarkan:",
    ["Pagu (Tertinggi)", "Pagu (Terendah)", "Nama Paket"]
)

# ========================================
# APPLY FILTERS
# ========================================
filtered_df = df.copy()

# Filter by search term
if search_term:
    filtered_df = filtered_df[
        filtered_df['nama_paket'].str.contains(search_term, case=False, na=False)
    ]

# Filter by metode
if selected_metode != 'Semua':
    filtered_df = filtered_df[filtered_df['metode_pengadaan'] == selected_metode]

# Filter by jenis
if selected_jenis:
    filtered_df = filtered_df[filtered_df['jenis_pengadaan'].isin(selected_jenis)]

# Filter by pagu range
filtered_df = filtered_df[
    (filtered_df['pagu'] >= pagu_range[0] * 1e9) &
    (filtered_df['pagu'] <= pagu_range[1] * 1e9)
]

# Filter high value only
if show_only_high_value:
    filtered_df = filtered_df[filtered_df['pagu'] > 1_000_000_000]

# Apply sorting
if sort_by == "Pagu (Tertinggi)":
    filtered_df = filtered_df.sort_values('pagu', ascending=False)
elif sort_by == "Pagu (Terendah)":
    filtered_df = filtered_df.sort_values('pagu', ascending=True)
else:
    filtered_df = filtered_df.sort_values('nama_paket')

# ========================================
# LAYOUT: COLUMNS
# ========================================
st.header("📊 Key Metrics (Columns Layout)")
st.write("**Contoh penggunaan `st.columns()` untuk layout horizontal**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_paket = len(filtered_df)
    delta = total_paket - len(df)
    st.metric(
        label="Total Paket",
        value=f"{total_paket:,}",
        delta=f"{delta:,} dari semua data"
    )

with col2:
    total_pagu = filtered_df['pagu'].sum()
    st.metric(
        label="Total Pagu",
        value=f"Rp {total_pagu / 1e12:.2f} T"
    )

with col3:
    avg_pagu = filtered_df['pagu'].mean()
    st.metric(
        label="Rata-rata Pagu",
        value=f"Rp {avg_pagu / 1e6:.2f} Jt"
    )

with col4:
    total_satker = filtered_df['nama_satker'].nunique()
    st.metric(
        label="Jumlah Satker",
        value=f"{total_satker:,}"
    )

st.markdown("---")

# ========================================
# LAYOUT: CONTAINERS
# ========================================
st.header("📦 Containers & Expanders")

# Container
with st.container():
    st.subheader("Container Example")
    st.write("Container digunakan untuk mengelompokkan elemen")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Metode Pengadaan:**")
        metode_count = filtered_df['metode_pengadaan'].value_counts().head(5)
        st.dataframe(metode_count, use_container_width=True)

    with col2:
        st.write("**Jenis Pengadaan:**")
        jenis_count = filtered_df['jenis_pengadaan'].value_counts().head(5)
        st.dataframe(jenis_count, use_container_width=True)

st.markdown("---")

# Expander
with st.expander("📖 Lihat Statistik Detail"):
    st.write("**Statistik Pagu:**")
    st.write(f"- Minimum: Rp {filtered_df['pagu'].min():,.0f}")
    st.write(f"- Maksimum: Rp {filtered_df['pagu'].max():,.0f}")
    st.write(f"- Median: Rp {filtered_df['pagu'].median():,.0f}")
    st.write(f"- Std Dev: Rp {filtered_df['pagu'].std():,.0f}")

st.markdown("---")

# ========================================
# DATA TABLE
# ========================================
st.header("📋 Data Table")
st.write(f"Menampilkan **{len(filtered_df):,}** paket dari total **{len(df):,}** paket")

# Pilih kolom yang akan ditampilkan
display_cols = ['nama_paket', 'pagu', 'metode_pengadaan', 'jenis_pengadaan', 'nama_satker']

# Format pagu untuk display
display_df = filtered_df[display_cols].copy()
display_df['pagu_formatted'] = display_df['pagu'].apply(lambda x: f"Rp {x/1e9:.2f} M")

# Tampilkan dataframe
st.dataframe(
    display_df[['nama_paket', 'pagu_formatted', 'metode_pengadaan', 'jenis_pengadaan', 'nama_satker']].head(50),
    use_container_width=True,
    height=400
)

# ========================================
# BUTTONS & ACTIONS
# ========================================
st.markdown("---")
st.header("🎯 Buttons & Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Reset Filters", type="primary"):
        st.rerun()

with col2:
    if st.button("📊 Show Summary"):
        st.balloons()
        st.success(f"""
        **Summary:**
        - Total Paket: {len(filtered_df):,}
        - Total Pagu: Rp {filtered_df['pagu'].sum() / 1e12:.2f} Triliun
        - Metode Terbanyak: {filtered_df['metode_pengadaan'].mode()[0]}
        """)

with col3:
    # Download button
    csv = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="rup_filtered.csv",
        mime="text/csv"
    )

# ========================================
# PROGRESS & STATUS
# ========================================
st.markdown("---")
st.header("⏳ Progress & Status Messages")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Progress Bar")
    progress = len(filtered_df) / len(df)
    st.progress(progress)
    st.write(f"Data yang ditampilkan: {progress * 100:.1f}%")

with col2:
    st.subheader("Status Messages")
    if len(filtered_df) == 0:
        st.error("⚠️ Tidak ada data yang sesuai filter")
    elif len(filtered_df) < 10:
        st.warning("⚡ Data yang ditampilkan sangat sedikit")
    else:
        st.success(f"✅ Menampilkan {len(filtered_df):,} paket")

# ========================================
# FOOTER
# ========================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><strong>Session 3: Streamlit Basics</strong></p>
        <p>Bootcamp Data Analysis | Day 2</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.markdown("---")
    st.subheader("📚 Yang Sudah Dipelajari")
    st.write("""
    ✅ Text Input
    ✅ Selectbox & Multiselect
    ✅ Slider
    ✅ Checkbox & Radio
    ✅ Columns Layout
    ✅ Containers & Expanders
    ✅ Metrics
    ✅ Data Table
    ✅ Buttons
    ✅ Progress Bar
    ✅ Status Messages
    """)

    st.info("💡 **Next:** Session 4 akan menambahkan visualisasi Plotly dan fitur advanced!")
