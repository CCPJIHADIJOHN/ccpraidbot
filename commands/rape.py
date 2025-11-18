import discord
from config.rapeurls import URLS
from utils.helpers import format_urls, send_ephemeral_delete

class RapeButton(discord.ui.View):
    def __init__(self, batches: int):
        super().__init__(timeout=None)
        self.batches = batches

    @discord.ui.button(label="Rape", style=discord.ButtonStyle.blurple)
    async def send_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Thugging the server with {self.batches} links", delay=1.0)
        for _ in range(self.batches):
            text = format_urls(URLS)
            if text:
                await interaction.followup.send(text, ephemeral=False)

async def rape_command(interaction: discord.Interaction, batches: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click to send {batches} batches.", view=RapeButton(batches), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {batches} batches...", delay=1.0)
        for _ in range(batches):
            text = format_urls(URLS)
            if text:
                await interaction.followup.send(text, ephemeral=False)
