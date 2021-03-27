from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Activity, ActivityType
from apscheduler.triggers.cron import CronTrigger

class Meta(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._message = "listening +help | Translating for {users:,} users in {guilds:,} servers"
        bot.scheduler.add_job(self.set, CronTrigger(second=0))

    @property
    def message(self):
        return self._message.format(users=len(self.bot.users), guilds=len(self.bot.guilds))

    async def set(self):
        _type, _name = self.message.split(" ", maxsplit=1)
        await self.bot.change_presence(activity=Activity(name=_name, type=ActivityType.listening))

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("meta")

def setup(bot):
    bot.add_cog(Meta(bot))