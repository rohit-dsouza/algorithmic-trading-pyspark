import React from 'react';
import logo from './logo.svg';
import './App.css';
import Budget from './Budget/Budget'
import Profit from './Profit/Profit'
import Portfolio from './Portfolio/Portfolio'

function getProfits() {
  let profit = -12;
  return profit;
};

function App() {
  return (
    <div className="App">
      <header className="AppTitle">
        Stock Market Prediction through Sentiment Analysis 
      </header>
    <Budget />
    <Profit value={getProfits()} />
    <Portfolio />
    </div>
  );
}

export default App;
