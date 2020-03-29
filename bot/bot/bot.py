import discord
import random
import threading
import time
import requests
import json
import asyncio
from discord.ext import commands

discordToken = ''
notificationChID = '281868313674645504'

twitchClientID = 'zee46vqcynbnldjtso0kui1kb6cf0h'
twitchLogin = 'cowboy_ebob'
discordTtwTrigger = ''

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

bot = commands.Bot(command_prefix='sc!')

@bot.command(pass_context=True)
async def notif(ctx, channel: discord.channel=notificationChID, timeout: int=3):
    global discordTtwTrigger
    while True:
        if twitchOnlineCheck.twitchTrigger == 'live' and discordTtwTrigger == '':
            discordTtwTrigger = 'live'
            print('s')
            await ctx.send('Eto zhivotnoe {}, snova podrubilo potok: https://www.twitch.tv/{}'.format(twitchLogin, twitchLogin))
            await asyncio.sleep(timeout)
        elif twitchOnlineCheck.twitchTrigger == '' and discordTtwTrigger == 'live':
            discordTtwTrigger = ''
            await asyncio.sleep(timeout)

@bot.command(name = 'ti_zhivoy')
async def ti_zhivoy(ctx):
    rand = random.randint(0, 3)
    if rand == 0:
         await ctx.send('ta sho tobi nado')
    if rand == 1:
         await ctx.send('ti gavna kusok anu idi suda')
    if rand == 2:
         await ctx.send('why are u bulling me?')
    if rand == 3:
        await ctx.send('a mozhet ti?')

@bot.command(name = 'dice')
async def dice(ctx, arg):
    if arg == 'default':
        result = random.randint(1, 6)
        await ctx.send(':game_die: is {}'.format(result))
    if arg == 'double':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = dice1 + dice2
        await ctx.send(':game_die: is {}, :game_die: is {}, :game_die::game_die: is {}'.format(dice1, dice2, result))

@bot.command(name = 'twtest')
async def twtest(ctx):
    print(twitchOnlineCheck.twitchIsStarted)
    if twitchOnlineCheck.twitchIsStarted == 'y':
        await ctx.send("+")
    if twitchOnlineCheck.twitchIsStarted == 'n':
        await ctx.send("-")

twitchOnlineCheck = ttwLiveChecker()
bot.run(discordToken)