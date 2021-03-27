from discord.ext.commands import (Cog, BucketType, command, cooldown)
import requests
from discord import Embed
from datetime import datetime

class Translate(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="translate", aliases=["tr"])
    @cooldown(1, 10, BucketType.guild)
    async def translate_text (self, ctx, *, text: str):
        url = "https://libretranslate.com/translate"
        targets = {
            "en": "English",
            "ar": "Arabic",
            "zh": "Chinese",
            "fr": "French",
            "de": "German",
            "hi": "Hindi",
            "ga": "Irish",
            "it": "Italian",
            "ja": "Japanese",
            "ko": "Korean",
            "pt": "Portuguese",
            "ru": "Russian",
            "es": "Spanish"
        }
        embed = Embed(title="Please wait!", description="Your text is being translated...", colour=0xFFC0CB, timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
        msg = await ctx.send(embed=embed)
        embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
        for target in targets.keys():
            data = {
                'q': text,
                'source': 'auto',
                'target': target
            }
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata['translatedText']
            embed.add_field(name=f"{targets[target]}:", value=f"`{output}`", inline=False)
        await msg.edit(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("translate")

def setup(bot):
    bot.add_cog(Translate(bot))