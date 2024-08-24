import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Loop through each dataset and create histograms
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Drop rows with missing values in relevant columns
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'Tamb'])
    
    # Create a figure for the histograms
    plt.figure(figsize=(14, 10))
    
    # Plot histogram for GHI
    plt.subplot(3, 2, 1)
    plt.hist(df['GHI'], bins=50, color='blue', edgecolor='black')
    plt.xlabel('GHI')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Global Horizontal Irradiance (GHI) - {location}')
    
    # Plot histogram for DNI
    plt.subplot(3, 2, 2)
    plt.hist(df['DNI'], bins=50, color='red', edgecolor='black')
    plt.xlabel('DNI')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Direct Normal Irradiance (DNI) - {location}')
    
    # Plot histogram for DHI
    plt.subplot(3, 2, 3)
    plt.hist(df['DHI'], bins=50, color='green', edgecolor='black')
    plt.xlabel('DHI')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Diffuse Horizontal Irradiance (DHI) - {location}')
    
    # Plot histogram for WS
    plt.subplot(3, 2, 4)
    plt.hist(df['WS'], bins=50, color='purple', edgecolor='black')
    plt.xlabel('Wind Speed (WS)')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Wind Speed (WS) - {location}')
    
    # Plot histogram for Air Temperature
    plt.subplot(3, 2, 5)
    plt.hist(df['Tamb'], bins=50, color='orange', edgecolor='black')
    plt.xlabel('Air Temperature (Tamb)')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Air Temperature (Tamb) - {location}')
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
