import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Loop through each file, load the dataset, and plot the GHI time series
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Convert 'Timestamp' to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Set 'Timestamp' as the index
    df.set_index('Timestamp', inplace=True)
    
    # Plot Global Horizontal Irradiance (GHI) over time
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['GHI'], label='GHI', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Global Horizontal Irradiance (GHI)')
    plt.title(f'Time Series Analysis of GHI - {location}')
    plt.legend()
    plt.grid(True)
    plt.show()
