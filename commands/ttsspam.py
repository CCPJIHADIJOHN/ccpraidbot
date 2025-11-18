import discord
import asyncio
from utils.helpers import send_ephemeral_delete

class TTSButton(discord.ui.View):
    def __init__(self, text: str, count: int):
        super().__init__(timeout=None)
        self.text = text
        self.count = count

    @discord.ui.button(label="TTS Spam", style=discord.ButtonStyle.blurple)
    async def tts_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Spamming `{self.count}` TTS messages...", delay=2.0)
        for _ in range(self.count):
            await interaction.followup.send(self.text, tts=True, ephemeral=False)
            await asyncio.sleep(0.3)

async def ttsspam_command(interaction: discord.Interaction, text: str, count: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(
            f"Click the button to spam `{count}` TTS messages!",
            view=TTSButton(text, count),
            ephemeral=True
        )
    else:
        await send_ephemeral_delete(interaction, f"Spamming TTS `{count}` times...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(text, tts=True, ephemeral=False)
            await asyncio.sleep(0.3)
