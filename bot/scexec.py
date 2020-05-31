import time
import json
import asyncio
import webbrowser
import string
import sys
import glob
import os
from soundscrape.soundscrape import process_soundcloud

# uri = 'https://soundcloud.com/kkuko/nkoha-black-swordsman'  # uri for test
class scdownloader(object):
    def __init__(self, m_uri):
        print (m_uri)
        for f in glob.glob('./bot/music/*.mp3'):
           os.unlink(f)
        mp3_count = glob.glob1('', "./bot/music/*.mp3")  
        vargs = {'path':'./bot/music/', 'folders': False, 'group': False, 'track': '', 'num_tracks': 9223372036854775807, 'bandcamp': False, 'downloadable': False, 'likes': False, 'open': False, 'artist_url': m_uri, 'keep': True}
        process_soundcloud(vargs)
        self.mp3_count = glob.glob("./bot/music/*.mp3")
#test = scdownloader(uri)