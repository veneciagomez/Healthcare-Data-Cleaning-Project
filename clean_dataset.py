import pandas as pd

# Load the dataset
file_path = 'healthcare_dataset.csv'  # Replace this with the actual path to your CSV file
df = pd.read_csv(file_path, encoding='utf-8')

# Step 1: Fix inconsistent capitalization for columns like "Name" and "Medical Condition"
df['Name'] = df['Name'].str.title()
df['Medical Condition'] = df['Medical Condition'].str.title()

# Step 2: Convert "Date of Admission" and "Discharge Date" to datetime format
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')

# Step 3: Remove rows where Quantity or UnitPrice is less than or equal to 0 (indicating errors or returns)
df_cleaned = df.drop_duplicates()

# Step 4: Check for missing values and fill or drop as needed
df_cleaned = df_cleaned.dropna()

# Step 5: Save the cleaned dataset
df_cleaned.to_csv('cleaned_healthcare_dataset.csv', index=False)

print("Data cleaning complete. Cleaned file saved as 'cleaned_healthcare_dataset.csv'.")
