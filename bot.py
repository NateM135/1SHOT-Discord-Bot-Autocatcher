import discord
from discord.ext import commands
import requests
import setup
import json

description = "Type $info to see more information."
TOKEN = setup.TOK
client = commands.Bot(command_prefix='!', self_bot=True, fetch_offline_members=False)
client.remove_command('help')
PREFIX = setup.PREFIX



@client.event
async def on_ready():
    print("we made it here")
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("azunyan <3")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.author == client.user:   
        return
    if message.author.id == 694191215062679604 and len(message.embeds) > 0 and "A Wild Pokémon Has Appeared!" in message.embeds[0].title:
        apiurl = "https://pokeapi.co/api/v2/pokemon/" + str(message.embeds[0].image.url.split('/')[8][:-4])
        r = requests.get(apiurl)
        data = r.json()
        name = data['name']
        await message.channel.send(PREFIX + "catch " + name)        
    await client.process_commands(message)
    
    
print("logging in")
client.run(TOKEN, bot=False)