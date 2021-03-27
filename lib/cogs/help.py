from typing import Optional
from discord import Embed
from discord.ext.commands import Cog, command
from datetime import datetime

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @command(name="help")
    async def help_command(self, ctx, cmd: Optional[str]):
        if cmd is None:
            embed = Embed(title="HELP", description="Welcome to Translator Bot's help dialog", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_image(url="https://i.imgur.com/ayhcIkj.gif")
            embed.add_field(name="What is Translator Bot?", value="It's a bot designed to translate text from one language to another or perform text spinning on given text. Other than that, it also has a few commands to convert provided input into funny text such as pirate talk, shakespearan english, etc.")
            embed.add_field(name="How does it work?", value="It makes use of multiple APIs to provide the result. The free versions of these APIs provide limited number of results hence functionality of the bot is a bit reduced. One of my objectives is to create my own APIs to overcome this.", inline=False)
            embed.add_field(name="Prefix", value="+", inline=False)
            embed.add_field(name="Commands", value="`translate` `translateto` `spin` `shakespeare` `yoda` `pirate` `morse` `minion` `about`", inline=False)
            embed.add_field(name="Get more info about each command", value="Use +help <command>", inline=False)
            await ctx.send(embed=embed)
        else:
            if cmd == "translate":
                embed = Embed(title="+translate", description="Auto-detects input language (if available) and translates to all available languages", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+translate <text>", inline=False)
                embed.add_field(name="Aliases", value="+tr", inline=False)
                embed.add_field(name="Cooldown", value="1 command every 1o secs for the whole server", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "translateto":
                embed = Embed(title="+translateto", description="Auto-detects input language (if available) and translates to chosen language", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+translateto <target-language> <text>", inline=False)
                embed.add_field(name="Target Languages", value="english, arabic, chinese, french, german, hindi, irish, italian, japanese, korean, portuguese, russian, spanish", inline=False)
                embed.add_field(name="Aliases", value="+trto", inline=False)
                embed.add_field(name="Cooldown", value="1 command every 5 seconds for the whole server", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "spin":
                embed = Embed(title="+spin", description="Performs text spinning on English input", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+spin <text>", inline=False)
                embed.add_field(name="Aliases", value="+sp", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "shakespeare":
                embed = Embed(title="+shakespeare", description="Converts English input to Shakespearan text", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+shakespeare <text>", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "yoda":
                embed = Embed(title="+yoda", description="Converts English input to how Yoda speaks", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+yoda <text>", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "pirate":
                embed = Embed(title="+pirate", description="Converts English input to pirate talk", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+pirate <text>", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "morse":
                embed = Embed(title="+morse", description="Converts English input to morse code", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+morse <text>", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "minion":
                embed = Embed(title="+minion", description="Changes input to resemble how the minions talk in Despicable Me", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+minion <text>", inline=False)
                embed.add_field(name="Cooldown", value="5 commands every hour for all the users globally", inline=False)
                await ctx.send(embed=embed)
            elif cmd == "about":
                embed = Embed(title="+about", description="Tells about Translator Bot's creator", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                embed.add_field(name="Syntax", value="+about", inline=False)
                await ctx.send(embed=embed)
            else:
                embed = Embed(title="Error!!!", description="The command you are looking for is not available", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("help")

def setup(bot):
    bot.add_cog(Help(bot))