import pandas as pd
from scipy import stats

# Define the file paths
file_paths = {
    'Togo': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/togo-dapaong_qc.csv',
    'Benin': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/benin-malanville.csv',
    'Sierra Leone': 'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/sierraleone-bumbuna.csv'
}

# Perform Z-score analysis for each dataset
for location, file_path in file_paths.items():
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Drop rows with missing values in relevant columns
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'Tamb'])
    
    # Calculate Z-scores for the relevant columns
    columns_to_check = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    z_scores = pd.DataFrame()
    
    for column in columns_to_check:
        z_scores[column] = stats.zscore(df[column])
    
    # Add Z-scores to the original dataframe
    df_with_z_scores = df.copy()
    df_with_z_scores[z_scores.columns] = z_scores
    
    # Flag points with Z-scores greater than 3 or less than -3
    threshold = 3
    flags = pd.DataFrame()
    
    for column in columns_to_check:
        flags[column + '_flag'] = (abs(df_with_z_scores[column]) > threshold).astype(int)
    
    # Combine the flagged points with the original dataframe
    df_with_flags = pd.concat([df_with_z_scores, flags], axis=1)
    
    # Save the results to a new CSV file
    output_path = f'C:/Users/user/Desktop/Github/SolarRadiationMeasurement/scripts/{location.lower()}_zscore_analysis_results.csv'
    df_with_flags.to_csv(output_path, index=False)

    print(f"Z-score analysis completed and results saved to '{location.lower()}_zscore_analysis_results.csv'.")
