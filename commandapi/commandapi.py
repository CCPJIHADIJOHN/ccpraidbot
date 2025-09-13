import discord
from discord import app_commands

Commands = {}

def add_command(name, handler, description):
    Commands[name] = {"handler": handler, "description": description}

async def register_commands(bot, guild_id=None):
    for name, cmd in Commands.items():
        app_cmd = app_commands.Command(
            name=name,
            description=cmd["description"],
            callback=cmd["handler"]
        )

        bot.tree.add_command(
            app_cmd,
            guild=discord.Object(id=guild_id) if guild_id else None
        )
        print(f"🔹 Registered command: /{name} - {cmd['description']}")

    if guild_id:
        await bot.tree.sync(guild=discord.Object(id=guild_id))
    else:
        await bot.tree.sync()
