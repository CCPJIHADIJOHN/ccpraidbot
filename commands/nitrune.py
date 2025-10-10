import discord

async def nitrune_command(interaction: discord.Interaction, user: discord.User):
    msg = await interaction.response.send_message(f"Telling {user.mention} about NITRUNE...", ephemeral=True)
    await interaction.followup.send(
        f"yo bro {user.mention} i found this nitrune game shit u gotta try it\nhttps://jeffbensonnitrune.neocities.org/",
        ephemeral=False
    )
    m = await interaction.original_response()
    await m.delete()
