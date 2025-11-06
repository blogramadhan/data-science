# Session 2 - DuckDB Notebooks

## 📝 Available Notebooks/Scripts

### ✅ 01_duckdb_intro.py
**Status:** Complete
**Topics:**
- DuckDB introduction & setup
- Basic SQL operations
- Loading data from files
- Performance comparison
- Export functionality

**Run:**
```bash
python 01_duckdb_intro.py
```

### 📋 Notebooks to Create (Exercises for Instruktur/Peserta)

#### 02_sql_basics.py
**Topics to Cover:**
```python
# JOIN Operations
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- Self JOIN

# Aggregations
- GROUP BY with multiple columns
- HAVING clause
- DISTINCT
- COUNT, SUM, AVG, MIN, MAX

# Subqueries
- Subquery in WHERE
- Subquery in SELECT
- Subquery in FROM (derived tables)

# Set Operations
- UNION, UNION ALL
- INTERSECT
- EXCEPT
```

**Sample Code Structure:**
```python
import duckdb
import pandas as pd

conn = duckdb.connect(':memory:')

# Create sample tables for JOIN practice
# ... create orders table
# ... create customers table
# ... demonstrate JOINs

# Aggregation examples
# ... GROUP BY examples
# ... HAVING examples

# Subquery examples
# ... various subquery patterns
```

---

#### 03_advanced_queries.py
**Topics to Cover:**
```python
# Window Functions
- ROW_NUMBER()
- RANK(), DENSE_RANK()
- LAG(), LEAD()
- SUM() OVER (PARTITION BY ...)
- Running totals
- Moving averages

# Common Table Expressions (CTEs)
- WITH clause
- Recursive CTEs
- Multiple CTEs

# CASE WHEN
- Simple CASE
- Searched CASE
- CASE in SELECT, WHERE, ORDER BY

# Advanced Features
- String functions (CONCAT, SUBSTRING, etc.)
- Date functions
- Type casting
- COALESCE, NULLIF
```

**Sample Code Structure:**
```python
import duckdb
from pathlib import Path

conn = duckdb.connect(':memory:')

# Load RUP dataset
data_path = Path.cwd() / '..' / '..' / '..' / 'datasets' / 'rup' / 'RUP-PaketPenyedia-Terumumkan-2025.parquet'

# Window function examples
query = '''
SELECT
    nama_paket,
    pagu,
    ROW_NUMBER() OVER (ORDER BY pagu DESC) as rank,
    SUM(pagu) OVER (ORDER BY pagu DESC) as running_total
FROM ...
'''

# CTE examples
# CASE WHEN examples
```

---

#### 04_pandas_duckdb_integration.py
**Topics to Cover:**
```python
# Pandas to DuckDB
- Register DataFrame
- Create table from DataFrame
- Insert DataFrame data

# DuckDB to Pandas
- Query result to DataFrame
- Streaming large results

# Performance Comparison
- Benchmarking queries
- Memory usage comparison
- When to use each tool

# Hybrid Workflows
- Use DuckDB for aggregations
- Use Pandas for final processing
- Best practices
```

**Sample Code Structure:**
```python
import duckdb
import pandas as pd
import time
import numpy as np

# Create test data
df = pd.read_parquet('path/to/data.parquet')

# Method 1: Pandas
start = time.time()
result_pandas = df.groupby('column').agg(...)
time_pandas = time.time() - start

# Method 2: DuckDB
conn = duckdb.connect(':memory:')
conn.register('data', df)

start = time.time()
result_duckdb = conn.execute('SELECT ... FROM data ...').df()
time_duckdb = time.time() - start

# Compare results
print(f'Pandas: {time_pandas:.4f}s')
print(f'DuckDB: {time_duckdb:.4f}s')
print(f'Speedup: {time_pandas/time_duckdb:.2f}x')
```

---

## 🎯 How to Create Notebooks

