# Bootcamp Data Analysis - Python, DuckDB & Streamlit

**Duration:** 2 Hari (16 Jam Total)

## Overview

Bootcamp intensif ini dirancang untuk membekali peserta dengan keterampilan praktis dalam analisis data menggunakan Python, DuckDB sebagai database analitik, dan Streamlit untuk membuat dashboard interaktif. Peserta akan belajar dari dasar hingga mampu membuat aplikasi data analysis end-to-end yang profesional.

## Target Peserta

- Data Analyst yang ingin upgrade skills
- Business Analyst yang ingin lebih technical
- Programmer yang ingin masuk ke bidang Data Analytics
- Fresh Graduate yang ingin berkarir di bidang data
- Professional yang perlu mengolah dan visualisasi data

## Prerequisites

- Pemahaman dasar programming (Python preferred)
- Familiar dengan konsep database (SQL dasar)
- Laptop dengan minimal 8GB RAM
- Python 3.8+ terinstall

## Tools & Libraries yang Digunakan

- Python 3.8+
- Pandas
- NumPy
- DuckDB
- Streamlit
- Plotly/Matplotlib/Seaborn
- Jupyter Notebook

---

# HARI 1: Fundamental Data Analysis dengan Python & DuckDB

## Session 1: Python for Data Analysis (09:00 - 12:00)

**Duration:** 3 jam

### 1.1 Setup Environment (30 menit)

- [ ] Install Python & Virtual Environment
- [ ] Setup IDE (VS Code/PyCharm)
- [ ] Install required libraries

```bash
pip install pandas numpy duckdb streamlit plotly matplotlib seaborn jupyter
```

- [ ] Verify installation
- [ ] Introduction to Jupyter Notebook

### 1.2 Python Fundamentals Review (45 menit)

- [ ] Data types dan structures
  - Lists, Tuples, Dictionaries, Sets
  - List comprehension
- [ ] Functions dan Lambda
- [ ] File I/O operations
- [ ] Error handling (try-except)
- [ ] Working with dates and times
- [ ] **LAB 1:** Manipulasi data dengan Python native

### 1.3 Pandas Essentials (90 menit)

- [ ] Series dan DataFrame
- [ ] Loading data (CSV, Excel, JSON, Parquet)
- [ ] Data inspection
  - `.head()`, `.info()`, `.describe()`, `.shape`
  - `.value_counts()`, `.unique()`, `.nunique()`
- [ ] Data selection & filtering
  - `.loc[]`, `.iloc[]`, boolean indexing
  - Query method
- [ ] Data manipulation
  - Sorting, filtering, grouping
  - Handling missing values
  - Data type conversion
  - String operations
- [ ] Aggregation & GroupBy
- [ ] Merge, Join, Concat
- [ ] Pivot tables & Cross tabulation
- [ ] **LAB 2:** Exploratory Data Analysis dengan Pandas

### 1.4 NumPy Basics (15 menit)

- [ ] Arrays dan operations
- [ ] Mathematical operations
- [ ] Array indexing & slicing
- [ ] Statistical functions

---

## BREAK (12:00 - 13:00)

---

## Session 2: DuckDB untuk Data Analytics (13:00 - 15:30)

**Duration:** 2.5 jam

### 2.1 Introduction to DuckDB (30 menit)

- [ ] Apa itu DuckDB?
- [ ] DuckDB vs Traditional Databases
- [ ] Use cases & advantages
  - OLAP vs OLTP
  - In-memory analytics
  - Columnar storage
- [ ] Installation & setup
- [ ] Create connection & database

### 2.2 SQL dengan DuckDB (60 menit)

- [ ] Basic SQL Review
  - SELECT, WHERE, ORDER BY
  - LIMIT, OFFSET, DISTINCT
  - JOIN operations (INNER, LEFT, RIGHT, FULL)
  - UNION, INTERSECT, EXCEPT
  - GROUP BY & aggregations
- [ ] DuckDB specific features
  - Reading CSV/Parquet/JSON directly
  - Query result to DataFrame
  - DataFrame to SQL
  - COPY statement
