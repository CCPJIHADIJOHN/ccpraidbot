import discord,asyncio

class TTSSpamButton(discord.ui.View):
    def __init__(self,text,count):super().__init__(timeout=None);self.text=text;self.count=count
    @discord.ui.button(label="TTS Spam",style=discord.ButtonStyle.blurple)
    async def tts_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        msg=await interaction.response.send_message(f"Spamming `{self.count}` TTS messages...",ephemeral=True);await asyncio.sleep(2)
        try:await msg.delete()
        except:pass
        for _ in range(self.count):
            await interaction.followup.send(self.text,tts=True,ephemeral=False)
            await asyncio.sleep(0.3)

async def bttsspam_command(interaction:discord.Interaction,text:str,count:int=5):
    msg=await interaction.response.send_message(f"Click the button to spam `{count}` TTS messages!",view=TTSSpamButton(text,count),ephemeral=True);await asyncio.sleep(5)
    try:await msg.delete()
    except:pass
