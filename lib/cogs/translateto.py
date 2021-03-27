from discord.ext.commands import (Cog, BucketType, command, cooldown)
import requests
from discord import Embed
from datetime import datetime

class Translateto(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="translateto", aliases=["trto"])
    @cooldown(1, 5, BucketType.guild)
    async def translateto_text(self, ctx, lang: str, *, text: str):
        lang = lang.lower()
        targets = {
            "english": "en",
            "arabic": "ar",
            "chinese": "zh",
            "french": "fr",
            "german": "de",
            "hindi": "hi",
            "irish": "ga",
            "italian": "it",
            "japanese": "ja",
            "korean": "ko",
            "portuguese": "pt",
            "russian": "ru",
            "spanish": "es"
        }
        if not lang in targets.keys():
            embed = Embed(title="Error!!!", description="Choose a correct language. Take a quick look at `+help trto`", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Please wait!", description="Your text is being translated...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            url = "https://libretranslate.com/translate"
            data = {
                'q': text,
                'source': 'auto',
                'target': targets[lang]
            }
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["translatedText"]
            embed.add_field(name=f"{lang.title()}:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("translateto")

def setup(bot):
    bot.add_cog(Translateto(bot))