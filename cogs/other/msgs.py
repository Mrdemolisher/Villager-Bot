from discord.ext import commands
import discord
from random import choice

class Msgs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.get_cog("Database")
        self.g = self.bot.get_cog("Global")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        self.g.msg_count += 1
        if "emerald" in message.content:
            if not message.guild == None:
                if self.db.getDoReplies(message.guild.id):
                    await message.send(choice(["hrmm", "hmm", "hrmmm", "hrghhmmm", "hrhhmmmmmmmmm", "hrmmmmmm", "hrmmmmmmmmmm", "hrmmmmm"]))
            else:
                await message.send(choice(["hrmm", "hmm", "hrmmm", "hrghhmmm", "hrhhmmmmmmmmm", "hrmmmmmm", "hrmmmmmmmmmm", "hrmmmmm"]))
                
def setup(bot):
    bot.add_cog(Msgs(bot))