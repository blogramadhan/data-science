# Session 5: Streamlit Applications

Folder ini berisi aplikasi Streamlit untuk pembelajaran bertahap dari dasar hingga advanced.

## 📚 Daftar Aplikasi

### 1. Hello Streamlit (LAB 10)
**File:** `01_hello_streamlit.py`

**Topik:**
- Basic text elements (title, header, markdown, code)
- Displaying data (dataframe, table, metrics, JSON)
- Status messages (success, info, warning, error)
- Simple charts (line, bar, area)
- Layout components (columns, containers, expanders, tabs)
- Custom CSS styling

**Cara Menjalankan:**
```bash
streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py
```

**Yang Dipelajari:**
- Struktur dasar aplikasi Streamlit
- Berbagai cara menampilkan teks dan data
- Layout dan organisasi konten
- Progress indicators
- Basic customization dengan CSS

---

### 2. Interactive Components Demo (LAB 11)
**File:** `02_components_demo.py`

**Topik:**
- Button widgets (button, download_button, link_button)
- Selection widgets (checkbox, toggle, radio, selectbox, multiselect)
- Slider widgets (slider, select_slider)
- Text input widgets (text_input, text_area, number_input)
- Date & time widgets (date_input, time_input)
- File uploader
- Forms dan form submission
- Session state management
- Callbacks
- Interactive charts dengan filters

**Cara Menjalankan:**
```bash
streamlit run day2/session5_streamlit/apps/02_components_demo.py
```

**Yang Dipelajari:**
- Semua jenis input widgets Streamlit
- Cara menggunakan session state untuk persist data
- Callback functions untuk handling events
- Form untuk batch input submission
- Dynamic content berdasarkan user input
- Interactive data visualization

**Fitur Interaktif:**
- Counter dengan increment/decrement
- Todo list dengan checkboxes
- Real-time chart filtering
- File upload dan preview
- Registration form

---

### 3. Data Explorer (LAB 12)
**File:** `03_data_explorer.py`

**Topik:**
- File upload (CSV, Excel)
- Integration Pandas & DuckDB
- Caching strategies (@st.cache_data, @st.cache_resource)
- Dynamic SQL query building
- Interactive data filtering
- Multiple analysis views (tabs)
- Distribution analysis
- Trend analysis
- Relationship analysis (scatter plots, correlation)
- Custom aggregations
- SQL playground
- Export functionality (CSV, Excel)

**Cara Menjalankan:**
```bash
streamlit run day2/session5_streamlit/apps/03_data_explorer.py
```

**Yang Dipelajari:**
- Complete data analysis workflow
- DuckDB integration dengan Streamlit
- Performance optimization dengan caching
- Dynamic query building dari filters
- Multiple visualization types dengan Plotly
- Advanced data manipulation
- Export hasil analisis

**Fitur Utama:**
- Upload data atau gunakan sample data
- Interactive filters (categorical, numeric, date range)
- 4 analysis tabs:
  - Distribution: histogram & pie charts
  - Trends: time series analysis
  - Relationships: scatter plots & correlation
  - Aggregations: custom grouping & aggregations
- SQL playground untuk custom queries
- Export filtered data dalam berbagai format

---

### 4. RUP Dashboard (Production Example)
**File:** `rup_dashboard.py`

**Topik:**
- Production-ready dashboard
- Real data analysis (RUP 2025)
- Advanced filtering
- Multiple KPIs
- Complex visualizations
- Professional UI/UX

**Cara Menjalankan:**
```bash
streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

**Yang Dipelajari:**
- Best practices untuk production dashboard
- Complex data processing pipeline
- Multiple coordinated visualizations
- Advanced filtering logic
- Professional styling & branding
- Performance optimization untuk dataset besar

---

## 🚀 Quick Start

### Prerequisites
```bash
# Install dependencies
pip install streamlit pandas numpy duckdb plotly openpyxl
```

### Menjalankan Aplikasi

#### Option 1: Individual App
```bash
# Dari root directory
streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py
streamlit run day2/session5_streamlit/apps/02_components_demo.py
streamlit run day2/session5_streamlit/apps/03_data_explorer.py
streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

