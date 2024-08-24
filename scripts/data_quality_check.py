import pandas as pd

# Function to check data quality
def check_data_quality(file_path):
    try:
        df = pd.read_csv(file_path)
        
        print(f"Data Quality Check for {file_path}:")
        print(f"File: {file_path}")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")
        print(f"Columns: {list(df.columns)}")
        
        # Missing values
        missing_values = df.isnull().sum()
        print("Missing values per column:")
        print(missing_values)
        
        # Summary statistics
        summary_stats = df.describe(include='all')
        print("Summary statistics:")
        print(summary_stats)
        
        print("\n========================================\n")
    
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

# Paths to the data files
files = [
    'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv',
    'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv'
]

for file in files:
    check_data_quality(file)
