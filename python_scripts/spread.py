import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the seed for reproducibility
np.random.seed(2024)

# Generate different distributions
normal_data = np.random.normal(loc=0, scale=1, size=1000)
uniform_data = np.random.uniform(low=-3, high=3, size=1000)
exponential_data = np.random.exponential(scale=1, size=1000)
chi_square_data = np.random.chisquare(df=2, size=1000)
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)

# Create a DataFrame to store all distributions
data = pd.DataFrame({
    'Normal': normal_data,
    'Uniform': uniform_data,
    'Exponential': exponential_data,
    'Chi-Square': chi_square_data,
    'Binomial': binomial_data
})

# Melt the DataFrame for easier plotting with seaborn
data_melted = data.melt(var_name='Distribution', value_name='Value')

# Plot density plots for all distributions on the same plot
plt.figure(figsize=(14, 8))
sns.kdeplot(data=data_melted, x='Value', hue='Distribution', fill=True, common_norm=False, alpha=0.5)

# Add titles and labels
plt.title('Visualizing Different Distributions with Density Plots')
plt.xlabel('Value')
plt.ylabel('Density')
#plt.legend(title='Distribution')

# Show the plot
plt.show()
