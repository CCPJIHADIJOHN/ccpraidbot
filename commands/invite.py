import discord

async def invite_command(interaction: discord.Interaction, count: int = 1):
    invite_url = f"https://discord.com/oauth2/authorize?client_id={interaction.client.user.id}&integration_type=1&scope=applications.commands"
    await interaction.response.send_message(f"Sending `{count}` invite link(s)...", ephemeral=True)
    for _ in range(count):
        await interaction.followup.send(invite_url, ephemeral=True)
