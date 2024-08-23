import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/benin-malanville.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing values in relevant columns
df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'Tamb'])

# Plot histograms for the variables
plt.figure(figsize=(14, 10))

# Plot histogram for GHI
plt.subplot(3, 2, 1)
plt.hist(df['GHI'], bins=50, color='blue', edgecolor='black')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of Global Horizontal Irradiance (GHI)')

# Plot histogram for DNI
plt.subplot(3, 2, 2)
plt.hist(df['DNI'], bins=50, color='red', edgecolor='black')
plt.xlabel('DNI')
plt.ylabel('Frequency')
plt.title('Histogram of Direct Normal Irradiance (DNI)')

# Plot histogram for DHI
plt.subplot(3, 2, 3)
plt.hist(df['DHI'], bins=50, color='green', edgecolor='black')
plt.xlabel('DHI')
plt.ylabel('Frequency')
plt.title('Histogram of Diffuse Horizontal Irradiance (DHI)')

# Plot histogram for WS
plt.subplot(3, 2, 4)
plt.hist(df['WS'], bins=50, color='purple', edgecolor='black')
plt.xlabel('Wind Speed (WS)')
plt.ylabel('Frequency')
plt.title('Histogram of Wind Speed (WS)')

# Plot histogram for Air Temperature
plt.subplot(3, 2, 5)
plt.hist(df['Tamb'], bins=50, color='orange', edgecolor='black')
plt.xlabel('Air Temperature (Tamb)')
plt.ylabel('Frequency')
plt.title('Histogram of Air Temperature (Tamb)')

# Adjust layout
plt.tight_layout()
plt.show()