- [ ] Advanced queries
  - Window functions (ROW_NUMBER, RANK, LAG, LEAD)
  - CTEs (Common Table Expressions)
  - Subqueries
  - CASE WHEN statements
- [ ] **LAB 3:** Complex queries dengan DuckDB

### 2.3 Integration Pandas & DuckDB (45 menit)

- [ ] Load data ke DuckDB dari Pandas
- [ ] Query DuckDB dari Python
- [ ] Convert between Pandas & DuckDB
- [ ] Performance comparison: Pandas vs DuckDB
- [ ] When to use which tool
- [ ] **LAB 4:** ETL Pipeline dengan Pandas & DuckDB

### 2.4 Best Practices (15 menit)

- [ ] When to use Pandas vs DuckDB
- [ ] Query optimization techniques
- [ ] Memory management
- [ ] Data partitioning strategies
- [ ] Indexing considerations

---

## BREAK (15:30 - 15:45)

---

## Session 3: Data Visualization (15:45 - 17:30)

**Duration:** 1 jam 45 menit

### 3.1 Matplotlib & Seaborn (45 menit)

- [ ] Matplotlib basics
  - Figure and Axes
  - Line plots, Bar charts, Histograms
  - Scatter plots, Pie charts
  - Subplots
  - Customization (colors, labels, legends, styles)
- [ ] Seaborn untuk statistical plots
  - Distribution plots (histplot, kdeplot, boxplot, violinplot)
  - Categorical plots (barplot, countplot, pointplot)
  - Relationship plots (scatterplot, lineplot, regplot)
  - Heatmaps & correlation matrices
  - Pair plots
- [ ] **LAB 5:** Create static visualizations

### 3.2 Plotly for Interactive Charts (45 menit)

- [ ] Introduction to Plotly
- [ ] Plotly Express vs Graph Objects
- [ ] Interactive line & bar charts
- [ ] Scatter & bubble charts
- [ ] Box plots & violin plots
- [ ] Sunburst & treemap charts
- [ ] Time series visualizations
- [ ] Customization & styling
- [ ] Adding interactivity (hover, click, zoom)
- [ ] **LAB 6:** Interactive dashboard prototype

### 3.3 Data Storytelling (15 menit)

- [ ] Choosing the right visualization
- [ ] Color theory & accessibility
- [ ] Chart best practices
- [ ] Dashboard design principles
- [ ] Common visualization mistakes

---

## Day 1 Wrap-up (17:30 - 17:45)

- [ ] Q&A Session
- [ ] Review key concepts
- [ ] Preview Day 2
- [ ] Mini Project Assignment (optional homework)

---

# HARI 2: Advanced Analytics & Interactive Dashboard

## Session 4: Advanced Data Analysis Techniques (09:00 - 12:00)

**Duration:** 3 jam

### 4.1 Data Cleaning & Transformation (60 menit)

- [ ] Handling missing data
  - Detection methods
  - Imputation strategies (mean, median, forward/backward fill)
  - Dropping vs filling
- [ ] Handling outliers
  - Detection (IQR, Z-score, visualization)
  - Treatment strategies
- [ ] Data normalization & standardization
- [ ] Encoding categorical variables
  - Label Encoding
  - One-Hot Encoding
  - Ordinal Encoding
- [ ] Feature engineering basics
  - Creating new features
  - Date/time features extraction
  - Binning & discretization
- [ ] **LAB 7:** Data cleaning pipeline

### 4.2 Time Series Analysis (60 menit)

- [ ] Working with datetime data
  - Parsing dates
  - DateTime indexing
  - Resampling & frequency conversion
- [ ] Time series aggregations
  - Rolling windows
  - Moving averages
  - Cumulative calculations
- [ ] Trend analysis
  - Year-over-Year (YoY) growth
  - Month-over-Month (MoM) growth
  - Seasonality detection
- [ ] Time series visualization
- [ ] **LAB 8:** Time series analysis project

### 4.3 Statistical Analysis (60 menit)

- [ ] Descriptive statistics
  - Central tendency (mean, median, mode)
  - Dispersion (variance, std dev, range)
  - Percentiles & quartiles
