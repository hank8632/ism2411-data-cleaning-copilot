This project uses Python and the pandas library to clean and organize a messy sales dataset. The script removes missing or invalid data, standardizes column names, and exports a cleaned CSV file for future analysis.

## How to Run

### Prerequisites
- Python 3 installed
- pandas library installed

Install pandas with:

```bash
pip install pandas

#Python and Pandas should be up to date
python --version
pip --version
python -m pip install --upgrade pip

#Run this script

python src/data_cleaning.py

#Files
data/raw/sales_data_raw.csv → Original raw sales dataset
data/processed/sales_data_clean.csv → Cleaned output dataset
src/data_cleaning.py → Python script used to clean and process the data