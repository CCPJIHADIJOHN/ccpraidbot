import discord
import os
import asyncio
import io
import random

MESSAGE = "T⁠H⁠I⁠S⁠ ⁠I⁠S⁠ ⁠T⁠H⁠E⁠ ⁠T⁠H⁠U⁠G⁠H⁠U⁠N⁠T⁠E⁠R⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠H⁠A⁠V⁠E⁠ ⁠B⁠E⁠E⁠N⁠ ⁠H⁠A⁠C⁠K⁠E⁠D⁠ ⁠B⁠Y⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠S⁠H⁠O⁠U⁠L⁠D⁠ ⁠K⁠I⁠L⁠L⁠ ⁠Y⁠O⁠U⁠R⁠S⁠E⁠L⁠V⁠E⁠S⁠ ⁠B⁠E⁠C⁠A⁠U⁠S⁠E⁠ ⁠Y⁠O⁠U⁠ ⁠A⁠R⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!⁠ ⁠A⁠N⁠D⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠R⁠E⁠ ⁠B⁠L⁠A⁠C⁠K⁠!⁠ ⁠S⁠O⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!"
FILES_DIR = os.path.join(os.path.dirname(__file__), "files")

FILES = []
for f in os.listdir(FILES_DIR):
    path = os.path.join(FILES_DIR, f)
    if os.path.isfile(path):
        try:
            with open(path, "rb") as fp:
                FILES.append((f, fp.read()))
        except:
            pass


class SendButton(discord.ui.View):
    def __init__(self, count: int = 10):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Send", style=discord.ButtonStyle.blurple)
    async def send_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Sending messages...", ephemeral=True)

        for _ in range(self.count):
            if FILES:
                name, data = random.choice(FILES)
                try:
                    bio = io.BytesIO(data)
                    await interaction.followup.send(content=f"**{MESSAGE}**", file=discord.File(bio, filename=name))
                    bio.close()
                except:
                    continue
            else:
                try:
                    await interaction.followup.send(content=f"**{MESSAGE}**")
                except:
                    continue

            await asyncio.sleep(0.2)


async def bsend_command(interaction: discord.Interaction, count: int = 10):
    await interaction.response.send_message(
        f"Click the button to send {count} messages!",
        view=SendButton(count),
        ephemeral=True
    )
