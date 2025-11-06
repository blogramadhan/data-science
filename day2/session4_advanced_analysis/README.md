# Session 4: Advanced Data Analysis Techniques

**Duration:** 3 jam (09:00 - 12:00)

## 📚 Overview

Session ini membahas teknik-teknik advanced untuk data cleaning, transformation, time series analysis, dan statistical analysis. Session ini akan mempersiapkan peserta untuk membuat dashboard yang comprehensive.

## 🎯 Learning Objectives

Setelah session ini, peserta akan mampu:
- Melakukan data cleaning dan handling missing values
- Mendeteksi dan handle outliers
- Perform feature engineering
- Analyze time series data
- Conduct statistical analysis
- Apply hypothesis testing basics

## 📁 Materi

### 1. Data Cleaning & Transformation (60 menit)

#### Handling Missing Data
```python
# Detection
df.isnull().sum()
df.info()
df.isna().sum() / len(df) * 100  # percentage

# Strategies
df.dropna()  # Drop missing
df.fillna(value)  # Fill with value
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill
df.fillna(df.mean())  # Fill with mean
df.interpolate()  # Interpolate
```

#### Handling Outliers
```python
# Detection methods
- IQR method
- Z-score method
- Visualization (box plots)

# Treatment strategies
- Remove outliers
- Cap values (winsorization)
- Transform (log, sqrt)
- Keep if valid
```

#### Data Normalization & Standardization
```python
# Normalization (0-1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df)

# Standardization (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_standardized = scaler.fit_transform(df)
```

#### Encoding Categorical Variables
```python
# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# One-Hot Encoding
pd.get_dummies(df['category'])
pd.get_dummies(df, columns=['category'])

# Ordinal Encoding (for ordered categories)
mapping = {'Low': 1, 'Medium': 2, 'High': 3}
df['priority_encoded'] = df['priority'].map(mapping)
```

#### Feature Engineering
```python
# Date features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['quarter'] = df['date'].dt.quarter
df['is_weekend'] = df['date'].dt.dayofweek >= 5

# Binning
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100],
                         labels=['Young', 'Adult', 'Middle', 'Senior'])

# Combine features
df['total'] = df['quantity'] * df['price']
df['ratio'] = df['value1'] / df['value2']
```

### 2. Time Series Analysis (60 menit)

#### Working with DateTime
```python
# Parsing dates
df['date'] = pd.to_datetime(df['date'])

# DateTime indexing
df.set_index('date', inplace=True)

# Resampling
df.resample('D').sum()  # Daily
df.resample('W').mean()  # Weekly
df.resample('M').sum()  # Monthly
df.resample('Q').mean()  # Quarterly
df.resample('Y').sum()  # Yearly
```

#### Time Series Aggregations
```python
# Rolling windows
df['rolling_mean_7d'] = df['value'].rolling(window=7).mean()
df['rolling_sum_30d'] = df['value'].rolling(window=30).sum()

# Moving averages
df['SMA_7'] = df['close'].rolling(window=7).mean()
df['EMA_7'] = df['close'].ewm(span=7, adjust=False).mean()

# Cumulative calculations
df['cumsum'] = df['value'].cumsum()
df['cumprod'] = df['value'].cumprod()
```

#### Trend Analysis
```python
# YoY (Year-over-Year) growth
df['yoy_growth'] = df['value'].pct_change(periods=12) * 100

# MoM (Month-over-Month) growth
df['mom_growth'] = df['value'].pct_change(periods=1) * 100

# Seasonality detection
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['value'], model='additive', period=12)
result.plot()
```

### 3. Statistical Analysis (60 menit)

#### Descriptive Statistics
```python
# Central tendency
df['value'].mean()
df['value'].median()
df['value'].mode()

# Dispersion
df['value'].var()  # Variance
df['value'].std()  # Standard deviation
df['value'].min()
df['value'].max()
df['value'].range()  # max - min

# Percentiles
df['value'].quantile([0.25, 0.5, 0.75])
df['value'].describe()
```

#### Correlation Analysis
```python
# Pearson correlation
df.corr(method='pearson')

# Spearman correlation
df.corr(method='spearman')

# Correlation matrix
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Pairwise correlation
df['col1'].corr(df['col2'])
```

#### Distribution Analysis
```python
# Histogram
df['value'].hist(bins=50)

# Normal distribution test
from scipy import stats
statistic, pvalue = stats.normaltest(df['value'])

# Skewness & Kurtosis
df['value'].skew()  # Measure of asymmetry
df['value'].kurt()  # Measure of tailedness
```

#### Basic Hypothesis Testing
```python
# T-test (compare two groups)
from scipy import stats
group1 = df[df['category'] == 'A']['value']
group2 = df[df['category'] == 'B']['value']
t_stat, p_value = stats.ttest_ind(group1, group2)

# Chi-square test (categorical data)
from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df['cat1'], df['cat2'])
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# ANOVA (compare multiple groups)
groups = [df[df['category'] == cat]['value'] for cat in df['category'].unique()]
f_stat, p_value = stats.f_oneway(*groups)
```

