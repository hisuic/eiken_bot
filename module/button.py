import discord

class ModeSelection(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="意味→単語", style=discord.ButtonStyle.success)
    async def ok(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user.mention} OK!")

    @discord.ui.button(label="単語→意味", style=discord.ButtonStyle.success)
    async def ng(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user.mention} NG")

