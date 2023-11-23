// SentimentHeatmap.js
import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Box, Typography, CircularProgress, Alert, useTheme } from '@mui/material';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const SentimentHeatmap = () => {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const theme = useTheme(); // Using MUI theme for styling

  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:8000/sentiment/api/sentiment-heatmap/')
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
      })
      .then(data => {
        setData(data);
        setIsLoading(false);
      })
      .catch(error => {
        setError(error.toString());
        setIsLoading(false);
      });
  }, []);

  const chartData = {
    labels: data.map(d => d.source),
    datasets: [
      {
        label: 'Very Negative',
        data: data.map(d => d.verynegative),
        backgroundColor: theme.palette.error.main,
      },
      {
        label: 'Negative',
        data: data.map(d => d.negative),
        backgroundColor: theme.palette.warning.main,
      },
      {
        label: 'Neutral',
        data: data.map(d => d.neutral),
        backgroundColor: theme.palette.info.main,
      },
      {
        label: 'Positive',
        data: data.map(d => d.positive),
        backgroundColor: theme.palette.success.main,
      },
      {
        label: 'Very Positive',
        data: data.map(d => d.verypositive),
        backgroundColor: theme.palette.primary.main,
      },
    ],
  };

  const options = {
    indexAxis: 'y',
    elements: {
      bar: {
        borderWidth: 2,
      },
    },
    responsive: true,
    plugins: {
      legend: {
        position: 'right',
        align: 'start',
      },
      title: {
        display: true,
        text: 'Sentiment Heatmap',
      },
    },
  };

  if (isLoading) {
    return <CircularProgress />;
  }

  if (error) {
    return <Alert severity="error">{error}</Alert>;
  }

  return (
    <Box sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom align="center">
        Sentiment Heatmap
      </Typography>
      <Bar data={chartData} options={options} />
    </Box>
  );
};

export default SentimentHeatmap;
