import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/togo-dapaong_qc.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing values in relevant columns
df = df.dropna(subset=['GHI', 'Tamb', 'WS', 'RH'])

# Create a bubble chart
plt.figure(figsize=(12, 8))

# Plot using Seaborn
sns.scatterplot(
    data=df,
    x='GHI',
    y='Tamb',
    size='RH',  # Bubble size represents RH
    sizes=(20, 200),  # Adjust bubble size range
    hue='WS',  # Color by WS
    palette='viridis',  # Color palette
    alpha=0.7,
    edgecolor=None
)

# Customize the plot
plt.title('Bubble Chart: GHI vs Tamb vs WS with Bubble Size representing RH')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.legend(title='Wind Speed (WS)')
plt.grid(True)

# Save the plot
output_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/bubble_chart_analysis.png'
plt.savefig(output_path)
plt.show()

print("Bubble chart created and saved to 'bubble_chart_analysis.png'.")
