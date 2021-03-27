from discord.ext.commands import (Cog, BucketType, command, cooldown)
import requests
from discord import Embed
from datetime import datetime

class Spin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="spin", aliases=["sp"])
    @cooldown(5, 3600, BucketType.default)
    async def spin_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/article_rewrite.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="Your text is being spun...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Spun Text:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("spin")

def setup(bot):
    bot.add_cog(Spin(bot))