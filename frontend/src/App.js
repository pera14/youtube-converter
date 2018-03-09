import React, { Component } from 'react';
import './App.css';

import { Download } from 'react-feather';

class App extends Component {
  render() {
    return (
      <div className="wrapper">
        <div className="header">
          <h1>Youtube-converter</h1>
          <p>Start by pasting link of youtube video or playlist you would like to download</p>
        </div>
        <div className="videoInput">
          <input type="text"/>
          <button className="btn">
            <Download className="feather" />
            download
          </button>
        </div>
      </div>
    );
  }
}

export default App;
