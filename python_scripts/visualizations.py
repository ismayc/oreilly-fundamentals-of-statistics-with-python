import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(2024)

# Generate different datasets
data1 = np.random.normal(loc=50, scale=10, size=1000)  # For histogram
data2 = np.random.uniform(low=20, high=80, size=100)   # For box plot
data3_x = np.random.normal(loc=0, scale=1, size=100)   # For scatter plot x-values
data3_y = np.random.normal(loc=0, scale=1, size=100)   # For scatter plot y-values
categories = ['A', 'B', 'C', 'D']
data4 = np.random.choice(categories, size=100)         # For bar graph

# Prepare data for the bar graph
bar_data = pd.Series(data4).value_counts().sort_index()

# Set up the 2x2 grid for plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Histogram
sns.histplot(data1, ax=axs[0, 0])
axs[0, 0].set_title('Histogram')
axs[0, 0].set_xlabel('Value')
axs[0, 0].set_ylabel('Frequency')

# Box plot
sns.boxplot(x=data2, ax=axs[0, 1])
axs[0, 1].set_title('Box Plot')
axs[0, 1].set_xlabel('Value')

# Scatter plot
sns.scatterplot(x=data3_x, y=data3_y, ax=axs[1, 0])
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X Value')
axs[1, 0].set_ylabel('Y Value')

# Bar graph
sns.barplot(x=bar_data.index, y=bar_data.values, ax=axs[1, 1])
axs[1, 1].set_title('Bar Graph')
axs[1, 1].set_xlabel('Category')
axs[1, 1].set_ylabel('Count')

# Adjust layout to increase space between plots
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.show()
