import discord

TOKEN = '---'
client = discord.Client()
@client.event
async def on_message(message):
    if message.author == discord.Client.user:
        return
    if message.author.id == '7898' and message.content.startswith('sc!test'):
            msg = 'test {0.author.mention}'.format(message)
            await discord.abc.Messageable.send(message.channel, msg)
    if message.content.startswith('sc!hello'):
        msg = 'hi {0.author.mention}'.format(message)
        await discord.abc.Messageable.send(message.channel, msg)
client.run(TOKEN)