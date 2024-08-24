import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Loop through each file, load the dataset, and plot the temperatures over time
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Drop rows with missing temperature values
    df = df.dropna(subset=['Tamb', 'TModA', 'TModB'])
    
    # Convert 'Timestamp' to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Create a figure and subplots for the temperatures
    plt.figure(figsize=(14, 8))
    
    # Plot Air Temperature over Time
    plt.subplot(3, 1, 1)
    plt.plot(df['Timestamp'], df['Tamb'], label='Air Temperature (Tamb)', color='green')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Air Temperature Over Time - {location}')
    plt.legend()
    plt.grid(True)
    
    # Plot Sensor Temperature A over Time
    plt.subplot(3, 1, 2)
    plt.plot(df['Timestamp'], df['TModA'], label='Sensor Temperature A (TModA)', color='orange')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Sensor Temperature A Over Time - {location}')
    plt.legend()
    plt.grid(True)
    
    # Plot Sensor Temperature B over Time
    plt.subplot(3, 1, 3)
    plt.plot(df['Timestamp'], df['TModB'], label='Sensor Temperature B (TModB)', color='purple')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Sensor Temperature B Over Time - {location}')
    plt.legend()
    plt.grid(True)
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
