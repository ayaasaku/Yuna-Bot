import discord
from discord import app_commands, Interaction
from discord.ext import commands

from modules.main import defaultEmbed


class MainCog(commands.Cog, name='main'):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='about', description='有關三月七')
    async def about(self, interaction: Interaction):
        embed = defaultEmbed(title="三月七 • March 7th Bot",
                             description="**三月七**是由**綾霞**製作的機器人")
        embed.set_author(name="三月七", url="https://github.com/Ayaakaa/March-7th-Bot",
                         icon_url="https://i.imgur.com/Zp9bgVN.jpeg")
        embed.set_image(url="https://i.imgur.com/sU7bXs1.jpeg")
        embed.set_footer(text=f"三月七 v{self.bot.version} - by 綾霞 Ayaakaa")
        await interaction.response.send_message(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        tuple1 = ('三月七：','小三月：','三月：')
        tuple2 = ('三月七:','小三月:','三月:')
        if msg.author.id == 831883841417248778 and msg.content[0:3] in tuple1 or msg.content[0:3] in tuple2 or msg.content[0:4] in tuple1 or msg.content[0:4] in tuple2:
            global text
            
            if msg.content[0:3] or msg.content[0:4] in tuple1: text = msg.content.split('：')[1]
            elif msg.content[0:3] or msg.content[0:4] in tuple2: text = msg.content.split(': ')[1]
            else: return
            
            if msg.reference != None or msg.reference is not None:
                reply_id = msg.reference.message_id
                await msg.delete()
                reply_message = await msg.channel.fetch_message(reply_id)
                await reply_message.reply(text)
                
            else:
                await msg.delete()
                await msg.channel.send(text)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MainCog(bot))