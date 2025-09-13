import discord
import os
import random
import asyncio

MESSAGE = "T⁠H⁠I⁠S⁠ ⁠I⁠S⁠ ⁠T⁠H⁠E⁠ ⁠T⁠H⁠U⁠G⁠H⁠U⁠N⁠T⁠E⁠R⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠H⁠A⁠V⁠E⁠ ⁠B⁠E⁠E⁠N⁠ ⁠H⁠A⁠C⁠K⁠E⁠D⁠ ⁠B⁠Y⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠S⁠H⁠O⁠U⁠L⁠D⁠ ⁠K⁠I⁠L⁠L⁠ ⁠Y⁠O⁠U⁠R⁠S⁠E⁠L⁠V⁠E⁠S⁠ ⁠B⁠E⁠C⁠A⁠U⁠S⁠E⁠ ⁠Y⁠O⁠U⁠ ⁠A⁠R⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!⁠ ⁠A⁠N⁠D⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠R⁠E⁠ ⁠B⁠L⁠A⁠C⁠K⁠!⁠ ⁠S⁠O⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!"
FILES_DIR = os.path.join(os.path.dirname(__file__), "files")

class SendButton(discord.ui.View):
    def __init__(self, count: int):
        super().__init__(timeout=None)
        self.count = count

    @discord.ui.button(label="Send", style=discord.ButtonStyle.blurple)
    async def send_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg = await interaction.response.send_message(f"Sending `{self.count}` messages...", ephemeral=True)
        # try to delete ephemeral immediately
        await asyncio.sleep(0)  
        try:
            await msg.delete()
        except:
            pass

        file_paths = [
            os.path.join(FILES_DIR, f)
            for f in os.listdir(FILES_DIR)
            if os.path.isfile(os.path.join(FILES_DIR, f))
        ]

        async def send_one():
            if file_paths:
                path = random.choice(file_paths)
                try:
                    file = discord.File(path)
                    await interaction.followup.send(content=f"**{MESSAGE}**", file=file, ephemeral=False)
                except Exception as e:
                    print(f"Error sending file {path}: {e}")
            else:
                await interaction.followup.send(content=f"**{MESSAGE}**", ephemeral=False)

        tasks = [asyncio.create_task(send_one()) for _ in range(self.count)]
        await asyncio.gather(*tasks)

async def bsend_command(interaction: discord.Interaction, count: int = 10):
    msg = await interaction.response.send_message(
        f"Click the button to send `{count}` messages!",
        view=SendButton(count),
        ephemeral=True
    )
    await asyncio.sleep(0)
    try:
        await msg.delete()
    except:
        pass