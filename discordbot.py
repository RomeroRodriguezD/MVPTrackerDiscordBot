import discord
from discord.ext import commands
import pandas as pd
import datetime
from datetime import timedelta
import re

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', description='MVP scheduler bot', intents=intents)

@client.command(name='mvp')
async def mvp(ctx, *, message):
    context = message
    context = str(context).lower()
    list = pd.read_csv('roamingmvp.csv')
    hour = datetime.datetime.now()
    for mvp in list.itertuples():
        print()
        if context == str(mvp.MVP).lower():
            if int(mvp.spawn) < 1000:
                n = int(mvp.spawn)
                respawn = hour + timedelta(minutes=n)
                respawn_clean_hour = respawn.strftime('%H:%M:%S')
                await ctx.send(f' MVP {context.title()} regresará a las {respawn_clean_hour}')
            else:
                await ctx.send(f'El MVP {context.title()} regresará tras {mvp.spawn} mob kills.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="si alguien mata algo"))

client.run('YourTokenHere')


