import pandas as pd
from scipy import stats
def calculate_summary_statistics(df):
    """
    Calculate and print summary statistics for each column in the dataframe.
    """

    print("Summary Statistics for each column:\n")
    
    print("1. Mean:")
    print(df.mean(), "\n")
    
    print("2. Median:")
    print(df.median(), "\n")
    
    print("3. Mode:")
    print(df.mode().iloc[0], "\n")  # iloc[0] to get the first mode if there are multiple modes
    
    print("4. Standard Deviation:")
    print(df.std(), "\n")
    
    print("5. Variance:")
    print(df.var(), "\n")
    
    print("6. Skewness:")
    print(df.skew(), "\n")
    
    print("7. Kurtosis:")
    print(df.kurtosis(), "\n")
    
    print("8. Z-score (standardized values):")
    z_scores = df.apply(stats.zscore)
    print(z_scores, "\n")
    
    print("9. Min and Max Values:")
    print("Min Values:\n", df.min(), "\n")
    print("Max Values:\n", df.max(), "\n")
    
    print("10. Range (Max - Min):")
    print(df.max() - df.min(), "\n")
    
    print("11. Quantiles (25%, 50%, 75%):")
    print(df.quantile([0.25, 0.5, 0.75]), "\n")

if __name__ == "__main__":
    # Load the dataset (replace 'solar_radiation_data.csv' with your actual file name)
    df = pd.read_csv('C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/benin-malanville.csv')
    df2=pd.read_csv('C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/sierraleone-bumbuna.csv')
    df3=pd.read_csv('C:/Users/user/Desktop/Github/SolarRadiationMeasurement/Src/togo-dapaong_qc.csv')
    # Ensure only numerical columns are analyzed
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    numerical_df2 = df.select_dtypes(include=['float64', 'int64'])
    numerical_df3 = df.select_dtypes(include=['float64', 'int64'])
    # Call the function to calculate and display summary statistics for benin-malanville
    print("Summary Statistics for Benin (Malanville):")
    calculate_summary_statistics(numerical_df)
    # Call the function to calculate and display summary statistics for sierraleone-bumbuna\
    print("Summary Statistics for Sierra Leone (Bumbuna):")
    calculate_summary_statistics(numerical_df2)
    # Call the function to calculate and display summary statistics for togo-dapaong_qc
    print("Summary Statistics for Togo (Dapaong QC):")
    calculate_summary_statistics(numerical_df3)