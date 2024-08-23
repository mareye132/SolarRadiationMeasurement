import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/togo-dapaong_qc.csv'

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
plt.title('Time Series Analysis of GHI')
plt.legend()
plt.grid(True)
plt.show()