#### Option 2: Dengan UV (Package Manager)
```bash
uv run streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py
```

---

## 📖 Learning Path

### Untuk Pemula
1. Mulai dengan **01_hello_streamlit.py**
   - Pelajari basic elements
   - Pahami struktur aplikasi Streamlit
   - Eksperimen dengan layout

2. Lanjut ke **02_components_demo.py**
   - Coba semua interactive widgets
   - Pelajari session state
   - Eksperimen dengan callbacks

3. Advanced: **03_data_explorer.py**
   - Upload data sendiri
   - Buat custom SQL queries
   - Eksperimen dengan visualizations

4. Production: **rup_dashboard.py**
   - Study struktur dashboard lengkap
   - Pelajari best practices
   - Adaptasi untuk project sendiri

---

## 🎯 Key Concepts

### 1. Streamlit's Execution Model
Streamlit re-runs entire script setiap kali ada interaksi:
```python
# Script runs from top to bottom on every interaction
st.title("My App")
name = st.text_input("Name")  # Re-runs when user types
st.write(f"Hello, {name}")    # Updates automatically
```

### 2. Session State
Persist data across reruns:
```python
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
```

### 3. Caching
Optimize performance:
```python
@st.cache_data  # Cache data (DataFrames, lists, etc.)
def load_data():
    return pd.read_csv('data.csv')

@st.cache_resource  # Cache resources (DB connections, models)
def init_connection():
    return duckdb.connect(':memory:')
```

### 4. Layout
Organize content:
```python
# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# Sidebar
with st.sidebar:
    st.write("Sidebar content")

# Expander
with st.expander("Click to expand"):
    st.write("Hidden content")
```

---

## 💡 Tips & Tricks

### 1. Development Mode
```bash
# Streamlit watches file changes and auto-reloads
streamlit run app.py
```

### 2. Change Port
```bash
streamlit run app.py --server.port 8502
```

### 3. Wide Layout
```python
st.set_page_config(layout="wide")
```

### 4. Custom Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### 5. Hide Hamburger Menu
```python
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
```

### 6. Loading States
```python
with st.spinner('Loading...'):
    # Long operation
    time.sleep(2)
st.success('Done!')
```

---

## 🐛 Common Issues

### Issue 1: Module Not Found
```bash
# Solution: Install missing package
pip install streamlit pandas numpy duckdb plotly
```

### Issue 2: Port Already in Use
```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

### Issue 3: Data Not Updating
```python
# Solution: Clear cache
st.cache_data.clear()
# Or manually clear from UI (C key or menu)
```

### Issue 4: Large File Upload
```python
# Solution: Increase upload limit in .streamlit/config.toml
[server]
maxUploadSize = 1000  # MB
```

---

## 📚 Resources

### Official Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [API Reference](https://docs.streamlit.io/library/api-reference)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Tutorials
- [30 Days of Streamlit](https://30days.streamlit.app)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Community Forum](https://discuss.streamlit.io)

### Integration Guides
- [Plotly with Streamlit](https://plotly.com/python/streamlit/)
- [DuckDB Docs](https://duckdb.org/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 🎓 Exercises

### Exercise 1: Customize Hello Streamlit
- Tambahkan custom CSS styling
- Buat layout 3 kolom
- Tambahkan gambar dan video
- Implement theme switcher

### Exercise 2: Build Calculator
- Buat calculator sederhana dengan buttons
- Simpan history di session state
- Tambahkan clear dan undo functionality

### Exercise 3: Personal Dashboard
- Upload data pribadi (expenses, habits, etc.)
- Buat visualizations
- Implement filters
- Add export functionality

### Exercise 4: Data Cleaning App
- Upload messy data
- Detect dan handle missing values
- Remove duplicates
- Fix data types
- Export clean data

---

## 🚀 Deployment

### Streamlit Community Cloud (Free)
1. Push code ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Deploy!

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

### Heroku
```bash
# Create Procfile
web: streamlit run app.py --server.port=$PORT
```

---

## 📝 License

Materi ini dibuat untuk keperluan edukasi Bootcamp Data Analysis.

---

## 👥 Contributors

- Bootcamp Data Analysis Team
- Contact: [Your Contact Info]

---

**Happy Learning! 🎉**
