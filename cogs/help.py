import config
from nextcord.ext import commands
from nextcord.ui import View,button,Button
from nextcord import Interaction, Embed,ButtonStyle,Member

class Help(commands.Cog):
    def __init__(self, React: commands.Bot):
        self.React = React

    @commands.command()
    async def help(self, ctx : commands.Context):
        embed = Embed(
            color=0xFFD06B,
            description= "``🕐`` ``|``กําลังโหลดกรุณารอสักครู่..."
        )
        message = await ctx.reply(embed=embed)
        embed = Embed(
            color=0x91CFFF, 
            description = f"""
``{config.Bot_prefix}help`` โชว์หน้าช่วยเหลือ
``{config.Bot_prefix}check (ip) (port) (id)`` ค้นหาข้อมูลผู้เล่น fivem
``{config.Bot_prefix}profile (discord id)`` ค้นหาข้อมูลดิสคอร์
``{config.Bot_prefix}botinfo`` ดูข้อมุลบอท"""
    )
        await message.edit(embed=embed)


def setup(React: commands.Bot):
    React.add_cog(Help(React))