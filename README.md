# 📊 Data-Driven Stock Analysis Dashboard

## 📌 Project Overview

This project analyzes stock market performance data and provides meaningful insights through data cleaning, analysis, visualization, and dashboard creation.

The project processes raw stock data from YAML files, transforms it into structured datasets, stores it in a SQL database, and visualizes key stock performance metrics using Streamlit and Power BI.

---

## 🎯 Objectives

- Analyze stock market trends
- Identify Top 10 Gainers and Losers
- Calculate stock volatility
- Perform cumulative return analysis
- Generate market summary statistics
- Visualize stock performance through dashboards

---

## 🛠️ Tech Stack

### Programming
- Python

### Libraries
- Pandas
- NumPy
- PyYAML
- SQLAlchemy
- PyMySQL
- Plotly
- Streamlit

### Database
- MySQL

### Visualization
- Power BI
- Streamlit

---

## 📂 Project Structure

```text
stock-analysis-project/
│
├── data/
│   ├── raw_yaml/
│   ├── processed_stock_data.csv
│   ├── final_stock_data.csv
│   └── correlation_matrix.csv
│
├── scripts/
│   ├── extract_transform.py
│   ├── analysis.py
│   └── db_upload.py
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## 🔄 Project Workflow

### Step 1: Data Extraction

- Read YAML stock files
- Convert to structured DataFrame
- Clean and validate records

### Step 2: Data Analysis

Calculated metrics:

- Daily Returns
- Top 10 Gainers
- Top 10 Losers
- Volatility Analysis
- Market Summary
- Cumulative Returns
- Correlation Matrix

### Step 3: Database Storage

- Create MySQL database
- Upload processed stock data
- Execute SQL analysis queries

### Step 4: Dashboard Development

#### Streamlit Dashboard

Features:
- Stock Filter
- Price Trend Analysis
- Top Gainers
- Top Losers
- Volatility Analysis
- Correlation Heatmap

#### Power BI Dashboard

Features:
- KPI Cards
- Price Trend Visualization
- Top Performing Stocks
- Market Summary
- Green vs Red Stock Analysis

---

## 📊 Key Business Insights

### Top Performing Stocks
Identifies stocks with highest cumulative returns.

### Loss Making Stocks
Highlights underperforming stocks.

### Volatility Analysis
Measures risk using standard deviation of returns.

### Market Summary
Provides:
- Average Price
- Average Volume
- Green vs Red Stock Distribution

---

## 🗄️ SQL Analysis

Implemented:

- Top 10 Gainers
- Top 10 Losers
- Volatility Analysis
- Monthly Performance
- Average Price Analysis

---

## ▶️ How To Run

### Clone Repository

```bash
git clone <repository-url>
cd stock-analysis-project
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Extraction

```bash
python scripts/extract_transform.py
```

### Run Analysis

```bash
python scripts/analysis.py
```

### Upload To MySQL

```bash
python scripts/db_upload.py
```

### Launch Streamlit Dashboard

```bash
python -m streamlit run app/streamlit_app.py
```

---

## 📈 Results

✔ Processed 14,000+ stock records

✔ Generated stock performance insights

✔ Built SQL-backed analytics system

✔ Developed interactive Streamlit dashboard

✔ Created Power BI visualizations

---

## 📷 Dashboard Screenshots

### Power BI Dashboard

(Add Screenshot Here)

### Streamlit Dashboard

(Add Screenshot Here)

---

## 🚀 Future Enhancements

- Live Stock API Integration
- Machine Learning Price Prediction
- Portfolio Optimization
- Real-Time Dashboard Updates
- Advanced Technical Indicators

---

## 👨‍💻 Author

**Vamsee Krishna M**

Data Analytics | Python | SQL | Power BI | Streamlit

---

## 📜 License

This project is developed for educational and portfolio purposes.
