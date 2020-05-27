import threading
import requests
import time
import json
import asyncio

twitchClientID = 'zee46vqcynbnldjtso0kui1kb6cf0h'
twitchLogin = 'cowboy_ebob'

class ttwLiveChecker(object):
    twitchIsStarted = ''
    twitchTrigger = ''
    def __init__(self, interval=3):
        self.interval = interval

        thread = threading.Thread(target=self.liveChecker, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()  
    
    
    def liveChecker(self):
        while True:
            response = requests.get('https://api.twitch.tv/helix/streams?user_login={}'.format(twitchLogin), headers={'Client-ID': twitchClientID})
            jsonRes = json.loads(response.text)
            try:
                print(jsonRes["data"][0]["type"])
                self.twitchIsStarted = 'y'
                time.sleep(self.interval)
            except:
                self.twitchIsStarted = 'n'
                time.sleep(self.interval)

            if self.twitchTrigger == '' and self.twitchIsStarted == 'y':
                self.twitchTrigger = 'live'
            elif self.twitchTrigger == 'live' and self.twitchIsStarted == 'n':
                self.twitchTrigger = ''