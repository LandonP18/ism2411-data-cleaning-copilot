"""
data_cleaning.py

This script loads a raw sales CSV file, applies a small sequence of
data-cleaning steps, and writes a cleaned CSV that is easier to analyze.
The goal is to demonstrate basic data cleaning in Python and produce
a simple, resume-ready example of working with messy real-world data.
"""

import os
from typing import List

import pandas as pd


# Copilot-style function: load the raw sales data from a CSV file.
# What: Read the raw CSV into a pandas DataFrame.
# Why: Keeping file I/O in a separate function makes the cleaning
#      pipeline easier to read, test, and reuse.
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw sales data from a CSV file into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the raw sales data.
    """
    return pd.read_csv(file_path)


# Copilot-style function: standardize column names in the DataFrame.
# What: Strip whitespace, lowercase names, and replace spaces/special
#       characters with underscores.
# Why: Consistent column names make it easier to write reliable,
#      reusable data cleaning and analysis code.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names by stripping whitespace, lowercasing,
    and replacing non-alphanumeric characters with underscores.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with raw column names.

    Returns
    -------
    pd.DataFrame
        DataFrame with cleaned, standardized column names.
    """
    df_clean = df.copy()
    df_clean.columns = (
        df_clean.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w]+", "_", regex=True)
    )
    return df_clean


# Helper function: strip leading/trailing whitespace from text columns.
# What: Remove extra spaces around strings in object/text columns.
# Why: Extra whitespace is a common source of subtle bugs when grouping
#      or merging on product names or categories.
def strip_text_columns(df: pd.DataFrame, text_columns: List[str] | None = None) -> pd.DataFrame:
    """
    Strip leading and trailing whitespace from selected text columns.
    If no columns are provided, all object (string) columns are cleaned.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    text_columns : list of str, optional
        Column names to strip. If None, all object columns are used.

    Returns
    -------
    pd.DataFrame
        DataFrame with trimmed text values.
    """
    df_clean = df.copy()

    if text_columns is None:
        text_columns = df_clean.select_dtypes(include="object").columns.tolist()

    for col in text_columns:
        # Convert to string first in case there are mixed types
        df_clean[col] = df_clean[col].astype(str).str.strip()

    return df_clean


# Copilot-style function: handle missing values in price and quantity.
# What: Convert numeric columns and drop rows with missing price/quantity.
# Why: Analyses based on incomplete price or quantity data can be misleading,
#      so we consistently remove rows that do not have valid numeric values.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values for price- and quantity-like columns by
    converting them to numeric and dropping rows with missing values.

    This implementation looks for columns whose names contain
    'price', 'qty', or 'quantity'.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with potentially missing or non-numeric values.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing price/quantity rows removed.
    """
    df_clean = df.copy()

    # Identify likely price and quantity columns based on their names
    price_cols = [c for c in df_clean.columns if "price" in c]
    qty_cols = [c for c in df_clean.columns if "qty" in c or "quantity" in c]

    # Convert these columns to numeric, coercing invalid values to NaN
    for col in price_cols + qty_cols:
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

    # Drop rows that are missing any required numeric value
    required_numeric_cols = list(set(price_cols + qty_cols))
    if required_numeric_cols:
        df_clean = df_clean.dropna(subset=required_numeric_cols)

    return df_clean


# Copilot-style function: remove clearly invalid rows.
# What: Drop rows with negative prices or quantities.
# Why: Negative prices or quantities usually represent data entry errors
#      and can distort revenue or volume calculations.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with clearly invalid numeric values, such as negative
    prices or negative quantities.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame after missing values have been handled.

    Returns
    -------
    pd.DataFrame
        DataFrame with invalid rows removed.
    """
    df_clean = df.copy()

    price_cols = [c for c in df_clean.columns if "price" in c]
    qty_cols = [c for c in df_clean.columns if "qty" in c or "quantity" in c]

    # Keep only rows where all price columns are non-negative
    for col in price_cols:
        df_clean = df_clean[df_clean[col] >= 0]

    # Keep only rows where all quantity columns are non-negative
    for col in qty_cols:
        df_clean = df_clean[df_clean[col] >= 0]

    return df_clean


if __name__ == "__main__":
    # Define input and output paths relative to the project root.
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Ensure the processed directory exists before writing the cleaned file.
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    # 1. Load the raw data from CSV.
    #    Why: We start with the original messy dataset so that all
    #    cleaning steps are reproducible in code.
    df_raw = load_data(raw_path)

    # 2. Standardize column names (lowercase, underscores, etc.).
    #    Why: Consistent column names make the rest of the cleaning
    #    pipeline more robust and easier to understand.
    df_clean = clean_column_names(df_raw)

    # 3. Strip leading/trailing whitespace from text columns.
    #    Why: Extra spaces in product names or categories can cause
    #    duplicates and grouping errors later.
    df_clean = strip_text_columns(df_clean)

    # 4. Handle missing values for price and quantity fields.
    #    Why: Dropping rows with missing price/quantity keeps
    #    downstream analysis from using incomplete records.
    df_clean = handle_missing_values(df_clean)

    # 5. Remove rows with clearly invalid values (e.g., negative numbers).
    #    Why: Negative prices/quantities are almost always data entry
    #    issues and would distort totals and averages.
    df_clean = remove_invalid_rows(df_clean)

    # 6. Write the cleaned dataset to the processed folder.
    #    Why: Saving a clean version makes it easy to reuse in other
    #    notebooks, scripts, or BI tools without repeating the steps.
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
