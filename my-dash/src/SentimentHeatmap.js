// SentimentHeatmap.js
import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const SentimentHeatmap = () => {
  const [heatmapData, setHeatmapData] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:8000/sentiment/api/sentiment-heatmap/') // Adjust the endpoint as needed
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
      })
      .then(data => {
        const labels = data.map(d => d.source);
        const veryNegativeData = data.map(d => d.verynegative);
        const negativeData = data.map(d => d.negative);
        const neutralData = data.map(d => d.neutral);
        const positiveData = data.map(d => d.positive);
        const veryPositiveData = data.map(d => d.verypositive);

        setHeatmapData({
          labels,
          datasets: [
            {
              label: 'Very Negative',
              data: veryNegativeData,
              backgroundColor: 'rgba(255, 99, 132, 0.5)'
            },
            {
              label: 'Negative',
              data: negativeData,
              backgroundColor: 'rgba(255, 159, 64, 0.5)'
            },
            {
              label: 'Neutral',
              data: neutralData,
              backgroundColor: 'rgba(255, 205, 86, 0.5)'
            },
            {
              label: 'Positive',
              data: positiveData,
              backgroundColor: 'rgba(75, 192, 192, 0.5)'
            },
            {
              label: 'Very Positive',
              data: veryPositiveData,
              backgroundColor: 'rgba(54, 162, 235, 0.5)'
            }
          ]
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
  if (!heatmapData.labels) return <div>Data not available</div>;

  return (
    <div>
      <h2 className="mb-4 text-center">Sentiment Heatmap</h2>
      <Bar data={heatmapData} options={{ responsive: true, indexAxis: 'y' }} />
    </div>
  );
};

export default SentimentHeatmap;
