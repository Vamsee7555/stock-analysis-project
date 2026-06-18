import pandas as pd
from sqlalchemy import create_engine
import os

file_path = os.path.join(os.path.dirname(__file__), "../data/final_stock_data.csv")
df = pd.read_csv(file_path)

df.columns = [col.lower() for col in df.columns]

# DB credentials
username = "root"
password = "12345"
host = "localhost"
database = "stock_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

df.to_sql("stocks", con=engine, if_exists='replace', index=False)

print("✅ Uploaded to DB")
