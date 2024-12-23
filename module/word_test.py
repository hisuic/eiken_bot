import discord
import os

from module.button import Button2, Button3, Button4
from module.getChoices import GetRandomWordFromAll
from module.getData import GetWord, GetMeaning

from dotenv import load_dotenv
load_dotenv()
NUMBER_OF_WORDS = os.getenv('NUMBER_OF_WORDS')

# =========================================================================
# # Viewのインスタンス生成時に引数を渡す (例: question="appleの意味は？")
# view = Button2(value1="value1", value2="value2")
# # メッセージと一緒にViewを送信
# await ctx.send("次の問題に回答してください！", view=view)
# # Viewのボタンが押される (またはタイムアウト) まで待機
# await view.wait()
# print(view.selected)
# =========================================================================

async def ModeSelection(ctx):
    view = Button2(value1="単語から意味を予測", value2="意味から単語を予測")
    await ctx.send("モードを選択して下さい。", view=view)
    await view.wait()
    return view.selected

async def WordTestAll(ctx):
    mode = await ModeSelection(ctx)
    if mode == 1:
        # 単語から意味を予測
        for i in range(10):
            correct_word_id = GetRandomWordFromAll()
            word = GetWord(correct_word_id)
            print(word)
    elif mode == 2:
        # 意味から単語を予測
        for i in range(10):
            correct_meaning_id = GetRandomWordFromAll()
            meaning = GetMeaning(correct_meaning_id)
            print(meaning)
    else:
        print("EXPECTED ERROR: Something went wrong around ModeSelection() in word_test.py")