- [ ] Correlation analysis
  - Pearson, Spearman correlation
  - Correlation matrices
  - Causation vs correlation
- [ ] Distribution analysis
  - Histogram analysis
  - Normal distribution
  - Skewness & kurtosis
- [ ] Basic hypothesis testing concepts
- [ ] A/B testing fundamentals
- [ ] **LAB 9:** Statistical analysis on real dataset

---

## BREAK (12:00 - 13:00)

---

## Session 5: Streamlit untuk Dashboard Interaktif (13:00 - 15:30)

**Duration:** 2.5 jam

### 5.1 Streamlit Basics (45 menit)

- [ ] Introduction to Streamlit
- [ ] Setup & first app
- [ ] Running Streamlit apps
- [ ] Basic components
  - `st.title()`, `st.header()`, `st.subheader()`
  - `st.write()`, `st.markdown()`, `st.text()`
- [ ] Displaying data
  - `st.dataframe()`, `st.table()`
  - `st.metric()` for KPIs
  - `st.json()`
- [ ] **LAB 10:** Hello Streamlit app

### 5.2 Interactive Components (60 menit)

- [ ] Input widgets
  - `st.button()`, `st.checkbox()`, `st.radio()`
  - `st.slider()`, `st.select_slider()`
  - `st.selectbox()`, `st.multiselect()`
  - `st.text_input()`, `st.number_input()`
  - `st.date_input()`, `st.time_input()`
  - `st.file_uploader()`
- [ ] Layout elements
  - `st.sidebar()` for navigation
  - `st.columns()` for grid layouts
  - `st.expander()` for collapsible sections
  - `st.tabs()` for multiple views
  - `st.container()`
- [ ] Charts & visualizations
  - Native charts: `st.line_chart()`, `st.bar_chart()`, `st.area_chart()`
  - `st.plotly_chart()` for Plotly
  - `st.pyplot()` for Matplotlib
- [ ] Session state management
- [ ] Caching with `@st.cache_data`
- [ ] **LAB 11:** Interactive data explorer

### 5.3 Integration dengan DuckDB (45 menit)

- [ ] Connect Streamlit to DuckDB
- [ ] Dynamic query execution
- [ ] Display query results
- [ ] Interactive filtering with DuckDB
- [ ] Performance optimization
- [ ] File upload & analysis
- [ ] Export results (CSV, Excel)
- [ ] **LAB 12:** Complete analytics dashboard

---

## BREAK (15:30 - 15:45)

---

## Session 6: Capstone Project (15:45 - 17:30)

**Duration:** 1 jam 45 menit

### 6.1 Project Brief (15 menit)

- [ ] Project requirements overview
- [ ] Dataset introduction
- [ ] Success criteria
- [ ] Team formation (if group project)

### 6.2 Project Development (60 menit)

**Objective:** Build end-to-end Data Analytics Dashboard

**Requirements:**

1. Load & explore dataset menggunakan Pandas
2. Store & query data dengan DuckDB
3. Perform comprehensive EDA dengan visualizations
4. Clean & transform data
5. Generate insights & statistical analysis
6. Create Streamlit dashboard dengan:
   - Data overview section (summary statistics, data quality checks)
   - Interactive filters (date range, categories, etc)
   - Multiple visualizations (charts, graphs, tables)
   - Key Performance Indicators (KPIs)
   - Export functionality
   - Professional UI/UX design

**Suggested Project Ideas:**

- **Sales Analysis Dashboard**
  - Revenue trends, product performance
  - Customer segmentation
  - Regional analysis

- **E-commerce Analytics**
  - Customer behavior analysis
  - Product recommendations
  - Conversion funnel analysis

- **HR Analytics Dashboard**
  - Employee performance metrics
  - Attrition analysis
  - Department insights

- **Financial Analysis Dashboard**
  - Expense tracking & budgeting
  - Profit & loss analysis
  - Financial forecasting

- **Marketing Campaign Analysis**
  - Campaign performance metrics
  - ROI analysis
  - Channel effectiveness

