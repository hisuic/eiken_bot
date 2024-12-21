import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
from module.word_test import ModeSelection
from module.button import Button_2

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$test'):
        # original
        # mode_selection = ModeSelection()
        # await message.channel.send('Test start', view=mode_selection)

        # test
        view = Button_2(value1 = "value1", value2 = "value2")
        # await message.send("選択肢です。", view=view)
        await view.wait()
        print(selected)

TOKEN = os.getenv('TOKEN')
client.run(str(TOKEN))
