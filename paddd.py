import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 3],
    'customer_name': ['Alice', 'Bob', 'Charlie'],
    'product_price': [19.99, 29.99, 39.99],
    'purchase_date': ['2024-01-01', '2024-01-02', '2024-01-03']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:\n")
print(df)

# Check all data types
print("\nAll Data Types:\n")
print(df.dtypes)

# Select numeric columns
print("\nNumeric Columns:\n")
print(df.select_dtypes(include=['number']))

# Select object/string columns
print("\nString Columns:\n")
print(df.select_dtypes(include=['object']))