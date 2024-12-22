import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
from module.word_test import ModeSelection
from module.button import Button2

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
    # Viewのインスタンス生成時に引数を渡す (例: question="appleの意味は？")
    view = Button2(value1="value1", value2="value2")
    # メッセージと一緒にViewを送信
    await ctx.send("次の問題に回答してください！", view=view)

    # Viewのボタンが押される (またはタイムアウト) まで待機
    await view.wait()

    print(view.selected)

TOKEN = os.getenv('TOKEN')
client.run(str(TOKEN))
