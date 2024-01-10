import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
data = pd.read_csv('nuclear_power_dataset.csv')

# Create a figure and subplots with the same size for all plots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.patch.set_facecolor('lightyellow')  # Set background color

# Custom colors for the bars in the countplot
custom_colors = {'Planned': 'lightgreen', 'Operational': 'lightblue', 'Under Construction': 'yellow'}

# Visualization 1: Bar plot - Power Plant Status
sns.countplot(x='Status', data=data, ax=axs[0, 0], palette=custom_colors)
axs[0, 0].set_title('Power Plant Status', color='red')

# Visualization 2: Donut chart - Status Distribution
status_counts = data['Status'].value_counts()
explode = [0.1 if status == 'Planned' else 0 for status in status_counts.index]
axs[0, 1].pie(status_counts, labels=None, autopct='%1.1f%%', startangle=140,
              colors=sns.color_palette('pastel'), wedgeprops=dict(width=0.4, edgecolor='black'), explode=explode,
              pctdistance=0.85)  # Increase pctdistance
axs[0, 1].legend(bbox_to_anchor=(1, 1), loc='upper left', labels=status_counts.index)
axs[0, 1].set_title('Status Distribution', color='red')

# Visualization 3: Histogram - Distribution of Power Plant Capacity
sns.histplot(data['Capacity_MW'], bins=20, kde=True, ax=axs[1, 0], color='blue')
axs[1, 0].set_title('Distribution of Power Plant Capacity', color='red')
axs[1, 0].set_xlabel('Capacity (MW)')
axs[1, 0].set_ylabel('Frequency')

# Visualization 4: Line plot - Start Year vs. Capacity
sns.lineplot(x='Start_Year', y='Capacity_MW', data=data, ax=axs[1, 1], marker='o', color='green')
axs[1, 1].set_title('Start Year vs. Capacity', color='red')
axs[1, 1].set_xlabel('Start Year')
axs[1, 1].set_ylabel('Capacity (MW)')

# Add the overall title with a larger font size, black background, and white letters
plt.suptitle('Nuclear Power Dashboard', fontsize=30, color='white', backgroundcolor='black')

# Add the additional text in the bottom right corner in a box
text_box = dict(boxstyle='round', facecolor='lightblue', edgecolor='pink')
# Place the additional text in the bottom right corner
fig.text(0.88, 0.03, "Name: Hemanth\nId.No: 22084847", fontsize=12, color='black', bbox=text_box)


fig.text(0.1, -0.05, "The nuclear power dataset provides comprehensive information on global nuclear power plants, covering factors such as country, plant name, capacity, start year, technology, status, generation data, and operator details. This dataset is valuable for analyzing the development of nuclear energy, understanding patterns in plant construction and operation, and examining the distribution of capacities across regions.", wrap=True, fontsize=10, color='black')

# Adjust layout
plt.tight_layout()

# Save the dashboard as an image (PNG format)
plt.savefig('nuclear_power_dashboard_with_text.png', dpi=300)
