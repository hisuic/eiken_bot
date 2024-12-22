import discord

from module.button import Button2, Button3, Button4

# =========================================================================
# # Viewのインスタンス生成時に引数を渡す (例: question="appleの意味は？")
# view = Button2(value1="value1", value2="value2")
# # メッセージと一緒にViewを送信
# await ctx.send("次の問題に回答してください！", view=view)
# # Viewのボタンが押される (またはタイムアウト) まで待機
# await view.wait()
# print(view.selected)
# =========================================================================

async def WordTest(ctx):
    view = Button2(value1="value1", value2="value2")
    await ctx.send("次の問題に回答してください！", view=view)
    await view.wait()
    print(view.selected)
