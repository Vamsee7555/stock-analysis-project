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

<img width="1865" height="837" alt="Screenshot 2026-07-14 135305" src="https://github.com/user-attachments/assets/1e3a7283-7f02-4dc0-b162-435944fc7a87" />
<img width="1898" height="857" alt="Screenshot 2026-07-14 135234" src="https://github.com/user-attachments/assets/e39a7045-4be0-4000-a5f4-927b90dc2077" />
<img width="1448" height="713" alt="Screenshot 2026-07-14 135356" src="https://github.com/user-attachments/assets/fba6aaea-8f3f-4ce7-808d-9cba0ccc1181" />
<img width="1447" height="562" alt="Screenshot 2026-07-14 135408" src="https://github.com/user-attachments/assets/4a23857c-7c8c-4e6d-9aca-787bff143280" />
<img width="1442" height="547" alt="Screenshot 2026-07-14 135424" src="https://github.com/user-attachments/assets/b326a96c-e4e3-4814-803b-457f7985cb7c" />
<img width="1426" height="552" alt="Screenshot 2026-07-14 135435" src="https://github.com/user-attachments/assets/16c71323-c438-467a-84c7-0d2ae804082d" />
<img width="1452" height="690" alt="Screenshot 2026-07-14 135450" src="https://github.com/user-attachments/assets/38167712-6d25-4a84-b9f2-187870a8b449" />
<img width="1303" height="247" alt="Screenshot 2026-07-14 135500" src="https://github.com/user-attachments/assets/497c74e4-4462-409d-b80f-367aa2647e69" />









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
