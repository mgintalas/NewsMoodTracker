import pandas as pd
import pyodbc
import os

# Environment Variables
SQL_SERVER_CONNECTION = os.environ.get('DB_CONN_NEWS')

# Establish a connection to the database
conn = pyodbc.connect(SQL_SERVER_CONNECTION)

# Read data into a DataFrame
df = pd.read_sql("SELECT SentimentScore FROM Articles", conn)

# Define bins for sentiment categories
bins = [-1, -0.6, -0.2, 0.2, 0.6, 1]
labels = ['Strongly Negative', 'Negative', 'Neutral', 'Positive', 'Strongly Positive']
df['Category'] = pd.cut(df['SentimentScore'], bins=bins, labels=labels)

# Calculate the count of articles in each category
heatmap_data = df['Category'].value_counts().sort_index()
