# Reflection: ism2411-data-cleaning-copilot

## What Copilot Generated

For this project, I used GitHub Copilot to help generate the first versions of several key functions in my `data_cleaning.py` file, including `load_data`, `clean_column_names`, and `handle_missing_values`. I prompted Copilot by writing short comments above each function that explained what I wanted the function to do. Once I started typing the function name and parameters, Copilot suggested full blocks of code. For example, when I described that I wanted to clean column names, Copilot generated code that used pandas string methods like `.str.strip()`, `.str.lower()`, and `.str.replace()` to standardize the names. It also helped generate the basic structure for loading the CSV file using `pd.read_csv`. These suggestions gave me a working starting point much faster than if I had written everything from scratch.

## What I Modified

Even though Copilot gave me helpful starting code, I did not use everything exactly as it suggested. I changed variable names to make them easier to understand and more consistent with business data analysis, such as using `price_cols` and `qty_cols` instead of vague names. I also edited the logic in how missing values were handled so it matched the assignment rules exactly. For example, I made sure all price and quantity columns were converted to numeric values using `pd.to_numeric(errors="coerce")` and then consistently removed rows that were missing either a price or a quantity. I also broke some of the cleaning steps into separate functions instead of combining too much logic together. This made the script easier to read, easier to follow, and easier to debug if something went wrong.

## What I Learned About Data Cleaning

This project helped me realize that data cleaning is one of the most important steps in any data analysis project. Before this assignment, I did not fully understand how many problems messy data can cause. Working with missing values, extra spaces in text, and negative numbers showed me how easy it is for bad data to completely change the results of an analysis. For example, keeping negative prices or quantities would make total sales numbers inaccurate and misleading. I also learned how important it is to be consistent in how you handle missing data so your results stay reliable. Writing the cleaning steps in code made me think more carefully about every decision I was making.

## What I Learned About Using Copilot

Using GitHub Copilot taught me that it is a powerful tool, but it still requires careful attention from the programmer. Copilot can quickly generate useful code, but it does not always know the exact goal of the assignment or the rules that need to be followed. I had to review every suggestion and decide whether it actually matched what the script was supposed to do. One clear example was when Copilot suggested converting values to numeric types but did not fully handle how missing values should be removed afterward. I had to step in and adjust that logic myself. This showed me that Copilot works best as an assistant to speed things up, not as an automatic solution.

## Overall Takeaway

Overall, this project helped me gain more confidence in writing simple data pipelines in Python and preparing messy datasets for analysis. I now better understand how small cleaning steps like fixing column names, trimming text, and removing invalid values can make a huge difference in data quality. I also learned how to use GitHub Copilot responsibly by treating it as a support tool rather than relying on it completely. This experience will be very useful for future business, finance, and analytics projects where clean and accurate data is necessary to make good decisions.
