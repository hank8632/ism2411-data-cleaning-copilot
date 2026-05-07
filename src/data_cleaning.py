# This script loads raw sales data, cleans common data quality issues,
# and saves a cleaned CSV file for analysis.

import pandas as pd


# Function to load the CSV file.
def load_data(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    print(f"Data loaded successfully from {file_path}")
    return data


# Function to clean column names.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:

    # Make a copy of the DataFrame.
    df = df.copy()

    # Standardize column names.
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df


# Function to handle missing values.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:

    # Make a copy of the DataFrame.
    df = df.copy()

    # Remove rows with missing values.
    df = df.dropna(subset=["price", "qty", "date_sold"])

    return df


# Function to remove invalid rows.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:

    # Make a copy of the DataFrame.
    df = df.copy()

    # If a price column exists, convert it to numbers.
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

        # Remove rows where price is missing, zero, or negative.
        df = df[df["price"] > 0]

    # If a quantity column exists, convert it to numbers.
    if "qty" in df.columns:
        df["qty"] = pd.to_numeric(df["qty"], errors="coerce")

        # Remove rows where quantity is missing, zero, or negative.
        df = df[df["qty"] > 0]

    return df


# Main program starts here.
if __name__ == "__main__":

    # File paths.
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load raw data.
    df_raw = load_data(raw_path)

    # Clean the data step-by-step.
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    # Save cleaned data to a new CSV file.
    df_clean.to_csv(cleaned_path, index=False)

    # Display preview of cleaned data.
    print("Cleaning complete. First few rows:")
    print(df_clean.head())