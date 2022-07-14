from httpx import get
from nextcord.ext import commands
from nextcord.ui import View,button,Button
from nextcord import Interaction, Embed,ButtonStyle,Member

class Profile(commands.Cog):
    def __init__(self, React: commands.Bot):
        self.React = React

    @commands.command()
    async def profile(self, ctx : commands.Context , id : str):
        embed = Embed(
            color=0xFFD06B,
            description= "``🕐`` ``|``กําลังโหลดกรุณารอสักครู่..."
        )
        message = await ctx.reply(embed=embed)
        try:
            user = await self.React.fetch_user(int(id))
            embed = Embed(
                color=0x91CFFF,
                description=f"""
> ``✨ Discord``:{str(user)}     
> ``🔥 Discord Tag``:{user.mention}           
"""
        )

            embed.set_author(name="DISCORD LOOKUP",icon_url="https://i.imgur.com/DUKbVld.png")
            if user.avatar:
                embed.set_thumbnail(url=user.avatar.url)

            if user.banner:
                embed.set_image(url=user.banner.url)
                
            await message.edit(embed=embed)
        except:
            embed = Embed(
                    color=0xFF9193,
                    description= f"``❌`` ``|`` ไม่พบดิสคอร์ดไอดี {id}"
            )
            await message.edit(
                embed=embed)

def setup(React: commands.Bot):
    React.add_cog(Profile(React))