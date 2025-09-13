# bghostping.py - button version
import discord, asyncio

class GhostpingButton(discord.ui.View):
    def __init__(self, user: discord.User, count: int):
        super().__init__(timeout=None)
        self.user = user
        self.count = count

    @discord.ui.button(label="Ghostping", style=discord.ButtonStyle.blurple)
    async def ghostping_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg = await interaction.response.send_message(f"Sending {self.count} ghostpings...", ephemeral=True)
        await asyncio.sleep(1)
        try: await msg.delete()
        except: pass
        for _ in range(self.count):
            m = await interaction.followup.send(self.user.mention, ephemeral=False)
            await m.delete()

async def bghostping_command(interaction: discord.Interaction, user: discord.User, count: int = 5):
    msg = await interaction.response.send_message(
        f"Click the button to send {count} ghostpings!",
        view=GhostpingButton(user, count),
        ephemeral=True
    )
    await asyncio.sleep(5)
    try: await msg.delete()
    except: pass
