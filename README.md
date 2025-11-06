# Bootcamp Data Science - Python, DuckDB & Streamlit
**Duration:** 2 Hari (16 Jam Total)

## Overview
Bootcamp intensif ini dirancang untuk membekali peserta dengan keterampilan praktis dalam analisis data menggunakan Python, DuckDB sebagai database analitik, dan Streamlit untuk membuat dashboard interaktif. Peserta akan belajar dari dasar hingga mampu membuat aplikasi data science end-to-end.

## Target Peserta
- Data Analyst yang ingin upgrade skills
- Programmer yang ingin masuk ke bidang Data Science
- Business Analyst yang ingin lebih technical
- Fresh Graduate yang ingin berkarir di bidang data

## Prerequisites
- Pemahaman dasar programming (Python preferred)
- Familiar dengan konsep database (SQL dasar)
- Laptop dengan minimal 8GB RAM
- Python 3.8+ terinstall

## Tools & Libraries yang Digunakan
```
- Python 3.8+
- Pandas
- NumPy
- DuckDB
- Streamlit
- Plotly/Matplotlib/Seaborn
- Scikit-learn
- Jupyter Notebook
```

---

# HARI 1: Fundamental Data Science & DuckDB

## Session 1: Python for Data Science (09:00 - 12:00)
**Duration:** 3 jam

