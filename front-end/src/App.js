import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Budget from './Budget/Budget'
import Profit from './Profit/Profit'
import Portfolio from './Portfolio/Portfolio'

function getProfits() {
  let profit = -12;
  return profit;
};



class App extends Component {
  constructor() {
    super()
    this.state = {
      profit: 0
    }
  }
  render() {
    return (
      <div className="App">
        <header className="AppTitle">
          Stock Market Prediction through Sentiment Analysis
      </header>
        <Budget functionHandle={this.fetchHelloWorld} />
        <Profit value={this.state.profit} />
        <Portfolio />
      </div>
    );
  }

  fetchHelloWorld = () => {
    console.log("fetching python localhost");
    fetch('http://127.0.0.1:5000/', {
      method: 'GET',
      mode: 'cors',
      dataType: 'json'
    })
      .then(r => r.json())
      .then(r => {
        console.log(r.jack)
        //let temp = JSON.parse(r)
        this.setState({
          profit: r.jack
        })
      })
      .catch(err => console.log(err))
  }
}

export default App;
