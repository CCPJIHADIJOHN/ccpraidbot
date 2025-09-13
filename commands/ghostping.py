# ghostping.py - non-button version
import discord, asyncio

async def ghostping_command(interaction: discord.Interaction, user: discord.User, count: int = 5):
    msg = await interaction.response.send_message(f"Sending {count} ghostpings...", ephemeral=True)
    await asyncio.sleep(1)
    try: await msg.delete()
    except: pass
    for _ in range(count):
        m = await interaction.followup.send(user.mention, ephemeral=False)
        await m.delete()
