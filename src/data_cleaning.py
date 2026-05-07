# This scrpit loads unorganized sales data, cleans common data quality issues,
# and saves a cleaner CSV file for analysis.

import pandas as pd

# Load the CSV file at the given path into pandas DataFrame.
def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

    # Standardize column names to lowercase with underscores and no extra spaces.
    def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        return df
    
    # Handle missing prices and quantities consistently (e.e., drop or fill rows).
    def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
        # Drop rows where 'price' or 'quantity' is missing, as they are critical for analysis.
        df = df.dropna(subset=['price', 'quantity'])
        return df
    