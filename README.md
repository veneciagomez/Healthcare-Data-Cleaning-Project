# Healthcare Data Cleaning Project

## Overview
This project involves cleaning and preparing a healthcare dataset for analysis. The dataset includes patient information, medical conditions, and billing details. The goal of this project is to clean the raw data by removing duplicates, fixing inconsistent formatting, and handling missing values to ensure it's ready for further analysis.

## Files Included
- **healthcare_dataset.csv**: The original, uncleaned dataset.
- **cleaned_healthcare_dataset.csv**: The cleaned version of the dataset, after processing.
- **clean_dataset.py**: A Python script that cleans the dataset by performing the following actions:
  - Removing duplicate rows
  - Standardizing capitalization in the `Name` and `Medical Condition` columns
  - Formatting the `Date of Admission` and `Discharge Date` columns
  - Handling missing values

## How to Use
To run the cleaning script and reproduce the results:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Healthcare-Data-Cleaning-Project.git
   ```
2. Ensure you have Python installed, along with the required libraries (like `pandas`).
3. Run the `clean_dataset.py` script to clean the dataset:
   ```bash
   python clean_dataset.py
   ```
   This will output a cleaned version of the dataset (`cleaned_healthcare_dataset.csv`).

## Technologies Used
- **Python**: Used for writing the script that cleans the data.
- **Pandas**: Used for data manipulation and cleaning.
