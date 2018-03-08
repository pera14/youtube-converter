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
import os
import subprocess


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
    '''yt = YouTube('www.youtube.com/watch?v=' + url)
    print url
    yt.streams.filter(subtype='mp3').first().download()
    name = yt.streams.first().default_filename'''
    yt = YouTube('www.youtube.com/watch?v=' + url)

    vids= yt.streams.filter(only_audio=True,subtype='mp4').all()
    for i in range(len(vids)):
        print(i,'. ',vids[i])

    vnum = int(input("Enter vid num: "))

    parent_dir = r"C:\Users\nsope\Downloads"
    vids[vnum].download()
    default_filename = vids[vnum].default_filename
    new_filename = vids[vnum].default_filename[:-4]+'.mp3'
    print default_filename,new_filename
    os.rename(default_filename, new_filename)

    print('done')
    return 'done'

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
    app.run(host='0.0.0.0', port=2525, debug=True)
