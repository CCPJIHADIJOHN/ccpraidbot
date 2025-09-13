import discord
from discord.ext import commands
from config.token import Token
import commandapi.commandapi as commandapi
from commands.talk import talk_command
from commands.bsend import bsend_command
from commands.ghostping import ghostping_command
from commands.blame import blame_command
from commands.impersonate import impersonate_command
from commands.ttsspam import ttsspam_command
from commands.btalk import btalk_command
from commands.bttsspam import bttsspam_command
from commands.send import send_command
from commands.bghost import bghostping_command
from commands.embedspam import embedspam_command
from commands.bembed import bembedspam_command

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

commandapi.add_command("talk", talk_command, "Say something through the bot")
commandapi.add_command("bsend", bsend_command, "Send the raid textwall via button")
commandapi.add_command("ghostping", ghostping_command, "Send 5 ghostpings")
commandapi.add_command("blame", blame_command, "blame a user for raid")
commandapi.add_command("impersonate", impersonate_command, "Make the bot take the name and avatar of a chosen user")
commandapi.add_command("ttsspam", ttsspam_command, "send tts messages.")
commandapi.add_command("btalk", btalk_command, "sends talk via button")
commandapi.add_command("btts", bttsspam_command, "sends tts via button")
commandapi.add_command("send", send_command, "Send the raid textwall normally")
commandapi.add_command("bghost", bghostping_command, "ghost ping via button")
commandapi.add_command("embedspam", embedspam_command, "Send preset embeds")
commandapi.add_command("bembedspam", bembedspam_command, "Send preset embeds via button")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await commandapi.register_commands(bot)

bot.run(Token)
