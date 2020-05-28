import time
import json
import asyncio
import webbrowser
import string
import sys
from soundscrape.soundscrape import process_soundcloud

uri = 'https://soundcloud.com/blessxshahmen/shahmen-1981985-pt-2-black-flowers'
class scdownloader(object):
    def __init__(self, m_uri):
        #browser = webbrowser.get('windows-default')
        #browser.open(m_uri + '/play')
        print (m_uri)
        vargs = {'path':'', 'folders': False, 'group': False, 'track': '', 'num_tracks': 9223372036854775807, 'bandcamp': False, 'downloadable': False, 'likes': False, 'open': False, 'artist_url': m_uri, 'keep': True}
        sound = process_soundcloud (vargs)

