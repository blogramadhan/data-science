"""
LAB 12: Data Explorer - Integration Streamlit & DuckDB
Bootcamp Data Analysis - Python, DuckDB & Streamlit

Topik yang dipelajari:
1. File upload & data loading
2. Integration Pandas & DuckDB
3. Dynamic SQL queries
4. Interactive data filtering
5. Data visualization
6. Export functionality
7. Caching strategies
"""

import streamlit as st
import pandas as pd
import numpy as np
import duckdb
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Data Explorer",
    page_icon="🔍",
    layout="wide"
)

# ========================================
# CACHE FUNCTIONS
# ========================================
@st.cache_resource
def init_duckdb():
    """Initialize DuckDB connection"""
    return duckdb.connect(':memory:')

@st.cache_data
def load_sample_data():
    """Generate sample sales data"""
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', '2024-12-31', freq='D')

    data = {
        'date': dates,
        'product': np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], len(dates)),
        'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], len(dates)),
        'region': np.random.choice(['North', 'South', 'East', 'West'], len(dates)),
        'sales': np.random.randint(100, 10000, len(dates)),
        'quantity': np.random.randint(1, 100, len(dates)),
        'discount': np.random.uniform(0, 0.3, len(dates))
    }

    df = pd.DataFrame(data)
    df['revenue'] = df['sales'] * (1 - df['discount'])
    df['profit'] = df['revenue'] * np.random.uniform(0.1, 0.3, len(df))

    return df


def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Try to convert common date columns stored as string/object."""
    date_keywords = ("date", "tanggal", "tgl", "time", "waktu")
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            continue
        if df[col].dtype == object:
            lower_name = col.lower()
            should_try = any(keyword in lower_name for keyword in date_keywords)
            if not should_try:
                unique_ratio = df[col].nunique(dropna=True) / max(len(df[col]), 1)
                should_try = unique_ratio > 0.3  # heuristic for potential timestamps
            if should_try:
                converted = pd.to_datetime(df[col], errors='coerce')
                if converted.notna().mean() > 0.5:
                    df[col] = converted
    return df


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Central place for light preprocessing before analysis."""
    df = df.copy()
    df = convert_date_columns(df)

    # Clean string columns: strip whitespace
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
        # Replace 'nan' string back to actual NaN
        df[col] = df[col].replace('nan', pd.NA)

    return df

# ========================================
# SESSION STATE
# ========================================
if 'data' not in st.session_state:
    st.session_state.data = None

if 'conn' not in st.session_state:
    st.session_state.conn = init_duckdb()

if 'filtered_df' not in st.session_state:
    st.session_state.filtered_df = None

# ========================================
# TITLE
# ========================================
st.title("🔍 Data Explorer with DuckDB")
st.markdown("Upload your data atau gunakan sample data untuk eksplorasi interaktif")
st.divider()

# ========================================
# DATA LOADING
# ========================================
st.header("1️⃣ Load Data")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Your Data")
    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=['csv', 'xlsx', 'xls'],
        help="Max 200MB"
    )

    if uploaded_file is not None:
        try:
            with st.spinner("📥 Membaca file..."):
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

            st.session_state.data = prepare_dataframe(df)
            st.success(f"✅ File '{uploaded_file.name}' loaded successfully!")

        except Exception as e:
            st.error(f"❌ Error loading file: {e}")
            st.session_state.data = None

with col2:
    st.subheader("📊 Use Sample Data")
    st.info("""
        Sample dataset berisi data penjualan dengan kolom:
        - date, product, category, region
        - sales, quantity, discount, revenue, profit
    """)

    if st.button("Load Sample Data"):
        with st.spinner("Menyiapkan sample dataset..."):
            st.session_state.data = prepare_dataframe(load_sample_data())
        st.success("✅ Sample data loaded!")

# Check if data is loaded
if st.session_state.data is None:
    st.warning("⚠️ Please upload a file or load sample data to continue.")
    st.stop()

df = st.session_state.data

# Register DataFrame in DuckDB
st.session_state.conn.register('data', df)

st.divider()

# ========================================
# DATA OVERVIEW
# ========================================
st.header("2️⃣ Data Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Rows", f"{len(df):,}")
with col2:
    st.metric("Total Columns", len(df.columns))
with col3:
    st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
with col4:
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    st.metric("Numeric Columns", len(numeric_cols))

# Data Preview
with st.expander("👁️ Preview Data", expanded=True):
    st.dataframe(df.head(10), use_container_width=True)

