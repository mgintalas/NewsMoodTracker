// App.js
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import SentimentList from './SentimentList';
import AvgSentimentBySource from './AvgSentimentBySource';
import NationalMood from './NationalMood';
import SentimentHeatmap from './SentimentHeatmap';
import SentimentOverTime from './SentimentOverTime';

const App = () => {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">News Sentiment Dashboard</a>
        </div>
      </nav>
      <div className="container mt-4">
        <NationalMood />
        <AvgSentimentBySource />
        <SentimentOverTime />
        <SentimentHeatmap />
      </div>
    </div>
  );
};

export default App;
