import discord,os,random,asyncio

MESSAGE = "T⁠H⁠I⁠S⁠ ⁠I⁠S⁠ ⁠T⁠H⁠E⁠ ⁠T⁠H⁠U⁠G⁠H⁠U⁠N⁠T⁠E⁠R⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠H⁠A⁠V⁠E⁠ ⁠B⁠E⁠E⁠N⁠ ⁠H⁠A⁠C⁠K⁠E⁠D⁠ ⁠B⁠Y⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ⁠C⁠C⁠P⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠S⁠H⁠O⁠U⁠L⁠D⁠ ⁠K⁠I⁠L⁠L⁠ ⁠Y⁠O⁠U⁠R⁠S⁠E⁠L⁠V⁠E⁠S⁠ ⁠B⁠E⁠C⁠A⁠U⁠S⁠E⁠ ⁠Y⁠O⁠U⁠ ⁠A⁠R⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!⁠ ⁠A⁠N⁠D⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠R⁠E⁠ ⁠B⁠L⁠A⁠C⁠K⁠!⁠ ⁠S⁠O⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!"
FILES_DIR=os.path.join(os.path.dirname(__file__),"files")

async def send_command(interaction:discord.Interaction,count:int=10):
    msg=await interaction.response.send_message(f"Sending {count} messages...",ephemeral=True);await asyncio.sleep(2)
    try:await msg.delete()
    except:pass
    file_paths=[os.path.join(FILES_DIR,f) for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR,f))]
    async def send_one():
        if file_paths:
            path=random.choice(file_paths)
            try:
                file=discord.File(path)
                await interaction.followup.send(content=f"**{MESSAGE}**",file=file,ephemeral=False)
            except:pass
        else:
            await interaction.followup.send(content=f"**{MESSAGE}**",ephemeral=False)
    tasks=[asyncio.create_task(send_one()) for _ in range(count)]
    await asyncio.gather(*tasks)
