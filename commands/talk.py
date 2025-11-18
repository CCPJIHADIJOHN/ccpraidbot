import discord
from utils.helpers import send_ephemeral_delete

class TalkButton(discord.ui.View):
    def __init__(self, text: str, count: int):
        super().__init__(timeout=None)
        self.text = text
        self.count = count

    @discord.ui.button(label="Talk", style=discord.ButtonStyle.blurple)
    async def talk_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending `{self.count}` messages...", delay=1.0)
        for _ in range(self.count):
            await interaction.followup.send(self.text, ephemeral=False)

async def talk_command(interaction: discord.Interaction, text: str, count: int = 1, button: bool = False):
    if button:
        await interaction.response.send_message(
            f"Click the button to send `{count}` messages!",
            view=TalkButton(text, count),
            ephemeral=True
        )
    else:
        await send_ephemeral_delete(interaction, f"Talking `{count}` times...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(text, ephemeral=False)
