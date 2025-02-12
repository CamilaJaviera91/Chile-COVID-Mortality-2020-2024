# Import the 'sys' module to modify the Python path for module discovery
import sys
sys.path.append('./postgres/queries/')  # Add the path to the 'queries' folder for importing custom modules

# Import the 'connection' function from the custom 'connection' file
from connection import connection

# Import necessary libraries
import psycopg2  # Library for connecting to and interacting with PostgreSQL databases
import locale    # Library for setting the locale to control date, time, and number formatting
import pandas as pd  # Library for working with structured data, like DataFrames, in Python

def yearly_deaths_by_gender_and_region():
    """
    Queries the PostgreSQL database to retrieve yearly deaths categorized by gender and region.

    Returns:
        pandas.DataFrame: A DataFrame containing the results of the query.
    """
    # Set the locale to Spanish (Spain) to ensure proper formatting of dates, numbers, etc.
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Set the locale to Spanish
    except locale.Error:
        print("Error: Could not establish the regional settings. Default locale will be used.")

    # Establish a connection to the database using the custom 'connection' function
    con = connection()  # Calls the connection() function from 'connection.py'
    if con is None:
        print("Error: Could not establish a connection to the database.")
        return  # Exit the function if the connection fails

    try:
        # Create a cursor object to interact with the PostgreSQL database
        cursor = con.cursor()

        # Execute the SQL query to retrieve yearly deaths grouped by gender and region
        cursor.execute('''
                        SELECT 
                            cd."AÑO" AS "year",                            -- Year of death
                            cd."NOMBRE_REGION" AS "region",               -- Name of the region
                            COUNT(cd."EDAD_CANT") AS "quantity",          -- Total number of deaths
                            SUM(CASE WHEN cd."SEXO_NOMBRE" = 'Mujer' THEN 1 ELSE 0 END) AS "Women", -- Count of women
                            SUM(CASE WHEN cd."SEXO_NOMBRE" = 'Hombre' THEN 1 ELSE 0 END) AS "Men"   -- Count of men
                        FROM covid_chile.covid_data cd
                        GROUP BY 
                            "year", 
                            "region"
                        ORDER BY 
                            "year";
        ''')

        # Fetch all rows from the query result
        records = cursor.fetchall()

        # Extract column names from the cursor description to use as DataFrame headers
        columns = [desc[0] for desc in cursor.description]  # List comprehension to get column names

        # Create a Pandas DataFrame from the query results
        df = pd.DataFrame(records, columns=columns)

        return df  # Return the resulting DataFrame to the caller

    except psycopg2.Error as e:
        # Handle database-related errors during query execution
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Safely close the cursor and database connection
        cursor.close()  # Close the cursor to release resources
        con.close()     # Close the connection to the database
        print("Connection closed successfully.")  # Confirm successful closure