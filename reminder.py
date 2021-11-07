import discord
from discord.ext import commands
import asyncio
import datetime

class Remindcommand(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command()
    async def reminder(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
 
            return val * time_dict[unit]


        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send("You didn't answer the time correctly")
            return

        if converted_time == -2:
            await ctx.send("The time must be an integer")   
            return

        embed = discord.Embed(title=f"Reminder",description=f"`{ctx.author}` your reminder for `{task}` has started for `{time}`!",color = 0x36393E)
        embed.set_footer(text="Reminder")

        await ctx.send(embed=embed)

        await asyncio.sleep(converted_time)
        embed2 = discord.Embed(title=f"Reminder",description=f"`{ctx.author}` your reminder for `{task}` has finished for `{time}`!",color = 0x36393E)
        embed2.set_footer(text="Reminder")

        msg = await ctx.reply(embed=embed)
        await msg.edit(embed=embed2)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog ready!')

def setup(bot):
    bot.add_cog(Remindcommand(bot))