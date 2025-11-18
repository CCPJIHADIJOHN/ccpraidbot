import discord
import asyncio
from config.presets import PRESET_MESSAGE
from utils.helpers import send_ephemeral_delete

class PresetButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Send Preset", style=discord.ButtonStyle.blurple)
    async def preset_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending `{self.count}` messages...", delay=2.0)
        for _ in range(self.count):
            await interaction.followup.send(PRESET_MESSAGE, ephemeral=False)

async def preset_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send `{count}` messages!", view=PresetButton(count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending `{count}` messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(PRESET_MESSAGE, ephemeral=False)
