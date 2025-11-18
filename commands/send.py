import discord
import asyncio
from config.presets import PRESET_MESSAGE
from utils.files import send_with_file, get_random_path
from utils.helpers import send_ephemeral_delete

class SendButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Send", style=discord.ButtonStyle.blurple)
    async def send_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, "Sending messages...", delay=2.0)
        async def send_one():
            path = get_random_path()
            try:
                if path:
                    await interaction.followup.send(content=f"**{PRESET_MESSAGE}**", file=discord.File(path), ephemeral=False)
                else:
                    await send_with_file(interaction, f"**{PRESET_MESSAGE}**")
            except:
                pass
        await asyncio.gather(*(send_one() for _ in range(self.count)))

async def send_command(interaction: discord.Interaction, count: int = 10, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} messages!", view=SendButton(count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} messages...", delay=2.0)
        async def send_one():
            path = get_random_path()
            try:
                if path:
                    await interaction.followup.send(content=f"**{PRESET_MESSAGE}**", file=discord.File(path), ephemeral=False)
                else:
                    await interaction.followup.send(content=f"**{PRESET_MESSAGE}**", ephemeral=False)
            except:
                pass
        await asyncio.gather(*(send_one() for _ in range(count)))
