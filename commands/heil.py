import discord
from config.arts import HEIL_ART
from utils.helpers import send_ephemeral_delete

class HeilButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Heil", style=discord.ButtonStyle.red)
    async def heil_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending {self.count} heils...", delay=1.0)
        for _ in range(self.count):
            await interaction.followup.send(HEIL_ART, ephemeral=False)

async def heil_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} heils!", view=HeilButton(count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} heils...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(HEIL_ART, ephemeral=False)
