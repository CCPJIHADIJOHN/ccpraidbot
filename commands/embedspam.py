import discord
import asyncio
from utils.embed import build, ExtraButtons, EmbedButton

async def embedspam_command(interaction: discord.Interaction, count: int = 10, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} embeds!", view=EmbedButton(count), ephemeral=True)
    else:
        await interaction.response.send_message(f"Sending {count} embeds...", ephemeral=True)
        for _ in range(count):
            try:
                embed, img = build()
                files = [discord.File(img)] if img else []
                await interaction.followup.send(embed=embed, files=files, view=ExtraButtons())
            except Exception as e:
                print(f"Error: {e}")
            await asyncio.sleep(0.3)
