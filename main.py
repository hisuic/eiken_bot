import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
from module.word_test import WordTest
from module.button import Button2, Button4

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def hello(ctx):
    print("hello")

@client.command()
async def test(ctx):
    await WordTest(ctx)

TOKEN = os.getenv('TOKEN')
client.run(str(TOKEN))
