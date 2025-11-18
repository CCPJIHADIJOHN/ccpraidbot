import discord

class BlameButton(discord.ui.View):
    def __init__(self, user: discord.User):
        super().__init__(timeout=None)
        self.user = user

    @discord.ui.button(label="Blame", style=discord.ButtonStyle.blurple)
    async def blame_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.followup.send(f"{self.user.mention}, raid has been executed successfully. Glory to the ccp thugs", ephemeral=False)

async def blame_command(interaction: discord.Interaction, user: discord.User, button: bool = False):
    if button:
        await interaction.response.send_message(
            "Blaming...",
            view=BlameButton(user),
            ephemeral=True
        )
    else:
        await interaction.response.send_message("Blaming...", ephemeral=True)
        await interaction.followup.send(f"{user.mention}, raid has been executed successfully. Glory to the ccp thugs", ephemeral=False)
