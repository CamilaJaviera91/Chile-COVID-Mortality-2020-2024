# Importing the matplotlib library for plotting and visualization
import matplotlib.pyplot as plt

# Importing the numpy library for numerical operations, such as creating index arrays
import numpy as np

# Importing the sys module to manipulate the Python runtime environment
import sys

# Adding the path to the folder containing the function to be imported
# This allows importing a custom module from a specific directory
sys.path.append('./source/postgres/queries/')

# Importing the 'yearly_deaths_by_gender_and_region' function from a custom module
# Renaming it as 'gr' for easier use
from yearly_deaths_by_gender_and_region import yearly_deaths_by_gender_and_region as gr

# Retrieve the DataFrame containing the yearly deaths data
df = gr()

# Group the data by year and calculate the sum of deaths for men and women
# This ensures that duplicate years are combined, summing their respective values
grouped_df = df.groupby('year', as_index=False).sum()

# Display the unique years in the grouped DataFrame
# This step helps verify that the grouping worked as expected
print(f"Unique years after grouping: {grouped_df['year'].tolist()}")

# Extract the 'year', 'Women', and 'Men' columns for plotting
years = grouped_df['year']  # Years in the dataset
women_deaths = grouped_df['Women']  # Total deaths of women per year
men_deaths = grouped_df['Men']  # Total deaths of men per year

# Create a list of indices (integers) corresponding to each year
# This is used to position the bars on the X-axis
x = np.arange(len(years))

# Plot the stacked bar chart
# Plot the bar for women's deaths first
plt.bar(x, women_deaths, label="Women", color="salmon")

# Plot the bar for men's deaths, stacking it on top of the women's deaths
plt.bar(x, men_deaths, bottom=women_deaths, label="Men", color="lightblue")

# Add annotations on top of each bar to show the exact number of deaths
for container in plt.gca().containers:  # Get all bar containers in the current axis
    plt.gca().bar_label(container, fmt='%d')  # Add the labels formatted as integers

# Add labels for the X and Y axes
plt.xlabel("Year")  # Label for the X-axis (years)
plt.ylabel("Deaths")  # Label for the Y-axis (number of deaths)

# Add a title to the chart
plt.title("Yearly Deaths by Gender")  # Descriptive title for the visualization

# Replace the default X-axis ticks with the actual year labels
plt.xticks(x, years)

# Add a legend to identify the colors used for men and women
plt.legend()

# Adjust the layout to prevent overlapping of elements (e.g., labels, title)
plt.tight_layout()

# Display the final chart
plt.show()