import numpy as np
import pandas as pd

# Parameters
N = 4  # Number of assets (currency pairs)
T = 10  # Number of days for the dataset
assets = ['AUD/USD', 'GBP/USD', 'EUR/USD', 'NZD/USD']

# Generate random volumes (in USD) for each asset over T days
np.random.seed(42)  # For reproducibility
volumes = np.random.uniform(low=1e6, high=5e6, size=(T, N))  # Random volumes in USD

# Generate random exchange rates (e.g., daily close prices)
exchange_rates = np.random.uniform(low=0.7, high=1.3, size=(T, N))

# Compute daily variances for each asset based on exchange rates
variances = np.var(exchange_rates, axis=0)

# Create a DataFrame to organize the dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=T, freq='D'),
    'AUD/USD Volume': volumes[:, 0],
    'GBP/USD Volume': volumes[:, 1],
    'EUR/USD Volume': volumes[:, 2],
    'NZD/USD Volume': volumes[:, 3],
    'AUD/USD Rate': exchange_rates[:, 0],
    'GBP/USD Rate': exchange_rates[:, 1],
    'EUR/USD Rate': exchange_rates[:, 2],
    'NZD/USD Rate': exchange_rates[:, 3]
}

df = pd.DataFrame(data)
df['AUD/USD Variance'] = variances[0]
df['GBP/USD Variance'] = variances[1]
df['EUR/USD Variance'] = variances[2]
df['NZD/USD Variance'] = variances[3]

df
