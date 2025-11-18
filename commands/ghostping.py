import discord
import asyncio
from utils.helpers import send_ephemeral_delete, delete_safe

class GhostpingButton(discord.ui.View):
    def __init__(self, user: discord.User, count: int):
        super().__init__(timeout=None)
        self.user = user
        self.count = count

    @discord.ui.button(label="Ghostping", style=discord.ButtonStyle.blurple)
    async def ghostping_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending {self.count} ghostpings...", delay=1.0)
        for _ in range(self.count):
            m = await interaction.followup.send(self.user.mention, ephemeral=False)
            await delete_safe(m)

async def ghostping_command(interaction: discord.Interaction, user: discord.User, count: int = 5, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} ghostpings!", view=GhostpingButton(user, count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} ghostpings...", delay=1.0)
        for _ in range(count):
            m = await interaction.followup.send(user.mention, ephemeral=False)
            await delete_safe(m)
