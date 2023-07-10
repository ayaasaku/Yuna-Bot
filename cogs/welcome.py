import random
from discord import Member, channel
from discord.ext import commands
from modules.main import defaultEmbed


class WelcomeCog(commands.Cog, name='welcome'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        member_name = member.display_name
        welcome_messages = ['歡迎加入奈奈應援團～', '奏是真冬的老婆喔', '我們群主很常改名字的']
        welcome_embed = defaultEmbed(title=f'歡迎 {member_name} 加入 Kuma²', description=random.choice(welcome_messages))
        welcome_embed.set_image(url='https://i.imgur.com/B0fhxZp.gif')
        if member.guild.id == 1001466950309924876:
            role = member.guild.get_role(1001478249773289562)
            await member.add_roles(role)
            
            channel = self.bot.get_channel(1001811652590719020)
            await channel.send(embed=welcome_embed)
   
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WelcomeCog(bot))