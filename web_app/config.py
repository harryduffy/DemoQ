import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask
from Queue import Queue
from dotenv import load_dotenv

load_dotenv()

def init():

    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    flask_app = Flask(__name__)
    q = Queue(30)

    return flask_app, q, sp