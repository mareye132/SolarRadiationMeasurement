import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Loop through each file, load the dataset, and plot the correlation matrix
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Drop columns that are not numerical or are not useful for correlation analysis
    df = df.drop(columns=['Timestamp', 'Comments'])
    
    # Compute the correlation matrix
    correlation_matrix = df.corr()
    
    # Plot the correlation matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Matrix - {location}')
    plt.show()
