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
    const getURLParameters = url =>
      (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
        (a, v) => ((a[v.slice(0, v.indexOf('='))] = v.slice(v.indexOf('=') + 1)), a),
        {}
    );

    const videoCode = getURLParameters(this.state.videoURL).v;
    console.log(`Video kod: ${videoCode}`);
    console.warn('Pozivamo GET, error ce biti verovatno dok ne sredimo kako da prihvatam fajl nazad.');
    fetch(`http://localhost:2525/api/song/${videoCode}`)
      .then(() => console.log('sent!'))
      .catch(() => console.log('err'));
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
          <button className="btn" onClick={this.handleSubmit}>
            <Download className="feather" />
            download
          </button>
        </div>

      </div>
    );
  }
}

export default App;
