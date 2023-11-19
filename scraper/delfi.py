import requests
from bs4 import BeautifulSoup
from googletrans import Translator, LANGUAGES
import pyodbc
import os
import datetime

# Constants
URL = 'https://www.delfi.lt/'
source = 'Delfi'
TOP_ARTICLES_LIMIT = 2

# Environment Variables
SQL_SERVER_CONNECTION = os.environ.get('DB_CONN_NEWS')

# Initialize Translator
translator = Translator()

# Function to delete today's records
def delete_todays_records(source):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    delete_query = "DELETE FROM Articles WHERE CONVERT(date, ScrapedDate) = ? AND Source = ?"

    try:
        with pyodbc.connect(SQL_SERVER_CONNECTION) as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, today, source)
                conn.commit()
                print(f"Deleted today's records for {source} ({today}).")
    except Exception as e:
        print("Error deleting today's records for {source}:", e)



# Function to scrape website
def scrape_website(url, source):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully retrieved URL:", url)
        else:
            print("Failed to retrieve URL. Status code:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, 'html.parser')

        # Add the correct selector here
        titles = soup.find_all('h3', class_='headline-title')  # Example selector

        # Limit to top 10 articles
        titles = titles[:TOP_ARTICLES_LIMIT]

        articles = []
        for title in titles:
            original_title = title.get_text().strip()
            print("Original Title:", original_title)
            
            # Detect language and translate if not English
            detected_lang = translator.detect(original_title).lang
            print("Detected Language:", detected_lang)

            if 'en' not in detected_lang:
                translated_title = translator.translate(original_title, dest='en').text
                print("Translated Title:", translated_title)
            else:
                translated_title = original_title
                
            article_link = title.find('a')['href']

            articles.append((original_title, translated_title, article_link, source))

        return articles

    except Exception as e:
        print("Error occurred:", e)
        return []

# Function to insert data into SQL Server
def insert_into_database(articles):
    try:
        with pyodbc.connect(SQL_SERVER_CONNECTION) as conn:
            with conn.cursor() as cursor:
                for original, translated, link, source in articles:
                    cursor.execute("INSERT INTO dbo.Articles (Title_LT, Title_EN, URL, Source) VALUES (?, ?, ?, ?)", original, translated, link, source)
                conn.commit()
                print("Data inserted into database successfully.")

    except Exception as e:
        print("Database insertion error:", e)

# Main execution
if __name__ == "__main__":
    if not SQL_SERVER_CONNECTION:
        print("Database connection string is not set in environment variables.")
    else:
        delete_todays_records(source)
        articles = scrape_website(URL, source)
        if articles:
            insert_into_database(articles)
        else:
            print("No articles scraped.")