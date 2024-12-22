import discord

class Button2(discord.ui.View):
    def __init__(self, value1: str = None, value2: str = None, timeout=15):
        super().__init__(timeout=timeout)
        self.value1 = value1
        self.value2 = value2
        self.selected = None

        # ボタン1
        button1 = discord.ui.Button(
            label=value1,
            style=discord.ButtonStyle.success,
            custom_id="button1"
        )
        button1.callback = self.on_button_click  # コールバックをセット

        # ボタン2
        button2 = discord.ui.Button(
            label=value2,
            style=discord.ButtonStyle.success,
            custom_id="button2"
        )
        button2.callback = self.on_button_click

        # Viewに追加
        self.add_item(button1)
        self.add_item(button2)

    async def on_button_click(self, interaction: discord.Interaction):
        cid = interaction.data["custom_id"]
        if cid == "button1":
            self.selected = 1
            await interaction.response.send_message(
                f"{interaction.user.mention} {self.value1} が選ばれました！", 
                ephemeral=True
            )
        elif cid == "button2":
            self.selected = 2
            await interaction.response.send_message(
                f"{interaction.user.mention} {self.value2} が選ばれました！", 
                ephemeral=True
            )
        self.stop()

    async def on_timeout(self):
        self.selected = None
        for item in self.children:
            item.disabled = True

# --- 呼び出し例 ---
# view = Button_2(value1="選択肢1", value2="選択肢2")
# await ctx.send("ボタンテスト", view=view)
# await view.wait()
# print(view.selected)
