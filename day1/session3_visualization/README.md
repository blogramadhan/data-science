# Session 3: Data Visualization

**Duration:** 1 jam 45 menit (15:45 - 17:30)

## 📚 Overview

Session ini membahas teknik visualisasi data menggunakan Matplotlib, Seaborn, dan Plotly. Peserta akan belajar membuat berbagai jenis visualisasi untuk exploratory data analysis dan presentation.

## 🎯 Learning Objectives

Setelah session ini, peserta akan mampu:
- Membuat static visualizations dengan Matplotlib & Seaborn
- Membuat interactive visualizations dengan Plotly
- Memilih chart type yang tepat untuk data
- Apply data storytelling principles
- Customize visualizations untuk presentation

## 📁 Materi

### 1. Matplotlib & Seaborn (45 menit)
**Topics:**
- Matplotlib basics (Figure, Axes)
- Common plot types (line, bar, scatter, histogram, pie)
- Seaborn for statistical plots
- Distribution plots (histplot, kdeplot, boxplot, violinplot)
- Categorical plots (barplot, countplot, pointplot)
- Relationship plots (scatterplot, lineplot, regplot)
- Heatmaps & correlation matrices
- Customization (colors, labels, legends, styles)

**Script:** `01_matplotlib_seaborn.py`

### 2. Plotly for Interactive Charts (45 menit)
**Topics:**
- Introduction to Plotly
- Plotly Express vs Graph Objects
- Interactive line & bar charts
- Scatter & bubble charts
- Box plots & violin plots
- Sunburst & treemap charts
- Time series visualizations
- Adding interactivity (hover, click, zoom)
- Export interactive charts

**Script:** `02_plotly_interactive.py`

### 3. Data Storytelling (15 menit)
**Topics:**
- Choosing the right visualization
- Color theory & accessibility
- Chart best practices
- Dashboard design principles
- Common visualization mistakes

**Doc:** Lihat README ini untuk guidelines

## 🚀 Quick Start

### Prerequisites
```bash
pip install matplotlib seaborn plotly pandas
```

### Run Scripts
```bash
# Matplotlib & Seaborn examples
python 01_matplotlib_seaborn.py

# Plotly interactive charts
python 02_plotly_interactive.py
```

## 📊 Chart Types Reference

### Distribution Charts
```
Use case: Show how data is distributed

- Histogram: Continuous data distribution
- Box Plot: Show quartiles and outliers
- Violin Plot: Distribution shape
- KDE Plot: Smooth distribution curve
```

### Comparison Charts
```
Use case: Compare values across categories

- Bar Chart: Compare discrete values
- Column Chart: Vertical comparison
- Grouped Bar: Compare multiple series
- Stacked Bar: Show composition
```

### Relationship Charts
```
Use case: Show correlation between variables

- Scatter Plot: 2 numeric variables
- Line Chart: Trends over time
- Bubble Chart: 3 variables (x, y, size)
- Heatmap: Correlation matrix
```

### Composition Charts
```
Use case: Show parts of a whole

- Pie Chart: Simple proportions (max 5-7 slices)
- Donut Chart: Pie with hole
- Stacked Area: Composition over time
- Treemap: Hierarchical composition
- Sunburst: Nested hierarchies
```

### Time Series Charts
```
Use case: Show trends over time

- Line Chart: Single or multiple series
- Area Chart: Filled line chart
- Candlestick: OHLC (Open, High, Low, Close)
- Range Chart: Min-max over time
```

## 💡 Data Storytelling Guidelines

### 1. Choose the Right Chart Type

```python
# Bad: Pie chart with too many slices
plt.pie(df['kategori'].value_counts())  # If > 7 categories

# Good: Bar chart for many categories
df['kategori'].value_counts().plot(kind='barh')
```

### 2. Use Appropriate Colors

```python
# Bad: Random colors
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00']

# Good: Color palette for accessibility
import seaborn as sns
colors = sns.color_palette('colorblind')

# Or use semantic colors
colors = {
    'positive': 'green',
    'negative': 'red',
    'neutral': 'gray'
}
```

### 3. Clear Labels & Titles

```python
# Bad: No labels
plt.plot(x, y)

# Good: Informative labels
plt.plot(x, y)
plt.title('Monthly Revenue Trend - 2024', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Revenue (Million Rp)')
plt.grid(True, alpha=0.3)
```

### 4. Remove Chart Junk

```python
# Remove unnecessary elements
sns.set_style('whitegrid')
plt.box(False)  # Remove box around plot
plt.tick_params(top=False, right=False)  # Remove unnecessary ticks
```

### 5. Highlight Key Insights

