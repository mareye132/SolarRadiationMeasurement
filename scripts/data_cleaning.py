import pandas as pd

# Define file paths
file_paths = {
    'benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'sierraleone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv',
    'togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv'
}

# Define thresholds for anomalies (example thresholds, adjust based on your context)
def define_thresholds(df):
    return {
        'GHI': (df['GHI'].quantile(0.01), df['GHI'].quantile(0.99)),
        'Tamb': (df['Tamb'].quantile(0.01), df['Tamb'].quantile(0.99)),
        'RH': (df['RH'].quantile(0.01), df['RH'].quantile(0.99)),
        'BP': (df['BP'].quantile(0.01), df['BP'].quantile(0.99))
    }

# Data cleaning function
def clean_data(file_path, cleaned_file_path):
    df = pd.read_csv(file_path)

    # Drop columns with all null values
    df = df.dropna(axis=1, how='all')

    # Handle missing values
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'WSgust', 'BP', 'Precipitation'])

    # Define thresholds for anomalies
    thresholds = define_thresholds(df)

    # Remove anomalies based on thresholds
    df = df[(df['GHI'] >= thresholds['GHI'][0]) & (df['GHI'] <= thresholds['GHI'][1])]
    df = df[(df['Tamb'] >= thresholds['Tamb'][0]) & (df['Tamb'] <= thresholds['Tamb'][1])]
    df = df[(df['RH'] >= thresholds['RH'][0]) & (df['RH'] <= thresholds['RH'][1])]
    df = df[(df['BP'] >= thresholds['BP'][0]) & (df['BP'] <= thresholds['BP'][1])]

    # Save the cleaned dataset
    df.to_csv(cleaned_file_path, index=False)

# Process each file
for key, file_path in file_paths.items():
    cleaned_file_path = f'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/{key}_cleaned.csv'
    clean_data(file_path, cleaned_file_path)
    print(f"Data cleaning completed for {key}. Cleaned dataset saved to '{cleaned_file_path}'.")
