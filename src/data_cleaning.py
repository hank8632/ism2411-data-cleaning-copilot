# This scrpit loads unorganized sales data, cleans common data quality issues,
# and saves a cleaner CSV file for analysis.

import pandas as pd

# Load the raw CSV file so we can begin cleaning the dataset.
# We use a separate function to keep the script organized and reusable.
def load_data(file_path: str):
    return pd.read_csv(file_path)


# Standardize column names to make them easier to work with in Python.
# Lowercase names with underscores are more consistent and reduce mistakes.
def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# Remove extra whitespace and handle missing numeric values consistently.
# This makes text fields cleaner and avoids issues in calculations later.
def handle_missing_values(df):
    if "product_name" in df.columns:
        df["product_name"] = df["product_name"].astype(str).str.strip()

    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()

    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    if "quantity" in df.columns:
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    df = df.dropna(subset=["price", "quantity"])
    return df


# Remove rows with values that clearly do not make sense.
# Negative prices and quantities are treated as bad data for this project.
def remove_invalid_rows(df):
    if "price" in df.columns:
        df = df[df["price"] >= 0]

    if "quantity" in df.columns:
        df = df[df["quantity"] >= 0]

    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())