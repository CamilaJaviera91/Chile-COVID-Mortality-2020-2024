from fpdf import FPDF # For create PDF documents programmatically.
import pandas as pd # For working with data in DataFrame format.
import os  # For file and directory operations.

# Load the data from the CSV file
df = pd.read_csv('./googlesheets/database/COVID_CLEAN.csv')

# Group the data by 'PERIODO' (period) and 'SEXO_NOMBRE' (gender),
# and count the number of occurrences to calculate the deaths
df_count = df.groupby(['PERIODO', 'SEXO_NOMBRE']).size().reset_index(name='MUERTES')

# Create a custom class for the PDF
class PDF(FPDF):
    def header(self):
        # Set the font for the header
        self.set_font('Arial', 'B', 12)
        # Add a title at the top of the page
        self.cell(0, 10, 'MONTHLY DEATHS BY GENDER', align='C', ln=True)
        # Add spacing after the header
        self.ln(10)

    def footer(self):
        # Position the footer at 15 mm from the bottom of the page
        self.set_y(-15)
        # Set the font for the footer
        self.set_font('Arial', 'I', 8)
        # Add a page number to the footer
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Create a PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', size=10)

# Add the table to the PDF
# Define the width of each column (in mm)
col_widths = [40, 80, 40]  # Adjusted column widths for better alignment
header = ['PERIODO', 'GENERO', 'MUERTES']  # Define the table headers

# Center the table horizontally
# Calculate the total table width and the starting X position
table_width = sum(col_widths)
start_x = (pdf.w - table_width) / 2  # pdf.w is the width of the page

# Add table headers to the PDF
pdf.set_x(start_x)  # Move to the calculated starting X position
for col, width in zip(header, col_widths):
    pdf.cell(width, 10, col, border=1, align='C')  # Add header cells
pdf.ln()  # Line break after the header

# Add rows of data to the PDF
for _, row in df_count.iterrows():
    pdf.set_x(start_x)  # Ensure each row starts at the same X position
    pdf.cell(col_widths[0], 10, str(row['PERIODO']), border=1, align='C')  # Add 'PERIODO' data
    pdf.cell(col_widths[1], 10, str(row['SEXO_NOMBRE']), border=1, align='C')  # Add 'SEXO_NOMBRE' data
    pdf.cell(col_widths[2], 10, str(row['MUERTES']), border=1, align='C')  # Add 'MUERTES' data
    pdf.ln()  # Line break after each row

# Define the folder path to save the PDF
FOLDER = './googlesheets/download/'  

# Check if the specified folder exists; if not, create it
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

# Save the PDF to the specified folder
pdf.output(FOLDER + 'monthly_deaths_by_gender.pdf')

print("PDF successfully created: 'monthly_deaths_by_gender.pdf'")