### 1.1 Setup Environment (30 menit)
- [ ] Install Python & Virtual Environment
- [ ] Setup IDE (VS Code/PyCharm)
- [ ] Install required libraries
```bash
pip install pandas numpy duckdb streamlit plotly scikit-learn jupyter
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
- [ ] **LAB 1:** Manipulasi data dengan Python native

### 1.3 Pandas Essentials (90 menit)
- [ ] Series dan DataFrame
- [ ] Loading data (CSV, Excel, JSON)
- [ ] Data inspection
  - `.head()`, `.info()`, `.describe()`, `.shape`
- [ ] Data selection & filtering
  - `.loc[]`, `.iloc[]`, boolean indexing
- [ ] Data manipulation
  - Sorting, filtering, grouping
  - Handling missing values
  - Data type conversion
- [ ] Aggregation & GroupBy
- [ ] Merge, Join, Concat
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
- [ ] Installation & setup
- [ ] Create connection & database

### 2.2 SQL dengan DuckDB (60 menit)
- [ ] Basic SQL Review
  - SELECT, WHERE, ORDER BY
  - JOIN operations
  - GROUP BY & aggregations
- [ ] DuckDB specific features
  - Reading CSV/Parquet directly
  - Query result to DataFrame
  - DataFrame to SQL
- [ ] Advanced queries
  - Window functions
  - CTEs (Common Table Expressions)
  - Subqueries
- [ ] **LAB 3:** Complex queries dengan DuckDB

### 2.3 Integration Pandas & DuckDB (45 menit)
- [ ] Load data ke DuckDB
- [ ] Query DuckDB dari Python
- [ ] Convert between Pandas & DuckDB
- [ ] Performance optimization tips
- [ ] **LAB 4:** ETL Pipeline dengan Pandas & DuckDB

### 2.4 Best Practices (15 menit)
- [ ] When to use Pandas vs DuckDB
- [ ] Query optimization
- [ ] Memory management
- [ ] Data partitioning

---

## BREAK (15:30 - 15:45)

---

## Session 3: Data Visualization (15:45 - 17:30)
**Duration:** 1 jam 45 menit

### 3.1 Matplotlib & Seaborn (45 menit)
- [ ] Basic plotting dengan Matplotlib
  - Line plots, Bar charts, Histograms
  - Scatter plots, Pie charts
  - Customization (colors, labels, legends)
- [ ] Seaborn untuk statistical plots
  - Distribution plots
  - Categorical plots
  - Heatmaps & correlation matrices
- [ ] **LAB 5:** Create static visualizations

### 3.2 Plotly for Interactive Charts (45 menit)
- [ ] Introduction to Plotly
- [ ] Interactive line & bar charts
- [ ] Scatter & bubble charts
- [ ] Box plots & violin plots
- [ ] 3D visualizations
- [ ] Customization & styling
- [ ] **LAB 6:** Interactive dashboard prototype

### 3.3 Data Storytelling (15 menit)
- [ ] Choosing the right visualization
- [ ] Color theory & accessibility
- [ ] Best practices for dashboards

---

## Day 1 Wrap-up (17:30 - 17:45)
- [ ] Q&A Session
- [ ] Review key concepts
- [ ] Preview Day 2
- [ ] Mini Project Assignment (optional homework)

---

# HARI 2: Machine Learning & Streamlit Dashboard

## Session 4: Introduction to Machine Learning (09:00 - 12:00)
**Duration:** 3 jam

### 4.1 Machine Learning Fundamentals (30 menit)
- [ ] What is Machine Learning?
- [ ] Types of ML (Supervised, Unsupervised, Reinforcement)
- [ ] ML Workflow overview
- [ ] Common algorithms overview
- [ ] Introduction to Scikit-learn

### 4.2 Data Preprocessing (60 menit)
- [ ] Feature engineering
- [ ] Handling missing values
  - Imputation strategies
  - Drop vs Fill
- [ ] Encoding categorical variables
  - Label Encoding
  - One-Hot Encoding
  - Target Encoding
- [ ] Feature scaling
  - StandardScaler
  - MinMaxScaler
- [ ] Train-Test split
- [ ] **LAB 7:** Prepare dataset untuk modeling

### 4.3 Supervised Learning - Regression (45 menit)
- [ ] Linear Regression
- [ ] Multiple Linear Regression
- [ ] Model training & prediction
- [ ] Model evaluation metrics
  - MAE, MSE, RMSE, R²
- [ ] **LAB 8:** Build regression model

### 4.4 Supervised Learning - Classification (45 menit)
- [ ] Logistic Regression
- [ ] Decision Trees
- [ ] Random Forest
- [ ] Model evaluation metrics
  - Accuracy, Precision, Recall, F1-Score
  - Confusion Matrix
  - ROC-AUC
- [ ] **LAB 9:** Build classification model

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
  - `st.title()`, `st.header()`, `st.write()`
  - `st.markdown()`, `st.text()`
- [ ] Displaying data
  - `st.dataframe()`, `st.table()`
  - `st.metric()`
- [ ] **LAB 10:** Hello Streamlit app

### 5.2 Interactive Components (60 menit)
- [ ] Input widgets
  - `st.button()`, `st.slider()`
  - `st.selectbox()`, `st.multiselect()`
  - `st.text_input()`, `st.number_input()`
  - `st.date_input()`, `st.file_uploader()`
- [ ] Layout elements
  - `st.sidebar()`
  - `st.columns()`
  - `st.expander()`, `st.tabs()`
- [ ] Charts & visualizations
  - `st.line_chart()`, `st.bar_chart()`
  - `st.plotly_chart()`, `st.pyplot()`
- [ ] **LAB 11:** Interactive data explorer

### 5.3 Integration dengan DuckDB & ML Models (45 menit)
- [ ] Connect Streamlit to DuckDB
- [ ] Query data dynamically
- [ ] Display query results
- [ ] Load & use ML models
- [ ] Real-time predictions
- [ ] **LAB 12:** ML prediction dashboard

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
**Objective:** Build end-to-end Data Science application

**Requirements:**
1. Load & explore dataset menggunakan Pandas
2. Store & query data dengan DuckDB
3. Perform EDA dengan visualizations
4. Build ML model (regression atau classification)
5. Create Streamlit dashboard dengan:
   - Data overview section
   - Interactive filters
   - Visualizations
   - ML prediction interface
   - Model performance metrics

**Suggested Project Ideas:**
- Sales forecasting dashboard
- Customer churn prediction
- Product recommendation system
- Financial analysis dashboard
- Healthcare prediction system

### 6.3 Project Presentation (30 menit)
- [ ] Each team/individual presents (5-7 menit)
- [ ] Demo aplikasi
- [ ] Explain technical approach
- [ ] Discuss challenges & solutions
- [ ] Q&A

---

## Final Session: Wrap-up & Next Steps (17:30 - 17:45)

### Review & Best Practices
- [ ] Key takeaways from 2 days
- [ ] Production deployment tips
  - Streamlit Cloud
  - Docker containerization
  - Environment variables
- [ ] Performance optimization
- [ ] Security considerations

### Resources & Learning Path
- [ ] Documentation links
  - [Python Pandas](https://pandas.pydata.org/docs/)
  - [DuckDB](https://duckdb.org/docs/)
  - [Streamlit](https://docs.streamlit.io/)
  - [Scikit-learn](https://scikit-learn.org/)
- [ ] Recommended courses & books
- [ ] Communities & forums
- [ ] Career paths in Data Science

### Certificate & Closing
- [ ] Final Q&A
- [ ] Feedback collection
- [ ] Certificate distribution
- [ ] Networking session

---

## Project Structure
```
bootcamp-data-science/

   day1/
      session1_python_pandas/
         notebooks/
            01_python_review.ipynb
            02_pandas_basics.ipynb
            03_numpy_intro.ipynb
         data/
   
      session2_duckdb/
         notebooks/
            01_duckdb_intro.ipynb
            02_sql_queries.ipynb
            03_pandas_duckdb_integration.ipynb
         data/
   
      session3_visualization/
          notebooks/
             01_matplotlib_seaborn.ipynb
             02_plotly_interactive.ipynb
          examples/

   day2/
      session4_machine_learning/
         notebooks/
            01_ml_intro.ipynb
            02_preprocessing.ipynb
            03_regression.ipynb
            04_classification.ipynb
         models/
         data/
   
      session5_streamlit/
         apps/
            01_hello_streamlit.py
            02_data_explorer.py
            03_ml_dashboard.py
         components/
   
      capstone_project/
          template/
          sample_projects/
          datasets/

   datasets/
      sample_sales.csv
      customer_data.csv
      README.md

   requirements.txt
   README.md
