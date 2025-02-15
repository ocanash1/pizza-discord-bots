import discord
import logging
from discord.ext import commands
from constants import AVATAR_CSV_FILE
from utils import get_member_data, create_csv_file

logger = logging.getLogger(__name__)


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mc"])
    async def member_count(self, ctx):
        logger.info("member count: {0}".format(ctx.guild.member_count))
        await ctx.channel.send("Member Count: {0}".format(ctx.guild.member_count))

    @commands.command(aliases=["csv"])
    async def download_csv(self, ctx):
        logger.info("generating csv file '{0}'".format(AVATAR_CSV_FILE))
        csv_data = []
        csv_cols = ["id", "name", "nickname",  "created_at",
                    "joined_at", "roles", "top_role", "avatar_url"]
        csv_data.append(csv_cols)

        members = self.bot.guilds[0].members
        for mem in members:
            row = get_member_data(mem)
            csv_data.append(row)

        create_csv_file(csv_data, AVATAR_CSV_FILE)
        await ctx.send(file=discord.File(AVATAR_CSV_FILE))


def setup(bot):
    bot.add_cog(Commands(bot))
