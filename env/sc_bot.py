import discord
import random

TOKEN = 'NjkwOTIyNDQ2MDM1MDkxNTM2.XnZ8Qw.xTxhidVrdoLrOirvaZhnvqVscos'
client = discord.Client()
@client.event
async def on_message(message):
    if message.author == discord.Client.user:
        return
    # add status check
    if message.content.startswith('sc!_ti_ne_sdoh?'):                                
        testRandInt = random.randint(0, 2)
        if testRandInt == 0:
            msg = 'hoba sas {0.author.mention}, ya tuta'.format(message)
            await discord.abc.Messageable.send(message.channel, msg)
        if testRandInt == 1:
            msg = 'ta sho tebe nado {0.author.mention}'.format(message)
            await discord.abc.Messageable.send(message.channel, msg)
        if testRandInt == 2:
            msg = 'da da ya'.format(message)
            await discord.abc.Messageable.send(message.channel, msg)

client.run(TOKEN)