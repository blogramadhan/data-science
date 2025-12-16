"""
LAB 11: Interactive Components Demo
Bootcamp Data Analysis - Python, DuckDB & Streamlit

Topik yang dipelajari:
1. Input widgets (buttons, checkboxes, sliders, etc.)
2. Session state management
3. Forms
4. Callbacks
5. Dynamic content
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Interactive Components",
    page_icon="🎮",
    layout="wide"
)

# ========================================
# SESSION STATE INITIALIZATION
# ========================================
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'todos' not in st.session_state:
    st.session_state.todos = []

if 'history' not in st.session_state:
    st.session_state.history = []

# ========================================
# TITLE
# ========================================
st.title("🎮 Interactive Components Demo")
st.markdown("Pelajari berbagai komponen interaktif Streamlit dan cara menggunakannya")
st.divider()

# ========================================
# 1. BUTTON WIDGETS
# ========================================
st.header("1️⃣ Button Widgets")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Button")
    if st.button("Click Me! 🖱️"):
        st.success("Button clicked!")
        st.session_state.counter += 1
    st.write(f"Button clicked {st.session_state.counter} times")

with col2:
    st.subheader("Download Button")
    sample_data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    csv = sample_data.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="sample_data.csv",
        mime="text/csv"
    )

with col3:
    st.subheader("Link Button")
    st.link_button(
        "🔗 Go to Streamlit Docs",
        "https://docs.streamlit.io"
    )

st.divider()

# ========================================
# 2. SELECTION WIDGETS
# ========================================
st.header("2️⃣ Selection Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Checkbox & Toggle")
    show_data = st.checkbox("Show Data Table", value=True)
    enable_feature = st.toggle("Enable Advanced Features", value=False)

    if show_data:
        st.dataframe(sample_data, use_container_width=True)

    if enable_feature:
        st.info("🚀 Advanced features enabled!")

    st.subheader("Radio Buttons")
    chart_type = st.radio(
        "Select chart type:",
        ["Line", "Bar", "Area"],
        horizontal=True
    )
    st.write(f"You selected: {chart_type}")

with col2:
    st.subheader("Select Box")
    city = st.selectbox(
        "Pilih kota:",
        ["Jakarta", "Bandung", "Surabaya", "Medan", "Bali"]
    )
    st.write(f"Kota terpilih: {city}")

    st.subheader("Multiselect")
    options = st.multiselect(
        "Pilih skills:",
        ["Python", "SQL", "DuckDB", "Streamlit", "Pandas", "Plotly"],
        default=["Python"]
    )
    st.write(f"Skills: {', '.join(options)}")

st.divider()

# ========================================
# 3. SLIDER WIDGETS
# ========================================
st.header("3️⃣ Slider Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Numeric Slider")
    age = st.slider("Pilih umur:", 0, 100, 25)
    st.write(f"Umur: {age} tahun")

    st.subheader("Range Slider")
    price_range = st.slider(
        "Pilih range harga (juta):",
        0.0, 100.0, (20.0, 80.0)
    )
    st.write(f"Range: Rp {price_range[0]}M - Rp {price_range[1]}M")

with col2:
    st.subheader("Select Slider")
    size = st.select_slider(
        "Pilih ukuran:",
        options=["XS", "S", "M", "L", "XL", "XXL"],
        value="M"
    )
    st.write(f"Size: {size}")

    st.subheader("Custom Slider")
    rating = st.select_slider(
        "Rating:",
        options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        value="⭐⭐⭐"
    )
    st.write(f"Your rating: {rating}")

st.divider()

# ========================================
# 4. TEXT INPUT WIDGETS
# ========================================
st.header("4️⃣ Text Input Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text Input")
    name = st.text_input("Masukkan nama:", placeholder="John Doe")
    if name:
        st.write(f"Hello, {name}! 👋")

    st.subheader("Password Input")
    password = st.text_input("Password:", type="password")
    if password:
        st.success("Password entered!")

with col2:
    st.subheader("Text Area")
    comment = st.text_area(
        "Tulis komentar:",
        placeholder="Tulis komentar Anda di sini...",
        height=100
    )
    if comment:
        st.info(f"Karakter: {len(comment)}")

    st.subheader("Number Input")
    quantity = st.number_input(
        "Jumlah:",
        min_value=0,
        max_value=100,
        value=1,
        step=1
    )
    st.write(f"Total: {quantity} items")

st.divider()

# ========================================
# 5. DATE & TIME WIDGETS
# ========================================
st.header("5️⃣ Date & Time Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Date Input")
    selected_date = st.date_input(
        "Pilih tanggal:",
        value=datetime.now()
    )
    st.write(f"Tanggal: {selected_date}")

    st.subheader("Date Range")
    date_range = st.date_input(
        "Pilih range tanggal:",
        value=(datetime.now(), datetime.now() + timedelta(days=7)),
        max_value=datetime.now() + timedelta(days=365)
    )
    if len(date_range) == 2:
        st.write(f"Dari: {date_range[0]} hingga {date_range[1]}")

with col2:
    st.subheader("Time Input")
    selected_time = st.time_input("Pilih waktu:")
    st.write(f"Waktu: {selected_time}")

st.divider()

# ========================================
# 6. FILE UPLOADER
# ========================================
st.header("6️⃣ File Uploader")

uploaded_file = st.file_uploader(
    "Upload file CSV atau Excel:",
    type=["csv", "xlsx", "xls"],
    help="File maksimal 200MB"
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success(f"✅ File '{uploaded_file.name}' berhasil di-upload!")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", len(df))
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            st.metric("Size", f"{uploaded_file.size / 1024:.2f} KB")

        with st.expander("👁️ Preview Data"):
            st.dataframe(df.head(10), use_container_width=True)

        with st.expander("📊 Data Info"):
            st.write("Columns:", df.columns.tolist())
            st.write("Data Types:")
            st.write(df.dtypes)

    except Exception as e:
        st.error(f"Error reading file: {e}")

st.divider()

# ========================================
# 7. FORMS
# ========================================
st.header("7️⃣ Forms")

st.markdown("""
Forms berguna untuk mengelompokkan inputs dan submit sekaligus.
Tanpa form, setiap input akan trigger re-run.
""")

with st.form("user_form"):
    st.subheader("Registration Form")

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        age_form = st.number_input("Age", 18, 100, 25)

    with col2:
        last_name = st.text_input("Last Name")
        city_form = st.selectbox("City", ["Jakarta", "Bandung", "Surabaya"])
        agree = st.checkbox("I agree to terms and conditions")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if first_name and last_name and email and agree:
            st.success(f"✅ Registration successful for {first_name} {last_name}!")
            user_data = {
                "Name": f"{first_name} {last_name}",
                "Email": email,
                "Age": age_form,
                "City": city_form
            }
            st.json(user_data)
        else:
            st.error("Please fill all required fields and agree to terms!")

st.divider()

# ========================================
# 8. SESSION STATE & CALLBACKS
# ========================================
st.header("8️⃣ Session State & Callbacks")

st.markdown("""
Session state memungkinkan Anda menyimpan data antar reruns.
Callbacks adalah functions yang dipanggil saat widget berubah.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Counter Example")

    def increment():
        st.session_state.counter += 1

    def decrement():
        st.session_state.counter -= 1

    def reset():
        st.session_state.counter = 0

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.button("➖ Decrement", on_click=decrement)
    with col_b:
        st.button("🔄 Reset", on_click=reset)
    with col_c:
        st.button("➕ Increment", on_click=increment)

    st.metric("Current Count", st.session_state.counter)

