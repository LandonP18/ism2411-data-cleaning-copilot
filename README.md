# ism2411-data-cleaning-copilot

Small, GitHub-ready Python project for **ISM 2411** that cleans a messy sales dataset using `pandas`. The goal is to show basic data cleaning skills and responsible use of GitHub Copilot.

---

## Project Overview

This project:

- Loads a raw CSV file containing messy sales data.
- Standardizes column names.
- Cleans up whitespace in text fields.
- Handles missing values for prices and quantities.
- Removes rows with clearly invalid numeric values (like negative prices/quantities).
- Writes a cleaned CSV that is ready for analysis or visualization.

---

## Project Structure

```text
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv        # provided raw dataset
│   └── processed/
│       └── sales_data_clean.csv      # created by the script
├── src/
│   └── data_cleaning.py              # main cleaning pipeline
├── README.md                         # project description and usage
└── reflection.md                     # explanation of Copilot usage
