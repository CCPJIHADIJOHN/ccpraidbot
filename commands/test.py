import discord
from utils.helpers import send_ephemeral_delete

class TestButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Test", style=discord.ButtonStyle.blurple)
    async def test_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending `{self.count}` test messages...", delay=1.0)
        for _ in range(self.count):
            await interaction.followup.send("test", ephemeral=False)

async def test_command(interaction: discord.Interaction, count: int = 1, button: bool = False):
    if button:
        await interaction.response.send_message(
            f"Click the button to send `{count}` test messages!",
            view=TestButton(count),
            ephemeral=True
        )
    else:
        await send_ephemeral_delete(interaction, f"Sending `{count}` test messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send("test", ephemeral=False)
