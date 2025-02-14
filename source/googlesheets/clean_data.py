# Import necessary libraries
import pandas as pd  # For data manipulation and handling
import matplotlib.pyplot as plt  # For plotting and visualizations
import warnings  # To handle and suppress warnings
import os  # For file and directory operations

# Import custom functions from google_sheets_utils
from google_sheets_utils import sheets_to_dataframe as sd  # Function to extract Google Sheets data as a DataFrame
from google_sheets_utils import csv_to_sheets as cs  # Function to upload a CSV file to Google Sheets

# Suppress warnings to avoid clutter in the output
warnings.filterwarnings('ignore')

# Set the default plotting style for visualizations
plt.style.use("default")

# Step 1: Extract data from Google Sheets into a Pandas DataFrame
# This function fetches data from a Google Sheet and returns it as a DataFrame for processing
df = sd()  # Uses the custom `sheets_to_dataframe` function to retrieve data

# Step 2: Specify columns to be removed from the DataFrame
# The listed columns contain data that is not relevant for the current analysis or processing task
columns_to_remove = [
    'EDAD_TIPO', 'COD_COMUNA', 'DIAG1', 'CAPITULO_DIAG1', 'GLOSA_CAPITULO_DIAG1',
    'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1', 'CODIGO_CATEGORIA_DIAG1', 'GLOSA_CATEGORIA_DIAG1',
    'CODIGO_SUBCATEGORIA_DIAG1', 'GLOSA_SUBCATEGORIA_DIAG1', 'DIAG2', 'CAPITULO_DIAG2',
    'GLOSA_CAPITULO_DIAG2', 'CODIGO_GRUPO_DIAG2', 'GLOSA_GRUPO_DIAG2', 'CODIGO_CATEGORIA_DIAG2',
    'GLOSA_CATEGORIA_DIAG2', 'CODIGO_SUBCATEGORIA_DIAG2', 'GLOSA_SUBCATEGORIA_DIAG2'
]

# Step 3: Remove the specified columns from the DataFrame
# The `drop` method removes unnecessary columns. The `inplace=True` parameter ensures changes are applied directly.
df.drop(columns=columns_to_remove, inplace=True)

# Step 4: Process the 'FECHA_DEF' (date of death) column
# Convert the 'FECHA_DEF' column to datetime format for consistency and ease of use
df['FECHA_DEF'] = pd.to_datetime(df['FECHA_DEF'])

# Extract the period (month and year) from the date column
# This step creates a new column 'PERIODO' that represents the month and year of each entry
df['PERIODO'] = df['FECHA_DEF'].dt.to_period('M')

# Step 4.1: Create an age range based on EDAD_CANT
# Define the age range limits
bins = [0, 12, 18, 30, 45, 60, 75, 90, 130]  # The limits of the ranges (adjust as needed)

# Define the labels for each range
labels = ['0-12 Años', '13-18 Años', '19-30 Años', '31-45 Años', 
          '46-60 Años', '61-75 Años', '76-90 Años', '91+ Años']

# Assign EDAD_CANT values to a range using pd.cut
df['RANGO_ETARIO'] = pd.cut(df['EDAD_CANT'], bins=bins, labels=labels, right=False)

# Verify the result
print(df[['EDAD_CANT', 'RANGO_ETARIO']].head())

# Step 5: Save the modified DataFrame to a new CSV file in the specified folder
# Define the folder path where the output CSV file will be saved
FOLDER = './googlesheets/database/'  

# Check if the specified folder exists; if not, create it
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

# Define the full path for the output file
output_file_path = FOLDER + 'COVID_CLEAN.csv'  

# Save the modified DataFrame to a CSV file
# The `index=False` parameter ensures that the DataFrame's index is not included in the output file
df.to_csv(output_file_path, index=False)

# Step 6: Reload the newly created CSV file (optional validation step)
# This step ensures the file was saved correctly by reading it back into a DataFrame
file_path = FOLDER + 'COVID_CLEAN.csv'  # Specify the path to the saved file
df = pd.read_csv(file_path)  # Reload the file for further validation or processing

# Step 7: Upload the cleaned CSV file to Google Sheets
# This step uses the custom `csv_to_sheets` function to upload the file to Google Sheets for sharing or further analysis
cs()  # Function handles the uploading process