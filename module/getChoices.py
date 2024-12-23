import os
import discord
import random

from dotenv import load_dotenv
load_dotenv()
NUMBER_OF_WORDS = os.getenv('NUMBER_OF_WORDS')

def GetRandomWordFromAll():
    random_number = random.randint(1, int(NUMBER_OF_WORDS))
    return random_number
