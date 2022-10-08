import discord
import asyncio
from discord.ext import commands
import datetime

from urllib import parse, request
import re

intents = discord.Intents.all();

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Le bot est opérationnel!");

@client.event
async def on_message(message):
    content = message.content.lower();
    content = content.split();
    
    if message.author.bot:
        return;
    
    for i in range(len(content)):
        word = content[i];
        word = word.replace('!', '');
        word = word.replace('.', '');
        word = word.replace('(', '');
        word = word.replace(')', '');
        word = word.replace('-', '');
        word = word.replace('#', '');
        word = word.lower();

        if word == "feur":
            msg = "**ROUGE!!!**\nEh oui! **Tu t'es fais troll {0.author.mention} !!!!!** :wink:\n\nRemercie <@847539356516089866> pour ce bot :joy:".format(message);
            await message.reply(msg);

            with open('img/answer.png', 'rb') as f:
                picture = discord.File(f);
                await message.channel.send(file=picture);
            
            print("{0.author.mention} a été trollé!".format(message));
            break;


client.run("CLÉ_PRIVÉE"); # Remplacer 'CLÉ_PRIVÉE' par votre clé à vous
