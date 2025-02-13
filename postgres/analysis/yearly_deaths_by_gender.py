import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd  # Make sure pandas is imported

# Add path to import the function
sys.path.append('./postgres/queries/')
from yearly_deaths_by_gender_and_region import yearly_deaths_by_gender_and_region as gr

# Retrieve the DataFrame
df = gr()

# Group data by year and sum the deaths of men and women
grouped_df = df.groupby('year', as_index=False).sum()

# Display unique years after grouping
print(f"Unique years after grouping: {grouped_df['year'].tolist()}")

# Grouped data
years = grouped_df['year']
women_deaths = grouped_df['Women']  # Women's deaths
men_deaths = grouped_df['Men']      # Men's deaths

# Create a list of indices for the columns (X-axis)
x = np.arange(len(years))

# Create the stacked bar chart
plt.bar(x, women_deaths, label="Women", color="salmon")
plt.bar(x, men_deaths, bottom=women_deaths, label="Men", color="lightblue")

# Add annotations to show the numbers on top of the bars
# Loop through each bar and add its value
for container in plt.gca().containers:  # Get all the bars in the current plot
    plt.gca().bar_label(container, fmt='%d')  # Format numbers as integers

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Deaths")
plt.title("Yearly Deaths by Gender")
plt.xticks(x, years)  # Replace indices with year labels
plt.legend()  # Show legend

# Display the chart
plt.tight_layout()
plt.show()