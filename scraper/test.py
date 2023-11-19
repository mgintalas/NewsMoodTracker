import os
import pyodbc

# Assuming you've set the environment variable with the name 'NEWS_DB_CONNECTION'
connection_string = os.environ.get('DB_CONN_NEWS')

# ... [rest of your script]

# Example of using the connection string in a function
def test_database_connection():
    try:
        with pyodbc.connect(connection_string, timeout=10) as conn:
            print("Connection successful")
    except Exception as e:
        print("Error connecting to database:", e)

if __name__ == "__main__":
    test_database_connection()
    # ... [rest of your script]
