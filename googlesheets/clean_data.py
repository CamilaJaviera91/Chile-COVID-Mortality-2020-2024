# Import necessary libraries
import pandas as pd  # For data manipulation and handling
import matplotlib.pyplot as plt  # For plotting and visualizations
import warnings  # To handle and suppress warnings
import os

# Import custom functions from google_sheets_utils
from google_sheets_utils import sheets_to_dataframe as sd  # Function to extract Google Sheets data as a DataFrame
from google_sheets_utils import csv_to_sheets as cs  # Function to upload a CSV file to Google Sheets

# Suppress warnings to avoid clutter in the output
warnings.filterwarnings('ignore')
# Set the default plotting style
plt.style.use("default")

# Step 1: Extract data from Google Sheets into a Pandas DataFrame
df = sd()  # Uses the custom `sheets_to_dataframe` function to retrieve data

# Step 2: Specify columns to be removed from the DataFrame
# These columns are not required for the current analysis or processing
columns_to_remove = [
    'EDAD_TIPO', 'COD_COMUNA', 'DIAG1', 'CAPITULO_DIAG1', 'GLOSA_CAPITULO_DIAG1',
    'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1', 'CODIGO_CATEGORIA_DIAG1', 'GLOSA_CATEGORIA_DIAG1',
    'CODIGO_SUBCATEGORIA_DIAG1', 'GLOSA_SUBCATEGORIA_DIAG1', 'DIAG2', 'CAPITULO_DIAG2',
    'GLOSA_CAPITULO_DIAG2', 'CODIGO_GRUPO_DIAG2', 'GLOSA_GRUPO_DIAG2', 'CODIGO_CATEGORIA_DIAG2',
    'GLOSA_CATEGORIA_DIAG2', 'CODIGO_SUBCATEGORIA_DIAG2', 'GLOSA_SUBCATEGORIA_DIAG2'
]

# Step 3: Remove the specified columns from the DataFrame
# The `inplace=True` parameter modifies the DataFrame directly without creating a copy
df.drop(columns=columns_to_remove, inplace=True)

# Step 4: Convert the 'date' column to datetime format
df['FECHA_DEF'] = pd.to_datetime(df['FECHA_DEF'])

# Extract the period (month and year) from the date
df['PERIODO'] = df['FECHA_DEF'].dt.to_period('M')

# Step 5: Save the modified DataFrame to a new CSV file in the specified folder
FOLDER = './googlesheets/database/' # Define the folder path where the CSV file will be saved

# Check if the directory exists, create it if it doesn't
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

output_file_path = FOLDER + 'COVID_CLEAN.csv'  # Full path to the output CSV file
df.to_csv(output_file_path, index=False)  # Save the DataFrame to a CSV file without including the index

# Step 6: Read the newly created CSV file back into a Pandas DataFrame
# This step is optional but ensures the file was saved correctly and can be reloaded
file_path = FOLDER + 'COVID_CLEAN.csv'  # Path to the saved CSV file
df = pd.read_csv(file_path)  # Reload the CSV file into a DataFrame for further processing or validation

# Step 7: Upload the cleaned CSV file to Google Sheets
cs()  # Uses the custom `csv_to_sheets` function to upload the CSV file to Google Sheets