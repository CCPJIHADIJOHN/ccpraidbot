import discord
from discord.ext import commands
from config.token import Token
import commandapi.commandapi as commandapi
from commands.talk import talk_command
from commands.ghostping import ghostping_command
from commands.blame import blame_command
from commands.impersonate import impersonate_command
from commands.ttsspam import ttsspam_command
from commands.send import send_command
from commands.embedspam import embedspam_command
from commands.preset import preset_command
from commands.invite import invite_command
from commands.rape import rape_command
from commands.heil import heil_command
from commands.andrewtate import andrewtate_command
from commands.spamping import spam_command
from commands.security import security_command

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

commandapi.add_command("talk", talk_command, "Say something through the bot")
commandapi.add_command("ghostping", ghostping_command, "Send 5 ghostpings")
commandapi.add_command("rape", rape_command, "rapes the server with random thugs( borrowed from jihad bot)")
commandapi.add_command("blame", blame_command, "blame a user for raid")
commandapi.add_command("impersonate", impersonate_command, "Make the bot take the name and avatar of a chosen user")
commandapi.add_command("ttsspam", ttsspam_command, "send tts messages.")
commandapi.add_command("send", send_command, "Send the raid textwall (button argument in command)")
commandapi.add_command("embedspam", embedspam_command, "Send preset embeds (optional button arg)")
commandapi.add_command("preset", preset_command, "spams preset")
commandapi.add_command("invite", invite_command, "get the bots invite url")
commandapi.add_command("heil", heil_command, "the third reich")
commandapi.add_command("andrewtate", andrewtate_command, "my name is andrew tate and you are a fucking nigger")
commandapi.add_command("spamping", spam_command, "like ghost ping but doesnt delete")
commandapi.add_command("security", security_command, "scare a nigga with this command")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await commandapi.register_commands(bot)

bot.run(Token)
