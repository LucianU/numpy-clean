import numpy as np

# Load the CSV into a NumPy structured array
raw_data = np.genfromtxt(
    "raw_sales_data.csv", delimiter=",", dtype=None, names=True, encoding="utf-8"
)

# Step 1: Handle Missing Transaction IDs with 0
transaction_ids = raw_data["Transaction_ID"]
missing_indices = np.where(np.isnan(transaction_ids))[0]
unique_placeholders = np.arange(-1, -1 - len(missing_indices), -1)
transaction_ids[missing_indices] = unique_placeholders

# Step 1': Replace missing dates with "Unknown"
dates = raw_data["Date"]
dates = np.array(["Unknown" if date == "" else date for date in dates], dtype=str)

# Step 2: Fill missing Amount with the column mean
amounts = raw_data["Amount"]
mean_amount = np.nanmean(amounts)
amounts = np.where(np.isnan(amounts), mean_amount, amounts)

# Step 3: Replace missing Customer Names with "Unknown"
customer_names = raw_data["Customer_Name"]
customer_names = np.array(
    ["Unknown" if name is None else name for name in customer_names], dtype=str
)

# Step 4: Remove duplicate Transaction IDs (keeping the first occurrence)
unique_indices = np.unique(transaction_ids, return_index=True)[1]

# Combine cleaned columns into a final array
cleaned_data = np.array(
    list(zip(
        transaction_ids[unique_indices],
        dates[unique_indices],
        customer_names[unique_indices],
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
    "cleaned_sales_data.csv",
    cleaned_data,
    delimiter=",",
    header="Transaction_ID,Date,Customer_Name,Amount",
    fmt=["%d", "%s", "%s", "%.2f"],
    comments=""
)

print("Data cleaned and saved to 'cleaned_sales_data.csv'.")
