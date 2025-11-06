# Session 2: DuckDB untuk Data Analytics

**Duration:** 2.5 jam (13:00 - 15:30)

## 📚 Overview

Session ini membahas penggunaan DuckDB sebagai database analitik untuk data analysis. DuckDB adalah embedded analytical database yang sangat cepat dan mudah digunakan untuk analisis data.

## 🎯 Learning Objectives

Setelah session ini, peserta akan mampu:
- Memahami konsep OLAP vs OLTP
- Menggunakan DuckDB untuk SQL analytics
- Integrasi DuckDB dengan Pandas
- Melakukan complex queries dan aggregations
- Optimize query performance

## 📁 Materi

### 1. Introduction to DuckDB (30 menit)
**Topik:**
- Apa itu DuckDB?
- DuckDB vs Traditional Databases (PostgreSQL, MySQL)
- Use cases & advantages
- OLAP vs OLTP
- In-memory analytics
- Columnar storage

**Script:** Baca dokumentasi dan jalankan `01_duckdb_intro.py`

### 2. SQL dengan DuckDB (60 menit)
**Topik:**
- Basic SQL Review (SELECT, WHERE, ORDER BY, LIMIT)
- JOIN operations
- GROUP BY & aggregations
- DuckDB specific features
- Reading CSV/Parquet directly
- Advanced queries (Window functions, CTEs, Subqueries)

**Script:** `02_sql_basics.py` dan `03_advanced_queries.py`

### 3. Integration Pandas & DuckDB (45 menit)
**Topik:**
- Load data ke DuckDB dari Pandas
- Query DuckDB dari Python
- Convert between Pandas & DuckDB
- Performance comparison
- When to use which tool

**Script:** `04_pandas_duckdb_integration.py`

### 4. Best Practices (15 menit)
**Topik:**
- Query optimization
- Memory management
- Indexing considerations

## 🚀 Quick Start

### Prerequisites
```bash
pip install duckdb pandas pyarrow
```

### Jalankan Scripts

#### Option 1: Jupyter Notebook
```bash
# Convert Python scripts to notebooks (optional)
jupyter nbconvert --to notebook *.py

# Or run in Jupyter
jupyter notebook
```

#### Option 2: Direct Python Execution
```bash
# Jalankan setiap script
python 01_duckdb_intro.py
python 02_sql_basics.py
python 03_advanced_queries.py
python 04_pandas_duckdb_integration.py
```

#### Option 3: Interactive Python
```bash
python -i 01_duckdb_intro.py
# Setelah script selesai, Anda bisa explore lebih lanjut
```

## 📝 Scripts

### 01_duckdb_intro.py
- Setup DuckDB connection
- Create first database
- Basic queries
- Load sample data

### 02_sql_basics.py
- SELECT, WHERE, ORDER BY
- JOIN operations
- GROUP BY & aggregations
- Reading files directly

### 03_advanced_queries.py
- Window functions (ROW_NUMBER, RANK, LAG, LEAD)
- Common Table Expressions (CTEs)
- Subqueries
- CASE WHEN statements
- Complex aggregations

### 04_pandas_duckdb_integration.py
- Load Pandas DataFrame to DuckDB
- Query DuckDB, get Pandas DataFrame
- Performance benchmarks
- Use cases for each tool

## 🎓 Exercises

### Exercise 1: Basic Queries
1. Load dataset RUP ke DuckDB
2. Filter paket dengan pagu > 1 miliar
3. Group by metode_pengadaan
4. Calculate total pagu per metode

### Exercise 2: Advanced Analytics
1. Find top 10 satker by total pagu
2. Calculate running total of pagu by date
3. Rank paket by pagu within each kategori
4. Create pivot table: metode vs kategori

### Exercise 3: Performance Comparison
1. Load large dataset (>100k rows)
2. Run same query in Pandas and DuckDB
3. Compare execution time
4. Document findings

## 💡 Key Concepts

### OLAP vs OLTP
```
OLAP (DuckDB):
- Analytical queries
- Read-heavy
- Aggregations
- Complex queries
- Column-oriented

OLTP (PostgreSQL, MySQL):
- Transactional
- Write-heavy
- Row-level operations
- Simple queries
- Row-oriented
```

### DuckDB Advantages
1. **Zero-dependency** - No server needed
2. **Fast** - Optimized for analytics
3. **SQL** - Standard SQL support
4. **Integration** - Easy Pandas integration
5. **File formats** - Direct CSV/Parquet reading

### When to Use DuckDB
- ✅ Analytical queries on medium-sized data (< 10GB)
- ✅ Rapid prototyping & exploration
- ✅ Local data analysis
- ✅ Integration with Python/Pandas workflows
- ❌ Production transactional systems
- ❌ Multi-user concurrent writes
- ❌ Distributed systems

## 📊 Dataset

Gunakan dataset RUP yang sudah tersedia:
```
datasets/rup/RUP-PaketPenyedia-Terumumkan-2025.parquet
```

Atau download dataset lain untuk practice.

## 🔗 Resources

### Official Documentation
- [DuckDB Docs](https://duckdb.org/docs/)
- [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview)

### Tutorials
- [DuckDB vs Pandas Performance](https://duckdb.org/2021/05/14/sql-on-pandas.html)
- [Working with Parquet Files](https://duckdb.org/docs/data/parquet)

### Cheat Sheets
- [SQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)
- [Window Functions Guide](https://mode.com/sql-tutorial/sql-window-functions/)

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError: No module named 'duckdb'
```bash
pip install duckdb
```

### Issue: Memory error with large files
```python
# Use streaming or chunking
conn.execute("COPY table TO 'output.parquet' (FORMAT PARQUET)")
```

### Issue: SQL syntax error
- Check DuckDB SQL dialect differences
- Use parameterized queries for safety

## 📚 Further Reading

- DuckDB Paper: "DuckDB: an Embeddable Analytical Database"
- Blog: "Why DuckDB?"
- Comparison: DuckDB vs SQLite vs Pandas

---

**Next Session:** [Session 3 - Data Visualization](../session3_visualization/)

**Previous Session:** [Session 1 - Python & Pandas](../session1_python_pandas/)
