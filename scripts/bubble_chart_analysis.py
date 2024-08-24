import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths for the three datasets
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Iterate over each dataset
for country, file_path in file_paths.items():
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
    plt.title(f'Bubble Chart: GHI vs Tamb vs WS with Bubble Size representing RH ({country})')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Ambient Temperature (Tamb)')
    plt.legend(title='Wind Speed (WS)')
    plt.grid(True)

    # Create output directory if it doesn't exist
    output_dir = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot
    output_path = os.path.join(output_dir, f'{country.lower()}_bubble_chart_analysis.png')
    plt.savefig(output_path)
    plt.show()

    print(f"Bubble chart for {country} created and saved to '{output_path}'.")