# Data Info
col1, col2 = st.columns(2)

with col1:
    with st.expander("📋 Column Info"):
        info_df = pd.DataFrame({
            'Column': df.columns,
            'Type': df.dtypes.values,
            'Non-Null': df.count().values,
            'Null': df.isnull().sum().values
        })
        st.dataframe(info_df, use_container_width=True)

with col2:
    with st.expander("📊 Descriptive Statistics"):
        st.dataframe(df.describe(), use_container_width=True)

st.divider()

# ========================================
# INTERACTIVE FILTERS
# ========================================
st.header("3️⃣ Interactive Filters")

# Create filter columns
filter_cols = st.columns(4)

# Dynamic filters based on data types
filters = {}
categorical_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
date_cols = df.select_dtypes(include=['datetime64']).columns

# Add filters
with filter_cols[0]:
    if len(categorical_cols) > 0:
        cat_col = st.selectbox("Select Category Column", categorical_cols)
        if cat_col:
            # Clean up unique values (strip whitespace and remove None)
            unique_vals = df[cat_col].dropna().astype(str).str.strip().unique().tolist()
            unique_vals = sorted([v for v in unique_vals if v])  # Remove empty strings
            selected_cat = st.multiselect(
                f"Filter {cat_col}",
                unique_vals,
                default=unique_vals
            )
            # Only add filter if user selected at least one value
            if selected_cat and len(selected_cat) > 0:
                filters[cat_col] = selected_cat

with filter_cols[1]:
    if len(numeric_cols) > 0:
        num_col = st.selectbox("Select Numeric Column", numeric_cols)
        if num_col:
            min_val = float(df[num_col].min())
            max_val = float(df[num_col].max())

            # Check if min and max are different
            if min_val < max_val:
                range_vals = st.slider(
                    f"Range for {num_col}",
                    min_val, max_val,
                    (min_val, max_val)
                )
                filters[num_col] = range_vals
            else:
                st.info(f"Column '{num_col}' has only one unique value: {min_val}")
                filters[num_col] = (min_val, max_val)

with filter_cols[2]:
    if len(date_cols) > 0:
        date_col = st.selectbox("Select Date Column", date_cols)
        if date_col:
            min_date = df[date_col].min()
            max_date = df[date_col].max()
            date_range = st.date_input(
                f"Date Range for {date_col}",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )
            # Ensure we have both start and end dates
            if isinstance(date_range, tuple) and len(date_range) == 2:
                filters[date_col] = date_range
            elif len(date_range) == 2:
                filters[date_col] = tuple(date_range)

with filter_cols[3]:
    st.write("")  # Spacer
    st.write("")
    if st.button("🔄 Reset Filters"):
        st.rerun()

# Apply filters using DuckDB
def build_query(filters):
    """Build SQL query based on filters"""
    query = "SELECT * FROM data WHERE 1=1"

    for col, val in filters.items():
        if isinstance(val, list):  # Categorical
            if len(val) > 0:
                # Escape single quotes in values to prevent SQL injection
                escaped_vals = [str(v).replace("'", "''") for v in val]
                values_str = "', '".join(escaped_vals)
                query += f" AND \"{col}\" IN ('{values_str}')"
        elif isinstance(val, tuple) and len(val) == 2:  # Range or date range
            if isinstance(val[0], (int, float)):  # Numeric range
                query += f" AND \"{col}\" >= {val[0]} AND \"{col}\" <= {val[1]}"
            else:  # Date range
                query += f" AND \"{col}\" >= '{val[0]}' AND \"{col}\" <= '{val[1]}'"

    return query

# Execute query
query = build_query(filters)
try:
    filtered_df = st.session_state.conn.execute(query).df()
    st.session_state.filtered_df = filtered_df  # Store in session state for sidebar

    # Show results
    if len(filtered_df) == 0:
        st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih.")
        st.info("💡 Tip: Periksa nilai filter atau gunakan tombol 'Reset Filters'")
    else:
        st.success(f"📊 Filtered data: {len(filtered_df):,} rows (from {len(df):,} total)")

except Exception as e:
    st.error(f"❌ Error applying filters: {e}")
    st.info("Menggunakan data asli tanpa filter...")
    filtered_df = df  # Fallback to original data
    st.session_state.filtered_df = df

