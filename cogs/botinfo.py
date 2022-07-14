import config
from nextcord.ext import commands
from nextcord import Embed,__version__
from datetime import datetime
from humanize import intcomma
start_time = datetime.utcnow()

class Botinfo(commands.Cog):
    def __init__(self, React: commands.Bot):
        self.React = React

    @commands.command()
    async def botinfo(self, ctx : commands.Context):
        embed = Embed(
                colour=0xFFFF00, 
                title="ข้อมูลของบอท"
            )

        embed.timestamp = datetime.utcnow()
        embed.add_field(
            name="🤖 ``ชื่อของบอท``", value=f"{self.React.user}", inline=False
        )
        embed.add_field(
            name="📁 ``จํานวนเซิฟเวอร์``",
            value=f"{intcomma(len(self.React.guilds))}",
        )
        embed.add_field(
            name="📁 ``สมาชิกทั้งหมด``",
            value=f"{intcomma(len(self.React.users))}",
        )
        embed.add_field(name="🤖 ``เวลาทำงาน``", value=f"{str(datetime.utcnow() - start_time).split('.')[0]}")
        embed.add_field(
            name="🤖 ``Ping ของบอท``",
            value=f"{round(self.React.latency * 1000)}ms",
        )
        embed.add_field(
            name="🤖 ``Nextcord.py``",
            value=f"Nextcord.py {__version__}",
        )
        embed.set_footer(text=f"┗Requested by {ctx.author}")
        embed.set_thumbnail(url=self.React.user.avatar.url)

        await ctx.send(embed=embed)


def setup(React: commands.Bot):
    React.add_cog(Botinfo(React))