### 6.3 Project Presentation (30 menit)

- [ ] Each team/individual presents (5-7 menit)
- [ ] Demo aplikasi
- [ ] Explain insights discovered
- [ ] Discuss technical approach
- [ ] Challenges & solutions
- [ ] Q&A

---

## Final Session: Wrap-up & Next Steps (17:30 - 17:45)

### Review & Best Practices

- [ ] Key takeaways from 2 days
- [ ] Data analysis workflow recap
- [ ] Production deployment tips
  - Streamlit Cloud (Community/Enterprise)
  - Docker containerization
  - Environment variables & secrets
- [ ] Performance optimization tips
- [ ] Security considerations
- [ ] Data privacy & ethics

### Resources & Learning Path

- [ ] Documentation links
  - [Python Pandas](https://pandas.pydata.org/docs/)
  - [DuckDB](https://duckdb.org/docs/)
  - [Streamlit](https://docs.streamlit.io/)
  - [Plotly](https://plotly.com/python/)
  - [Seaborn](https://seaborn.pydata.org/)
- [ ] Recommended books
  - "Python for Data Analysis" by Wes McKinney
  - "Storytelling with Data" by Cole Nussbaumer Knaflic
- [ ] Online communities
  - Stack Overflow
  - Reddit (r/datascience, r/dataanalysis)
  - Kaggle
- [ ] Practice datasets
  - Kaggle Datasets
  - UCI Machine Learning Repository
  - Government open data portals
- [ ] Career paths in Data Analytics

### Certificate & Closing

- [ ] Final Q&A
- [ ] Feedback collection
- [ ] Certificate distribution
- [ ] Networking session

---

## Project Structure

```
bootcamp-data-analysis/
│
├── day1/
│   ├── session1_python_pandas/
│   │   ├── notebooks/
│   │   │   ├── 01_python_review.ipynb
│   │   │   ├── 02_pandas_basics.ipynb
│   │   │   ├── 03_pandas_advanced.ipynb
│   │   │   └── 04_numpy_intro.ipynb
│   │   └── data/
│   │
│   ├── session2_duckdb/
│   │   ├── notebooks/
│   │   │   ├── 01_duckdb_intro.ipynb
│   │   │   ├── 02_sql_basics.ipynb
│   │   │   ├── 03_advanced_queries.ipynb
│   │   │   └── 04_pandas_duckdb_integration.ipynb
│   │   └── data/
│   │
│   └── session3_visualization/
│       ├── notebooks/
│       │   ├── 01_matplotlib_seaborn.ipynb
│       │   ├── 02_plotly_interactive.ipynb
│       │   └── 03_data_storytelling.ipynb
│       └── examples/
│
├── day2/
│   ├── session4_advanced_analysis/
│   │   ├── notebooks/
│   │   │   ├── 01_data_cleaning.ipynb
│   │   │   ├── 02_time_series.ipynb
│   │   │   └── 03_statistical_analysis.ipynb
│   │   └── data/
│   │
│   ├── session5_streamlit/
│   │   ├── apps/
│   │   │   ├── 01_hello_streamlit.py
│   │   │   ├── 02_components_demo.py
│   │   │   ├── 03_data_explorer.py
│   │   │   └── 04_analytics_dashboard.py
│   │   ├── components/
│   │   └── utils/
│   │
│   └── capstone_project/
│       ├── template/
│       │   ├── app.py
│       │   ├── utils.py
│       │   └── config.py
│       ├── sample_projects/
│       │   ├── sales_dashboard/
│       │   ├── hr_analytics/
│       │   └── financial_dashboard/
│       └── datasets/
│
├── datasets/
│   ├── sales/
│   │   ├── sales_data.csv
│   │   └── README.md
│   ├── ecommerce/
│   │   ├── orders.csv
│   │   ├── customers.csv
│   │   └── README.md
│   └── hr/
│       ├── employees.csv
│       └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation Guide

### 1. Clone atau Download Repository

```bash
git clone <repository-url>
cd bootcamp-data-analysis
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import pandas, duckdb, streamlit, plotly; print('All packages installed successfully!')"
```

---

## Running the Materials

### Jupyter Notebooks

```bash
jupyter notebook
# Navigate to day1/ or day2/ folders
```

### Streamlit Apps

```bash
# Run basic app
streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py

# Run dashboard
streamlit run day2/session5_streamlit/apps/04_analytics_dashboard.py
```

---

## Sample requirements.txt

```
# Data Processing
pandas>=2.0.0
numpy>=1.24.0
duckdb>=0.9.0
openpyxl>=3.1.0
pyarrow>=14.0.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0

# Dashboard
streamlit>=1.28.0

# Development
jupyter>=1.0.0
notebook>=7.0.0
ipykernel>=6.25.0

# Utilities
python-dotenv>=1.0.0
```

---

## Tips for Instructors

### Preparation

- [ ] Test all notebooks sebelum bootcamp
- [ ] Prepare multiple datasets (different domains)
- [ ] Setup demo environment & backup laptop
- [ ] Prepare troubleshooting guide
- [ ] Create feedback forms (pre & post)
- [ ] Prepare certificates template
- [ ] Setup communication channel (Slack/WhatsApp group)

### During Bootcamp

- [ ] Start with environment check (30 menit before)
- [ ] Ice breaking session
- [ ] Encourage hands-on practice
- [ ] Use real-world examples & case studies
- [ ] Time management (stick to schedule)
- [ ] Regular breaks (importance!)
- [ ] Interactive Q&A after each session
- [ ] Help struggling participants individually
- [ ] Take photos for documentation
- [ ] Collect attendance

### After Bootcamp

- [ ] Share all materials & recordings
- [ ] Share additional datasets
- [ ] Collect feedback (survey)
- [ ] Provide additional resources
- [ ] Setup follow-up support channel (Slack/Discord)
- [ ] Alumni network for future collaboration
- [ ] Certificate distribution
- [ ] Post-bootcamp project showcase (optional)

---

## Assessment Criteria (Capstone Project)

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Data Quality & Cleaning** | 20% | Proper data loading, cleaning, handling missing values |
| **DuckDB Usage** | 15% | Effective use of DuckDB for queries and analysis |
| **Data Analysis** | 20% | Quality of insights, statistical analysis, EDA |
| **Visualization** | 20% | Clear, informative, and aesthetic charts |
| **Streamlit Dashboard** | 20% | User-friendly interface, interactivity, design |
| **Code Quality** | 5% | Clean, documented, organized code |

**Total: 100%**

**Grading Scale:**
- A (90-100): Excellent - Production ready dashboard
- B (80-89): Good - Well-functioning dashboard with minor improvements needed
- C (70-79): Satisfactory - Basic requirements met
- D (60-69): Needs Improvement - Missing key components
- F (<60): Incomplete

---

## Common Issues & Troubleshooting

### Installation Issues

**Problem:** pip install fails
```bash
# Solution: Upgrade pip
python -m pip install --upgrade pip
```

**Problem:** DuckDB import error
```bash
# Solution: Reinstall DuckDB
pip uninstall duckdb
pip install duckdb --no-cache-dir
```

### Streamlit Issues

**Problem:** Streamlit won't start
```bash
# Check port availability
streamlit run app.py --server.port 8502
```

**Problem:** Module not found in Streamlit
```bash
# Run with correct Python interpreter
python -m streamlit run app.py
```

---

## Additional Resources

### Cheat Sheets

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Video Tutorials

- Python for Data Analysis (YouTube)
- Streamlit Official Tutorials
- Plotly Chart Examples

### Practice Platforms

- Kaggle Learn
- DataCamp
- LeetCode (SQL)
- HackerRank (SQL & Python)

---

## License

This bootcamp material is created for educational purposes.

## Contact

For questions or support, contact: [Your Contact Information]

---

## Changelog

**Version 1.0** (2024)
- Initial release
- Focus on Data Analysis (removed Machine Learning)
- Added Advanced Analytics session
- Enhanced Time Series Analysis
- Expanded Statistical Analysis section

---

**Happy Learning!**
