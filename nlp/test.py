import os
import pyodbc
from textblob import TextBlob
import datetime

# Environment Variables
SQL_SERVER_CONNECTION = os.environ.get('DB_CONN_NEWS')

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Function to update sentiment scores in the database
def update_article_sentiments():
    try:
        with pyodbc.connect(SQL_SERVER_CONNECTION) as conn:
            cursor = conn.cursor()
            
            # Select English titles from articles that don't have a sentiment score yet
            cursor.execute("SELECT ArticleID, Title_EN FROM Articles WHERE SentimentScore IS NULL")
            articles_to_update = cursor.fetchall()
            
            for article_id, title_en in articles_to_update:
                sentiment_score = analyze_sentiment(title_en)
                # Round the sentiment score to 2 decimal places
                rounded_sentiment_score = round(sentiment_score, 2)
                
                # Update the article with the rounded sentiment score
                cursor.execute("UPDATE Articles SET SentimentScore = ? WHERE ArticleID = ?", rounded_sentiment_score, article_id)
            
            conn.commit()
            print("Sentiment scores updated successfully.")
            
    except Exception as e:
        print("Error updating sentiment scores:", e)



# Main execution
if __name__ == "__main__":
    if not SQL_SERVER_CONNECTION:
        print("Database connection string is not set in environment variables.")
    else:
        update_article_sentiments()
