import discord

async def talk_command(interaction: discord.Interaction, text: str, count: int = 1):
    msg=await interaction.response.send_message(f"Talking `{count}` times...",ephemeral=True)
    for _ in range(count):
        await interaction.followup.send(text,ephemeral=False)
    m=await interaction.original_response()
    await m.delete()
