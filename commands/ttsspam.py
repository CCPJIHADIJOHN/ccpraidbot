import discord,asyncio

async def ttsspam_command(interaction:discord.Interaction,text:str,count:int=5):
    msg=await interaction.response.send_message(f"Spamming TTS `{count}` times...",ephemeral=True)
    for _ in range(count):
        await interaction.followup.send(text,tts=True,ephemeral=False)
        await asyncio.sleep(0.3)
    m=await interaction.original_response()
    await m.delete()
