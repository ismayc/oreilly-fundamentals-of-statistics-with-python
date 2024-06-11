import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(2024)

# Generate different datasets
binom_samples = np.random.binomial(n=20, p=0.5, size=10000)
poisson_samples = np.random.poisson(lam=5, size=10000)
normal_samples = np.random.normal(loc=10, scale=1, size=10000)
exponential_samples = np.random.exponential(scale=4, size=10000)

# Set up the 2x2 grid for plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Binomial Distribution Histogram
sns.histplot(binom_samples, kde=False, bins=30, ax=axs[0, 0])
axs[0, 0].set_title('Binomial Distribution (n=10, p=0.5)')
axs[0, 0].set_xlabel('Number of Successes')
axs[0, 0].set_ylabel('Frequency')

# Poisson Distribution Histogram
sns.histplot(poisson_samples, kde=False, bins=30, ax=axs[0, 1])
axs[0, 1].set_title('Poisson Distribution (λ=5)')
axs[0, 1].set_xlabel('Number of Events')
axs[0, 1].set_ylabel('Frequency')

# Normal Distribution Histogram
sns.histplot(normal_samples, kde=False, bins=30, ax=axs[1, 0])
axs[1, 0].set_title('Normal Distribution (μ=10, σ=1)')
axs[1, 0].set_xlabel('Value')
axs[1, 0].set_ylabel('Frequency')

# Exponential Distribution Histogram
sns.histplot(exponential_samples, kde=False, bins=30, ax=axs[1, 1])
axs[1, 1].set_title('Exponential Distribution (λ=4)')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout to increase space between plots
plt.tight_layout()
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
