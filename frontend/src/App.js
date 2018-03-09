import React, { Component } from 'react';
import './App.css';

import { Download } from 'react-feather';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      videoURL: '',
      isValidURL: true
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const isValidYoutube = (/^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+/).test(event.target.value);
    if (isValidYoutube) {
      this.setState({ videoURL: event.target.value, isValidURL: true });
    }
    else {
      (event.target.value === '') ? this.setState({ isValidURL: true }) : this.setState({ isValidURL: false })
    }
  }

  handleSubmit(event) {
    alert('ytURL: ' + this.state.videoURL);
    event.preventDefault();
  }

  render() {
    return (
      <div className="wrapper">
        <div className="header">
          <h1>Youtube-converter</h1>
          <p>Start by pasting link of youtube video or playlist you would like to download</p>
        </div>
        <div className="videoInput">
          <input className={this.state.isValidURL ? '' : 'danger'} onChange={this.handleChange}/>
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
