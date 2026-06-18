import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load data
file_path = os.path.join(os.path.dirname(__file__), "../data/final_stock_data.csv")
df = pd.read_csv(file_path)

df['date'] = pd.to_datetime(df['date'])

# Page config
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Stock Performance Dashboard")

# Sidebar
st.sidebar.header("Filters")

stocks = df['symbol'].unique()
selected_stock = st.sidebar.selectbox("Select Stock", stocks)

# Filter
filtered_df = df[df['symbol'] == selected_stock]

# 📊 Price Trend
st.subheader(f"{selected_stock} Price Trend")
fig1 = px.line(filtered_df, x='date', y='close', title="Closing Price")
st.plotly_chart(fig1, use_container_width=True)

# 📈 Cumulative Return
st.subheader("Cumulative Return")
fig2 = px.line(filtered_df, x='date', y='cumulative_return', title="Growth Over Time")
st.plotly_chart(fig2, use_container_width=True)

# 🔝 Top Gainers
st.subheader("Top 10 Gainers")
returns = df.groupby('symbol')['daily_return'].sum().sort_values(ascending=False).head(10)
st.bar_chart(returns)

# 🔻 Top Losers
st.subheader("Top 10 Losers")
losers = df.groupby('symbol')['daily_return'].sum().sort_values().head(10)
st.bar_chart(losers)

# ⚡ Volatility
st.subheader("Top 10 Volatile Stocks")
volatility = df.groupby('symbol')['daily_return'].std().sort_values(ascending=False).head(10)
st.bar_chart(volatility)

# 🔗 Correlation Heatmap
st.subheader("Stock Correlation Heatmap")
pivot = df.pivot(index='date', columns='symbol', values='close')
corr = pivot.corr()

fig3 = px.imshow(corr, text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

# 📊 Market Summary
st.subheader("Market Summary")

col1, col2, col3 = st.columns(3)

returns_all = df.groupby('symbol')['daily_return'].sum()

col1.metric("Green Stocks", int((returns_all > 0).sum()))
col2.metric("Red Stocks", int((returns_all < 0).sum()))
col3.metric("Avg Price", round(df['close'].mean(), 2))

st.write("Average Volume:", round(df['volume'].mean(), 2))