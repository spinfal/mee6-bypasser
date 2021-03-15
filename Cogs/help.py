import discord

from discord.ext import commands

# ------------------------ COGS ------------------------ #  

class HelpCog(commands.Cog, name="help command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'help')
    async def help (self, ctx):
        embed = discord.Embed(title=f"__**Help**__", description="OwO", color=0xdeaa0c)
        embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')
        embed.add_field(name="__COMMANDS :__", value=f"**{self.bot.command_prefix}add <Level number> <Role ID> :** Add a role reward.\n**{self.bot.command_prefix}remove <Level number> :** Remove a role reward.\n**{self.bot.command_prefix}rolerewards :** Display the list of role rewards.\n**{self.bot.command_prefix}removepreviousrewards <true/false> :** Change setting.\n", inline=False)
        embed.set_footer(text="Mee6 is stupid")
        await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(HelpCog(bot))