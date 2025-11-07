# Bootcamp Analisis Data - Python, DuckDB & Streamlit

**Durasi:** 2 Hari (16 Jam Total)

## 🎯 Tentang Bootcamp

Bootcamp intensif ini dirancang untuk membekali peserta dengan keterampilan praktis dalam analisis data menggunakan Python, DuckDB sebagai database analitik, dan Streamlit untuk membuat dashboard interaktif. Peserta akan belajar langsung menggunakan **dataset RUP (Rencana Umum Pengadaan) 2025** sebagai studi kasus.

### 📊 Dataset: RUP 2025
- **Topik**: Rencana Umum Pengadaan Barang/Jasa Pemerintah 2025
- **Jumlah Records**: 16,430 paket pengadaan
- **Ukuran File**: ~1.3 MB (format Parquet)
- **Informasi Detail**: [datasets/rup/README.md](datasets/rup/README.md)

### 🎓 Target Peserta

- Data Analyst yang ingin meningkatkan kemampuan
- Business Analyst yang ingin lebih technical
- Programmer yang ingin masuk ke bidang Data Analytics
- Fresh Graduate yang ingin berkarir di bidang data
- Professional yang perlu mengolah dan visualisasi data

### ✅ Prerequisites

- Pemahaman dasar programming (Python preferred)
- Familiar dengan konsep database (SQL dasar)
- Laptop dengan minimal 8GB RAM
- Python 3.8+ terinstall

### 🛠️ Tools & Libraries

- Python 3.9+
- Pandas untuk manipulasi data
- NumPy untuk operasi numerik
- DuckDB untuk query analitik
- Streamlit untuk dashboard interaktif
- Plotly untuk visualisasi interaktif
- Matplotlib & Seaborn untuk visualisasi static
- Jupyter Notebook untuk eksplorasi

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Clone repository
git clone <repository-url>
cd data-science

# Install dependencies dengan uv
uv sync

# Atau dengan pip
pip install pandas numpy duckdb streamlit plotly matplotlib seaborn jupyter openpyxl pyarrow
```

### 2. Jalankan Jupyter Notebook

```bash
uv run jupyter notebook

# Buka notebook: day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb
```

### 3. Jalankan Streamlit Apps

```bash
# LAB 10: Hello Streamlit (Basic)
uv run streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py

# LAB 11: Interactive Components
uv run streamlit run day2/session5_streamlit/apps/02_components_demo.py

# LAB 12: Data Explorer
uv run streamlit run day2/session5_streamlit/apps/03_data_explorer.py

