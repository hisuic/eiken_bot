import discord

class Button_2(discord.ui.View):
    def __init__(self, *, value1: str = None, value2: str = None, timeout=180):
    # def __init__(self, *, value: str = None, timeout=180):
        # str = None は、引数が文字列型、引数が渡されなかった場合にデフォルトでNoneに設定される。
        """
        question : 何らかの引数 (例: 出題する単語や意味など)
        """
        super().__init__(timeout=timeout)
        self.value1 = value1         # 渡された引数を保存
        self.value2 = value2
        self.selected = None         # どのボタンが押されたかを記録する変数

        self.add_item(
            discord.ui.Button(
                label=value1, style=discord.ButtonStyle.success, custom_id="button1"
            )
        )
        self.add_item(
            discord.ui.Button(
                label=value2, style=discord.ButtonStyle.success, custom_id="button2"
            )
        )

        @discord.ui.button()
        async def on_button_click(self, interaction: discord.Interaction):
            if interaction.data["custom_id"] == "button1":
                self.selected = 1
                await interaction.response.send_message(f"{interaction.user.mention} {self.value1} が選ばれました！")
            elif interaction.data["custom_id"] == "button2":
                self.selected = 2
                await interaction.response.send_message(f"{interaction.user.mention} {self.value2} が選ばれました！")
            self.stop()

    # @discord.ui.button(label={self.value1}, style=discord.ButtonStyle.success)
    # async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     """OKボタン(意味→単語)"""
    #     self.selected = 1  # どちらのボタンが押されたかを保存
    #     await interaction.response.send_message(
    #         f"{interaction.user.mention} OK!"
    #     )
    #     self.stop()  # これでViewの待機が終了
    #
    # @discord.ui.button(label={self.value2}, style=discord.ButtonStyle.success)
    # async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     """NGボタン(単語→意味)"""
    #     self.selected = 2
    #     await interaction.response.send_message(
    #         f"{interaction.user.mention} NG"
    #     )
    #     self.stop()

# class Button_4(discord.ui.View):
#     def __init__(self, *, value1: str = None, value2: str = None, value3: str = None, value4: str = None, timeout=180):
#     # def __init__(self, *, value: str = None, timeout=180):
#         # str = None は、引数が文字列型、引数が渡されなかった場合にデフォルトでNoneに設定される。
#         """
#         question : 何らかの引数 (例: 出題する単語や意味など)
#         """
#         super().__init__(timeout=timeout)
#         self.value1 = value1
#         self.value2 = value2
#         self.value3 = value3
#         self.value4 = value4
#         self.selected = None         # どのボタンが押されたかを記録する変数
#
#     @discord.ui.button(label={self.value1}, style=discord.ButtonStyle.success)
#     async def button0(self, interaction: discord.Interaction, button: discord.ui.Button):
#         """OKボタン(意味→単語)"""
#         self.selected = 0  # どちらのボタンが押されたかを保存
#         await interaction.response.send_message(
#             f"{interaction.user.mention} OK!"
#         )
#         self.stop()  # これでViewの待機が終了
#
#     @discord.ui.button(label={self.value2}, style=discord.ButtonStyle.success)
#     async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
#         """NGボタン(単語→意味)"""
#         self.selected = 1
#         await interaction.response.send_message(
#             f"{interaction.user.mention} NG"
#         )
#         self.stop()
#
#     @discord.ui.button(label={self.value3}, style=discord.ButtonStyle.success)
#     async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
#         """OKボタン(意味→単語)"""
#         self.selected = 3  # どちらのボタンが押されたかを保存
#         await interaction.response.send_message(
#             f"{interaction.user.mention} OK!"
#         )
#         self.stop()  # これでViewの待機が終了
#
#     @discord.ui.button(label={self.value4}, style=discord.ButtonStyle.success)
#     async def button4(self, interaction: discord.Interaction, button: discord.ui.Button):
#         """NGボタン(単語→意味)"""
#         self.selected = 4
#         await interaction.response.send_message(
#             f"{interaction.user.mention} NG"
#         )
#         self.stop()
