import pandas as pd
from sqlalchemy import create_engine

# Define the path to the CSV file
file_path = r'C:\Users\LENOVO\Downloads\Ecommerce\sales_data.csv'

# Step 1: Load the Data
df = pd.read_csv(file_path, low_memory=False)
print("Original Data:")
print(df.head())

# Step 2: Clean the Data
# Remove duplicates
df = df.drop_duplicates()

# Normalize Date Format to YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce').dt.strftime('%Y-%m-%d')

# Handle missing values in 'Amount' and 'Qty'
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce').fillna(0)

# Step 3: Transform the Data
# Calculate Revenue
df['Revenue'] = df['Amount'] * df['Qty']

# Assuming a fixed cost percentage of 70% of the sale price
df['Cost'] = df['Amount'] * df['Qty'] * 0.7
df['Profit'] = df['Revenue'] - df['Cost']

print("Transformed Data:")
print(df.head())

# Step 4: Calculate Key Metrics
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()

print(f"Total Revenue: {total_revenue}")
print(f"Total Profit: {total_profit}")

# Step 5: Save the Transformed Data
transformed_file_path = r'C:\Users\LENOVO\Downloads\Ecommerce\transformed_sales_data.csv'
df.to_csv(transformed_file_path, index=False)
print("Transformed data saved to 'transformed_sales_data.csv'")

# Step 6: Load Data into PostgreSQL
# Database connection details
db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/sales_db'

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Load DataFrame into PostgreSQL
df.to_sql('sales_data', engine, if_exists='replace', index=False)
print("Data loaded into PostgreSQL database")
