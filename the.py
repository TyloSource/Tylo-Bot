
from discord.ext import commands
import discord
import aiohttp
import random
import datetime


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="screenshot",aliases=["ss"])
    async def screenshot(self, ctx, *, Website):
        if not Website.lower().startswith("https://"):
            e=discord.Embed(
                description=f"{self.bot.icons['cross']} You need to screenshot a website!",color = 0x36393E
            )
            await ctx.reply(
                embed=e,
                mention_author=False
            )
            return
        Url = f"https://api.popcat.xyz/screenshot?url={Website}"
        e=discord.Embed(
            description=f"""
`URL:` {Website}
`Invoker:` {ctx.author.mention}
            """,color = 0x36393E
        )
        e.set_image(url=Url)
        e.set_footer(text=f"Powered by api.popcat.xyz")
        await ctx.reply(
            embed=e,
            mention_author=False
        )


def setup(bot):
    bot.add_cog(Fun(bot))