import discord
import os

from module.button import Button2, Button3, Button4, Button4Numbers
from module.getChoices import GetRandomWordFromAll, GetFourChoicesFromAll
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

def Array2MarkdownBulletPoints(items):
    """
    Converts a list of strings into a Markdown bullet point string.

    Args:
        items (list): A list of strings to be converted.

    Returns:
        str: A string formatted as Markdown bullet points.
    """
    if not items:
        return ""
    return "\n".join(f"- {item}" for item in items)

async def TestWith4NumberChoices(ctx, choices, quiz_word):
    choices_bulletpoints = Array2MarkdownBulletPoints(choices)
    view = Button4Numbers()
    await ctx.send("## " + quiz_word + "\n" + choices_bulletpoints, view=view)
    await view.wait()
    # print(view.selected) # debug
    return view.selected

async def WordTestAll(ctx):
    mode = await ModeSelection(ctx)

    if mode == 1:
        # 単語から意味を予測
        count = 0
        for i in range(10):
            correct_word_id = GetRandomWordFromAll()
            word = GetWord(correct_word_id)
            # print(word) # debug
            choices, answer = GetFourChoicesFromAll(correct_word_id, 2)
            selected = await TestWith4NumberChoices(ctx, choices, word)
            if selected == answer:
                count += 1
                await ctx.send("Correct!")
            else:
                await ctx.send("Wrong! \nThe correct meaning is: " + choices[answer])
        await ctx.send(str(count) + "問正解です。")

    elif mode == 2:
        # 意味から単語を予測
        count = 0
        for i in range(10):
            correct_meaning_id = GetRandomWordFromAll()
            meaning = GetMeaning(correct_meaning_id)
            # print(meaning) # debug
            choices, answer = GetFourChoicesFromAll(correct_meaning_id, 1)
            selected = await TestWith4NumberChoices(ctx, choices, meaning)
            if selected == answer:
                count += 1
                await ctx.send("Correct!")
            else:
                await ctx.send("Wrong! \nThe correct word is: " + choices[answer])
        await ctx.send(str(count) + "問正解です。")

    else:
        print("EXPECTED ERROR: Something went wrong around ModeSelection() in word_test.py")
