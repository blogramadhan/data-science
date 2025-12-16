"""
Session 4: Streamlit Dashboard Complete
Dashboard RUP 2025 - Production Ready

Fokus: Tabs, Charts, Filtering, Caching, Export, Deploy
Durasi: 120 menit
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from pathlib import Path

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Dashboard RUP 2025 - Complete",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# CUSTOM CSS
# ========================================
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# LOAD DATA with CACHING
# ========================================
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_data():
    """Load RUP data with caching"""
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    data_path = project_root / 'datasets' / 'rup' / 'RUP-PaketPenyedia-Terumumkan-2025.parquet'

    if not data_path.exists():
        st.error(f"Dataset not found at {data_path}")
        st.stop()

    df = pd.read_parquet(data_path)
    # Convert date column
    df['tgl_pengumuman_paket'] = pd.to_datetime(df['tgl_pengumuman_paket'])
    return df

# Load data with progress
with st.spinner('⏳ Loading data...'):
    df = load_data()

# ========================================
# HEADER
# ========================================
st.markdown('<h1 class="main-header">📊 Dashboard RUP 2025 - Production Ready</h1>', unsafe_allow_html=True)
st.markdown("Dashboard lengkap untuk analisis dan monitoring Rencana Umum Pengadaan")
st.markdown("---")

# ========================================
# SIDEBAR FILTERS
# ========================================
st.sidebar.header("🔍 Filter Data")

# Metode filter
st.sidebar.subheader("Metode Pengadaan")
metode_options = ['Semua'] + sorted(df['metode_pengadaan'].unique().tolist())
selected_metode = st.sidebar.selectbox('', metode_options, key='metode')

# Jenis filter
st.sidebar.subheader("Jenis Pengadaan")
jenis_options = ['Semua'] + sorted(df['jenis_pengadaan'].dropna().unique().tolist())
selected_jenis = st.sidebar.selectbox('', jenis_options, key='jenis')

# Satker filter (top 20 only for performance)
st.sidebar.subheader("Satuan Kerja")
top_satkers = df['nama_satker'].value_counts().head(20).index.tolist()
satker_options = ['Semua'] + sorted(top_satkers)
selected_satker = st.sidebar.selectbox('', satker_options, key='satker')

# Pagu range
st.sidebar.subheader("Range Pagu")
min_pagu = float(df['pagu'].min())
max_pagu = float(df['pagu'].max())
pagu_range = st.sidebar.slider(
    'Dalam Miliar Rp:',
    min_value=min_pagu/1e9,
    max_value=max_pagu/1e9,
    value=(min_pagu/1e9, max_pagu/1e9),
    format="%.2f"
)

# Status filters
st.sidebar.subheader("Status Khusus")
show_pdn = st.sidebar.checkbox('Hanya PDN', False)
show_ukm = st.sidebar.checkbox('Hanya UKM', False)
show_pradipa = st.sidebar.checkbox('Hanya PRADIPA', False)

# ========================================
# APPLY FILTERS
# ========================================
@st.cache_data
def apply_filters(_df, metode, jenis, satker, pagu_min, pagu_max, pdn, ukm, pradipa):
    """Apply filters with caching"""
    filtered = _df.copy()

    if metode != 'Semua':
        filtered = filtered[filtered['metode_pengadaan'] == metode]

    if jenis != 'Semua':
        filtered = filtered[filtered['jenis_pengadaan'] == jenis]

    if satker != 'Semua':
        filtered = filtered[filtered['nama_satker'] == satker]

    filtered = filtered[
        (filtered['pagu'] >= pagu_min * 1e9) &
        (filtered['pagu'] <= pagu_max * 1e9)
    ]

    if pdn:
        filtered = filtered[filtered['status_pdn'] == 'PDN']

    if ukm:
        filtered = filtered[filtered['status_ukm'] == 'UKM']

    if pradipa:
        filtered = filtered[filtered['status_pradipa'] == 'PraDIPA']

    return filtered

filtered_df = apply_filters(
    df, selected_metode, selected_jenis, selected_satker,
    pagu_range[0], pagu_range[1],
    show_pdn, show_ukm, show_pradipa
)

# Check if empty
if len(filtered_df) == 0:
    st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih.")
    st.info("💡 Coba sesuaikan filter di sidebar")
    st.stop()

# ========================================
# KEY METRICS
# ========================================
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_paket = len(filtered_df)
    pct = (total_paket / len(df) * 100)
    st.metric(
        label="Total Paket",
        value=f"{total_paket:,}",
        delta=f"{pct:.1f}% dari total"
    )

with col2:
    total_pagu = filtered_df['pagu'].sum()
    pct_pagu = (total_pagu / df['pagu'].sum() * 100)
    st.metric(
        label="Total Pagu",
        value=f"Rp {total_pagu/1e12:.2f} T",
        delta=f"{pct_pagu:.1f}% dari total"
    )

with col3:
    avg_pagu = filtered_df['pagu'].mean()
    st.metric(
        label="Rata-rata Pagu",
        value=f"Rp {avg_pagu/1e6:.2f} Jt"
    )

with col4:
    total_satker = filtered_df['nama_satker'].nunique()
    st.metric(
        label="Jumlah Satker",
        value=f"{total_satker:,}"
    )

st.markdown("---")

# ========================================
# TABS FOR DIFFERENT ANALYSES
# ========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview & Distribution",
    "🏢 Top Satker",
    "📅 Trend Analysis",
    "📋 Data Table & Export"
])

# ========================================
# TAB 1: Overview
# ========================================
with tab1:
    st.header("Overview & Distribution")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribusi Metode Pengadaan")
        metode_count = filtered_df['metode_pengadaan'].value_counts()
        fig = px.pie(
            values=metode_count.values,
            names=metode_count.index,
            title='',
            hole=0.3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Distribusi Jenis Pengadaan")
        jenis_count = filtered_df['jenis_pengadaan'].value_counts().head(5)
        fig = px.bar(
            x=jenis_count.index,
            y=jenis_count.values,
            labels={'x': 'Jenis', 'y': 'Jumlah Paket'},
            color=jenis_count.values,
            color_continuous_scale='Blues'
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # Status Distribution
    st.subheader("Distribusi Status Khusus")
    status_data = {
        'Status': ['PDN', 'UKM', 'PRADIPA'],
        'Ya': [
            (filtered_df['status_pdn'] == 'PDN').sum(),
            (filtered_df['status_ukm'] == 'UKM').sum(),
            (filtered_df['status_pradipa'] == 'PraDIPA').sum()
        ],
        'Tidak': [
            (filtered_df['status_pdn'] != 'PDN').sum(),
            (filtered_df['status_ukm'] != 'UKM').sum(),
            (filtered_df['status_pradipa'] != 'PraDIPA').sum()
        ]
    }

    fig = go.Figure(data=[
        go.Bar(name='Ya', x=status_data['Status'], y=status_data['Ya']),
        go.Bar(name='Tidak', x=status_data['Status'], y=status_data['Tidak'])
    ])
    fig.update_layout(barmode='stack', height=400)
    st.plotly_chart(fig, use_container_width=True)

# ========================================
# TAB 2: Top Satker
# ========================================
with tab2:
    st.header("Top Satuan Kerja")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Berdasarkan Jumlah Paket")
        top_satker_count = filtered_df['nama_satker'].value_counts().head(10)
        fig = px.bar(
            y=top_satker_count.index,
            x=top_satker_count.values,
            orientation='h',
            labels={'x': 'Jumlah Paket', 'y': 'Satker'},
            color=top_satker_count.values,
            color_continuous_scale='Viridis'
        )
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Berdasarkan Total Pagu")
        top_satker_pagu = filtered_df.groupby('nama_satker')['pagu'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(
            y=top_satker_pagu.index,
            x=top_satker_pagu.values / 1e9,
            orientation='h',
            labels={'x': 'Total Pagu (Miliar Rp)', 'y': 'Satker'},
            color=top_satker_pagu.values,
            color_continuous_scale='RdYlGn'
        )
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # Detailed table
    st.subheader("Detail Statistik Satker")
    satker_stats = filtered_df.groupby('nama_satker').agg({
        'pagu': ['count', 'sum', 'mean']
    }).round(2)
    satker_stats.columns = ['Jumlah Paket', 'Total Pagu', 'Rata-rata Pagu']
    satker_stats['Total Pagu (M)'] = (satker_stats['Total Pagu'] / 1e9).round(2)
    satker_stats['Rata-rata (Jt)'] = (satker_stats['Rata-rata Pagu'] / 1e6).round(2)
    satker_stats = satker_stats.sort_values('Total Pagu', ascending=False).head(15)

    st.dataframe(
        satker_stats[['Jumlah Paket', 'Total Pagu (M)', 'Rata-rata (Jt)']],
        use_container_width=True
    )

# ========================================
# TAB 3: Trend
# ========================================
with tab3:
    st.header("Trend Analysis")

    # Monthly trend
    monthly_data = filtered_df.copy()
    monthly_data['bulan'] = monthly_data['tgl_pengumuman_paket'].dt.to_period('M').astype(str)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tren Jumlah Paket per Bulan")
        monthly_count = monthly_data.groupby('bulan').size().reset_index(name='jumlah')
        fig = px.line(
            monthly_count,
            x='bulan',
            y='jumlah',
            markers=True,
            labels={'bulan': 'Bulan', 'jumlah': 'Jumlah Paket'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Tren Total Pagu per Bulan")
        monthly_pagu = monthly_data.groupby('bulan')['pagu'].sum().reset_index()
        monthly_pagu['pagu_miliar'] = monthly_pagu['pagu'] / 1e9
        fig = px.bar(
            monthly_pagu,
            x='bulan',
            y='pagu_miliar',
            labels={'bulan': 'Bulan', 'pagu_miliar': 'Total Pagu (Miliar Rp)'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    # Cumulative trend
    st.subheader("Kumulatif Pengumuman Paket")
    monthly_count['kumulatif'] = monthly_count['jumlah'].cumsum()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_count['bulan'],
        y=monthly_count['kumulatif'],
        mode='lines+markers',
        name='Kumulatif',
        fill='tozeroy'
    ))
    fig.update_layout(
        xaxis_title="Bulan",
        yaxis_title="Jumlah Paket (Kumulatif)",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ========================================
# TAB 4: Data Table & Export
# ========================================
with tab4:
    st.header("Data Table & Export")

    # Display options
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Menampilkan **{len(filtered_df):,}** paket dari total **{len(df):,}** paket")
    with col2:
        num_rows = st.selectbox("Rows to display:", [50, 100, 200, 500], index=0)

    # Prepare display data
    display_cols = ['nama_paket', 'pagu', 'metode_pengadaan', 'jenis_pengadaan', 'nama_satker', 'status_pdn', 'status_ukm']
    display_df = filtered_df[display_cols].copy()
    display_df['pagu_formatted'] = display_df['pagu'].apply(lambda x: f"Rp {x/1e9:.2f} M")

    # Data table
    st.dataframe(
        display_df[['nama_paket', 'pagu_formatted', 'metode_pengadaan', 'jenis_pengadaan', 'nama_satker', 'status_pdn', 'status_ukm']].head(num_rows),
        use_container_width=True,
        height=500
    )

    # Export section
    st.subheader("📥 Export Data")
    col1, col2, col3 = st.columns(3)

    with col1:
        # CSV export
        csv = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"rup_filtered_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:
        # Summary stats export
        summary = pd.DataFrame({
            'Metric': ['Total Paket', 'Total Pagu (T)', 'Avg Pagu (Jt)', 'Total Satker'],
            'Value': [
                len(filtered_df),
                f"{filtered_df['pagu'].sum() / 1e12:.2f}",
                f"{filtered_df['pagu'].mean() / 1e6:.2f}",
                filtered_df['nama_satker'].nunique()
            ]
        })
        csv_summary = summary.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Summary",
            data=csv_summary,
            file_name=f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col3:
        if st.button("🔄 Reset All Filters", type="primary", use_container_width=True):
            st.rerun()

# ========================================
# FOOTER
# ========================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><strong>Dashboard RUP 2025 - Production Ready</strong></p>
        <p>Session 4: Streamlit Dashboard Complete | Bootcamp Data Science</p>
        <p>Data Source: Sistem Informasi Rencana Umum Pengadaan</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar footer
with st.sidebar:
    st.markdown("---")
    st.subheader("ℹ️ Tentang Dashboard")
    st.info("""
    Dashboard ini menampilkan analisis komprehensif data RUP 2025 menggunakan:

    - **Pandas**: Data manipulation
    - **Plotly**: Interactive visualization
    - **Streamlit**: Web dashboard

    Gunakan filter di atas untuk menyesuaikan tampilan data.
    """)

    st.markdown("---")
    st.subheader("🚀 Deploy")
    st.write("""
    **Cara deploy ke Streamlit Cloud:**
    1. Push code ke GitHub
    2. Buka streamlit.io/cloud
    3. Connect repository
    4. Deploy!
    """)
