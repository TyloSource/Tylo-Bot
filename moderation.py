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

class Moderation(commands.Cog):
    "<:soccer:899621880120639509> | Fun commands like meme, hug and more" 
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members = True)
    async def unban(self,ctx,member_id):
      channel = self.client.get_channel(882327599131541514)
      if member_id == None:
        await ctx.send("You need to mention a ID!")
      await ctx.guild.unban(discord.Object(id=member_id))
      embed = discord.Embed(title="Unban",description=f"{member_id} has been unbanned\n from {ctx.guild}!",color = 0x36393E)
      embed.set_footer(text=f"Invoked by {ctx.author}!")
      await ctx.send(f"{member_id} has been unbanned!")
      await channel.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def role(self,ctx,member: discord.Member,*, role:discord.Role=None):
       user = ctx.message.author
       embed = discord.Embed(title=f"Role added.", description=f"Admin {user} has given {member} the role {role}!",color = 0x36393E)
       embed.set_thumbnail(url=member.avatar_url)
       embed.add_field(name="User", value=user.name, inline=True)
       embed.add_field(name="Role Given", value=f"{role}", inline=True)
       if member == None:
        await ctx.send('Please mention a member.')
       if role == None:
        await ctx.send("Mention a role.")
       await member.add_roles(role)
       await ctx.send("User has been roled.")
       channel = self.client.get_channel(882327599131541514)
       await channel.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def unrole(self,ctx,member: discord.Member,*, role:discord.Role=None):
       user = ctx.message.author
       embed = discord.Embed(title=f"Role removed.", description=f"Admin {user} has unroled {member} from the role {role}!",color = 0x36393E)
       embed.set_thumbnail(url=member.avatar_url)
       embed.add_field(name="User", value=user.name, inline=True)
       embed.add_field(name="Role removed", value=f"{role}", inline=True)
       if member == None:
         await ctx.send('Please mention a member.')
       if role == None:
         await ctx.send("Mention a role.")
       await member.remove_roles(role)
       await ctx.send("User has been unroled.")
       channel = self.client.get_channel(882327599131541514)
       await channel.send(embed=embed)
    @commands.command(name='ban', help='Bans people.')
    @commands.has_permissions(kick_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
      user = ctx.message.author
      embed = discord.Embed(title = "```Banned```", description = f'```{member} you have been banned from GCC {reason}.```',color = 0x36393E, timestamp = datetime.utcnow())
      await member.send(embed=embed)
      await member.ban(reason=reason)
      channels = self.client.get_channel(882327599131541514)

      await ctx.send(f'User {member} has been banned.')
      await channels.send(f'User {member} has been banned {reason} by {user.mention}.')
    @commands.command(help='Kicks people out the server.')
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
      user = ctx.message.author
      embed = discord.Embed(title = "```Kicked```", description = f'```@{member} you have been kicked from GCC for {reason}.```',color = 0x36393E, timestamp = datetime.utcnow())
      await member.send(embed=embed)
      await member.kick(reason=reason)

      channels = self.client.get_channel(882327599131541514)

      await ctx.send(f'User {member} has been kicked for.')
      await channels.send(f'User {member} has been kicked {reason} by {user.mention}.')
    @commands.command(help='Mute command.')
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, user: discord.Member, *, msg):
      if get(ctx.guild.roles, name="Muted"):
          ifmute = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
          if ifmute in user.roles:
            await ctx.send(f"{user.mention} is already muted!")
          else:

              if msg == "1m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 1 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(60)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "2m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 2 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(120)
                if ifmute in user.roles:
                    await ctx.send(f'{user.mention} has been automatically unmuted.')
                    await user.remove_roles(thing)

              if msg == "3m":
                ifyes=discord.Embed(title="User Muted", description=f'{user.mention} has been muted for 3 minute.', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(180)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)
                

              if msg == "4m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 4 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(240)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "5m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 5 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(300)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "6m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 6 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(360)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "7m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 7 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(420)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "8m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 8 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(480)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "9m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 9 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(540)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "10m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 10 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "11m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 11 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(660)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "12m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 12 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(720)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "13m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 13 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(780)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "14m":
                ifyes=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 14 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyes)
                await asyncio.sleep(840)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "15m":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 15 minute.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(900)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "1h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 1 hour.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(3600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "2h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 2 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(7200)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)
            
              if msg == "3h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 3 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(10800)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)


              if msg == "4h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 4 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(14400)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "5h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 5 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(18000)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "6h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 6 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(21600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "7h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 7 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(25200)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "8h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 8 hours.```', color=0x0067b3)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(28800)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "9h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 9 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(32400)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "10h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 10 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(36000)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "11h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 11 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(39600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

            
              if msg == "12h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 12 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(43200)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "13h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 13 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(46800)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "14h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 14 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(50400)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "15h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 15 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(54000)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "16h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 16 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(57600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "17h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 1 minute.```', color=0x0067b3)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(61200)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "18h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 18 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(64800)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "19h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 19 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(68400)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "20h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 20 hour.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(72000)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "21h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 21 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(75600)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "22h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 22 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(79200)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "23h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 23 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(82800)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "24h":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 24 hours.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(86400)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

              if msg == "1y":
                ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been muted for 1 year.```', color=0x36393E)
                rolenam = 'Muted'
                thing = discord.utils.get(ctx.guild.roles, name=rolenam)
                await user.add_roles(thing)
                await ctx.send(embed=ifyess)
                await asyncio.sleep(31536000)
                if ifmute in user.roles:
                    await ctx.send(f"{user.mention} has been automatically unmuted.")
                    await user.remove_roles(thing)

      else:
        isno=discord.Embed(title="Role Created", description=f'Muted role has been created, please edit its permission and rerun the command again.', color=0x36393E)
        await ctx.send(embed=isno)
        await ctx.guild.create_role(name="Muted", colour=discord.Colour(0x0067b3))
    @commands.command(help='Unmute command.')
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, user: discord.Member,):
        if get(ctx.guild.roles, name="Muted"):
           ifmute = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
           if ifmute in user.roles:
              ifyess=discord.Embed(title="```User Muted```", description=f'```{user.mention} has been unmuted.```', color=0x36393E, timestamp = datetime.utcnow())
              rolenam = 'Muted'
              thing = discord.utils.get(ctx.guild.roles, name=rolenam)
              await user.remove_roles(thing)
              await ctx.send(embed=ifyess)
           else:
              await ctx.send("User is not muted.")


def setup(bot):
    bot.add_cog(Moderation(bot))