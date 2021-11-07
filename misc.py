from __future__ import print_function
import discord
from asyncio import tasks
from discord import user
from discord import role
from discord import channel
from discord import embeds
from discord import player
from discord.audit_logs import _transform_explicit_content_filter
from discord.errors import ClientException
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from copy import deepcopy
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from asyncio import sleep as s
from io import BytesIO
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from asyncio.tasks import Task, wait
from datetime import datetime
from discord.ext import menus
from discord.ext import menus
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
from random import choice
import aiofiles
import math
from discord.ext.commands import Cog
import aiosqlite
import DiscordEconomy
from PIL import Image,ImageFilter
from io import BytesIO
import requests
import googletrans

import psutil

class Fun2(commands.Cog):
    """Admin-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help='Tells User Info.')
    async def userinfo(self,ctx, user : discord.Member):
       guild = ctx.guild
       if user is None:
          user = ctx.author

       role_string = ' '.join([r.mention for r in user.roles][1:])
       date_format = "%a, %d %b %Y %I:%M %p"
       embed=discord.Embed(title="Information", description= 'User information.', colour=0x36393E, timestamp = datetime.utcnow())
       embed.set_thumbnail(url=user.avatar_url)
       embed.add_field(name="Registered Date", value=user.created_at.strftime(date_format))
       embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
       embed.add_field(name="Username", value=user.name, inline=True)
       embed.add_field(name="Nickname", value=user.nick, inline=True)
       embed.add_field(name="User ID", value=user.id, inline=True)
       embed.add_field(name="Status", value=user.status, inline=True)
       members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
       embed.add_field(name="Join position", value=f"{str(members.index(user)+1)}/{guild.member_count}")
       embed.add_field(name="Top role", value=user.top_role.name, inline=True)
       embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
       perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
       embed.add_field(name="Permissions", value=perm_string, inline=False)
       await ctx.send(embed=embed)

    @commands.command()
    async def hack(self,message,member: discord.Member):
      me544 = "Nokia","IOS","MacOS","Linus","Windows"
      ctx = message
      meiscoolio="https://cdn.upload.systems/uploads/6J8nBaFS.png"
      message = await message.send(f"Hacking {member} now.")
      await message.edit(content="Hacking is at 1%!")
      await asyncio.sleep(2)
      await message.edit(content="Hacking is at 2%!")
      await message.edit(content="Hacking is at 3%!")
      await message.edit(content="Hacking is at 4%!")
      await message.edit(content="Hacking is at 5%!")
      await message.edit(content="Hacking is at 6%!")
      await message.edit(content="Hacking is at 7%!")
      await message.edit(content="Hacking is at 8%!")
      await message.edit(content="Hacking is at 9%!")
      await message.edit(content="Hacking is at 10%!")
      await message.edit(content="Hacking is at 11%!")
      await message.edit(content="Hacking is at 12%!")
      await message.edit(content="Hacking is at 13%!")
      await message.edit(content="Hacking is at 14%!")
      await message.edit(content="Hacking is at 15%!")
      await message.edit(content="Hacking is at 16%!")
      await message.edit(content="Hacking is at 17%!")
      await message.edit(content="Hacking is at 18%!")
      await message.edit(content="Hacking is at 19%!")
      await message.edit(content="Hacking is at 20%!")
      await message.edit(content="Hacking is at 21%!")
      await message.edit(content="Hacking is at 22%!")
      await message.edit(content="Hacking is at 23%!")
      await message.edit(content="Hacking is at 24%!")
      await message.edit(content="Hacking is at 25%!")
      await message.edit(content="Hacking is at 26%!")
      await message.edit(content="Hacking is at 27%!")
      await message.edit(content="Hacking is at 28%!")
      await message.edit(content="Hacking is at 29%!")
      await message.edit(content="Hacking is at 30%!")
      await message.edit(content="Hacking is at 31%!")
      await message.edit(content="Hacking is at 32%!")
      await message.edit(content="Hacking is at 33%!")
      await message.edit(content="Hacking is at 34%!")
      await message.edit(content="Hacking is at 35%!")
      await message.edit(content="Hacking is at 36%!")
      await message.edit(content="Hacking is at 37%!")
      await message.edit(content="Hacking is at 38%!")
      await message.edit(content="Hacking is at 39%!")
      await message.edit(content="Hacking is at 40%!")
      await message.edit(content="Hacking is at 41%!")
      await message.edit(content="Hacking is at 42%!")
      await message.edit(content="Hacking is at 43%!")
      await message.edit(content="Hacking is at 44%!")
      await message.edit(content="Hacking is at 45%!")
      await message.edit(content="Hacking is at 46%!")
      await message.edit(content="Hacking is at 47%!")
      await message.edit(content="Hacking is at 48%!")
      await message.edit(content="Hacking is at 49%!")
      await message.edit(content="Hacking is at 50%! (Wait 15 seconds as I don't want to abuse the Discord API.)")
      await asyncio.sleep(15)
      await message.edit(content="Hacking is at 51%!")
      await message.edit(content="Hacking is at 52%!")
      await message.edit(content="Hacking is at 53%!")
      await message.edit(content="Hacking is at 54%!")
      await message.edit(content="Hacking is at 55%!")
      await message.edit(content="Hacking is at 56%!")
      await message.edit(content="Hacking is at 57%!")
      await message.edit(content="Hacking is at 58%!")
      await message.edit(content="Hacking is at 59%!")
      await message.edit(content="Hacking is at 60%!")
      await message.edit(content="Hacking is at 61%!")
      await message.edit(content="Hacking is at 62%!")
      await message.edit(content="Hacking is at 63%!")
      await message.edit(content="Hacking is at 64%!")
      await message.edit(content="Hacking is at 65%!")
      await message.edit(content="Hacking is at 66%!")
      await message.edit(content="Hacking is at 67%!")
      await message.edit(content="Hacking is at 68%!")
      await message.edit(content="Hacking is at 69%!")
      await message.edit(content="Hacking is at 70%!")
      await message.edit(content="Hacking is at 71%!")
      await message.edit(content="Hacking is at 72%!")
      await message.edit(content="Hacking is at 73%!")
      await message.edit(content="Hacking is at 74%!")
      await message.edit(content="Hacking is at 75%!")
      await message.edit(content="Hacking is at 76%!")
      await message.edit(content="Hacking is at 77%!")
      await message.edit(content="Hacking is at 78%!")
      await message.edit(content="Hacking is at 79%!")
      await message.edit(content="Hacking is at 80%!")
      await message.edit(content="Hacking is at 81%!")
      await message.edit(content="Hacking is at 82%!")
      await message.edit(content="Hacking is at 83%!")
      await message.edit(content="Hacking is at 84%!")
      await message.edit(content="Hacking is at 85%!")
      await message.edit(content="Hacking is at 86%!")
      await message.edit(content="Hacking is at 87%!")
      await message.edit(content="Hacking is at 88%!")
      await message.edit(content="Hacking is at 89%!")
      await message.edit(content="Hacking is at 90%!")
      await message.edit(content="Hacking is at 91%!")
      await message.edit(content="Hacking is at 92%!")
      await message.edit(content="Hacking is at 93%!")
      await message.edit(content="Hacking is at 94%!")
      await message.edit(content="Hacking is at 95%!")
      await message.edit(content="Hacking is at 96%!")
      await message.edit(content="Hacking is at 98%!")
      await message.edit(content="Hacking is at 98%!")
      await message.edit(content="Hacking is at 99%!")
      await asyncio.sleep(5)
      await message.edit(content="Hacking is at 100%, woohoo it's done!")
      await asyncio.sleep(1)
      me =  (random.randint(1, 255))
      me2 = (random.randint(1, 255))
      me3 = (random.randint(1, 255))
      me4 = (random.randint(1, 255))
      me5 = (random.randint(1,500))
      me6 = (random.randint(0,100))
      me7 = "New York,America","Paris,France","Tokyo,Japan","Cardiff,Wales","London,England","Florida,America","Homeless.","Mumbai,India","Shanghai,China","Bejing,China","Moscow,Russia","Seoul,South Korea","Wuhan,China","Madrid,Spain"
      me8 = "Male","Female","N/A"
      me9 = "Male","Female","Loser"
      me10 = (random.randint(1,100))
      me11 = "Hooker","Actor","Teacher","Slut","YouTuber","Streamer","Software Engineer","Architecture","Nurse","Doctor","Surgeon","Jobless","Dentist","Tylo #1 Supporter","It Manager","Manager","CEO","Chairman","Director","IT Lead"
      me12 = "99%","100%"
      me13 = (random.randint(1,500000))
      me14 = "Pepe Bank","No Bank"
      me15 = (random.randint(1,200))


      embed = discord.Embed(title=f"{member} information.",description="<:Tylo1:893183296463339520> 200% Accuracy by the top hacker known as Tylo best hacker out of every pepe! ",color = 0x36393E)
      embed.set_thumbnail(url=meiscoolio)
      embed.add_field(name="IP Address",value=f"{me}.{me2}.{me3}.{me4}",inline=True)
      embed.add_field(name="Address",value=(random.choice(me7)),inline=True)
      embed.add_field(name="Platform",value=(random.choice(me544)),inline=True)
      embed.add_field(name="Friends",value=me5,inline=True)
      embed.add_field(name="Popular",value=f"{me6}%",inline=True)
      embed.add_field(name="Age",value=me10,inline=True)
      embed.add_field(name="Gender",value=(random.choice(me9)),inline=True)
      embed.add_field(name="Relationship",value=(random.choice(me8)),inline=True)
      embed.add_field(name="Job",value=(random.choice(me11)),inline=True)
      embed.add_field(name="Money",value=F"£{me13}",inline=True)
      embed.add_field(name="Bank",value=(random.choice(me14)),inline=True)
      embed.add_field(name="Brain Cells",value=me15,inline=True)
      embed.add_field(name="Supporter",value=f"{member} is a {(random.choice(me12))} supporter! \n \n I also support Tylo 100%!",inline=True)


      await ctx.send(embed=embed)

    @commands.command(aliases=['tr'])
    async def translate(self,ctx, lang_to, *args):
        member = ctx.author
        """
        Translates the given text to the language `lang_to`.
        The language translated from is automatically detected.
        """

        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            raise commands.BadArgument("Invalid language to translate text to")

        text = ' '.join(args)
        translator = googletrans.Translator()
        text_translated = translator.translate(text, dest=lang_to).text
        embed = discord.Embed(title="Translation",description = f"Translation to {lang_to}! \n ```{args}``` \n ```{text_translated}```",color= 0x36393E,timestamp = datetime.utcnow())
        embed.set_footer(text=f"Invoked by {member.name} ")

        await ctx.send(embed=embed)

    @commands.command(aliases=["mcount","countm"])
    async def membercount(self,ctx):
      guild = ctx.guild
      embed = discord.Embed(title="Member",description=f"The member count is `{guild.member_count}`",color = 0x36393E,timestamp = datetime.utcnow())
      await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self,ctx,member: discord.Member):
       embed = discord.Embed(title="Avatar",color = (0xF85252), timestamp = datetime.utcnow())
       embed.set_image(url=member.avatar_url)
       await ctx.send(embed=embed)

    @commands.command(name='latency', help='This command returns the latency')
    async def latency(self,ctx):
        embed = discord.Embed(title='Pong', description = f'Latency = {round(self.bot.latency * 100)}ms',color = 0x36393E,timestamp=datetime.utcnow())
        await ctx.send(embed=embed)

    @commands.command(help='Time.')
    async def time(self,ctx):
       embed = discord.Embed(title = "`Time`",timestamp = datetime.utcnow())
       await ctx.send(embed=embed)
    
    @commands.command(help='Howgay.')
    async def howgay(self,ctx, member : discord.Member):
       embed = discord.Embed(title = "```Gay Levels```", description = f'```{member} is {(random.randint(1, 101))}% gay.```', color = 0x36393E, timestamp = datetime.utcnow())
       await ctx.send(embed = embed)

    @commands.command(pass_context=True, help='Random number out of 1-100.')
    async def randomnumber(self,ctx):
      embed = discord.Embed(title = '```Random number```', description = f'```{(random.randint(1, 101))}```', color = 0x36393E, timestamp = datetime.utcnow())
      await ctx.send(embed = embed)

    @commands.command(pass_context=True, help='Random number out of 1-100.')
    async def howcool(self,ctx, user: discord.Member):
      embed = discord.Embed(title = '```How cool```', description = f'```{user} is {(random.randint(1, 101))}% cool.```', color = 0x36393E, timestamp = datetime.utcnow())
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.send(embed = embed)

    @commands.command()
    async def maths(self,ctx,a:int,b:int):
      if a is None:
        await ctx.send("Example is .maths 5 12")
      if b is None:
        await ctx.send("Example is .maths 5 12")
      await ctx.send("Do you want plus,times,minus and divide?")
      def check(message):
                return message.author == ctx.author
      what = await self.bot.wait_for("message",timeout=30,check=check)
      if "plus" in what.content:
        embed = discord.Embed(title="Answer",description=f"{a}+{b}={a+b}",color = 0x36393E)
        await ctx.send(embed=embed)
      if "minus" in what.content:
        embed = discord.Embed(title="Answer",description=f"{a}-{b}={a-b}",color=0x36393E)
        await ctx.send(embed=embed)
      if "times" in what.content:
        embed = discord.Embed(title="Answer",description=f"{a}x{b}={a*b}",color=0x36393E)
        await ctx.send(embed=embed)
      if "divide" in what.content:
        embed = discord.Embed(title="Answer",description=f"{a}÷{b}={a/b}",color = 0x36393E)
        await ctx.send(embed)
    @commands.command()
    async def userid(self,ctx, member: discord.Member):
      embed = discord.Embed(title=f"{member} ID",description=member.id)
      await ctx.send(embed=embed)
    @commands.command()
    async def msgchange(self,ctx):
       msg = await ctx.send("what would you like to send?")
       def check(message):
                return message.author == ctx.author
       what = await self.bot.wait_for('message', timeout=30,check=check)
       await msg.edit(content=what.content)

def setup(bot):
    bot.add_cog(Fun2(bot))