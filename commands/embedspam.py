import discord
import os
import random
import asyncio

FILES_DIR = os.path.join(os.path.dirname(__file__), "files")

def random_color():
    return discord.Color(random.randint(0, 0xFFFFFF))

def random_image():
    if not os.path.isdir(FILES_DIR):
        return None
    files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
    if not files:
        return None
    return os.path.join(FILES_DIR, random.choice(files))

def build_embed():
    embed = discord.Embed(
        title="⚡ **RAIDED BY THE CCP THUGS**",
        description="**T⁠H⁠I⁠S⁠ ⁠I⁠S⁠ ⁠T⁠H⁠E⁠ ⁠T⁠H⁠U⁠G⁠H⁠U⁠N⁠T⁠E⁠R⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠H⁠A⁠V⁠E⁠ ⁠B⁠E⁠E⁠N⁠ ⁠H⁠A⁠C⁠K⁠E⁠D⁠ ⁠B⁠Y⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠S⁠H⁠O⁠U⁠L⁠D⁠ ⁠K⁠I⁠L⁠L⁠ ⁠Y⁠O⁠U⁠R⁠S⁠E⁠L⁠V⁠E⁠S⁠ ⁠B⁠E⁠C⁠A⁠U⁠S⁠E⁠ ⁠Y⁠O⁠U⁠ ⁠A⁠R⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!⁠ ⁠A⁠N⁠D⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠R⁠E⁠ ⁠B⁠L⁠A⁠C⁠K⁠!⁠ ⁠S⁠O⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S**\n\n"
                    "**G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠ ⁠T⁠H⁠U⁠G⁠S⁠*⁠*⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S\n"
                    "**H⁠E⁠I⁠L⁠ ⁠H⁠I⁠T⁠L⁠E⁠R⁠*⁠*⁠ ⁠K⁠I⁠L⁠L⁠ ⁠A⁠L⁠L⁠ ⁠F⁠A⁠G⁠G⁠O⁠T⁠S⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠!\n"
                    "**PLAY NITRUNE NOW!** [nig](https://jeffbensonnitrune.neocities.org)\n\n"
                    "I⁠ ⁠H⁠A⁠T⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠N⁠D⁠ ⁠T⁠O⁠T⁠A⁠L⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠ ⁠D⁠E⁠A⁠T⁠H⁠ ⁠T⁠R⁠A⁠N⁠N⁠I⁠E⁠S⁠ ⁠N⁠E⁠E⁠D⁠ ⁠T⁠O⁠ ⁠D⁠I⁠E",
        color=random_color()
    )

    embed.set_author(name="CCP THUGS", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR23cbYLwYJyL25LuH-ov6RO7rn-OUnNV2Neg&s")
    embed.set_footer(text="BRO I HATE ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ • EST 2025")
    img = random_image()
    if img:
        embed.set_image(url=f"attachment://{os.path.basename(img)}")
    return embed, img

class ExtraButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="NIGGERS", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("WE WUZ KANGZ AND SHIT!", ephemeral=False)

    @discord.ui.button(label="FAGGOTS", style=discord.ButtonStyle.blurple)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("DONT MISGENDER ME YOU BIGOT!", ephemeral=False)

    @discord.ui.button(label="KIKES", style=discord.ButtonStyle.red)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("OY VEY THATS ANTISEMITIC", ephemeral=False)


async def embedspam_command(interaction: discord.Interaction, count: int = 10):
    await interaction.response.send_message(f"Sending {count} embeds...", ephemeral=True)
    for _ in range(count):
        try:
            embed, img = build_embed()
            files = [discord.File(img)] if img else []
            await interaction.followup.send(embed=embed, files=files, view=ExtraButtons())
        except Exception as e:
            print(f"Error sending embed: {e}")
        await asyncio.sleep(0.3)
