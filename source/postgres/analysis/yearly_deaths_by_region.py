# Importing the matplotlib library for plotting and visualization
import matplotlib.pyplot as plt

# Importing the numpy library for numerical operations, such as creating index arrays
import numpy as np

# Importing the sys module to manipulate the Python runtime environment
import sys

# Adding the path to the folder containing the function to be imported
sys.path.append('./source/postgres/queries/')

# Importing the 'yearly_deaths_by_gender_and_region' function from a custom module
from yearly_deaths_by_gender_and_region import yearly_deaths_by_gender_and_region as gr

# Retrieve the DataFrame containing the yearly deaths data
df = gr()

# Group the data by year and region, summing deaths for women and men
grouped_df = df.groupby(['year', 'region'], as_index=False).agg({
    'Women': 'sum',
    'Men': 'sum'
})

# Create a new column for total deaths by region
grouped_df['Total_Deaths'] = grouped_df['Women'] + grouped_df['Men']

# Pivot the table to organize regions as columns
pivot_df = grouped_df.pivot(index='year', columns='region', values='Total_Deaths').fillna(0)

# Extract unique years and regions for the plot
years = pivot_df.index
regions = pivot_df.columns

# Create a stacked bar plot
x = np.arange(len(years))  # Positions for the X-axis
width = 0.85  # Width of the bars

# Plot each region as a layer in the stacked bar chart
bottom_values = np.zeros(len(years))  # Initialize the bottom layer
for region in regions:
    plt.bar(x, pivot_df[region], label=region, bottom=bottom_values, width=width)
    bottom_values += pivot_df[region]  # Update the bottom layer for the next region

# Add annotations on top of each bar to show the exact number of deaths
for container in plt.gca().containers:  # Get all bar containers in the current axis
    plt.gca().bar_label(container, fmt='%d')  # Add the labels formatted as integers

# Add labels, title, and legend
plt.xlabel("Year")
plt.ylabel("Total Deaths")
plt.title("Yearly Deaths by Region")
plt.xticks(x, years, rotation=45)  # Rotate the years for better visibility
plt.legend(title="Regions", bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside

# Adjust layout and show the chart
plt.tight_layout()
plt.show()