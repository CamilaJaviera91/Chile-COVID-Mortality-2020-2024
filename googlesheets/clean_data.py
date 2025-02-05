
#Add libraries
import pandas as pd
import matplotlib.pyplot as plt
import warnings

#Add libraries from google_sheets_utils
from google_sheets_utils import sheets_to_dataframe as sd
from google_sheets_utils import csv_to_sheets as cs

#Add warnings and plt style
warnings.filterwarnings('ignore')
plt.style.use("default")

#Obtain data frame from google_sheets_extractor
df = sd()

#Columns to be removed
columns_to_remove = ['EDAD_TIPO', 'COD_COMUNA', 'DIAG1', 'CAPITULO_DIAG1', 'GLOSA_CAPITULO_DIAG1', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1', 'CODIGO_CATEGORIA_DIAG1', 'GLOSA_CATEGORIA_DIAG1', 'CODIGO_SUBCATEGORIA_DIAG1', 'GLOSA_SUBCATEGORIA_DIAG1', 'DIAG2', 'CAPITULO_DIAG2', 'GLOSA_CAPITULO_DIAG2', 'CODIGO_GRUPO_DIAG2', 'GLOSA_GRUPO_DIAG2', 'CODIGO_CATEGORIA_DIAG2', 'GLOSA_CATEGORIA_DIAG2', 'CODIGO_SUBCATEGORIA_DIAG2', 'GLOSA_SUBCATEGORIA_DIAG2']

#Remove the columns
df.drop(columns=columns_to_remove, inplace=True)

#Current folder
folder = './database/'

#Save the modified .CSV file
output_file_path = folder + 'COVID_CLEAN.csv'
df.to_csv(output_file_path, index=False)

#Read the new .CSV file
file_path = folder + 'COVID_CLEAN.csv'
df = pd.read_csv(file_path)

#Save the .csv file to Google Sheets
cs()