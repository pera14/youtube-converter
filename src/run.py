#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask import request
from flask import url_for
from flask import Response
import json

from time import gmtime, strftime
from flask import send_file
from pytube import YouTube


DEVELOPMENT = False
if DEVELOPMENT:
    import os
    import threading, webbrowser

app = Flask(__name__, static_folder='www')
api = Api(app)


@app.route('/<path:path>')
def static_file(path):
    try:
        return app.send_static_file(path)
    except:
        return "Error"


@app.route('/api/song/<url>', methods=['GET'])
def song(url):
    yt = YouTube('www.youtube.com/watch?v=' + url)
    print url
    yt.streams.first().download()
    name = yt.streams.first().default_filename

    return name

@app.route('/api/playlist/<url>', methods=['GET'])
def playlist(url):
    yt = YouTube(url)
    yt.streams.first().download()
    name = yt.streams.first().default_filename
    return name

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    if DEVELOPMENT:
        url = "http://localhost:8080"
        threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run(host='0.0.0.0', port=8080, debug=True)
