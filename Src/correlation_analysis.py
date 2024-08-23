import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path
file_path = 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/sierraleone-bumbuna.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Drop columns that are not numerical or are not useful for correlation analysis
df = df.drop(columns=['Timestamp', 'Comments'])

# Compute the correlation matrix
correlation_matrix = df.corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
