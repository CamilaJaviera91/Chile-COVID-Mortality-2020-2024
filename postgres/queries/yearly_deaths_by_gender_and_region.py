# Import the connection function from the 'connection' file
import sys
sys.path.append('./postgres/queries/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def yearly_deaths_by_gender_and_region():
    """
    Queries the movie recommendation database to retrieve yearly deaths by gender
    and region.
    """
    # Set the locale to Spanish (Spain) to ensure proper formatting
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        print("Error: Could not establish the regional settings.")
    
    # Establish a connection using the connection function from 'connection.py'
    con = connection()
    if con is None:
        print("Error: Could not establish a connection to the database.")
        return

    try:
        cursor = con.cursor()  # Create a cursor to interact with the database

        # Execute the SQL query to retrieve the genre-based statistics
        cursor.execute('''
                        select 
                            cd."AÑO" as "year",
                            cd."NOMBRE_REGION" as "region",
                            count(cd."EDAD_CANT") as "quantity",
                            sum(case when cd."SEXO_NOMBRE" = 'Mujer' then 1 else 0 end) as "Women",
                            sum(case when cd."SEXO_NOMBRE" = 'Hombre' then 1 else 0 end) as "Men"
                        from covid_chile.covid_data cd
                        group by 
                            "year", 
                            "region"
                        order by 
                            "year";
        ''')

        records = cursor.fetchall()  # Fetch all the results from the query

        # Convert results into a DataFrame for better visualization and manipulation.
        columns = [desc[0] for desc in cursor.description]  # Extract column names from query result
        df = pd.DataFrame(records, columns=columns)  # Create DataFrame

        return df  # Return DataFrame

    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")  # Handle query execution errors
        return None

    finally:
        # Close cursor and connection safely to avoid resource leaks
        cursor.close()
        con.close()
        print("Connection closed successfully.")