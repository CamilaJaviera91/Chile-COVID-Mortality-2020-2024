# Importing the matplotlib library for plotting and visualization
import matplotlib.pyplot as plt

# Importing the numpy library for numerical operations, such as creating index arrays
import numpy as np

# Importing the sys module to manipulate the Python runtime environment
import sys

# Importing the pandas library to work with structured data (DataFrames)
import pandas as pd  # Ensure pandas is installed in your environment

# Adding the path to the folder containing the function to be imported
# This allows importing a custom module from a specific directory
sys.path.append('./postgres/queries/')

# Importing the 'yearly_deaths_by_gender_and_region' function from a custom module
# Renaming it as 'gr' for easier use
from yearly_deaths_by_gender_and_region import yearly_deaths_by_gender_and_region as gr

# Retrieve the DataFrame containing the yearly deaths data
df = gr()

# Group the data by year and region, calculating the sum of deaths for men and women
# This ensures that duplicate years and regions are combined, summing their respective values
grouped_df = df.groupby('year', as_index=False).sum()

# Create a new column to represent the total deaths by region
grouped_df['Total_Deaths'] = grouped_df['Women'] + grouped_df['Men']

# Extract and display unique region names
unique_regions = grouped_df['region'].unique()
print(f"Unique regions: {unique_regions}")

# Extract the 'year', 'region', and 'Total_Deaths' columns for plotting
years = grouped_df['year']
regions = grouped_df['region']  # Region names
total_deaths = grouped_df['Total_Deaths']

# Create a list of indices (integers) corresponding to each year
# This is used to position the bars on the X-axis
x = np.arange(len(years))

# Plot the bar chart showing total deaths by region
plt.bar(x, total_deaths, label="Total Deaths", color="lightblue")

# Add annotations on top of each bar to show the exact number of deaths
for container in plt.gca().containers:  # Get all bar containers in the current axis
    plt.gca().bar_label(container, fmt='%d')  # Add the labels formatted as integers

# Add labels for the X and Y axes
plt.xlabel("Year")  # Label for the X-axis (years)
plt.ylabel("Deaths")  # Label for the Y-axis (number of deaths)

# Add a title to the chart
plt.title("Yearly Deaths by Region")  # Descriptive title for the visualization

# Replace the default X-axis ticks with the actual year labels
plt.xticks(x, years)

# Add a legend to identify the chart
plt.legend()

# Adjust the layout to prevent overlapping of elements (e.g., labels, title)
plt.tight_layout()

# Display the final chart
plt.show()