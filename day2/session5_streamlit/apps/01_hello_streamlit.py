"""
LAB 10: Hello Streamlit - Aplikasi Streamlit Pertama
Bootcamp Data Analysis - Python, DuckDB & Streamlit

Topik yang dipelajari:
1. Basic text elements
2. Displaying data
3. Status messages
4. Media elements
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# SIDEBAR (Moved to top for theme selection)
# ========================================
with st.sidebar:
    st.subheader("About")
    st.info("""
        **Hello Streamlit App**

        Aplikasi ini mendemonstrasikan:
        - Text elements
        - Data display
        - Status messages
        - Simple charts
        - Layout components
    """)

    st.divider()

    st.header("📋 Sidebar Menu")
    st.write("Sidebar berguna untuk navigasi dan filter.")

    st.subheader("Settings")
    show_code = st.checkbox("Show code examples", value=True)
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])

    st.divider()

    st.caption("Bootcamp Data Analysis 2025")

# ========================================
# CUSTOM CSS (Theme-based)
# ========================================
# Apply theme-based CSS
if theme == "Dark":
    theme_css = """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
        color: #FAFAFA;
    }
    .highlight {
        background-color: #FFA726;
        padding: 5px;
        border-radius: 3px;
        color: #000;
    }
    </style>
    """
elif theme == "Light":
    theme_css = """
    <style>
    .stApp {
        background-color: #FFFFFF;
        color: #000000;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
        color: #000000;
    }
    .highlight {
        background-color: #FFEB3B;
        padding: 5px;
        border-radius: 3px;
        color: #000;
    }
    </style>
    """
else:  # Auto
    theme_css = """
    <style>
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    .highlight {
        background-color: #FFEB3B;
        padding: 5px;
        border-radius: 3px;
    }
    </style>
    """

st.markdown(theme_css, unsafe_allow_html=True)

# ========================================
# 1. BASIC TEXT ELEMENTS
# ========================================
st.title("👋 Hello Streamlit!")
st.subheader("Selamat datang di dunia Streamlit - Framework untuk membuat Data Apps dengan mudah!")

st.markdown("---")

st.header("1️⃣ Text Elements")

st.text("Ini adalah text biasa menggunakan st.text()")

st.markdown("""
### Ini adalah Markdown
Anda bisa menggunakan **bold**, *italic*, atau `code` dengan mudah.

- Item 1
- Item 2
- Item 3

[Link ke dokumentasi Streamlit](https://docs.streamlit.io)
""")

st.write("st.write() adalah 'magic command' yang bisa menampilkan apapun:")
st.write("- String")
st.write("- Numbers:", 42)
st.write("- Lists:", [1, 2, 3, 4, 5])

# Code display
st.subheader("Code Display")
code = '''def hello_world():
    print("Hello, Streamlit!")
    return "Welcome to Data Analysis"'''
st.code(code, language='python')

# LaTeX
st.subheader("Mathematical Expressions")
st.latex(r'''
    a^2 + b^2 = c^2
''')
st.latex(r'''
    \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
''')

st.divider()  # Horizontal divider

# ========================================
# 2. DISPLAYING DATA
# ========================================
st.header("2️⃣ Displaying Data")

# Create sample data
df = pd.DataFrame({
    'Nama': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Usia': [25, 30, 35, 28, 32],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Bali'],
    'Gaji': [5000000, 7000000, 6500000, 5500000, 8000000]
})

st.subheader("DataFrame (Interactive)")
st.write("Menggunakan st.dataframe() - bisa di-sort dan di-scroll:")
st.dataframe(df, use_container_width=True)

st.subheader("Table (Static)")
st.write("Menggunakan st.table() - static table:")
st.table(df.head(3))

# Metrics
st.subheader("Metrics - KPI Display")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Karyawan",
        value=len(df),
        delta="2 orang"
    )

with col2:
    st.metric(
        label="Rata-rata Gaji",
        value=f"Rp {df['Gaji'].mean()/1e6:.1f}M",
        delta=f"{10.5}%"
    )

with col3:
    st.metric(
        label="Rata-rata Usia",
        value=f"{df['Usia'].mean():.1f} tahun",
        delta="-2 tahun"
    )

# JSON display
st.subheader("JSON Display")
sample_json = {
    "name": "Streamlit Tutorial",
    "version": "1.0",
    "topics": ["Python", "Data Science", "Dashboard"],
    "author": {
        "name": "Bootcamp Instructor",
        "email": "instructor@bootcamp.com"
    }
}
st.json(sample_json)

st.divider()

# ========================================
# 3. STATUS MESSAGES
# ========================================
st.header("3️⃣ Status Messages")

st.success("✅ Success! Data berhasil dimuat.")
st.info("ℹ️ Info: Streamlit akan auto-refresh setiap kali Anda save file.")
st.warning("⚠️ Warning: Pastikan data sudah di-backup sebelum melanjutkan.")
st.error("❌ Error: File tidak ditemukan!")

# Spinner demo
st.subheader("Loading Spinner")
with st.spinner("Memuat data demo..."):
    time.sleep(1.5)
st.success("Data berhasil dimuat!")

# Progress bar
st.subheader("Progress Bar")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)
st.success("Progress completed!")

st.divider()

# ========================================
# 4. CHARTS (Simple)
# ========================================
st.header("4️⃣ Simple Charts")

st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(df.set_index('Nama')['Gaji'])

st.subheader("Area Chart")
st.area_chart(chart_data)

st.divider()

# ========================================
# 5. COLUMNS & CONTAINERS
# ========================================
st.header("5️⃣ Layout: Columns & Containers")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.write("Ini adalah kolom pertama")
    st.image("https://via.placeholder.com/150", caption="Placeholder Image")

with col2:
    st.subheader("Column 2")
    st.write("Ini adalah kolom kedua")
    st.button("Click me!")

with col3:
    st.subheader("Column 3")
    st.write("Ini adalah kolom ketiga")
    st.checkbox("Check this box")

# Container
st.subheader("Container Example")
with st.container():
    st.write("Ini adalah container")
    st.write("Semua elements dalam container akan di-group")

    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        st.metric("Metric 1", "100")
    with sub_col2:
        st.metric("Metric 2", "200")

st.divider()

# ========================================
# 6. EXPANDER & TABS
# ========================================
st.header("6️⃣ Expander & Tabs")

# Expander
with st.expander("📖 Klik untuk membaca lebih lanjut"):
    st.write("""
        Expander berguna untuk menyembunyikan konten yang panjang atau detail teknis.
        User bisa expand/collapse sesuai kebutuhan.
    """)
    st.code("""
        with st.expander("Title"):
            st.write("Content here")
    """, language='python')

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Data", "📈 Chart", "ℹ️ Info"])

with tab1:
    st.subheader("Data Tab")
    st.dataframe(df)

with tab2:
    st.subheader("Chart Tab")
    st.bar_chart(df.set_index('Nama')['Usia'])

with tab3:
    st.subheader("Info Tab")
    st.info("Tabs berguna untuk mengorganisir konten yang berbeda dalam satu page.")

st.divider()

# ========================================
# FOOTER
# ========================================
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>🎓 Bootcamp Data Analysis - Python, DuckDB & Streamlit</p>
        <p>LAB 10: Hello Streamlit</p>
    </div>
""", unsafe_allow_html=True)

# Balloons for fun!
if st.button("🎉 Celebrate!"):
    st.balloons()
    st.success("Selamat! Anda telah menyelesaikan LAB 10!")
