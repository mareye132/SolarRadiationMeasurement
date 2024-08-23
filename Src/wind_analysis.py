import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/benin-malanville.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing wind speed or wind direction values
df = df.dropna(subset=['WS', 'WD'])

# Convert Timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Plot Wind Speed over Time
plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(df['Timestamp'], df['WS'], label='Wind Speed (WS)', color='blue')
plt.xlabel('Timestamp')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Speed Over Time')
plt.legend()
plt.grid(True)

# Plot Wind Direction over Time
plt.subplot(2, 1, 2)
plt.plot(df['Timestamp'], df['WD'], label='Wind Direction (WD)', color='red')
plt.xlabel('Timestamp')
plt.ylabel('Wind Direction (degrees)')
plt.title('Wind Direction Over Time')
plt.legend()
plt.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
