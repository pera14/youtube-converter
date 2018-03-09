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
import time

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
    now = time.time()
    yt = YouTube('www.youtube.com/watch?v=' + url)

    vids= yt.streams.filter(only_audio=True,subtype="webm").all()
    #vids= yt.streams.filter().all()
    for i in range(len(vids)):
        print(i,'. ',vids[i])

    #vnum = int(input("Unesite broj: "))
    vnum=1
    parent_dir = r"C:\Users\nsope\Downloads"
    vids[vnum].download()
    default_filename = vids[vnum].default_filename
    new_filename = vids[vnum].default_filename[:-4]+'mp3'
    #print default_filename,new_filename
    #os.renme(default_filename, new_filename)
    now2 = time.time()
    print(now2-now)
    return send_file(default_filename,
                     attachment_filename=new_filename,
                     as_attachment=True)

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
    app.run(host='0.0.0.0', port=2525, debug=True)
