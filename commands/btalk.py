import discord,asyncio

class TalkButton(discord.ui.View):
    def __init__(self,text,count):super().__init__(timeout=None);self.text=text;self.count=count
    @discord.ui.button(label="Talk",style=discord.ButtonStyle.blurple)
    async def talk_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        msg=await interaction.response.send_message(f"Sending `{self.count}` messages...",ephemeral=True);await asyncio.sleep(2)
        try:await msg.delete()
        except:pass
        for _ in range(self.count):await interaction.followup.send(self.text,ephemeral=False)

async def btalk_command(interaction:discord.Interaction,text:str,count:int=5):
    msg=await interaction.response.send_message(f"Click the button to send `{count}` messages!",view=TalkButton(text,count),ephemeral=True);await asyncio.sleep(5)
    try:await msg.delete()
    except:pass