# Production Dashboard - Analisis RUP
uv run streamlit run day2/session5_streamlit/apps/rup_dashboard.py
```

---

## 📁 Struktur Project

```
data-science/
├── day1/
│   ├── session1_python_pandas/
│   │   └── notebooks/
│   │       └── 01_exploratory_data_analysis_rup.ipynb  ✅
│   ├── session2_duckdb/
│   │   ├── notebooks/
│   │   │   └── 01_duckdb_intro.py  ✅
│   │   └── README.md  ✅
│   └── session3_visualization/
│       └── README.md  ✅
│
├── day2/
│   ├── session4_advanced_analysis/
│   │   └── README.md  ✅
│   └── session5_streamlit/
│       ├── apps/
│       │   ├── 01_hello_streamlit.py  ✅
│       │   ├── 02_components_demo.py  ✅
│       │   ├── 03_data_explorer.py  ✅
│       │   ├── rup_dashboard.py  ✅
│       │   └── README.md  ✅
│       └── STREAMLIT_QUICKSTART.md  ✅
│
├── datasets/
│   └── rup/
│       ├── RUP-PaketPenyedia-Terumumkan-2025.parquet  ✅
│       └── README.md  ✅
│
├── pyproject.toml  ✅
└── README.md
```

---

# 📚 HARI 1: Fundamental Data Analysis

## Session 1: Python & Pandas untuk Analisis Data (09:00 - 12:00)

**Durasi:** 3 jam
**Format:** Hands-on dengan Jupyter Notebook
**Dataset:** RUP 2025

### Materi Pembelajaran

#### 1.1 Setup Environment (30 menit)
- Setup Python & Virtual Environment (uv/venv)
- Install libraries yang dibutuhkan
- Pengenalan Jupyter Notebook
- Membuka dataset RUP 2025

#### 1.2 Exploratory Data Analysis (EDA) dengan Pandas (150 menit)

**Topik yang Dipelajari:**

**A. Loading dan Inspeksi Data**
- Membaca file Parquet dengan Pandas
- Inspeksi struktur data: `.head()`, `.info()`, `.describe()`, `.shape`
- Memahami kolom-kolom dalam dataset RUP
- Identifikasi tipe data dan missing values

**B. Data Selection & Filtering**
- Menggunakan `.loc[]` dan `.iloc[]` untuk seleksi data
- Boolean indexing untuk filtering
- Query method untuk filter kompleks
- Contoh: Filter paket dengan pagu > 1 miliar

**C. Data Aggregation**
- GroupBy operations untuk agregasi
- Menghitung total pagu per metode pengadaan
- Menghitung jumlah paket per satuan kerja
- Top 10 satker dengan pagu terbesar

**D. Data Manipulation**
- Sorting data berdasarkan multiple columns
- Handling missing values (detection & treatment)
- String operations untuk cleaning
- Date/time operations

**E. Statistical Summary**
- Descriptive statistics (mean, median, std, percentiles)
- Distribution analysis
- Outlier detection
- Correlation analysis antar variabel numerik

**F. Data Visualization dengan Pandas**
- Bar charts untuk categorical data
- Histogram untuk distribusi pagu
- Time series plotting
- Basic styling dan customization

#### 📓 Notebook:
`day1/session1_python_pandas/notebooks/01_exploratory_data_analysis_rup.ipynb`

**Praktik yang Dilakukan:**
- Analisis distribusi pagu pengadaan
- Identifikasi satker dengan pengadaan terbanyak
- Analisis metode pengadaan yang paling umum digunakan
- Trend pengumuman pengadaan dari waktu ke waktu
- Identifikasi outliers dan data quality issues

---

## BREAK (12:00 - 13:00)

---

## Session 2: DuckDB untuk Query Analitik (13:00 - 15:30)

**Durasi:** 2.5 jam
**Format:** Interactive Python Script
**Dataset:** RUP 2025

### Materi Pembelajaran

#### 2.1 Introduction to DuckDB (30 menit)

**Konsep:**
- Apa itu DuckDB dan mengapa menggunakannya?
- OLAP vs OLTP database
- DuckDB vs Traditional Databases (PostgreSQL, MySQL)
- In-memory analytics & columnar storage
- Use cases: kapan pakai Pandas vs DuckDB

**Setup:**
- Install dan import DuckDB
- Create connection (in-memory vs persistent)
- Basic query execution

#### 2.2 SQL dengan DuckDB (90 menit)

**A. Basic SQL Operations**
- SELECT, WHERE, ORDER BY, LIMIT
- DISTINCT untuk unique values
- Agregasi: COUNT, SUM, AVG, MIN, MAX
- GROUP BY dan HAVING
- Filtering dengan multiple conditions

**B. DuckDB Specific Features**
- Read Parquet file langsung tanpa loading ke memory
- Query Pandas DataFrame dengan SQL
- Convert query result ke DataFrame
- COPY statement untuk export

**C. Advanced SQL Queries**
- JOIN operations (INNER, LEFT, RIGHT)
- Subqueries dan nested queries
- CTEs (Common Table Expressions) untuk query kompleks
- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
- CASE WHEN untuk conditional logic
- Aggregate functions dengan OVER clause

**Contoh Query dengan Dataset RUP:**
```sql
-- Top 10 Satker by Total Pagu
-- Running total of pengumuman
-- Ranking paket within kategori
-- Monthly aggregations
-- Complex filtering dengan multiple conditions
```

#### 2.3 Integration Pandas & DuckDB (30 menit)

**Workflow Integration:**
- Register Pandas DataFrame sebagai DuckDB table
- Query DuckDB table dan dapatkan hasilnya sebagai DataFrame
- Performance comparison: Pandas GroupBy vs DuckDB SQL
- Best practices: kapan pakai Pandas, kapan pakai DuckDB
- Handling large datasets efficiently

#### 📄 Script:
`day1/session2_duckdb/notebooks/01_duckdb_intro.py`

**Praktik yang Dilakukan:**
- Query top satker by pagu menggunakan SQL
- Calculate running totals dengan window functions
- Pivot analysis: metode pengadaan vs kategori
- Time series aggregation by month/quarter
- Performance benchmarking vs Pandas

---

## BREAK (15:30 - 15:45)

---

## Session 3: Data Visualization (15:45 - 17:30)

**Durasi:** 1 jam 45 menit
**Format:** Teori + Demo + Practice
**Referensi:** `day1/session3_visualization/README.md`

### Materi Pembelajaran

#### 3.1 Static Visualization dengan Matplotlib & Seaborn (45 menit)

**Matplotlib Basics:**
- Figure dan Axes architecture
- Plot types: line, bar, scatter, histogram, pie
- Customization: colors, labels, legends, grid
- Subplots untuk multiple charts
- Export ke image files (PNG, PDF)

**Seaborn untuk Statistical Plots:**
- Distribution plots: histplot, kdeplot, boxplot, violinplot
- Categorical plots: barplot, countplot, pointplot
- Relationship plots: scatterplot, regplot
- Heatmaps untuk correlation matrix
- Built-in themes dan color palettes

**Praktik dengan Dataset RUP:**
- Histogram distribusi pagu
- Box plot pagu by metode pengadaan
- Bar chart top 10 satker
- Heatmap correlation numeric variables

#### 3.2 Interactive Visualization dengan Plotly (45 menit)

**Plotly Fundamentals:**
- Plotly Express vs Graph Objects
- Interactive charts: hover, zoom, pan, select
- Chart types: line, bar, scatter, box, sunburst, treemap
- Subplots dan layout customization
- Export ke HTML untuk sharing

**Advanced Features:**
- Add annotations dan shapes
- Update layout dan styling
- Multiple traces on single chart
- Responsive design

**Praktik dengan Dataset RUP:**
- Interactive bar chart dengan hover info
- Time series line chart dengan zoom
- Scatter plot dengan color by category
- Treemap untuk hierarchical view

#### 3.3 Data Storytelling (15 menit)

**Principles:**
- Memilih chart type yang tepat untuk data
- Color theory dan accessibility (colorblind-friendly)
- Chart best practices (avoid chartjunk)
- Dashboard design principles
- Common visualization mistakes

**Chart Selection Guide:**
- Comparison → Bar chart
- Distribution → Histogram, Box plot
- Relationship → Scatter plot
- Composition → Pie chart, Treemap
- Trend → Line chart

---

## Day 1 Wrap-up (17:30 - 17:45)

- Recap: Pandas, DuckDB, Visualization
- Q&A Session
- Preview Day 2: Advanced Analysis & Streamlit Dashboard
- Optional homework: Eksplorasi dataset RUP lebih lanjut

---

# 📊 HARI 2: Advanced Analytics & Dashboard Interaktif

## Session 4: Advanced Data Analysis Techniques (09:00 - 12:00)

**Durasi:** 3 jam
**Format:** Teori + Code Examples
**Referensi:** `day2/session4_advanced_analysis/README.md`

### Materi Pembelajaran

#### 4.1 Data Cleaning & Transformation (60 menit)

**A. Handling Missing Data**
- Detection: `.isnull()`, `.isna()`, `.info()`
- Strategies:
  - Drop: `dropna()`
  - Fill: `fillna()` dengan value/mean/median
  - Forward/Backward fill: `ffill()`, `bfill()`
  - Interpolation
- Best practices untuk missing data

**B. Handling Outliers**
- Detection methods:
  - IQR (Interquartile Range) method
  - Z-score method
  - Visualization dengan box plots
- Treatment strategies:
  - Remove outliers
  - Winsorization (capping)
  - Transformation (log, sqrt)
- Kapan outliers adalah data valid vs error

**C. Encoding Categorical Variables**
- Label Encoding untuk ordinal data
- One-Hot Encoding untuk nominal data
- Target Encoding
- Frequency Encoding

**D. Feature Engineering**
- Date/time feature extraction (year, month, quarter, day of week)
- Binning continuous variables
- Creating ratio features
- Text feature engineering (length, word count)

**Contoh dengan Dataset RUP:**
- Clean nama satker yang tidak konsisten
- Handle missing values di kolom pagu
- Create features: pagu_category (small, medium, large)
- Extract features dari tanggal: month, quarter, is_end_of_year

#### 4.2 Time Series Analysis (60 menit)

**A. DateTime Operations**
- Parsing dates dengan `pd.to_datetime()`
- DateTime indexing
- Resampling: daily, weekly, monthly, quarterly
- Time zones handling

**B. Time Series Aggregations**
- Rolling windows: moving average, moving sum
- Expanding windows
- Cumulative calculations: cumsum, cumprod
- Lead and lag operations

**C. Trend Analysis**
- Growth calculations: MoM, YoY, QoQ
- Trend detection
- Seasonality analysis dengan decomposition
- Simple forecasting concepts

**Contoh dengan Dataset RUP:**
- Monthly trend of pengumuman paket
- 7-day & 30-day moving averages
- MoM growth rate calculation
- Identify peak seasons for pengadaan

#### 4.3 Statistical Analysis (60 menit)

**A. Descriptive Statistics**
- Central tendency: mean, median, mode
- Dispersion: variance, std dev, range, IQR
- Percentiles dan quantiles
- Skewness dan kurtosis

**B. Correlation Analysis**
- Pearson correlation (linear relationship)
- Spearman correlation (monotonic relationship)
- Correlation matrix visualization
- Causation vs correlation

**C. Distribution Analysis**
- Histogram analysis
- Normal distribution testing
- Q-Q plots
- Distribution fitting

**D. Hypothesis Testing Basics**
- Null hypothesis vs alternative hypothesis
- P-values interpretation
- T-test untuk comparing two groups
- Chi-square test untuk categorical data
- ANOVA untuk comparing multiple groups

**E. A/B Testing Fundamentals**
- Design A/B test
- Sample size calculation
- Statistical significance
- Interpreting results

**Contoh dengan Dataset RUP:**
- Test if pagu follows normal distribution
- Compare pagu across different metode (ANOVA)
- Correlation between pagu and other numeric variables
- Hypothesis testing: Are government procurements larger in Q4?

---

## BREAK (12:00 - 13:00)

---

## Session 5: Streamlit Dashboard Interaktif (13:00 - 17:30)

**Durasi:** 4.5 jam (termasuk break)
**Format:** Hands-on Labs
**Applications:** 4 Streamlit apps

### 5.1 Streamlit Basics - LAB 10 (13:00 - 14:00)

**App:** `01_hello_streamlit.py`

**Topik yang Dipelajari:**

**A. Text Elements**
- `st.title()`, `st.header()`, `st.subheader()`
- `st.text()` vs `st.markdown()` vs `st.write()`
- `st.code()` untuk syntax highlighting
- `st.latex()` untuk mathematical expressions
- `st.divider()` untuk separators

**B. Displaying Data**
- `st.dataframe()` - interactive sortable table
- `st.table()` - static table
- `st.metric()` - KPI cards dengan delta
- `st.json()` - formatted JSON display

**C. Status Messages**
- `st.success()`, `st.info()`, `st.warning()`, `st.error()`
- `st.spinner()` untuk loading states
- `st.progress()` untuk progress bars

**D. Basic Charts**
- `st.line_chart()`, `st.bar_chart()`, `st.area_chart()`
- Simple data visualization

**E. Layout**
- `st.columns()` untuk column layout
- `st.container()` untuk grouping
- `st.expander()` untuk collapsible sections
- `st.tabs()` untuk tabbed interface

**Praktik:**
- Buat halaman welcome dengan berbagai text elements
- Display dataset RUP dengan interactive table
- Show KPIs menggunakan metrics
- Create simple charts
- Implement responsive layout dengan columns

---

### 5.2 Interactive Components - LAB 11 (14:00 - 15:15)

**App:** `02_components_demo.py`

**Topik yang Dipelajari:**

**A. Input Widgets**
- Buttons: `st.button()`, `st.download_button()`, `st.link_button()`
- Selection: `st.checkbox()`, `st.toggle()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`
- Sliders: `st.slider()`, `st.select_slider()`
- Text input: `st.text_input()`, `st.text_area()`, `st.number_input()`
- Date & time: `st.date_input()`, `st.time_input()`
- File: `st.file_uploader()`

**B. Forms**
- `st.form()` untuk batch input submission
- Form submit button
- Validation

**C. Session State**
- Understanding Streamlit's execution model
- `st.session_state` untuk persist data
- Callbacks dan event handling
- Counter example
- Shopping cart example

**D. Sidebar**
- `st.sidebar` untuk navigation dan filters
- Organizing controls

**Praktik:**
- Build interactive counter dengan buttons
- Create todo list dengan checkboxes
- Implement filter system dengan multiple widgets
- Create registration form
- File uploader dengan preview
- Dynamic chart filtering

---

## BREAK (15:15 - 15:30)

---

### 5.3 Data Explorer - LAB 12 (15:30 - 16:45)

**App:** `03_data_explorer.py`

**Topik yang Dipelajari:**

**A. Complete Data Analysis Workflow**
- File upload (CSV, Excel, Parquet)
- Data preview dan summary statistics
- Interactive filtering system
- Multiple analysis tabs

**B. DuckDB Integration**
- `@st.cache_resource` untuk DuckDB connection
- `@st.cache_data` untuk caching data
- Dynamic SQL query building dari filters
- Query execution dan result display

**C. Interactive Filters**
- Categorical filters (multiselect)
- Numeric filters (range slider)
- Date range filters
- Apply filters button
- Real-time filtering

**D. Multiple Analysis Views**
- Tab 1: Distribution Analysis
  - Histogram untuk numeric columns
  - Pie chart untuk categorical columns
- Tab 2: Trend Analysis
  - Time series line charts
  - Moving averages
  - Growth calculations
- Tab 3: Relationship Analysis
  - Scatter plots
  - Correlation heatmap
- Tab 4: Aggregations
  - Custom groupBy operations
  - Pivot tables
  - Summary statistics by group

**E. SQL Playground**
- Custom SQL query editor
- Execute user queries
- Display results
- Error handling

**F. Export Functionality**
- Download filtered data as CSV
- Download to Excel
- Download query results

**Praktik:**
- Upload dataset RUP atau custom data
- Apply multiple filters
- Explore data dengan different views
- Write custom SQL queries
- Export results

---

### 5.4 Production Dashboard - RUP Analysis (16:45 - 17:30)

**App:** `rup_dashboard.py`

**Topik yang Dipelajari:**

**A. Production-Ready Dashboard**
- Professional UI/UX design
- Branding dan styling
- Page configuration (`st.set_page_config()`)
- Custom CSS

**B. Complex Data Processing**
- Data loading pipeline
- Caching strategy untuk performance
- Error handling
- Data validation

**C. Advanced Visualizations**
- Multiple coordinated charts
- Plotly advanced features
- Custom color schemes
- Responsive design

**D. KPIs dan Metrics**
- Key performance indicators
- Trend indicators dengan delta
- Summary statistics cards
- Comparison metrics

**E. Interactive Filters**
- Sidebar filters
- Cascading filters
- Reset functionality
- Filter state management

**F. Best Practices**
- Code organization
- Performance optimization
- User experience considerations
- Deployment preparation

**Praktik:**
- Study struktur dashboard lengkap
- Analyze code patterns
- Understand performance optimization
- Learn best practices untuk production
- Customize dashboard

---

## Day 2 Wrap-up (17:30 - 17:45)

### Review & Next Steps

**Key Takeaways:**
- Data cleaning dan preprocessing techniques
- Time series dan statistical analysis
- Building interactive dashboards dengan Streamlit
- Integration Pandas + DuckDB + Streamlit

**Resources untuk Belajar Lebih Lanjut:**
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [DuckDB Documentation](https://duckdb.org/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)

**Next Steps:**
- Practice dengan dataset lain
- Build custom dashboard untuk use case sendiri
- Explore advanced Streamlit features
- Deploy dashboard ke Streamlit Cloud

**Q&A Session**

---

## 📚 Resources & Learning Materials

### Official Documentation
- **Pandas:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- **DuckDB:** [https://duckdb.org/docs/](https://duckdb.org/docs/)
- **Streamlit:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Plotly:** [https://plotly.com/python/](https://plotly.com/python/)
- **Seaborn:** [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- **Matplotlib:** [https://matplotlib.org/](https://matplotlib.org/)

### Cheat Sheets
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Python Graph Gallery](https://python-graph-gallery.com/)

### Recommended Books
- **"Python for Data Analysis"** by Wes McKinney (Creator of Pandas)
- **"Storytelling with Data"** by Cole Nussbaumer Knaflic
- **"Practical Statistics for Data Scientists"** by Peter Bruce & Andrew Bruce

### Online Learning Platforms
- **Kaggle Learn** - Free interactive courses
- **DataCamp** - Hands-on data science courses
- **Real Python** - Python tutorials and articles
- **Towards Data Science** - Medium publication for data science

### Practice Datasets
- **Kaggle Datasets** - Thousands of datasets untuk practice
- **UCI Machine Learning Repository** - Classic datasets
- **Data.gov** - US Government open data
- **Google Dataset Search** - Search engine untuk datasets

---

## 🐛 Troubleshooting

### Installation Issues

**Problem:** `pip install` gagal
```bash
# Solution: Upgrade pip
python -m pip install --upgrade pip setuptools wheel
```

**Problem:** DuckDB import error
```bash
# Solution: Reinstall DuckDB
pip uninstall duckdb
pip install duckdb --no-cache-dir
```

**Problem:** Jupyter tidak bisa start
```bash
# Solution: Install ulang Jupyter
pip install --upgrade jupyter notebook
```

### Streamlit Issues

**Problem:** Streamlit tidak bisa start
```bash
# Check port availability
streamlit run app.py --server.port 8502
```

**Problem:** Module not found di Streamlit
```bash
# Run with correct Python interpreter
python -m streamlit run app.py
```

**Problem:** File upload size limit
```toml
# Create .streamlit/config.toml
[server]
maxUploadSize = 1000  # MB
```

### Data Loading Issues

**Problem:** File Parquet tidak bisa dibaca
```bash
# Install pyarrow
pip install pyarrow
```

**Problem:** Memory error dengan dataset besar
```python
# Use DuckDB untuk query large files
import duckdb
df = duckdb.query("SELECT * FROM 'large_file.parquet' LIMIT 10000").df()
```

---

## 💡 Tips & Best Practices

### Untuk Belajar Efektif
1. **Practice, practice, practice** - Kerjakan semua labs
2. **Eksperimen dengan dataset lain** - Jangan hanya RUP
3. **Bangun project sendiri** - Apply ke use case pribadi
4. **Join komunitas** - Stack Overflow, Reddit, Discord
5. **Read the docs** - Documentation adalah teman terbaik
6. **Version control** - Gunakan Git untuk tracking progress

### Untuk Development
1. **Use virtual environments** - Isolate dependencies
2. **Write clean code** - Follow PEP 8 style guide
3. **Comment your code** - Explain the "why", not the "what"
4. **Test incrementally** - Don't write too much before testing
5. **Cache expensive operations** - Use `@st.cache_data` di Streamlit
6. **Handle errors gracefully** - Always use try-except blocks

### Untuk Dashboard Production
1. **Optimize performance** - Cache data, use efficient queries
2. **Design for users** - Think about user experience
3. **Mobile responsive** - Test di berbagai screen sizes
4. **Error handling** - Show friendly error messages
5. **Add loading states** - Use spinners dan progress bars
6. **Documentation** - README untuk setup instructions

---

## 🚀 Next Steps

### Setelah Bootcamp
1. **Build portfolio project** - Showcase your skills
2. **Deploy your dashboard** - Use Streamlit Cloud (free)
3. **Contribute to open source** - Learn from others
4. **Explore advanced topics:**
   - Machine Learning dengan scikit-learn
   - Deep Learning dengan TensorFlow/PyTorch
   - Big Data dengan Apache Spark
   - Cloud platforms (AWS, GCP, Azure)

### Career Path Options
- **Data Analyst** - Business insights dan reporting
- **Business Intelligence** - Dashboard dan visualization
- **Data Engineer** - Data pipeline dan infrastructure
- **Data Scientist** - Machine learning dan predictive models
- **Analytics Engineer** - dbt, SQL, data modeling

### Continue Learning
- Join data science communities (Kaggle, Reddit, Discord)
- Follow data science blogs dan newsletters
- Attend meetups dan conferences
- Build personal projects dan portfolio
- Network dengan professionals di industry

---

## 📞 Support & Contact

**Untuk pertanyaan atau dukungan:**
- Email: [your-email@example.com]
- GitHub Issues: [repository-issues-url]
- Discord/Slack: [community-link]

**Feedback:**
Kami sangat menghargai feedback Anda untuk meningkatkan materi bootcamp ini. Silakan kirim feedback melalui form atau email.

---

## 📄 License

Materi bootcamp ini dibuat untuk keperluan edukasi dan dapat digunakan secara bebas untuk pembelajaran.

---

## 🙏 Acknowledgments

Terima kasih kepada:
- Komunitas open source Python, Pandas, DuckDB, dan Streamlit
- Semua contributor dan maintainer libraries yang digunakan
- Peserta bootcamp yang memberikan feedback

---

**Selamat Belajar! Happy Coding! 🎉**

*Last updated: 2024*
