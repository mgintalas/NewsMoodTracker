// SentimentList.js
import React, { useState, useEffect } from 'react';

const SentimentList = () => {
  const [sentiments, setSentiments] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:8000/sentiment/api/avg-sentiment-by-source/')  // Update this if your API URL is different
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setSentiments(data);
        setIsLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Average Sentiment by Source</h1>
      <ul>
        {sentiments.map((sentiment, index) => (
          <li key={index}>{sentiment.source}: {sentiment.avgSentiment}</li>
        ))}
      </ul>
    </div>
  );
};

export default SentimentList;
