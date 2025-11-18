import discord
import random
from utils.helpers import send_ephemeral_delete

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def build_security_embed(user: discord.User):
    ip = generate_ip()
    embed = discord.Embed(
        title="🚨 SECURITY ALERT",
        description=f"**Unauthorized Access Detected**\n\nUser: {user.mention}\nUser ID: `{user.id}`\n\n**Network Information**\nIP Address: `{ip}`\nLocation: Unknown\nDevice: Discord Client\n\n**Threat Assessment**\nSeverity: HIGH\nAction Required: Immediate\nStatus: ACTIVE THREAT",
        color=discord.Color.red()
    )
    embed.set_author(name="Discord Security Team", icon_url="https://cdn.discordapp.com/emojis/1234567890.png")
    embed.set_footer(text="🔴 Threat Level: HIGH • Discord Security System")
    embed.set_thumbnail(url=user.display_avatar.url)
    return embed

class SecurityButton(discord.ui.View):
    def __init__(self, user: discord.User, count: int):
        super().__init__(timeout=None)
        self.user = user
        self.count = count

    @discord.ui.button(label="Send Alert", style=discord.ButtonStyle.red)
    async def security_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await send_ephemeral_delete(interaction, f"Sending {self.count} security alerts...", delay=1.0)
        for _ in range(self.count):
            embed = build_security_embed(self.user)
            await interaction.followup.send(embed=embed, ephemeral=False)

async def security_command(interaction: discord.Interaction, user: discord.User, count: int = 1, button: bool = False):
    if button:
        await interaction.response.send_message(f"Click the button to send {count} security alerts!", view=SecurityButton(user, count), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} security alerts...", delay=1.0)
        for _ in range(count):
            embed = build_security_embed(user)
            await interaction.followup.send(embed=embed, ephemeral=False)
