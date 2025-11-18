import discord
import asyncio
from utils.helpers import send_ephemeral_delete, delete_safe

class SpamButton(discord.ui.View):
    def __init__(self, user: discord.User, count: int, message: str):
        super().__init__(timeout=None)
        self.user = user
        self.count = count
        self.message = message

    @discord.ui.button(label="Spam", style=discord.ButtonStyle.red)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Spamming {self.count} messages...", delay=1.0)
        for _ in range(self.count):
            await interaction.channel.send(f"{self.user.mention} {self.message}")

async def spam_command(interaction: discord.Interaction, user: discord.User, count: int = 10, message: str = "GET SPAMMED", button: bool = False):
    if button:
        await interaction.response.send_message(
            f"Click to spam {user.mention} {count} times!",
            view=SpamButton(user, count, message),
            ephemeral=True
        )
    else:
        await send_ephemeral_delete(interaction, f"Spamming {count} messages...", delay=1.0)
        for _ in range(count):
            await interaction.channel.send(f"{user.mention} {message}")