#### A/B Testing Fundamentals
```python
# Define hypotheses
# H0: No difference between groups
# H1: Significant difference exists

# Calculate conversion rates
conversion_A = df[df['group'] == 'A']['converted'].mean()
conversion_B = df[df['group'] == 'B']['converted'].mean()

# Statistical test
from scipy.stats import proportions_ztest
counts = np.array([conversions_A_count, conversions_B_count])
nobs = np.array([total_A, total_B])
z_stat, p_value = proportions_ztest(counts, nobs)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print(f"Significant difference (p={p_value:.4f})")
else:
    print(f"No significant difference (p={p_value:.4f})")
```

## 🎓 Practical Exercises

### Exercise 1: Data Cleaning Pipeline
```python
# Using RUP dataset:
1. Identify missing values per column
2. Handle missing values appropriately
3. Detect outliers in 'pagu' column
4. Handle outliers using IQR method
5. Create categorical encoding for 'metode_pengadaan'
6. Create new features from date columns
```

### Exercise 2: Time Series Analysis
```python
# Using RUP dataset:
1. Aggregate pengumuman by month
2. Calculate rolling average (7-day, 30-day)
3. Calculate MoM growth rate
4. Identify seasonal patterns
5. Visualize trend with decomposition
```

### Exercise 3: Statistical Analysis
```python
# Using RUP dataset:
1. Calculate descriptive statistics for 'pagu'
2. Create correlation matrix for numeric columns
3. Test if 'pagu' follows normal distribution
4. Compare pagu distribution across methods (ANOVA)
5. Create visualizations for findings
```

### Exercise 4: Complete Analysis Pipeline
```python
# End-to-end analysis:
1. Load and clean data
2. Handle missing values and outliers
3. Create new features
4. Perform time series analysis
5. Calculate statistics
6. Create comprehensive report with visualizations
```

## 💡 Best Practices

### Data Cleaning
1. **Document everything** - Keep track of cleaning steps
2. **Make copies** - Never modify original data directly
3. **Validate results** - Check data after each transformation
4. **Be consistent** - Use same methods across similar data
5. **Consider domain knowledge** - Not all outliers are errors

### Feature Engineering
1. **Start simple** - Basic features often work best
2. **Domain knowledge** - Use business understanding
3. **Test iteratively** - One feature at a time
4. **Avoid data leakage** - Don't use future information
5. **Document** - Explain feature logic

### Statistical Analysis
1. **Check assumptions** - Each test has requirements
2. **Choose right test** - Match test to data type
3. **Consider sample size** - Larger samples = more reliable
4. **Report properly** - Include statistics and p-values
5. **Don't p-hack** - Avoid fishing for significance

## 🔧 Code Templates

### Data Cleaning Template
```python
import pandas as pd
import numpy as np

def clean_data(df):
    """Complete data cleaning pipeline"""
    df = df.copy()

    # 1. Handle duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    # Check missing percentages
    missing_pct = df.isnull().sum() / len(df) * 100
    print("Missing values (%):\n", missing_pct[missing_pct > 0])

    # Fill or drop
    df['numeric_col'].fillna(df['numeric_col'].median(), inplace=True)
    df['category_col'].fillna('Unknown', inplace=True)

    # 3. Handle outliers
    Q1 = df['value'].quantile(0.25)
    Q3 = df['value'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Cap outliers
    df['value'] = df['value'].clip(lower_bound, upper_bound)

    # 4. Data types
    df['date'] = pd.to_datetime(df['date'])
    df['category'] = df['category'].astype('category')

    return df

# Usage
df_clean = clean_data(df_raw)
```

### Time Series Analysis Template
```python
import pandas as pd

def analyze_time_series(df, date_col, value_col, freq='M'):
    """Time series analysis pipeline"""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)

    # Resample
    ts = df[value_col].resample(freq).sum()

    # Calculate metrics
    results = pd.DataFrame({
        'value': ts,
        'rolling_mean_3': ts.rolling(3).mean(),
        'rolling_mean_6': ts.rolling(6).mean(),
        'yoy_growth': ts.pct_change(12) * 100,
        'mom_growth': ts.pct_change(1) * 100
    })

    return results

# Usage
results = analyze_time_series(df, 'date', 'revenue', freq='M')
```

### Statistical Summary Template
```python
def statistical_summary(df, numeric_cols):
    """Generate comprehensive statistical summary"""
    summary = pd.DataFrame()

    for col in numeric_cols:
        stats = {
            'count': df[col].count(),
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max(),
            'q25': df[col].quantile(0.25),
            'q75': df[col].quantile(0.75),
            'skewness': df[col].skew(),
            'kurtosis': df[col].kurt()
        }
        summary[col] = pd.Series(stats)

    return summary.T

# Usage
summary = statistical_summary(df, ['pagu', 'quantity'])
print(summary)
```

## 📚 Resources

### Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statsmodels](https://www.statsmodels.org/)

### Tutorials
- [Pandas Time Series](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Statistics in Python](https://realpython.com/python-statistics/)

### Books
- "Practical Statistics for Data Scientists" by Bruce & Bruce
- "Python for Data Analysis" by Wes McKinney

---

**Next Session:** [Session 5 - Streamlit Dashboard](../session5_streamlit/)

**Previous Session:** [Day 1, Session 3 - Visualization](../../day1/session3_visualization/)
