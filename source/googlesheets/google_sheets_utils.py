# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting and visualization
import warnings  # To handle warnings
from google.oauth2 import service_account  # For Google API authentication
from googleapiclient.discovery import build  # For interacting with Google APIs
from googleapiclient.errors import HttpError  # To handle errors from Google API

# Suppress warnings to keep the console clean
warnings.filterwarnings('ignore')
# Set the default plotting style
plt.style.use("default")

# Define the folder where the database files are stored
FOLDER = './source/googlesheets/database/'

# Spreadsheet ID for the Google Sheets file
# This ID is obtained from the URL of the Google Sheet
# Example URL: https://docs.google.com/spreadsheets/d/1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz/edit#gid=0
# The ID in this case would be: "1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz"
SPREADSHEET_ID = '1Q0p_w4YwXYZFqseHEhs8AH_UoJY4ll8Vl4iryrIbMo8'

# Path to the credentials JSON file required for Google API authentication
# The credentials file contains information such as client email, private key, etc.
SERVICE_ACCOUNT_FILE = './source/googlesheets/ignore/credentials.json'

# Define the required scopes for accessing Google Sheets and Drive APIs
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',  # Full access to Google Sheets
    'https://spreadsheets.google.com/feeds',  # Legacy access to Google Sheets
    'https://www.googleapis.com/auth/drive.file',  # Access to files created by the app
    'https://www.googleapis.com/auth/drive'  # Full access to Google Drive
]

# Load the service account credentials from the JSON file
# These credentials are used to authenticate the Google Sheets API requests
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Function to transform data from Google Sheets into a Pandas DataFrame
def sheets_to_dataframe():
    """
    Connects to a Google Sheet, reads its content, saves it as a CSV file,
    and then loads the CSV file into a Pandas DataFrame.

    Returns:
        dfe (DataFrame): A Pandas DataFrame containing the Google Sheets data.
    """

    # Define the range of data to read from the Google Sheet
    RANGE_NAME = 'COVID!A:AA'  # Example range: Read all columns from rows A to AA

    # Build a connection to the Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Fetch the data from the specified range in the Google Sheet
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])  # Retrieve the values from the response

    # Convert the Google Sheets data into a Pandas DataFrame
    data_frame = pd.DataFrame(values)

    try:
        # Save the DataFrame to a CSV file for local storage
        output_file_path = FOLDER + 'COVID.csv'
        data_frame.to_csv(output_file_path, index=False, columns=None, header=False)

        # Read the saved CSV file back into a DataFrame
        dfe = pd.read_csv(output_file_path)
        print("Document Saved")  # Notify the user that the document has been saved successfully

    except NameError as e:
        # Handle errors that might occur (e.g., issues with the file path or name)
        print(e)

    return dfe  # Return the DataFrame for further use

# Function to upload data from a CSV file to Google Sheets
def csv_to_sheets():
    """
    Reads a local CSV file, prepares its content for Google Sheets,
    and uploads it to a specified range in the spreadsheet.

    Returns:
        None
    """

    # Read the cleaned CSV file that will be uploaded
    df = pd.read_csv(FOLDER + 'COVID_CLEAN.csv')  # Ensure the file exists in the specified folder
    # print(df)  # Uncomment this line to preview the DataFrame if needed

    try:
        # Build a connection to the Google Sheets API
        service = build('sheets', 'v4', credentials=creds)

        # Prepare the data for insertion
        # Combine the column headers and data into a list
        data = [df.columns.tolist()] + df.to_numpy(dtype=str).tolist()

        # Define the body of the request with the prepared data
        body = {
            'values': data  # Specify the data to be inserted
        }

        # Update the specified range in the Google Sheet with the new data
        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,  # The ID of the spreadsheet
            range='COVID_CLEAN!A1',  # The range where the data will be inserted
            valueInputOption='USER_ENTERED',  # Specify how the data should be interpreted
            body=body
        ).execute()

        # Notify the user of the number of cells updated
        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        # Handle errors from the Google Sheets API
        print(f"An error occurred: {error}")