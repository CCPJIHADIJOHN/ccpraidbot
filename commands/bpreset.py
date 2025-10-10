import discord, asyncio
from config.preset import PRESET_MESSAGE

class BPresetButton(discord.ui.View):
    def __init__(self, count):
        super().__init__(timeout=None)
        self.text = PRESET_MESSAGE
        self.count = count

    @discord.ui.button(label="Send Preset", style=discord.ButtonStyle.blurple)
    async def bpreset_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg = await interaction.response.send_message(f"Sending `{self.count}` messages...", ephemeral=True)
        await asyncio.sleep(2)
        try:
            await msg.delete()
        except:
            pass
        for _ in range(self.count):
            await interaction.followup.send(self.text, ephemeral=False)

async def bpreset_command(interaction: discord.Interaction, count: int = 5):
    msg = await interaction.response.send_message(
        f"Click the button to send `{count}` messages!",
        view=BPresetButton(count),
        ephemeral=True
    )
    await asyncio.sleep(5)
    try:
        await msg.delete()
    except:
        pass
