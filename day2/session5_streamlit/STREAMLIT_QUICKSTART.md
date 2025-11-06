# 🚀 Streamlit Quick Start Guide

Panduan cepat untuk memulai dengan Streamlit - Framework Python untuk membuat Data Apps.

---

## 📋 Table of Contents

1. [Installation](#installation)
2. [First App](#first-app)
3. [Basic Components](#basic-components)
4. [Data Display](#data-display)
5. [Interactive Widgets](#interactive-widgets)
6. [Layout](#layout)
7. [Charts](#charts)
8. [Session State](#session-state)
9. [Caching](#caching)
10. [Tips & Tricks](#tips--tricks)

---

## 🔧 Installation

```bash
# Install Streamlit
pip install streamlit

# Verify installation
streamlit hello

# Install dengan dependencies lengkap
pip install streamlit pandas numpy plotly
```

---

## 👋 First App

### 1. Buat file `app.py`:

```python
import streamlit as st

st.title("Hello Streamlit! 👋")
st.write("Ini adalah aplikasi Streamlit pertama saya")

name = st.text_input("Siapa nama Anda?")
if name:
    st.write(f"Halo, {name}!")
```

### 2. Run aplikasi:

```bash
streamlit run app.py
```

### 3. Buka browser di: `http://localhost:8501`

---

## 📝 Basic Components

### Text Elements

```python
import streamlit as st

# Judul & Headers
st.title("Judul Utama")
st.header("Header")
st.subheader("Sub Header")

# Text
st.text("Plain text")
st.write("Magic write - bisa display apapun")

# Markdown
st.markdown("**Bold** and *italic* text")
st.markdown("""
### Markdown List
- Item 1
- Item 2
""")

# Code
st.code("""
def hello():
    print("Hello World")
""", language='python')

# LaTeX
st.latex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")
```

### Status Messages

```python
st.success("✅ Success message")
st.info("ℹ️ Info message")
st.warning("⚠️ Warning message")
st.error("❌ Error message")

# Progress
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")
```

---

## 📊 Data Display

### DataFrames

```python
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Jakarta', 'Bandung', 'Surabaya']
})

# Interactive dataframe (sortable, scrollable)
st.dataframe(df, use_container_width=True)

# Static table
st.table(df)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", 100, delta=10)
col2.metric("Revenue", "$50K", delta="-5%")
col3.metric("Active", 85, delta=5)

# JSON
st.json({
    "name": "John",
    "age": 30,
    "skills": ["Python", "SQL"]
})
```

---

## 🎮 Interactive Widgets

### Buttons

```python
# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("Thank you!")

# Toggle
enabled = st.toggle("Enable feature")
```

### Selection

```python
# Radio buttons
option = st.radio(
    "Choose one:",
    ["Option A", "Option B", "Option C"]
)

# Selectbox (dropdown)
city = st.selectbox(
    "Select city:",
    ["Jakarta", "Bandung", "Surabaya"]
)

# Multiselect
skills = st.multiselect(
    "Select skills:",
    ["Python", "SQL", "JavaScript", "Go"],
    default=["Python"]
)
```

### Sliders

```python
# Numeric slider
age = st.slider("Age:", 0, 100, 25)

# Range slider
price_range = st.slider(
    "Price range:",
    0, 1000,
    (200, 800)
)

# Select slider
size = st.select_slider(
    "Size:",
    options=["XS", "S", "M", "L", "XL"]
)
```

### Text Input

```python
# Text input
name = st.text_input("Name:", placeholder="Enter your name")

# Text area
bio = st.text_area("Bio:", height=100)

# Number input
quantity = st.number_input(
    "Quantity:",
    min_value=0,
    max_value=100,
    value=1,
    step=1
)

# Password
password = st.text_input("Password:", type="password")
```

### Date & Time

```python
from datetime import datetime

# Date input
date = st.date_input("Date:", datetime.now())

# Time input
time = st.time_input("Time:")

# Date range
start_date, end_date = st.date_input(
    "Date range:",
    value=(datetime.now(), datetime.now())
)
```

### File Upload

```python
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

---

## 📐 Layout

### Columns

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Content 1")

with col2:
    st.header("Column 2")
    st.write("Content 2")

with col3:
    st.header("Column 3")
    st.write("Content 3")

# Custom column widths
col1, col2 = st.columns([3, 1])  # 3:1 ratio
```

### Tabs

```python
tab1, tab2, tab3 = st.tabs(["📊 Data", "📈 Chart", "ℹ️ Info"])

with tab1:
    st.header("Data Tab")
    st.dataframe(df)

with tab2:
    st.header("Chart Tab")
    st.line_chart(df)

with tab3:
    st.header("Info Tab")
    st.info("This is info")
```

### Sidebar

```python
with st.sidebar:
    st.header("Sidebar")
    option = st.selectbox("Choose:", ["A", "B", "C"])
    st.button("Click")
```

### Expander

```python
with st.expander("Click to expand"):
    st.write("Hidden content")
    st.dataframe(df)
```

### Container

```python
with st.container():
    st.write("Inside container")
    st.button("Button")

# Empty container for dynamic content
placeholder = st.empty()
placeholder.text("This will be replaced")
time.sleep(2)
placeholder.text("Updated!")
```

---

## 📈 Charts

### Native Streamlit Charts

```python
import numpy as np
import pandas as pd

# Sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Line chart
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Map (requires lat/lon columns)
map_data = pd.DataFrame({
    'lat': [-6.2, -6.9, -7.8],
    'lon': [106.8, 107.6, 110.4]
})
st.map(map_data)
```

### Plotly Charts

```python
import plotly.express as px

# Sample data
df = px.data.iris()

# Interactive scatter plot
fig = px.scatter(
    df,
    x='sepal_width',
    y='sepal_length',
    color='species',
    title='Iris Dataset'
)
st.plotly_chart(fig, use_container_width=True)

# Bar chart
fig = px.bar(df, x='species', y='sepal_length')
st.plotly_chart(fig)

# Line chart
fig = px.line(df, x='sepal_width', y='sepal_length')
st.plotly_chart(fig)
```

### Matplotlib/Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.scatter(df['sepal_width'], df['sepal_length'])
ax.set_xlabel('Sepal Width')
ax.set_ylabel('Sepal Length')
st.pyplot(fig)
```

---

## 💾 Session State

Session state allows you to persist data across reruns:

```python
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Use session state
st.write(f"Counter: {st.session_state.counter}")

if st.button("Increment"):
    st.session_state.counter += 1

if st.button("Reset"):
    st.session_state.counter = 0

# Using callbacks
def increment():
    st.session_state.counter += 1

st.button("Increment with Callback", on_click=increment)
```

### Session State with Forms

```python
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 18, 100)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.user_data = {
            "name": name,
            "age": age
        }

if 'user_data' in st.session_state:
    st.write("Saved data:", st.session_state.user_data)
```

---

## ⚡ Caching

Caching improves performance by avoiding re-computation:

### Cache Data

```python
@st.cache_data
def load_data():
    # This will only run once
    df = pd.read_csv('large_file.csv')
    return df

df = load_data()  # Fast on subsequent runs
st.dataframe(df)

# Clear cache
st.cache_data.clear()
```

### Cache Resources

```python
import duckdb

@st.cache_resource
def init_connection():
    # This will only run once
    return duckdb.connect(':memory:')

conn = init_connection()  # Reuses connection
```

### Cache with TTL (Time To Live)

```python
from datetime import timedelta

@st.cache_data(ttl=timedelta(hours=1))
def load_api_data():
    # Cache expires after 1 hour
    return fetch_from_api()
```

---

## 💡 Tips & Tricks

### 1. Page Configuration

```python
st.set_page_config(
    page_title="My App",
    page_icon="📊",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"
)
```

### 2. Custom CSS

```python
st.markdown("""
    <style>
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Big Text</p>', unsafe_allow_html=True)
```

### 3. Hide Elements

```python
# Hide hamburger menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
```

### 4. Download Button

```python
# CSV download
csv = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv"
)

# JSON download
import json
json_data = json.dumps(data)
st.download_button(
    label="Download JSON",
    data=json_data,
    file_name="data.json",
    mime="application/json"
)
```

### 5. Stop Execution

```python
if not st.session_state.get('authenticated'):
    st.warning("Please login first")
    st.stop()  # Stops execution here

st.write("Protected content")
```

### 6. Rerun App

```python
if st.button("Refresh"):
    st.rerun()  # Reruns the entire app
```

### 7. Query Parameters

```python
# Get query parameters from URL
params = st.experimental_get_query_params()
page = params.get('page', ['home'])[0]

# Set query parameters
st.experimental_set_query_params(page='about')
```

### 8. Animations

```python
# Balloons
if st.button("Celebrate"):
    st.balloons()

# Snow
if st.button("Winter"):
    st.snow()
```

---

## 🎯 Common Patterns

### Pattern 1: Filter Data

```python
df = load_data()

# Filters in sidebar
with st.sidebar:
    min_value = st.slider("Min value:", 0, 100, 0)
    category = st.multiselect("Category:", df['category'].unique())

# Apply filters
filtered_df = df[
    (df['value'] >= min_value) &
    (df['category'].isin(category))
]

st.dataframe(filtered_df)
```

### Pattern 2: Multi-page App

```python
# pages/home.py
def show():
    st.title("Home Page")
    st.write("Welcome!")

# pages/about.py
def show():
    st.title("About Page")
    st.write("About us")

# main.py
import pages.home as home
import pages.about as about

page = st.sidebar.selectbox("Page:", ["Home", "About"])

if page == "Home":
    home.show()
else:
    about.show()
```

### Pattern 3: Form Validation

```python
with st.form("registration"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register")

    if submitted:
        if not email or '@' not in email:
            st.error("Invalid email")
        elif len(password) < 8:
            st.error("Password must be at least 8 characters")
        elif password != confirm:
            st.error("Passwords don't match")
        else:
            st.success("Registration successful!")
```

---

## 🐛 Debugging

```python
# Show debug info
st.write("Debug:", variable)

# Show entire session state
st.write(st.session_state)

# Try-except blocks
try:
    result = risky_operation()
    st.success("Success!")
except Exception as e:
    st.error(f"Error: {e}")
    st.exception(e)  # Shows full traceback
```

---

## 📚 Resources

- [Official Documentation](https://docs.streamlit.io)
- [API Reference](https://docs.streamlit.io/library/api-reference)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Gallery](https://streamlit.io/gallery)
- [Forum](https://discuss.streamlit.io)
- [GitHub](https://github.com/streamlit/streamlit)

---

## 🚀 Next Steps

1. **Practice:** Build simple apps dengan concepts di atas
2. **Explore:** Lihat [Streamlit Gallery](https://streamlit.io/gallery) untuk inspirasi
3. **Integrate:** Connect dengan databases, APIs, ML models
4. **Deploy:** Share apps di [Streamlit Community Cloud](https://share.streamlit.io)

---

**Happy Coding! 🎉**
