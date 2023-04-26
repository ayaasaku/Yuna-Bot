from discord import Member
from discord.ext import commands


class OtherCog(commands.Cog, name='other'):
    def __init__(self, bot):
        self.bot = bot       
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OtherCog(bot))