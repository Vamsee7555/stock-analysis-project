import pandas as pd
import os

# Load data
file_path = os.path.join(os.path.dirname(__file__), "../data/processed_stock_data.csv")
df = pd.read_csv(file_path)

print("✅ Data Loaded:", df.shape)

# Standardize column names
df.columns = [col.lower() for col in df.columns]

# Fix column name (IMPORTANT)
if 'ticker' in df.columns:
    df.rename(columns={'ticker': 'symbol'}, inplace=True)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort
df = df.sort_values(['symbol', 'date'])

# 📈 Daily Return
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# 📊 Total Return per stock
returns = df.groupby('symbol')['daily_return'].sum()

# 🔝 Top 10 Gainers
top_gainers = returns.sort_values(ascending=False).head(10)

# 🔻 Top 10 Losers
top_losers = returns.sort_values().head(10)

print("\n🏆 Top 10 Gainers:\n", top_gainers)
print("\n📉 Top 10 Losers:\n", top_losers)

# 📊 Market Summary
green = (returns > 0).sum()
red = (returns < 0).sum()

print(f"\n📊 Market Summary:")
print(f"Green Stocks: {green}")
print(f"Red Stocks: {red}")
print(f"Average Price: {df['close'].mean():.2f}")
print(f"Average Volume: {df['volume'].mean():.2f}")

# 📉 Volatility
volatility = df.groupby('symbol')['daily_return'].std()
top_volatile = volatility.sort_values(ascending=False).head(10)

print("\n⚡ Top 10 Volatile Stocks:\n", top_volatile)

# 📈 Cumulative Return
df['cumulative_return'] = (1 + df['daily_return']).groupby(df['symbol']).cumprod()

# 🔗 Correlation
pivot = df.pivot(index='date', columns='symbol', values='close')
correlation = pivot.corr()

# 💾 Save outputs
output_path = os.path.join(os.path.dirname(__file__), "../data/final_stock_data.csv")
corr_path = os.path.join(os.path.dirname(__file__), "../data/correlation_matrix.csv")

df.to_csv(output_path, index=False)
correlation.to_csv(corr_path)

print("\n🎉 Analysis completed successfully!")
print(f"📁 Final data saved: {output_path}")
