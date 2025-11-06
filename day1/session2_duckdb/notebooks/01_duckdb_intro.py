"""
Session 2.1: Introduction to DuckDB
Bootcamp Data Analysis - Python, DuckDB & Streamlit

Topics:
1. What is DuckDB?
2. Setup and first connection
3. Basic SQL operations
4. Loading data
"""

# %% [markdown]
# # Introduction to DuckDB
#
# DuckDB adalah embedded analytical database yang:
# - Fast untuk analytical queries
# - Zero-dependency (no server needed)
# - Support standard SQL
# - Easy integration dengan Python/Pandas

# %%
import duckdb
import pandas as pd
import numpy as np
from pathlib import Path

print("DuckDB version:", duckdb.__version__)

# %% [markdown]
# ## 1. Create Connection

# %%
# In-memory database
conn = duckdb.connect(':memory:')
print("✅ Connected to DuckDB (in-memory)")

# %%
# Or persistent database
# conn = duckdb.connect('my_database.db')

# %% [markdown]
# ## 2. Basic SQL Operations

# %%
# Create table
conn.execute("""
    CREATE TABLE employees (
        id INTEGER,
        name VARCHAR,
        department VARCHAR,
        salary INTEGER
    )
""")

print("✅ Table 'employees' created")

# %%
# Insert data
conn.execute("""
    INSERT INTO employees VALUES
        (1, 'Alice', 'Engineering', 75000),
        (2, 'Bob', 'Sales', 65000),
        (3, 'Charlie', 'Engineering', 80000),
        (4, 'David', 'Marketing', 60000),
        (5, 'Eve', 'Engineering', 85000)
""")

print("✅ Data inserted")

# %%
# Simple SELECT
result = conn.execute("SELECT * FROM employees").df()
print("\n📊 All Employees:")
print(result)

# %%
# WHERE clause
result = conn.execute("""
    SELECT * FROM employees
    WHERE department = 'Engineering'
""").df()
print("\n👨‍💻 Engineering Department:")
print(result)

# %%
# ORDER BY
result = conn.execute("""
    SELECT * FROM employees
    ORDER BY salary DESC
""").df()
print("\n💰 Employees by Salary (Highest first):")
print(result)

# %%
# Aggregations
result = conn.execute("""
    SELECT
        department,
        COUNT(*) as employee_count,
        AVG(salary) as avg_salary,
        MAX(salary) as max_salary
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
""").df()
print("\n📊 Department Statistics:")
print(result)

# %% [markdown]
# ## 3. Loading Data from Files
#
# DuckDB can read files directly without loading into memory first!

# %%
# Find RUP dataset path
project_root = Path.cwd().parent.parent.parent
data_path = project_root / 'datasets' / 'rup' / 'RUP-PaketPenyedia-Terumumkan-2025.parquet'

if data_path.exists():
    print(f"✅ Found dataset: {data_path}")

    # Read Parquet file directly with SQL!
    query = f"""
        SELECT * FROM '{data_path}' LIMIT 10
    """

    df = conn.execute(query).df()
    print("\n📊 RUP Data (first 10 rows):")
    print(df.head())

    # Get row count
    count_query = f"SELECT COUNT(*) as total FROM '{data_path}'"
    total = conn.execute(count_query).fetchone()[0]
    print(f"\n📈 Total records in RUP dataset: {total:,}")

    # Get column info
    info_query = f"DESCRIBE SELECT * FROM '{data_path}'"
    columns_info = conn.execute(info_query).df()
    print("\n📋 Dataset Columns:")
    print(columns_info)

else:
    print(f"⚠️ Dataset not found at: {data_path}")
    print("Creating sample data instead...")

    # Create sample data
    sample_data = pd.DataFrame({
        'nama_paket': ['Paket A', 'Paket B', 'Paket C'],
        'pagu': [1000000000, 2000000000, 1500000000],
        'metode_pengadaan': ['Tender', 'Tender', 'Penunjukan Langsung']
    })

    conn.register('rup_sample', sample_data)
    result = conn.execute("SELECT * FROM rup_sample").df()
    print("\n📊 Sample RUP Data:")
    print(result)

# %% [markdown]
# ## 4. Performance Demonstration

# %%
# Create larger dataset for performance test
print("\n⏱️ Performance Test...")

# Generate sample data
np.random.seed(42)
n_rows = 100000

large_df = pd.DataFrame({
    'id': range(n_rows),
    'value': np.random.randint(0, 1000, n_rows),
    'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows)
})

print(f"Created dataset with {n_rows:,} rows")

# %%
# Method 1: Pandas aggregation
import time

start = time.time()
pandas_result = large_df.groupby('category')['value'].agg(['sum', 'mean', 'count'])
pandas_time = time.time() - start

print(f"\n🐼 Pandas aggregation: {pandas_time:.4f} seconds")
print(pandas_result)

# %%
# Method 2: DuckDB aggregation
conn.register('large_data', large_df)

start = time.time()
duckdb_result = conn.execute("""
    SELECT
        category,
        SUM(value) as sum,
        AVG(value) as mean,
        COUNT(*) as count
    FROM large_data
    GROUP BY category
""").df()
duckdb_time = time.time() - start

print(f"\n🦆 DuckDB aggregation: {duckdb_time:.4f} seconds")
print(duckdb_result)

# %%
# Comparison
speedup = pandas_time / duckdb_time
print(f"\n⚡ DuckDB is {speedup:.2f}x faster for this query!")

# %% [markdown]
# ## 5. Export Results

# %%
# Export to CSV
conn.execute("""
    COPY (
        SELECT * FROM employees
    ) TO 'employees_export.csv' (HEADER, DELIMITER ',')
""")
print("✅ Exported to employees_export.csv")

# %%
# Export to Parquet
conn.execute("""
    COPY (
        SELECT * FROM employees
    ) TO 'employees_export.parquet' (FORMAT PARQUET)
""")
print("✅ Exported to employees_export.parquet")

# %% [markdown]
# ## 📚 Key Takeaways
#
# 1. DuckDB is fast for analytical queries
# 2. Can read files directly without loading to memory
# 3. Standard SQL syntax
# 4. Easy Python integration
# 5. Perfect for local data analysis
#
# **Next:** Advanced SQL queries and Pandas integration

# %%
# Clean up
conn.close()
print("\n✅ Connection closed")

# %%
# Summary
print("""
✅ Session 2.1 Complete!

What we learned:
- Creating DuckDB connection
- Basic SQL operations (SELECT, WHERE, ORDER BY)
- Aggregations (COUNT, AVG, MAX, SUM)
- Reading files directly (Parquet, CSV)
- Performance comparison with Pandas
- Export results

Next: 02_sql_basics.py - Advanced SQL queries
""")