with st.expander("🔍 View SQL Query & Active Filters"):
    if filters:
        st.write("**Active Filters:**")
        for col, val in filters.items():
            st.write(f"- `{col}`: {val}")

        # Debug: Show available values in data for categorical filters
        st.divider()
        st.write("**Debug Info:**")
        for col, val in filters.items():
            if isinstance(val, list):
                actual_values = df[col].dropna().astype(str).str.strip().unique().tolist()
                st.write(f"- Available values in `{col}`: {sorted(actual_values)}")
                # Check if filter values exist in data
                missing = [v for v in val if v not in actual_values]
                if missing:
                    st.warning(f"⚠️ Values tidak ditemukan di data: {missing}")

        st.divider()
    st.write("**SQL Query:**")
    st.code(query, language='sql')

st.divider()

# ========================================
# DATA ANALYSIS
# ========================================
st.header("4️⃣ Data Analysis")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribution", "📈 Trends", "🔗 Relationships", "📋 Aggregations"])

with tab1:
    st.subheader("Distribution Analysis")

    col1, col2 = st.columns(2)

    with col1:
        if len(numeric_cols) > 0:
            dist_col = st.selectbox("Select column for distribution", numeric_cols, key='dist')
            if dist_col:
                fig = px.histogram(
                    filtered_df,
                    x=dist_col,
                    nbins=50,
                    title=f"Distribution of {dist_col}"
                )
                st.plotly_chart(fig, use_container_width=True)

    with col2:
        if len(categorical_cols) > 0:
            cat_dist_col = st.selectbox("Select categorical column", categorical_cols, key='cat_dist')
            if cat_dist_col:
                value_counts = filtered_df[cat_dist_col].value_counts()
                fig = px.pie(
                    values=value_counts.values,
                    names=value_counts.index,
                    title=f"Distribution of {cat_dist_col}"
                )
                st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Trend Analysis")

    if len(date_cols) > 0 and len(numeric_cols) > 0:
        col1, col2 = st.columns(2)

        with col1:
            trend_date = st.selectbox("Date column", date_cols, key='trend_date')
        with col2:
            trend_metric = st.selectbox("Metric", numeric_cols, key='trend_metric')

        if trend_date and trend_metric:
            # Aggregate by date
            trend_query = f"""
                SELECT
                    {trend_date},
                    SUM({trend_metric}) as total,
                    AVG({trend_metric}) as average,
                    COUNT(*) as count
                FROM data
                GROUP BY {trend_date}
                ORDER BY {trend_date}
            """

            trend_data = st.session_state.conn.execute(trend_query).df()

            agg_type = st.radio("Aggregation", ["Total", "Average", "Count"], horizontal=True)
            y_col = agg_type.lower()

            fig = px.line(
                trend_data,
                x=trend_date,
                y=y_col,
                title=f"{agg_type} {trend_metric} Over Time",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Need date and numeric columns for trend analysis")

with tab3:
    st.subheader("Relationship Analysis")

    if len(numeric_cols) >= 2:
        col1, col2, col3 = st.columns(3)

        with col1:
            x_col = st.selectbox("X-axis", numeric_cols, key='x_axis')
        with col2:
            y_col = st.selectbox("Y-axis", [c for c in numeric_cols if c != x_col], key='y_axis')
        with col3:
            color_col = st.selectbox("Color by (optional)", ['None'] + list(categorical_cols), key='color')

        if x_col and y_col:
            color_param = None if color_col == 'None' else color_col

            fig = px.scatter(
                filtered_df.sample(min(1000, len(filtered_df))),  # Sample for performance
                x=x_col,
                y=y_col,
                color=color_param,
                title=f"{x_col} vs {y_col}",
                trendline="ols"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Correlation
            corr = filtered_df[[x_col, y_col]].corr().iloc[0, 1]
            st.metric("Correlation Coefficient", f"{corr:.3f}")
    else:
        st.info("Need at least 2 numeric columns for relationship analysis")

with tab4:
    st.subheader("Custom Aggregations")

    col1, col2 = st.columns(2)

    with col1:
        if len(categorical_cols) > 0:
            group_col = st.selectbox("Group by", categorical_cols, key='group')
        else:
            group_col = None

    with col2:
        if len(numeric_cols) > 0:
            agg_col = st.selectbox("Aggregate column", numeric_cols, key='agg')
            agg_func = st.selectbox("Function", ["SUM", "AVG", "MIN", "MAX", "COUNT"], key='func')
        else:
            agg_col = None

    if group_col and agg_col:
        agg_query = f"""
            SELECT
                {group_col},
                {agg_func}({agg_col}) as {agg_func.lower()}_{agg_col},
                COUNT(*) as count
            FROM data
            GROUP BY {group_col}
            ORDER BY {agg_func.lower()}_{agg_col} DESC
        """

        agg_result = st.session_state.conn.execute(agg_query).df()

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(agg_result, use_container_width=True)

        with col2:
            fig = px.bar(
                agg_result,
                x=group_col,
                y=f"{agg_func.lower()}_{agg_col}",
                title=f"{agg_func} of {agg_col} by {group_col}"
            )
            st.plotly_chart(fig, use_container_width=True)

st.divider()

# ========================================
# SQL PLAYGROUND
# ========================================
st.header("5️⃣ SQL Playground")

st.info("💡 Tulis custom SQL query untuk analisis lebih lanjut. Table name: `data`")

# Show available columns
with st.expander("📋 Available Columns"):
    st.write(", ".join(df.columns.tolist()))

sql_query = st.text_area(
    "Enter SQL Query:",
    value="SELECT * FROM data LIMIT 10",
    height=100
)

col1, col2 = st.columns([1, 4])

with col1:
    execute_btn = st.button("▶️ Execute Query")

with col2:
    if st.button("📋 Sample Queries"):
        st.code("""
-- Top 5 baris by sales
SELECT *
FROM data
ORDER BY sales DESC
LIMIT 5;

-- Total sales per category
SELECT category, SUM(sales) AS total_sales
FROM data
GROUP BY category
ORDER BY total_sales DESC;

-- Filter revenue dan urutkan tanggal
SELECT date, product, revenue
FROM data
WHERE revenue > 5000
ORDER BY date DESC;

-- Pivot sederhana: rata-rata sales per region & category
SELECT region, category, AVG(sales) AS avg_sales
FROM data
GROUP BY region, category
ORDER BY region, avg_sales DESC;
        """, language='sql')

if execute_btn:
    try:
        result = st.session_state.conn.execute(sql_query).df()
        st.success(f"✅ Query executed successfully! Returned {len(result)} rows.")
        st.dataframe(result, use_container_width=True)

        # Export query result
        csv = result.to_csv(index=False)
        st.download_button(
            "📥 Download Query Result",
            data=csv,
            file_name=f"query_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Query error: {e}")

st.divider()

# ========================================
# EXPORT
# ========================================
st.header("6️⃣ Export Data")

col1, col2, col3 = st.columns(3)

with col1:
    # Export filtered data as CSV
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        "📥 Download Filtered Data (CSV)",
        data=csv,
        file_name=f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

with col2:
    # Export as Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        filtered_df.to_excel(writer, index=False, sheet_name='Data')
    excel_data = output.getvalue()

    st.download_button(
        "📥 Download Filtered Data (Excel)",
        data=excel_data,
        file_name=f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with col3:
    # Export summary statistics
    summary = filtered_df.describe().to_csv()
    st.download_button(
        "📥 Download Summary Stats",
        data=summary,
        file_name=f"summary_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

# ========================================
# SIDEBAR
# ========================================
with st.sidebar:
    st.header("🔍 Data Explorer")

    st.info("""
        **Features:**
        - Upload CSV/Excel or use sample data
        - Interactive filtering with DuckDB
        - Multiple analysis views
        - SQL playground
        - Export functionality
        - Real-time updates
    """)

    st.divider()

    st.subheader("📊 Quick Stats")
    if st.session_state.data is not None:
        # Use filtered data from session state if available
        display_df = st.session_state.get('filtered_df', st.session_state.data)
        st.metric("Current Data Size", f"{len(display_df):,} rows")
        st.metric("Total Columns", len(display_df.columns))

        # Count numeric columns from the display dataframe
        num_cols_count = len(display_df.select_dtypes(include=[np.number]).columns)
        if num_cols_count > 0:
            st.metric("Numeric Columns", num_cols_count)

    st.divider()

    st.subheader("⚙️ Settings")
    show_nulls = st.checkbox("Show null values", value=True)
    max_rows = st.slider("Max rows to display", 10, 100, 10)

    st.divider()
    st.caption("Bootcamp Data Analysis 2025")

# ========================================
# FOOTER
# ========================================
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>🎓 Bootcamp Data Analysis - Python, DuckDB & Streamlit</p>
        <p>LAB 12: Data Explorer with DuckDB Integration</p>
    </div>
""", unsafe_allow_html=True)
