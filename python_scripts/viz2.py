import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(2024)

# Generate different datasets
data1 = pd.DataFrame({
    'A': np.random.normal(loc=0, scale=1, size=100),
    'B': np.random.normal(loc=5, scale=2, size=100),
    'C': np.random.uniform(low=0, high=10, size=100),
    'D': np.random.beta(a=2, b=5, size=100)
})

data2 = pd.DataFrame({
    'A': np.random.normal(loc=0, scale=1, size=100),
    'B': np.random.normal(loc=5, scale=2, size=100),
    'C': np.random.uniform(low=0, high=10, size=100),
    'D': np.random.beta(a=2, b=5, size=100)
})

# Create a time series dataset
time_series_data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2023', periods=100, freq='D'),
    'Value': np.random.randn(100).cumsum()
})
time_series_data.set_index('Date', inplace=True)

# Set up the 2x2 grid for plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Heatmap 1 for data1 correlations
corr1 = data1.corr()
sns.heatmap(corr1, ax=axs[0, 0], cmap='coolwarm', annot=True)
axs[0, 0].set_title('Heatmap of Data1 Correlation Matrix')

# Heatmap 2 for data2 correlations
corr2 = data2.corr()
sns.heatmap(corr2, ax=axs[0, 1], cmap='viridis', annot=True)
axs[0, 1].set_title('Heatmap of Data2 Correlation Matrix')

# Histogram for column A from data1
sns.histplot(data1['A'], kde=True, ax=axs[1, 0])
axs[1, 0].set_title('Histogram of Column A in Data1')

# Scatter plot for columns A vs. B from data1
sns.scatterplot(x=data1['A'], y=data1['B'], ax=axs[1, 1])
axs[1, 1].set_title('Scatter Plot of A vs. B in Data1')
axs[1, 1].set_xlabel('A')
axs[1, 1].set_ylabel('B')

# Adjust layout to increase space between plots
plt.tight_layout()
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
