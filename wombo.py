import requests
import discord
from discord.ext import commands

import json
import time
auth = {'authorization': "", 'content-type': 'text/plain;charset=UTF-8'}

r = requests.Session()



found = False

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
         await ctx.channel.send(f'Please format as follows: (!run <style> <query> | e.g. !run synthwave cars). Find more styles at https://discord.com/channels/855241948411854889/855241948411854891/937080642930352178')

@client.command()
async def run(ctx, number, name):
    global id
    message = await ctx.channel.send('auto generating image...')
    inital = r.post('https://app.wombo.art/api/tasks', headers=auth, json={'premium': 'false'})
    id = json.loads(inital.text)["id"]

    conversiontable = {'synthwave': 1, 'ukiyoe': 2, 'steampunk': 4, 'fantasyart' : 5, 'vibrant': 6, 'hd' : 7, "pastel": 8, 'psychic': 9, 'darkfantasy': 10, 'festive': 12, 'mystical' : 11, 'rosegold': 18, 'provenance': 17, 'wuhtercuhler': 16, 'sdali': 15, 'baroque': 13, 'etching': 14}

    firstr = r.put(f'https://app.wombo.art/api/tasks/{id}', headers=auth, json={'input_spec': {'prompt': name, 'style': conversiontable[number], 'display_freq': 10}})
    await message.edit(content=firstwarefare())


def firstwarefare():
    global found
    secondrs = r.get(f'https://app.wombo.art/api/tasks/{id}', headers=auth)
    if not json.loads(secondrs.text)["generated_photo_keys"] and not found:
        return firstwarefare()
    else:
        found = True
        if len(json.loads(secondrs.text)["photo_url_list"]) < 19:
            return firstwarefare()
        else:
            for i in json.loads(secondrs.text)["photo_url_list"]:
                if '19.jpg' in i:
                    return i



client.run('')