import yaml
import pandas as pd
import os

input_folder = os.path.join(os.path.dirname(__file__), "../data/raw_yaml")
output_file = os.path.join(os.path.dirname(__file__), "../data/processed_stock_data.csv")

all_data = []

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            file_path = os.path.join(root, file)

            print(f"📄 Reading: {file_path}")

            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)

                print("🔍 Sample data:", str(data)[:200])  # preview

                # 🔥 Flatten everything
                def extract_records(obj):
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            yield from extract_records(value)
                    elif isinstance(obj, list):
                        for item in obj:
                            yield from extract_records(item)
                    else:
                        return

                # Try extracting structured records
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            all_data.append(item)

                elif isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, list):
                            for item in value:
                                if isinstance(item, dict):
                                    all_data.append(item)

# ❌ If empty
if not all_data:
    print("❌ No usable records found. YAML structure is deeply nested.")
    exit()

df = pd.DataFrame(all_data)

print("\n✅ Raw Columns:", df.columns.tolist())

# 🔧 Normalize column names
df.columns = [col.lower() for col in df.columns]

# Try fixing column names
rename_map = {
    'date': 'date',
    'timestamp': 'date',
    'time': 'date',
    'symbol': 'symbol',
    'ticker': 'symbol',
    'close': 'close',
    'closing_price': 'close'
}

df.rename(columns=rename_map, inplace=True)

# Check required columns
required_cols = ['date', 'symbol', 'close']
missing = [col for col in required_cols if col not in df.columns]

if missing:
    print(f"❌ Missing required columns: {missing}")
    exit()

# Clean
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date', 'symbol', 'close'])

df = df.sort_values(['symbol', 'date'])

# Daily return
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# Save
df.to_csv(output_file, index=False)

print("\n🎉 SUCCESS! Data extracted properly.")
print(f"📊 Total rows: {len(df)}")