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