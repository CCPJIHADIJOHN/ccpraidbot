import discord
from config.presets import ANDREW_TATE
from utils.helpers import send_ephemeral_delete

class AndrewTateButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Andrew Tate", style=discord.ButtonStyle.red)
    async def tate_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending {self.count} Andrew Tate messages...", delay=1.0)
        for _ in range(self.count):
            await interaction.followup.send(ANDREW_TATE, ephemeral=False)

async def andrewtate_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} Andrew Tate messages!", view=AndrewTateButton(count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} Andrew Tate messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(ANDREW_TATE, ephemeral=False)
