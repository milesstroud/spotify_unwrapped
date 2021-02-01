import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from lyricsgenius import Genius
import pandas as pd
import json
import numpy as np
import re
import csv
import dateutil.parser
import datetime
from gspread_pandas import Spread


#Tokens/Authorization
genius_token = ''
spotify_secret = ''
spotify_id = ''
spotify_redirect = 'http://localhost'

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=spotify_id,client_secret=spotify_secret,redirect_uri=spotify_redirect))
#
genius = Genius(genius_token)

def lyrics_search(song,artist):
    genius_result = genius.search_song(song,artist)
    lyrics = genius_result.lyrics
    return lyrics


#Function to do our favorite thing...clean strings!
def lyrics_cleaner(lyrics):
    #Remove brackets, usually contain song component (intro, verse,etc.)
    lyrics = re.sub("\[.*\]","",lyrics)
    #Remove newlines
    lyrics = lyrics.replace("\n",". ")
    #Remove . issues
    lyrics = lyrics.replace(" . ","")
    lyrics = lyrics.replace("..",".")
    if lyrics.startswith('.'):
        lyrics = lyrics[2:]
    return lyrics

audio_features = ['danceability', 'duration_ms', 'energy', 'id', 'instrumentalness', 'key',
                  'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature',
                  'type', 'valence']
def audio_Features(id):
    audio_metrics = dict.fromkeys(audio_features, None)
    results = sp.audio_features(tracks=[id])
    for index, feature in enumerate(audio_features):
        audio_metrics[feature] = results[0][feature]
    return audio_metrics




def timestamp_cleaner(timestamp):
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    timestamp = datetime.datetime.strptime(timestamp,date_format)
    timestamp = timestamp - datetime.timedelta(hours=5)
    return timestamp
