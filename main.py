import discord
import os
from dotenv import load_dotenv
from module.word_test import ChooseMode

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
        choose_mode = ChooseMode()
        await message.channel.send('Test start', view=choose_mode)

TOKEN = os.getenv('TOKEN')
client.run(str(TOKEN))