with col2:
    st.subheader("Todo List")

    def add_todo():
        if st.session_state.new_todo:
            st.session_state.todos.append({
                'task': st.session_state.new_todo,
                'done': False
            })
            st.session_state.new_todo = ""

    st.text_input("New todo:", key="new_todo", on_change=add_todo)

    if st.session_state.todos:
        for idx, todo in enumerate(st.session_state.todos):
            col_check, col_task = st.columns([1, 5])
            with col_check:
                done = st.checkbox("", value=todo['done'], key=f"todo_{idx}")
                st.session_state.todos[idx]['done'] = done
            with col_task:
                if todo['done']:
                    st.markdown(f"~~{todo['task']}~~")
                else:
                    st.write(todo['task'])
    else:
        st.info("No todos yet. Add one above!")

st.divider()

# ========================================
# 9. INTERACTIVE CHART WITH FILTERS
# ========================================
st.header("9️⃣ Interactive Chart with Filters")

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100)
data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(50, 200, 100),
    'Profit': np.random.randint(10, 50, 100),
    'Category': np.random.choice(['A', 'B', 'C'], 100)
})

col1, col2, col3 = st.columns(3)

with col1:
    category_filter = st.multiselect(
        "Filter by Category:",
        options=['A', 'B', 'C'],
        default=['A', 'B', 'C']
    )

with col2:
    metric_choice = st.selectbox(
        "Select Metric:",
        ["Sales", "Profit"]
    )

with col3:
    chart_type_interactive = st.radio(
        "Chart Type:",
        ["Line", "Bar"],
        horizontal=True
    )

# Filter data
filtered_data = data[data['Category'].isin(category_filter)]

# Create chart
if chart_type_interactive == "Line":
    fig = px.line(
        filtered_data,
        x='Date',
        y=metric_choice,
        color='Category',
        title=f"{metric_choice} Over Time"
    )
else:
    fig = px.bar(
        filtered_data,
        x='Date',
        y=metric_choice,
        color='Category',
        title=f"{metric_choice} Over Time"
    )

st.plotly_chart(fig, use_container_width=True)

# Show statistics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sales", f"${filtered_data['Sales'].sum():,}")
with col2:
    st.metric("Avg Sales", f"${filtered_data['Sales'].mean():.2f}")
with col3:
    st.metric("Total Profit", f"${filtered_data['Profit'].sum():,}")
with col4:
    st.metric("Avg Profit", f"${filtered_data['Profit'].mean():.2f}")

st.divider()

# ========================================
# SIDEBAR
# ========================================
with st.sidebar:
    st.header("🎮 Component Demo")

    st.info("""
        **Topics Covered:**
        - Button widgets
        - Selection widgets
        - Sliders
        - Text inputs
        - Date & time
        - File uploader
        - Forms
        - Session state
        - Callbacks
        - Interactive charts
    """)

    st.divider()

    st.subheader("Quick Actions")
    if st.button("🎉 Celebrate"):
        st.balloons()

    if st.button("❄️ Let it Snow"):
        st.snow()

    st.divider()
    st.caption("Bootcamp Data Analysis 2025")

# ========================================
# FOOTER
# ========================================
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>🎓 Bootcamp Data Analysis - Python, DuckDB & Streamlit</p>
        <p>LAB 11: Interactive Components Demo</p>
    </div>
""", unsafe_allow_html=True)
