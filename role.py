import discord
import asyncio

intents = discord.Intents.default()
intents.guilds = True  # we only need guild info

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} ({client.user.id})\n")
    for guild in client.guilds:
        try:
            # Try to create an invite for the system channel (if available)
            if guild.system_channel:
                invite = await guild.system_channel.create_invite(max_age=0, max_uses=0, unique=False)
                print(f"{guild.name} ({guild.id}): {invite.url}")
            else:
                print(f"{guild.name} ({guild.id}): No system channel to create invite")
        except discord.Forbidden:
            print(f"{guild.name} ({guild.id}): Missing permission to create invite")
        except Exception as e:
            print(f"{guild.name} ({guild.id}): Error - {e}")
    await client.close()

# replace with your bot token
TOKEN = "MTQwODU5MzEyMDc2OTM0NzcxNA.Gp7-lU.x-ZRnnSadi9-xW31DTSNzJ_N20rhKbxk538gW0"
asyncio.run(client.start(TOKEN))

