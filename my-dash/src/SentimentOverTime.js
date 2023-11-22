// SentimentOverTime.js
import React, { useState, useEffect } from 'react';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
  import { Line } from 'react-chartjs-2';
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

const SentimentOverTime = () => {
  const [chartData, setChartData] = useState(null); // Changed to null initially
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:8000/sentiment/api/sentiment-over-time/') // Use the correct URL to your API
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
      })
      .then(data => {
        setChartData({
          labels: data.map(item => item.date),
          datasets: [{
            label: 'Average Sentiment',
            data: data.map(item => parseFloat(item.avgsentiment)), // Parsing to float to be safe
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
        });
        setIsLoading(false);
      })
      .catch(error => {
        setError(error.toString());
        setIsLoading(false);
      });
  }, []);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!chartData) return <div>No chart data available</div>; // Conditional rendering check

  return (
    <div>
      <h2 className="mb-4 text-center">Sentiment Over Time</h2>
      <Line data={chartData} options={{ responsive: true }} />
    </div>
  );
};

export default SentimentOverTime;