```

---

## Installation Guide

### 1. Clone atau Download Repository
```bash
git clone <repository-url>
cd bootcamp-data-science
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
python -c "import pandas, duckdb, streamlit; print('All packages installed successfully!')"
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
streamlit run day2/session5_streamlit/apps/01_hello_streamlit.py
```

---

## Sample requirements.txt
```
pandas>=2.0.0
numpy>=1.24.0
duckdb>=0.9.0
streamlit>=1.28.0
plotly>=5.17.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
jupyter>=1.0.0
notebook>=7.0.0
openpyxl>=3.1.0
```

---

## Tips for Instructors

### Preparation
- [ ] Test all notebooks sebelum bootcamp
- [ ] Prepare backup datasets
- [ ] Setup demo environment
- [ ] Prepare troubleshooting guide
- [ ] Create feedback forms

### During Bootcamp
- [ ] Start with environment check (30 menit before)
- [ ] Encourage hands-on practice
- [ ] Use real-world examples
- [ ] Time management (stick to schedule)
- [ ] Regular breaks
- [ ] Interactive Q&A
- [ ] Help struggling participants

### After Bootcamp
- [ ] Share materials & recordings
- [ ] Collect feedback
- [ ] Provide additional resources
- [ ] Follow-up support channel (Slack/Discord)

---

## Assessment Criteria (Capstone Project)

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Data Processing** | 20% | Proper data loading, cleaning, transformation |
| **DuckDB Usage** | 15% | Effective use of DuckDB for queries |
| **Visualization** | 20% | Clear, informative, and aesthetic charts |
| **ML Model** | 25% | Model accuracy, proper evaluation, interpretation |
| **Streamlit App** | 15% | User-friendly interface, interactivity |
| **Code Quality** | 5% | Clean, documented, organized code |

---

## License
This bootcamp material is created for educational purposes.

## Contact
For questions or support, contact: [Your Contact Information]

---

**Happy Learning!**
