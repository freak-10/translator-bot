from discord.ext.commands import (Cog, BucketType, command, cooldown)
import requests
from discord import Embed
from datetime import datetime

class Funtranslate(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="yoda")
    @cooldown(5, 3600, BucketType.default)
    async def yoda_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/yoda.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="Being converted to yoda, your text is...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Yoda Text:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @command(name="pirate")
    @cooldown(5, 3600, BucketType.default)
    async def pirate_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/pirate.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="Let's blow to the sky some ships while yer text be bein' converted...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Pirate Text:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @command(name="shakespeare")
    @cooldown(5, 3600, BucketType.default)
    async def shakespeare_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/shakespeare.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="Thy text is travelling backeth to the elizabethan era...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Shakespeare Text:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @command(name="morse")
    @cooldown(5, 3600, BucketType.default)
    async def morse_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/morse.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="-... . .. -. --. / -- --- .-. ... . / -.-. --- -.. . -.. .-.-.- .-.-.- .-.-.-", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Morse Code:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @command(name="minion")
    @cooldown(5, 3600, BucketType.default)
    async def minion_text(self, ctx, *, text: str):
        try:
            url = "https://api.funtranslations.com/translate/minion.json"
            data = {
                'text': text
            }
            embed = Embed(title="Please wait!", description="Eat a bananaaaaa while you wait...", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            msg = await ctx.send(embed=embed)
            outputdata = (requests.post(url, data=data)).json()
            output = outputdata["contents"]["translated"]
            embed = Embed(title="Your Text:", description=f"```{text}```", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="Minion Text:", value=f"```{output}```", inline=False)
            await msg.edit(embed=embed)
        except:
            embed = Embed(title="Error!!!", description=f"{outputdata['error']['message']}", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await msg.edit(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("funtranslate")

def setup(bot):
    bot.add_cog(Funtranslate(bot))
