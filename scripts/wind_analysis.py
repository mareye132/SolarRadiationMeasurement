import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Loop through each file, load the dataset, and plot Wind Speed and Wind Direction
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Drop rows with missing wind speed or wind direction values
    df = df.dropna(subset=['WS', 'WD'])
    
    # Convert 'Timestamp' to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Create a figure and subplots for Wind Speed and Wind Direction
    plt.figure(figsize=(14, 6))
    
    # Plot Wind Speed over Time
    plt.subplot(2, 1, 1)
    plt.plot(df['Timestamp'], df['WS'], label='Wind Speed (WS)', color='blue')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Speed (m/s)')
    plt.title(f'Wind Speed Over Time - {location}')
    plt.legend()
    plt.grid(True)
    
    # Plot Wind Direction over Time
    plt.subplot(2, 1, 2)
    plt.plot(df['Timestamp'], df['WD'], label='Wind Direction (WD)', color='red')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Direction (degrees)')
    plt.title(f'Wind Direction Over Time - {location}')
    plt.legend()
    plt.grid(True)
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
