"""
Dashboard Analisis RUP (Rencana Umum Pengadaan) 2025
Bootcamp Data Analysis - Python, DuckDB & Streamlit
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import duckdb
from datetime import datetime
import numpy as np

# Page config
st.set_page_config(
    page_title="Dashboard RUP 2025",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">📊 Dashboard Analisis RUP 2025</h1>', unsafe_allow_html=True)
st.markdown("---")

# Load data function with caching
@st.cache_data
def load_data():
    """Load RUP data from parquet file"""
    import os
    from pathlib import Path

    # Get the project root directory (3 levels up from this file)
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent.parent.parent
    data_path = project_root / 'datasets' / 'rup' / 'RUP-PaketPenyedia-Terumumkan-2025.parquet'

    df = pd.read_parquet(data_path)

    # Convert date columns
    date_columns = ['tgl_awal_pemilihan', 'tgl_akhir_pemilihan',
                    'tgl_awal_kontrak', 'tgl_akhir_kontrak',
                    'tgl_buat_paket', 'tgl_pengumuman_paket']

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    return df

# Initialize DuckDB connection
@st.cache_resource
def init_duckdb():
    """Initialize DuckDB connection"""
    return duckdb.connect(':memory:')

# Load data
with st.spinner('⏳ Loading data...'):
    df = load_data()
    conn = init_duckdb()

    # Register DataFrame in DuckDB
    conn.register('rup', df)

st.success(f'✅ Data loaded successfully! Total records: {len(df):,}')

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Metode Pengadaan filter
metode_options = ['Semua'] + sorted(df['metode_pengadaan'].dropna().unique().tolist())
selected_metode = st.sidebar.selectbox('Metode Pengadaan', metode_options)

# Jenis Pengadaan filter
jenis_options = ['Semua'] + sorted(df['jenis_pengadaan'].dropna().unique().tolist())
selected_jenis = st.sidebar.selectbox('Jenis Pengadaan', jenis_options)

# Satker filter
satker_options = ['Semua'] + sorted(df['nama_satker'].dropna().unique().tolist())
selected_satker = st.sidebar.selectbox('Satuan Kerja', satker_options, help="Satuan Kerja")

# Pagu range filter
min_pagu = float(df['pagu'].min())
max_pagu = float(df['pagu'].max())
pagu_range = st.sidebar.slider(
    'Range Pagu (Miliar Rp)',
    min_value=min_pagu/1e9,
    max_value=max_pagu/1e9,
    value=(min_pagu/1e9, max_pagu/1e9),
    format="%.2f"
)

# Status filters
st.sidebar.subheader("Status")
show_pdn = st.sidebar.checkbox('Hanya PDN', False)
show_ukm = st.sidebar.checkbox('Hanya UKM', False)
show_pradipa = st.sidebar.checkbox('Hanya PRADIPA', False)

# Apply filters using DuckDB
def apply_filters():
    query = "SELECT * FROM rup WHERE 1=1"

    if selected_metode != 'Semua':
        query += f" AND metode_pengadaan = '{selected_metode}'"

    if selected_jenis != 'Semua':
        query += f" AND jenis_pengadaan = '{selected_jenis}'"

    if selected_satker != 'Semua':
        query += f" AND nama_satker = '{selected_satker}'"

    query += f" AND pagu >= {pagu_range[0] * 1e9} AND pagu <= {pagu_range[1] * 1e9}"

    if show_pdn:
        query += " AND status_pdn = 'PDN'"

    if show_ukm:
        query += " AND status_ukm = 'UKM'"

    if show_pradipa:
        query += " AND status_pradipa = 'PraDIPA'"

    return conn.execute(query).df()

filtered_df = apply_filters()

# Main content
if len(filtered_df) == 0:
    st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih.")
    st.stop()

# Key Metrics
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_paket = len(filtered_df)
    st.metric(
        label="Total Paket",
        value=f"{total_paket:,}",
        delta=f"{(total_paket/len(df)*100):.1f}% dari total"
    )

with col2:
    total_pagu = filtered_df['pagu'].sum()
    st.metric(
        label="Total Pagu",
        value=f"Rp {total_pagu/1e12:.2f} T",
        delta=f"{(total_pagu/df['pagu'].sum()*100):.1f}% dari total"
    )

with col3:
    avg_pagu = filtered_df['pagu'].mean()
    st.metric(
        label="Rata-rata Pagu",
        value=f"Rp {avg_pagu/1e9:.2f} M"
    )

with col4:
    total_satker = filtered_df['nama_satker'].nunique()
    st.metric(
        label="Jumlah Satker",
        value=f"{total_satker:,}"
    )

st.markdown("---")

# Tabs for different analyses
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "💰 Analisis Pagu",
    "🏢 Satuan Kerja",
    "📋 Metode & Jenis",
    "📅 Timeline"
])

with tab1:
    st.header("Overview Data RUP")

    col1, col2 = st.columns(2)

    with col1:
        # Status distribution
        st.subheader("Status Khusus")
        status_data = {
            'Status': ['PDN', 'UKM', 'PRADIPA'],
            'Ya': [
                (filtered_df['status_pdn'] == 'Ya').sum(),
                (filtered_df['status_ukm'] == 'Ya').sum(),
                (filtered_df['status_pradipa'] == 'Ya').sum()
            ],
            'Tidak/Lainnya': [
                (filtered_df['status_pdn'] != 'Ya').sum(),
                (filtered_df['status_ukm'] != 'Ya').sum(),
                (filtered_df['status_pradipa'] != 'Ya').sum()
            ]
        }

        fig = go.Figure(data=[
            go.Bar(name='Ya', x=status_data['Status'], y=status_data['Ya']),
            go.Bar(name='Tidak/Lainnya', x=status_data['Status'], y=status_data['Tidak/Lainnya'])
        ])
        fig.update_layout(
            barmode='stack',
            title='Distribusi Status PDN, UKM, dan PRADIPA',
            xaxis_title='Status',
            yaxis_title='Jumlah Paket',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Top 10 paket berdasarkan pagu
        st.subheader("Top 10 Paket Berdasarkan Pagu")
        top_paket = filtered_df.nlargest(10, 'pagu')[['nama_paket', 'pagu', 'nama_satker']]
        top_paket['pagu_miliar'] = top_paket['pagu'] / 1e9

        fig = px.bar(
            top_paket,
            y='nama_paket',
            x='pagu_miliar',
            orientation='h',
            title='',
            labels={'pagu_miliar': 'Pagu (Miliar Rp)', 'nama_paket': 'Nama Paket'},
            hover_data=['nama_satker']
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # Data table
    st.subheader("📋 Data Tabel")
    display_cols = ['nama_paket', 'pagu', 'nama_satker', 'metode_pengadaan',
                   'jenis_pengadaan', 'status_pdn', 'status_ukm']

    display_df = filtered_df[display_cols].copy()
    display_df['pagu'] = display_df['pagu'].apply(lambda x: f"Rp {x/1e9:.2f} M")

    st.dataframe(
        display_df.head(100),
        use_container_width=True,
        height=400
    )

with tab2:
    st.header("💰 Analisis Pagu")

    col1, col2 = st.columns(2)

    with col1:
        # Distribusi pagu
        st.subheader("Distribusi Pagu")
        fig = px.histogram(
            filtered_df,
            x=filtered_df['pagu']/1e9,
            nbins=50,
            title='',
            labels={'x': 'Pagu (Miliar Rp)', 'count': 'Frekuensi'}
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Box plot pagu
        st.subheader("Box Plot Pagu")
        fig = px.box(
            filtered_df,
            y=filtered_df['pagu']/1e9,
            title='',
            labels={'y': 'Pagu (Miliar Rp)'}
        )
        st.plotly_chart(fig, use_container_width=True)

    # Statistik pagu
    st.subheader("📊 Statistik Pagu")
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

    with stats_col1:
        st.metric("Minimum", f"Rp {filtered_df['pagu'].min()/1e9:.2f} M")
    with stats_col2:
        st.metric("Maximum", f"Rp {filtered_df['pagu'].max()/1e9:.2f} M")
    with stats_col3:
        st.metric("Median", f"Rp {filtered_df['pagu'].median()/1e9:.2f} M")
    with stats_col4:
        st.metric("Std Dev", f"Rp {filtered_df['pagu'].std()/1e9:.2f} M")

with tab3:
    st.header("🏢 Analisis Satuan Kerja")

    # Query using DuckDB for aggregation
    query = """
    SELECT
        nama_satker,
        COUNT(*) as jumlah_paket,
        SUM(pagu) as total_pagu,
        AVG(pagu) as rata_pagu,
        SUM(CASE WHEN status_pdn = 'Ya' THEN 1 ELSE 0 END) as paket_pdn,
        SUM(CASE WHEN status_ukm = 'Ya' THEN 1 ELSE 0 END) as paket_ukm
    FROM rup
    GROUP BY nama_satker
    ORDER BY total_pagu DESC
    LIMIT 15
    """

    # Use the filtered query if filters are applied
    if selected_metode != 'Semua' or selected_jenis != 'Semua' or selected_satker != 'Semua':
        conn.register('filtered_rup', filtered_df)
        query = query.replace('FROM rup', 'FROM filtered_rup')

    satker_stats = conn.execute(query).df()
    satker_stats['total_pagu_miliar'] = satker_stats['total_pagu'] / 1e9

    col1, col2 = st.columns(2)

    with col1:
        # Top Satker by jumlah paket
        st.subheader("Top 15 Satker - Jumlah Paket")
        fig = px.bar(
            satker_stats,
            y='nama_satker',
            x='jumlah_paket',
            orientation='h',
            title='',
            labels={'jumlah_paket': 'Jumlah Paket', 'nama_satker': 'Satuan Kerja'}
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Top Satker by total pagu
        st.subheader("Top 15 Satker - Total Pagu")
        fig = px.bar(
            satker_stats,
            y='nama_satker',
            x='total_pagu_miliar',
            orientation='h',
            title='',
            labels={'total_pagu_miliar': 'Total Pagu (Miliar Rp)', 'nama_satker': 'Satuan Kerja'}
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

    # Detailed table
    st.subheader("📊 Detail Statistik Satuan Kerja")
    display_satker = satker_stats.copy()
    display_satker['total_pagu'] = display_satker['total_pagu'].apply(lambda x: f"Rp {x/1e12:.2f} T")
    display_satker['rata_pagu'] = display_satker['rata_pagu'].apply(lambda x: f"Rp {x/1e9:.2f} M")
    display_satker = display_satker.drop('total_pagu_miliar', axis=1)

    st.dataframe(display_satker, use_container_width=True, height=400)

with tab4:
    st.header("📋 Analisis Metode & Jenis Pengadaan")

    col1, col2 = st.columns(2)

    with col1:
        # Metode pengadaan
        st.subheader("Distribusi Metode Pengadaan")
        metode_counts = filtered_df['metode_pengadaan'].value_counts().head(10)

        fig = px.pie(
            values=metode_counts.values,
            names=metode_counts.index,
            title='',
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        # Metode pengadaan by pagu
        st.subheader("Total Pagu per Metode")
        metode_pagu = filtered_df.groupby('metode_pengadaan')['pagu'].sum().sort_values(ascending=False).head(10)
        metode_pagu_df = pd.DataFrame({
            'Metode': metode_pagu.index,
            'Total Pagu (Miliar Rp)': metode_pagu.values / 1e9
        })

        fig = px.bar(
            metode_pagu_df,
            x='Total Pagu (Miliar Rp)',
            y='Metode',
            orientation='h',
            title=''
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Jenis pengadaan
        st.subheader("Distribusi Jenis Pengadaan")
        jenis_counts = filtered_df['jenis_pengadaan'].value_counts()

        fig = px.bar(
            x=jenis_counts.index,
            y=jenis_counts.values,
            title='',
            labels={'x': 'Jenis Pengadaan', 'y': 'Jumlah Paket'}
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

        # Jenis pengadaan by pagu
        st.subheader("Total Pagu per Jenis")
        jenis_pagu = filtered_df.groupby('jenis_pengadaan')['pagu'].sum().sort_values(ascending=False)
        jenis_pagu_df = pd.DataFrame({
            'Jenis': jenis_pagu.index,
            'Total Pagu (Miliar Rp)': jenis_pagu.values / 1e9
        })

        fig = px.bar(
            jenis_pagu_df,
            x='Jenis',
            y='Total Pagu (Miliar Rp)',
            title=''
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("📅 Analisis Timeline")

    # Filter out null dates
    timeline_df = filtered_df[filtered_df['tgl_pengumuman_paket'].notna()].copy()

    if len(timeline_df) > 0:
        timeline_df['bulan'] = timeline_df['tgl_pengumuman_paket'].dt.to_period('M').astype(str)
        timeline_df['tahun'] = timeline_df['tgl_pengumuman_paket'].dt.year

        col1, col2 = st.columns(2)

        with col1:
            # Pengumuman per bulan
            st.subheader("Pengumuman Paket per Bulan")
            monthly_counts = timeline_df.groupby('bulan').size().reset_index(name='jumlah')

            fig = px.line(
                monthly_counts,
                x='bulan',
                y='jumlah',
                title='',
                labels={'bulan': 'Bulan', 'jumlah': 'Jumlah Paket'},
                markers=True
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Total pagu per bulan
            st.subheader("Total Pagu per Bulan")
            monthly_pagu = timeline_df.groupby('bulan')['pagu'].sum().reset_index()
            monthly_pagu['pagu_miliar'] = monthly_pagu['pagu'] / 1e9

            fig = px.bar(
                monthly_pagu,
                x='bulan',
                y='pagu_miliar',
                title='',
                labels={'bulan': 'Bulan', 'pagu_miliar': 'Total Pagu (Miliar Rp)'}
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

        # Heatmap timeline
        st.subheader("📊 Heatmap Aktivitas Pengumuman")
        timeline_df['hari_dalam_minggu'] = timeline_df['tgl_pengumuman_paket'].dt.day_name()
        timeline_df['minggu'] = timeline_df['tgl_pengumuman_paket'].dt.isocalendar().week

        heatmap_data = timeline_df.groupby(['minggu', 'hari_dalam_minggu']).size().reset_index(name='jumlah')
        heatmap_pivot = heatmap_data.pivot(index='hari_dalam_minggu', columns='minggu', values='jumlah').fillna(0)

        # Reorder days
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_pivot = heatmap_pivot.reindex([day for day in days_order if day in heatmap_pivot.index])

        fig = px.imshow(
            heatmap_pivot,
            labels=dict(x="Minggu", y="Hari", color="Jumlah Paket"),
            title='',
            aspect='auto',
            color_continuous_scale='Blues'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Tidak ada data tanggal pengumuman yang valid untuk ditampilkan.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>Dashboard Analisis RUP 2025 | Bootcamp Data Analysis</p>
        <p>Data Source: Sistem Informasi Rencana Umum Pengadaan</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.markdown("---")
    st.subheader("ℹ️ Tentang Dashboard")
    st.info("""
    Dashboard ini menampilkan analisis komprehensif data RUP 2025 menggunakan:

    - **Pandas**: Data manipulation
    - **DuckDB**: SQL analytics
    - **Plotly**: Interactive visualization
    - **Streamlit**: Web dashboard

    Gunakan filter di atas untuk menyesuaikan tampilan data.
    """)

    # Export data
    st.markdown("---")
    st.subheader("📥 Export Data")
    if st.button("Export Filtered Data (CSV)"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"rup_filtered_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
