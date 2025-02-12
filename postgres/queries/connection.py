# Importing the psycopg2 library to interact with a PostgreSQL database
import psycopg2

# Importing the OperationalError class to handle database connection errors
from psycopg2 import OperationalError

# Function to establish a connection to the PostgreSQL database
def connection():
    try:
        # Attempt to create a connection to the database
        conn = psycopg2.connect(
            host="localhost",           # Address of the PostgreSQL server (localhost for a local machine)
            database="postgres",        # Name of the database to connect to
            user="postgres",            # Username for the PostgreSQL database
            password="1234",            # Password for the specified user
            port="5432"                 # Port number where PostgreSQL is listening (default is 5432)
        )
        # Print a success message if the connection is established
        print("Connection Successful")
        return conn  # Return the connection object to be used elsewhere in the application
    
    except OperationalError as e:
        # Catch and handle errors that occur during the connection attempt
        print(f"Database connection failed: {e}")  # Print the error message for debugging
        return None  # Return None to indicate the connection attempt was unsuccessful