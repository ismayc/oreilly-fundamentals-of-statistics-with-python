import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from scipy.stats import mode

# Set the seed for reproducibility
np.random.seed(2024)

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate normal distribution data
normal_samples = np.random.normal(loc=mean, scale=std_dev, size=30000)

# Calculate mode
#mode_value = mode(normal_samples).mode[0]

# Plot the distribution
plt.figure(figsize=(12, 6))
sns.histplot(normal_samples, kde=True, bins=30)

# Add lines for mean, median, and mode
plt.axvline(np.mean(normal_samples), color='r', linestyle='--', label='Mean (μ)')
plt.axvline(np.median(normal_samples), color='g', linestyle='-.', label='Median')
#plt.axvline(mode_value, color='b', linestyle='-', label='Mode')

# Adding title and labels
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show plot
plt.show()
