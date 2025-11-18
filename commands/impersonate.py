import discord

async def impersonate_command(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"Impersonating {user}", ephemeral=True)
    avatar_bytes = await user.display_avatar.read()
    try:
        await interaction.client.user.edit(username=user.name, avatar=avatar_bytes, global_name=user.display_name)
    except TypeError:
        await interaction.client.user.edit(username=user.name, avatar=avatar_bytes)
