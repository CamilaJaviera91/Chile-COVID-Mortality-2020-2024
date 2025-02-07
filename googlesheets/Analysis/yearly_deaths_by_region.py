# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file
df = pd.read_csv('./googlesheets/database/COVID_CLEAN.csv')

# Group the data by 'AÑO' (year) and 'NOMBRE_REGION' (region), 
# then count the number of records in each group to calculate deaths
df_count = df.groupby(['AÑO', 'NOMBRE_REGION']).size().reset_index(name='MUERTES')

# Set the figure size for the plot
plt.figure(figsize=(10,6))

# Create a bar plot using seaborn
# 'data=df_count' refers to the DataFrame with counted deaths
# 'x' is the year, 'y' is the number of deaths, and 'hue' is the region
sns.barplot(data=df_count, x='AÑO', y='MUERTES', hue='NOMBRE_REGION')

# Add title and labels to the plot
plt.title('Yearly Deaths by Region')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')

# Rotate the x-axis labels by 45 degrees for better readability
plt.xticks(rotation=45)

# Adjust the layout to prevent clipping of labels
plt.tight_layout()

# Show the plot
plt.show()