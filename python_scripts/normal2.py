import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(2024)

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate normal distribution data
normal_samples = np.random.normal(loc=mean, scale=std_dev, size=10000)

# Plot the distribution
plt.figure(figsize=(12, 6))
sns.histplot(normal_samples, kde=True, bins=30)

# Add lines for mean and standard deviations
plt.axvline(mean, color='r', linestyle='--', label='Mean (μ)')
plt.axvline(mean + std_dev, color='g', linestyle='-.', label='1σ')
plt.axvline(mean - std_dev, color='g', linestyle='-.')
plt.axvline(mean + 2*std_dev, color='b', linestyle='-.', label='2σ')
plt.axvline(mean - 2*std_dev, color='b', linestyle='-.')
plt.axvline(mean + 3*std_dev, color='purple', linestyle='-.', label='3σ')
plt.axvline(mean - 3*std_dev, color='purple', linestyle='-.')

# Adding shaded areas for the empirical rule
plt.fill_betweenx([0, 200], mean - std_dev, mean + std_dev, color='green', alpha=0.2)
plt.fill_betweenx([0, 200], mean - 2*std_dev, mean + 2*std_dev, color='blue', alpha=0.2)
plt.fill_betweenx([0, 200], mean - 3*std_dev, mean + 3*std_dev, color='purple', alpha=0.2)

# Adding title and labels
plt.title('Normal Distribution and Empirical Rule')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show plot
plt.show()
