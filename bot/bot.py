import discord
import random
import time
import json
import asyncio
import glob
import livechecker                  #my module
import scexec                       #my module
from discord.ext import commands

discordToken = 'NjkwOTIyNDQ2MDM1MDkxNTM2.XtL5hg.4BMMBzNIPfWkaUu9G_kJ5SJ0kok'
notificationChID = '281868313674645504'

discordTtwTrigger = ''
twitchOnlineCheck = livechecker.ttwLiveChecker()

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

@bot.command(pass_context=True)
async def scloud(ctx, arg_uri):
    music = scexec.scdownloader(arg_uri)
    author = ctx.author
    channel = author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="./ffmpeg-static/bin/ffmpeg.exe", source=music.mp3_count[0]), after=lambda e: print('done', e))   

@bot.command(pass_context=True)
async def scstop(ctx):
    #author = ctx.author
    #channel = author.voice.channel
    bot.voice_clients.remove
    for f in glob.glob('./bot/music/*.mp3'):
           os.unlink(f)

#@bot.command(name = 'twtest')
#async def twtest(ctx):
#    print(twitchOnlineCheck.twitchIsStarted)
#    if twitchOnlineCheck.twitchIsStarted == 'y':
#        await ctx.send("+")
#    if twitchOnlineCheck.twitchIsStarted == 'n':
#       await ctx.send("-")

bot.run(discordToken)