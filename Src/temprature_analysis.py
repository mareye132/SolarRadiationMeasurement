import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/togo-dapaong_qc.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing temperature values
df = df.dropna(subset=['Tamb', 'TModA', 'TModB'])

# Convert Timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Plot Air Temperature over Time
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(df['Timestamp'], df['Tamb'], label='Air Temperature (Tamb)', color='green')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Air Temperature Over Time')
plt.legend()
plt.grid(True)

# Plot Sensor Temperature A over Time
plt.subplot(3, 1, 2)
plt.plot(df['Timestamp'], df['TModA'], label='Sensor Temperature A (TModA)', color='orange')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Sensor Temperature A Over Time')
plt.legend()
plt.grid(True)

# Plot Sensor Temperature B over Time
plt.subplot(3, 1, 3)
plt.plot(df['Timestamp'], df['TModB'], label='Sensor Temperature B (TModB)', color='purple')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Sensor Temperature B Over Time')
plt.legend()
plt.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
