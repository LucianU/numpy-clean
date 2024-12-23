import pandas as pd

# Create raw sales data
data = {
    "Transaction ID": [101, 102, 103, 103, 105, 106, None],
    "Date": ["2024-01-01", "2024-01-02", None, "2024-01-03", "2024-01-05", "2024-01-06", "2024-01-07"],
    "Customer Name": ["Alice", "Bob", "Charlie", "Charlie", "Eve", None, "Grace"],
    "Amount": [200, None, 300, 300, 400, 500, 600],
}

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("raw_sales_data.csv", index=False)
