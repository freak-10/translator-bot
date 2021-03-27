from discord import Embed
from discord.ext.commands import Cog, command
from datetime import datetime

class About(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="about")
    async def tell_about(self, ctx):
        embed = Embed(title="About the creator", description="freak#1531 is my creator's discord ID", colour=0xFFC0CB, timestamp=datetime.utcnow())
        embed.set_image(url="https://i.imgur.com/ayhcIkj.gif")
        embed.add_field(name="Why I made the bot?", value="This bot was made as a project for my college's Hackoonamatata Hackathon. I have always been interested in discord bots and how I could make them. This was my first attempt at making a functional one.", inline=False)
        embed.add_field(name="How can I improve it?", value="I am using free versions of the APIs and there are limits to their usage. This makes the bot a bit worse than what it could be. How I would improve is try to make my own APIs to get rid of this issue. I will also try to add more commands in the future.", inline=False)
        embed.add_field(name="Github Repository", value="[Star this if you like the bot](https://github.com/freak-10/translator-bot)")
        embed.add_field(name="My GitHub", value="[My GitHub](https://github.com/freak-10)", inline=False)
        embed.add_field(name="My LinkedIn", value="[My LinkedIn](https://www.linkedin.com/in/sumanth-kotikalapudi-396b60207/)", inline=False)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("about")

def setup(bot):
    bot.add_cog(About(bot))