import numpy as np

# Simulated raw data
raw_data = np.array(
    [
        (101, "2024-12-20", "Alice", 100.5),
        (102, "", "Charlie", 200.0),
        (101, "2024-12-20", "Alice", 100.5),
        (103, "2024-12-21", "Bob", 150.0),
        (None, "", "Eve", None),
        (None, "2024-12-23", "Lucian", 75.0)
    ],
    dtype=[
        ("Transaction_ID", "float"),
        ("Date", "U10"),
        ("Customer_Name", "U50"),
        ("Amount", "float"),
    ],
)

# Handle missing Transaction IDs
transaction_ids = raw_data["Transaction_ID"]
missing_indices = np.where(np.isnan(transaction_ids))[0]
unique_placeholders = np.arange(-1, -1 - len(missing_indices), -1)
transaction_ids[missing_indices] = unique_placeholders

# Remove duplicates by Transaction_ID
unique_indices = np.unique(transaction_ids, return_index=True)[1]

# Replace missing dates with "Unknown"
dates = raw_data["Date"]
dates = np.array(["Unknown" if not date else date for date in dates], dtype=str)

# Replace missing amounts with the mean
amounts = raw_data["Amount"]
missing_amounts = np.isnan(amounts)  # Identify valid entries
mean_amount = np.nanmean(amounts)  # Calculate the mean of valid amounts
amounts[missing_amounts] = mean_amount # Replace only missing values

"""
amounts = raw_data["Amount"]
mean_amount = np.nanmean(amounts)
amounts = np.where(np.isnan(amounts), mean_amount, amounts)
"""

# Combine cleaned columns into a final array
cleaned_data = np.array(
    list(zip(
        transaction_ids[unique_indices],
        dates[unique_indices],
        raw_data["Customer_Name"][unique_indices],
        amounts[unique_indices]
    )),
    dtype=[
        ("Transaction_ID", "int"),
        ("Date", "U10"),
        ("Customer_Name", "U50"),
        ("Amount", "float"),
    ],
)

# Save cleaned data back to a CSV
np.savetxt(
    "test_cleaned_sales_data.csv",
    cleaned_data,
    delimiter=",",
    header="Transaction_ID,Date,Customer_Name,Amount",
    fmt=["%d", "%s", "%s", "%.2f"],
    comments=""
)

print("Data cleaned and saved to 'test_cleaned_sales_data.csv'.")
