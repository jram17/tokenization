import numpy as np
import pandas as pd

# Simulated dataset for trade volumes over 10 days for 4 currency pairs
data_volumes = {
    "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", 
             "2023-10-06", "2023-10-07", "2023-10-08", "2023-10-09", "2023-10-10"],
    "EUR/USD Volume": [1200000, 1100000, 1300000, 1250000, 1150000, 1180000, 1240000, 1190000, 1170000, 1130000],
    "GBP/USD Volume": [1500000, 1400000, 1600000, 1480000, 1420000, 1510000, 1470000, 1530000, 1440000, 1460000],
    "AUD/USD Volume": [900000, 950000, 920000, 890000, 880000, 870000, 910000, 860000, 940000, 880000],
    "NZD/USD Volume": [800000, 750000, 810000, 790000, 820000, 830000, 780000, 770000, 810000, 790000],
    "EUR/USD Rate": [1.17, 1.16, 1.18, 1.19, 1.15, 1.16, 1.17, 1.18, 1.16, 1.15],
    "GBP/USD Rate": [1.35, 1.34, 1.36, 1.33, 1.32, 1.34, 1.35, 1.36, 1.34, 1.33],
    "AUD/USD Rate": [0.71, 0.72, 0.71, 0.70, 0.71, 0.72, 0.71, 0.72, 0.71, 0.70],
    "NZD/USD Rate": [0.67, 0.66, 0.67, 0.66, 0.65, 0.68, 0.67, 0.66, 0.68, 0.67]
}

# Create a DataFrame for volumes
df_volumes = pd.DataFrame(data_volumes)

# Covariance matrix for currency pairs (from earlier calculation)
cov_matrix = np.array([
    [0.000179, 0.000096, -0.000008, -0.000010],
    [0.000096, 0.000173, 0.000042, 0.000040],
    [-0.000008, 0.000042, 0.000054, 0.000003],
    [-0.000010, 0.000040, 0.000003, 0.000090]
])

# List to store portfolio variances for each day
corrected_portfolio_variances = []

# Loop over each day to create the portfolio and calculate variance
for index, row in df_volumes.iterrows():
    # Get the trade volumes for the day
    volumes = np.array([row["EUR/USD Volume"], row["GBP/USD Volume"], row["AUD/USD Volume"], row["NZD/USD Volume"]])
    
    # Get the exchange rates for the day
    exchange_rates = np.array([row["EUR/USD Rate"], row["GBP/USD Rate"], row["AUD/USD Rate"], row["NZD/USD Rate"]])
    
    # Adjust the asset volumes by the exchange rates
    adjusted_volumes = volumes * exchange_rates
    
    # Calculate the total volume for the day (sum of adjusted volumes)
    total_volume = np.sum(adjusted_volumes)
    
    # Calculate the allocation weights (proportional to the adjusted volume of each asset)
    weights = adjusted_volumes / total_volume
    
    # Calculate the portfolio variance for the day using weights and the covariance matrix
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    
    # Store the portfolio variance for the day
    corrected_portfolio_variances.append(portfolio_variance)

# Combine with dates to show portfolio variance for each day
corrected_portfolio_variance_df = pd.DataFrame({
    "Date": df_volumes["Date"],
    "Corrected Portfolio Variance": corrected_portfolio_variances
})

# Display the result
print(corrected_portfolio_variance_df)
