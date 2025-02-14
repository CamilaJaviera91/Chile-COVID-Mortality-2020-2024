# Import necessary libraries
import pandas as pd  # For working with data in DataFrame format
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For creating attractive and informative statistical plots

# Load the dataset from a CSV file into a pandas DataFrame
# Replace './googlesheets/database/COVID_CLEAN.csv' with the path to your dataset
df = pd.read_csv('./source/googlesheets/database/COVID_CLEAN.csv')

# Group the data by 'AÑO' (year) and 'RANGO_ETARIO' (age range)
# Use the size() function to count the number of rows (records) in each group
# Reset the index to turn the grouped DataFrame into a regular DataFrame
# Rename the count column as 'MUERTES' (deaths)
df_count = df.groupby(['AÑO', 'RANGO_ETARIO']).size().reset_index(name='MUERTES')

# Set the figure size for the plot to make it visually appealing and clear
plt.figure(figsize=(10, 6))

# Create a bar plot using seaborn
# 'data=df_count' specifies the DataFrame to use for the plot
# 'x' is the column representing the year (AÑO), which will appear on the x-axis
# 'y' is the column representing the number of deaths (MUERTES), which will appear on the y-axis
# 'hue' differentiates the data by age range (RANGO_ETARIO), creating separate bars for each region within the same year
sns.barplot(data=df_count, x='AÑO', y='MUERTES', hue='RANGO_ETARIO')

# Add annotations to show the numbers on top of the bars
# Loop through each bar and add its value
for container in plt.gca().containers:  # Get all the bars in the current plot
    plt.gca().bar_label(container, fmt='%d')  # Format numbers as integers

# Add a descriptive title to the plot to indicate what the graph represents
plt.title('Yearly Deaths by Age Range')

# Label the x-axis to indicate it represents the year
plt.xlabel('Year')

# Label the y-axis to indicate it represents the number of deaths
plt.ylabel('Number of Deaths')

# Rotate the x-axis labels by 45 degrees to prevent overlap and improve readability
plt.xticks(rotation=45)

# Adjust the layout to prevent labels, titles, or other elements from being cut off
plt.tight_layout()

# Display the final plot to the screen
plt.show()