### Option 1: Write Python Scripts
1. Create `.py` files dengan struktur seperti di atas
2. Gunakan `# %%` untuk cell markers (VS Code & Jupyter)
3. Gunakan `# %% [markdown]` untuk markdown cells
4. Run dengan Python atau buka di Jupyter

### Option 2: Convert to Jupyter Notebooks
```bash
# Install jupytext
pip install jupytext

# Convert .py to .ipynb
jupytext --to notebook 01_duckdb_intro.py

# Or use nbconvert
jupyter nbconvert --to notebook *.py
```

### Option 3: Create in Jupyter Directly
```bash
# Start Jupyter
jupyter notebook

# Create new notebook
# Copy code from Python files
# Add markdown cells for explanations
```

---

## 📚 Dataset untuk Practice

### RUP Dataset
**Location:** `datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet`

**Sample Queries:**
```sql
-- Top 10 paket by pagu
SELECT nama_paket, pagu, nama_satker
FROM rup
ORDER BY pagu DESC
LIMIT 10;

-- Aggregation by metode
SELECT
    metode_pengadaan,
    COUNT(*) as total_paket,
    SUM(pagu) as total_pagu,
    AVG(pagu) as avg_pagu
FROM rup
GROUP BY metode_pengadaan
ORDER BY total_pagu DESC;

-- Window function - rank within category
SELECT
    nama_paket,
    metode_pengadaan,
    pagu,
    ROW_NUMBER() OVER (
        PARTITION BY metode_pengadaan
        ORDER BY pagu DESC
    ) as rank_in_method
FROM rup
ORDER BY metode_pengadaan, rank_in_method;
```

---

## 🎓 Exercises

### Exercise 1: Basic SQL
1. Load RUP dataset
2. Find all packages with pagu > 1 billion
3. Count packages per metode_pengadaan
4. Calculate average pagu per kategori

### Exercise 2: JOINs
Create 2 tables:
- satker (id, nama, provinsi)
- paket (id, satker_id, pagu)

Practice all JOIN types.

### Exercise 3: Window Functions
1. Rank packages by pagu (overall)
2. Rank packages by pagu within each metode
3. Calculate running total of pagu
4. Calculate moving average (last 7 days)

### Exercise 4: Performance
1. Load dataset > 100k rows
2. Benchmark 5 different queries
3. Compare Pandas vs DuckDB
4. Document findings

---

## 💡 Tips

### Writing Good SQL
```sql
-- Use meaningful aliases
SELECT
    mp.nama as metode,
    COUNT(*) as jumlah_paket
FROM metode_pengadaan mp
GROUP BY mp.nama;

-- Format for readability
SELECT
    column1,
    column2,
    SUM(column3) as total
FROM table1
WHERE condition1
    AND condition2
GROUP BY
    column1,
    column2
HAVING total > 1000
ORDER BY total DESC;

-- Use CTEs for complex queries
WITH top_satker AS (
    SELECT satker_id, SUM(pagu) as total
    FROM paket
    GROUP BY satker_id
    ORDER BY total DESC
    LIMIT 10
)
SELECT s.nama, ts.total
FROM top_satker ts
JOIN satker s ON ts.satker_id = s.id;
```

### DuckDB-Specific Tips
```python
# Read file directly
df = conn.execute("SELECT * FROM 'file.parquet'").df()

# Register Pandas DataFrame
conn.register('my_table', df)

# Parameterized queries (safe from SQL injection)
conn.execute("SELECT * FROM table WHERE id = ?", [user_id])

# Export results
conn.execute("COPY (SELECT * FROM table) TO 'output.parquet'")
```

---

## 🔗 Resources

- [DuckDB Documentation](https://duckdb.org/docs/)
- [SQL Tutorial](https://www.sqltutorial.org/)
- [Window Functions Guide](https://mode.com/sql-tutorial/sql-window-functions/)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview)

---

**Note untuk Instruktur:**
File-file Python script (02-04) bisa dibuat sebagai template/starter code untuk peserta, atau sebagai exercise yang harus dikerjakan selama bootcamp. File 01 sudah complete sebagai contoh.
