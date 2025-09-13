import discord

async def blame_command(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message("Blaming...", ephemeral=True)
    await interaction.followup.send(f"{user.mention}, raid has been executed successfully. Glory to the ccp thugs", ephemeral=False)