```python
# Highlight specific data points
plt.bar(months, revenue)
plt.bar('July', revenue_july, color='red', label='Record high')
plt.legend()
```

## 🎨 Color Palettes

### Seaborn Palettes
```python
import seaborn as sns

# Qualitative (for categories)
sns.color_palette('Set2')
sns.color_palette('Paired')

# Sequential (for gradients)
sns.color_palette('Blues')
sns.color_palette('YlOrRd')

# Diverging (for positive/negative)
sns.color_palette('RdYlGn')
sns.color_palette('coolwarm')

# Colorblind-friendly
sns.color_palette('colorblind')
```

### Plotly Color Scales
```python
import plotly.express as px

# Built-in color scales
px.scatter(..., color_continuous_scale='Viridis')
px.scatter(..., color_continuous_scale='Plasma')
px.scatter(..., color_continuous_scale='Blues')
```

## 📝 Best Practices

### Do's ✅
- Keep it simple
- Use consistent colors
- Label axes clearly
- Add title and caption
- Sort data logically
- Use appropriate scale
- Test for colorblindness
- Export high resolution

### Don'ts ❌
- Don't use 3D unless necessary
- Don't use too many colors
- Don't distort scales
- Don't use pie charts for > 7 categories
- Don't overcrowd with text
- Don't use default styles
- Don't forget axis labels
- Don't use red-green for colorblind

## 🎓 Exercises

### Exercise 1: RUP Distribution Analysis
```python
# Using RUP dataset:
1. Create histogram of pagu distribution
2. Create box plot of pagu by metode_pengadaan
3. Create bar chart of top 10 satker by total pagu
4. Add proper labels, title, and colors
```

### Exercise 2: Time Series Visualization
```python
# Using RUP dataset:
1. Aggregate pengumuman by month
2. Create line chart of monthly trend
3. Add markers for significant points
4. Highlight peak months
```

### Exercise 3: Relationship Analysis
```python
# Create your own analysis:
1. Scatter plot of 2 numeric variables
2. Add regression line
3. Color by category
4. Add correlation coefficient in title
```

### Exercise 4: Interactive Dashboard
```python
# Using Plotly:
1. Create 4 different chart types
2. Use subplots to combine them
3. Add interactive filters
4. Export as HTML
```

## 📚 Example Visualizations

### Example 1: Simple Bar Chart
```python
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [23, 45, 56, 78]}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Value'], color='steelblue')
plt.title('Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Sales (Million Rp)')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('bar_chart.png', dpi=300)
plt.show()
```

### Example 2: Seaborn Heatmap
```python
import seaborn as sns
import pandas as pd

# Correlation matrix
corr = df.corr()

# Plot
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1)
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=300)
plt.show()
```

### Example 3: Plotly Interactive
```python
import plotly.express as px

# Load data
df = px.data.iris()

# Create interactive scatter
fig = px.scatter(df, x='sepal_width', y='sepal_length',
                 color='species', size='petal_length',
                 hover_data=['petal_width'],
                 title='Iris Dataset - Interactive Scatter Plot')

# Customize
fig.update_layout(
    hovermode='closest',
    height=600
)

# Show or save
fig.show()
# fig.write_html('scatter_plot.html')
```

## 🔗 Resources

### Documentation
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Plotly Python](https://plotly.com/python/)

### Tutorials
- [Python Graph Gallery](https://python-graph-gallery.com/)
- [From Data to Viz](https://www.data-to-viz.com/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Books
- "Storytelling with Data" by Cole Nussbaumer Knaflic
- "The Visual Display of Quantitative Information" by Edward Tufte
- "Better Data Visualizations" by Jonathan Schwabish

### Tools
- [ColorBrewer](https://colorbrewer2.org/) - Color schemes
- [Coolors](https://coolors.co/) - Color palette generator
- [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) - Colorblind simulator

## 🎨 Quick Reference

### Matplotlib Basic Template
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, marker='o', linestyle='-', color='steelblue')
ax.set_title('Title', fontsize=14, fontweight='bold')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show()
```

### Seaborn Basic Template
```python
import seaborn as sns

sns.set_style('whitegrid')
sns.set_palette('colorblind')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='category', y='value', ax=ax)
ax.set_title('Title', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Plotly Basic Template
```python
import plotly.express as px

fig = px.bar(df, x='category', y='value',
             title='Title',
             labels={'value': 'Value Label'},
             color='category')

fig.update_layout(
    height=600,
    showlegend=True
)

fig.show()
```

---

**Next Session:** [Day 2 - Session 4: Advanced Analysis](../../day2/session4_advanced_analysis/)

**Previous Session:** [Session 2 - DuckDB](../session2_duckdb/)
