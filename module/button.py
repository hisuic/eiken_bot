import discord

# --- 呼び出し例 ---
# view = Button_2(value1="選択肢1", value2="選択肢2")
# await ctx.send("ボタンテスト", view=view)
# await view.wait()
# print(view.selected)

class Button2(discord.ui.View):
    def __init__(self, value1: str = None, value2: str = None, timeout=15):
        super().__init__(timeout=timeout)
        self.value1 = value1
        self.value2 = value2
        self.selected = None

        button1 = discord.ui.Button(
            label=value1,
            style=discord.ButtonStyle.success,
            custom_id="button1"
        )
        button1.callback = self.on_button_click  # コールバックをセット

        button2 = discord.ui.Button(
            label=value2,
            style=discord.ButtonStyle.success,
            custom_id="button2"
        )
        button2.callback = self.on_button_click

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

class Button3(discord.ui.View):
    def __init__(self, value1: str = None, value2: str = None, value3: str = None, timeout=15):
        super().__init__(timeout=timeout)
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.selected = None

        button1 = discord.ui.Button(
            label=value1,
            style=discord.ButtonStyle.success,
            custom_id="button1"
        )
        button1.callback = self.on_button_click

        button2 = discord.ui.Button(
            label=value2,
            style=discord.ButtonStyle.success,
            custom_id="button2"
        )
        button2.callback = self.on_button_click

        button3 = discord.ui.Button(
            label=value3,
            style=discord.ButtonStyle.success,
            custom_id="button3"
        )
        button3.callback = self.on_button_click

        self.add_item(button1)
        self.add_item(button2)
        self.add_item(button3)

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
        elif cid == "button3":
            self.selected = 3
            await interaction.response.send_message(
                f"{interaction.user.mention} {self.value3} が選ばれました！", 
                ephemeral=True
            )
        self.stop()

    async def on_timeout(self):
        self.selected = None
        for item in self.children:
            item.disabled = True

class Button4(discord.ui.View):
    def __init__(self, value1: str = None, value2: str = None, value3: str = None, value4: str = None, timeout=15):
        super().__init__(timeout=timeout)
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.selected = None

        button1 = discord.ui.Button(
            label=value1,
            style=discord.ButtonStyle.success,
            custom_id="button1"
        )
        button1.callback = self.on_button_click

        button2 = discord.ui.Button(
            label=value2,
            style=discord.ButtonStyle.success,
            custom_id="button2"
        )
        button2.callback = self.on_button_click

        button3 = discord.ui.Button(
            label=value3,
            style=discord.ButtonStyle.success,
            custom_id="button3"
        )
        button3.callback = self.on_button_click

        button4 = discord.ui.Button(
            label=value4,
            style=discord.ButtonStyle.success,
            custom_id="button4"
        )
        button4.callback = self.on_button_click

        self.add_item(button1)
        self.add_item(button2)
        self.add_item(button3)
        self.add_item(button4)

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
        elif cid == "button3":
            self.selected = 3
            await interaction.response.send_message(
                f"{interaction.user.mention} {self.value3} が選ばれました！", 
                ephemeral=True
            )
        elif cid == "button4":
            self.selected = 4
            await interaction.response.send_message(
                f"{interaction.user.mention} {self.value4} が選ばれました！", 
                ephemeral=True
            )
        self.stop()

    async def on_timeout(self):
        self.selected = None
        for item in self.children:
            item.disabled = True
