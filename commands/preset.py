import discord
from config.preset import PRESET_MESSAGE

async def preset_command(interaction: discord.Interaction, count: int = 5):
    await interaction.response.send_message(f"Sending `{count}` messages...", ephemeral=True)
    for _ in range(count):
        await interaction.followup.send(PRESET_MESSAGE, ephemeral=False)
