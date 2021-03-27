from glob import glob
from discord.ext.commands import Bot as BotBase
from discord import Intents
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown
from discord.errors import HTTPException, Forbidden
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from datetime import datetime
import os

PREFIX = "+"
OWNER_IDS = [565126636115197954]
COGS = [path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()
        self.cogs_ready = Ready()
        super().__init__(
            command_prefix = PREFIX,
            owner_ids = OWNER_IDS,
            intents = Intents.all()
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")
        print("Setup Complete")

    def run(self):
        print("Running Setup...")
        self.setup()
        self.TOKEN = os.environ['BOT_TOKEN']
        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot Connected")

    async def on_disconnect(self):
        print("Bot Disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            embed = Embed(title="OOPS", description="Something went wrong", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await args[0].send(embed=embed)
        else:
            embed = Embed(title="OOPS", description="An error occured", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await args[0].send(embed=embed)
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif isinstance(exc, BadArgument):
            pass
        elif isinstance(exc, MissingRequiredArgument):
            embed = Embed(title="Error!!!", description="One or more required arguments are missing", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await ctx.send(embed=embed)
        elif isinstance(exc, CommandOnCooldown):
            embed = Embed(title="Error!!!", description=f"That command is on {str(exc.cooldown.type).split('.')[-1]} cooldown. Try once more in {exc.retry_after:,.2f} seconds", colour=0xFFC0CB, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
            await ctx.send(embed=embed)
        elif hasattr(exc, "original"):
            if isinstance(exc.original, HTTPException):
                embed = Embed(title="Error!!!", description="Unable to send message", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                await ctx.send(embed=embed)
            elif isinstance(exc.original, Forbidden):
                embed = Embed(title="Error!!!", description="I do not have permission to do that", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                await ctx.send(embed=embed)
            else:
                raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            while not self.cogs_ready.all_ready():
                await sleep(0.1)
            self.ready = True
            print("Bot Ready")
            meta = self.get_cog("Meta")
            await meta.set()

        else:
            print("Bot Reconnected")

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)
        if ctx.command is not None and ctx.guild is not None:
            if self.ready:
                await self.invoke(ctx)
            else:
                embed = Embed(title="Error!!!", description="Not yet ready. Try again after a few seconds", colour=0xFFC0CB, timestamp=datetime.utcnow())
                embed.set_thumbnail(url="https://i.imgur.com/ayhcIkj.gif")
                await ctx.send(embed=embed)
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()