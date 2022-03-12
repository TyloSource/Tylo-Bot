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

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'),intents=discord.Intents.all(),case_insensitive=True)

client.ses = aiohttp.ClientSession() 

economy = DiscordEconomy.Economy()

client.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}


async def is_registered(ctx):
    r = await economy.is_registered(ctx.message.author.id)
    return r

is_registered = commands.check(is_registered)

@client.event
async def on_ready():
    servers = list(client.guilds)
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"Watching {str(len(servers))} servers!"))
    client.load_extension('jishaku')
    client.load_extension("image")
    client.load_extension("reminder")
    client.load_extension("the")
    client.load_extension("owner")
    client.load_extension("music")
    client.load_extension("games")
    client.load_extension("moderation")
    client.load_extension("misc")
    for guild in client.guilds:
        client.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    print('no errors found, starting bot...')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Error",description=f":error: {error}",color = 0x36393E ,timestamp = datetime.utcnow())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.NSFWChannelRequired):
        embed = discord.Embed(title="Error",description=f":error: {error}",color = 0x36393E,timestamp = datetime.utcnow())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) == 0 and int(m) == 0:
            embed = discord.Embed(title=f"Cooldown",description=f"Chill wait {int(s)} seconds\nThen do the command again",color = 0x36393E,timestamp = datetime.utcnow())
            await ctx.send(embed=embed)
        elif int(h) == 0 and int(m) != 0:
            embed = discord.Embed(title=f"Cooldown",description=f"Chill wait {int(m)}minutes and {int(s)} seconds\nThen do the command again",color = 0x36393E,timestamp = datetime.utcnow())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Cooldown",description=f"Chill wait {int(h)}hours, {int(m)}minutes and {int(s)} seconds\nThen do the command again",color = 0x36393E,timestamp = datetime.utcnow())
            await ctx.send(embed=embed)

@client.command(help='Says if the bot is online.')
async def status(ctx):
   embed = discord.Embed(title = "```Status```", description = '```The bot is online and working perfectly.```', color = (0x36393E ), timestamp = datetime.utcnow())
   await ctx.send(embed = embed)

@client.command(help='What to do while bored.')
async def bored(ctx):
   embed = discord.Embed(
       title = "```What to do while bored?```", 
       description = '```Play a game.\n Go on the internet.\n Go for a walk.\n Talk with a friend.\n \n Have fun.\n Take a bath. \n Learn a new skill. \n Play with previous toys. \n Plan to rule the world. \n Plan how to survive a world incident. \n Build a fort. \n Invite friends over. \n Make a song. \n Do something you used to enjoy. \n Watch YouTube. \n Plan how to survive a nuclear attack. \n Plan on how to murder someone you despise. \n Make a Discord Server. \n Listen to Music. \n By the way this was sponsored by NordVPN use the code Help for 20% off\n. ```' 
       , color = (0xF85252), timestamp = datetime.utcnow())
   await ctx.send(embed=embed)



 
@client.command(help='Suggetions.')
async def suggest(ctx, *, msg):
  embed = discord.Embed(title = "```Suggestion```", description = f'```{msg} \n \nby {ctx.author.mention}.```', color = 0x36393E, timestamp = datetime.utcnow())
  channel = client.get_channel(884496329231978596)
  msg = await channel.send(embed=embed)
  await msg.add_reaction("✅")
  await msg.add_reaction("↔️")
  await msg.add_reaction("❎")

@client.command(help='Basically an announcement with the bot.')
@has_permissions(manage_messages=True)
async def announce(ctx, *, msg):
  embed = discord.Embed(title = "```Announcement```", description = f'```Author is {ctx.author.mention} mentioned: {msg}```', color = 0x36393E , timestamp = datetime.utcnow())
  channel = client.get_channel(883063220091371571)
  pizza = '@everyone'
  await channel.send(embed=embed)
  await channel.send(pizza)

@client.command(help='Basically an announcement with the bot.')
@has_permissions(manage_messages=True)
async def dm(ctx, member:discord.Member, *, msg):
  user = ctx.message.author
  embed = discord.Embed(title = f'```This DM was from {ctx.message.author} .```', description =f'```{msg}```', color = 0x36393E, timestamp = datetime.utcnow())
  channel = client.get_channel(882327599131541514)
  await channel.send(f'{user} has sent a DM containing to {member} mentioning: {msg}')
  await ctx.send('DM has been sent.')
  await member.send(embed=embed)

@client.command(help='Confession.')
async def confess(ctx,*,message):
  user = ctx.message.author
  embed = discord.Embed(title = "```Anonymous Confession```", description = f'```{message}```', color = 0x36393E, timestamp = datetime.utcnow())
  channel = client.get_channel(885257575480852540)
  channels = client.get_channel(882327599131541514)
  await channel.send(embed=embed)
  await channels.send(f'The user {user} has sent the Anonymous confession ({message})!')
  await ctx.send('The confession has been sent.')


@client.command(name='creator', help='Who made the bot.')
async def Creator(ctx):
  thes = 'The bot was made by Goblin, also thanks to Yulfio for making the mute command.!'
  await asyncio.sleep(1)
  await ctx.send(thes)

#removes the help command so they use cmds.
client.remove_command('help')

@client.command(pass_context=True)
@has_permissions(manage_nicknames=True)
async def name(ctx,user: discord.Member,nick):
    member = ctx.message.author
    embed = discord.Embed(title='Nickname Change', description = f'Nickname has been changed by {member}!',color = 0x36393E)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="From", value=user.name, inline=True)
    embed.add_field(name="To", value=nick, inline=True)
    await user.edit(nick=nick)
    channel = client.get_channel(882327599131541514)
    await ctx.send(f'{member.mention} has changed {user} nickname from {user} to {nick}.')
    await channel.send(embed=embed)



@client.command(pass_context=True)
@has_permissions(manage_roles=True)
async def unverify(ctx, user: discord.Member):
  member = ctx.message.author
  embed = discord.Embed(title = "```Unverify```", description = f'```{user} you have been removed from the role Member.```', color = 0x36393E, timestamp = datetime.utcnow())
  rolenam = 'Member'
  thing = discord.utils.get(ctx.guild.roles, name=rolenam)
  channel = client.get_channel(882327599131541514)
  await channel.send(f'{member} has unverified {user}.')
  await ctx.send(embed=embed)
  await user.remove_roles(thing)

@client.command(pass_context=True)
async def vhelp(ctx):
  embed = discord.Embed(title = "```How do I verify?```", description = '```You verify by saying .verify \n \nExample  \n \n.verify```', color = 0x36393E, timestamp = datetime.utcnow())
  await ctx.send(embed=embed)

bad_words = ["fuck","shit","cunt","retard","slut","slut","ass","asshole","bitch","bastard","cunt","choad","bloodly","bollocks","wanker","pedo","nonce","bugger","bullshit","arsehole","motherfucker","slut","slut","cocksucker","twat","pussy","nigger","nigga","shitter","bloody nonce","fanny","dickhead","knob","prick","pr1ck"]

@client.listen()
@commands.has_role("Member")
async def on_message(message):

    if message.author == client.user:
        return

    user = message.author
    channel = client.get_channel(882327599131541514)
    guild = client.get_guild(881874875155898438)
    rolenam = "Member"
    role = discord.utils.get(guild.roles, name=rolenam)
    embed = discord.Embed(title="Blacklisted word mentioned!", description = f"`{message.content}`", color=0x36393E,timestamp = datetime.utcnow())
    embed.set_footer(text=f'Message was by {user}.')
    guild = client.get_guild(881874875155898438)
    message_split = message.content.split(" ")
    rolenam = "Member"
    role = discord.utils.get(guild.roles, name=rolenam)

    for message_word in message_split:
        for bad_word in bad_words:
            if(bad_word == message_word.lower()):
                if role in user.roles:
                    return
                else:
                   await channel.send(embed=embed)
                   await message.delete()
                   await message.channel.send(f"{user.mention} message has been deleted, detected as a blacklisted word.")
                   channel = client.get_channel(882327599131541514)
                   await channel.send(embed=embed)
    
@client.command(help='Nice quote.')
async def quotes(ctx):
  nice_quotes = 'Positive anything is better than negative nothing.','Miracles happen to those who believe in them.', 'One small positive thought can change your whole day.', 'Keep looking up… that’s the secret of life. ', 'Being positive is a sign of intelligence.', 'If you are positive, you’ll see opportunities instead of obstacles.', 'Once you choose hope, anything’s possible.', 'You can, you should, and if you’re brave enough to start, you will.', 'Small steps motivate. Big steps overwhelm.', 'The first step is you have to say that you can.', 'A problem is a chance for you to do your best.', 'The most important thing is to look ahead.', 'Problems are not stop signs, they are guidelines.', 'A little progress each day adds up to big results.', 'I am thankful to all who said no to me. It is because of them that I’m doing it myself.', 'Try to be a rainbow in someone’s cloud.', 'With the new day comes new strength and new thoughts.', 'Victory is in having done your best. If you’ve done your best, you’ve won.', 'Believe deep down in your heart that you’re destined to do great things.', 'In the end, everything will be okay. If it’s not okay, it’s not yet the end.', 'One person can make a difference, and everyone should try.', 'Mix a little foolishness with your serious plans. It is lovely to be silly at the right moment.', 'One small positive thought can change your whole day.', 'Joy is not in things; it is in us.', 'Optimism is a happiness magnet. If you stay positive, good things and good people will be drawn to you.', 'There isn’t anything that I cannot be or do or have.', 'Wherever you go, no matter what the weather, always bring your own sunshine.', 'Be the light in the dark, be the calm in the storm and be at peace while at war.', 'Arise, awake and stop not till the goal is reached.', 'First say to yourself what you would be; and then do what you have to do.', 'Life has no limitations, except the ones you make.', 'How high you fly is derived from how big you think.', 'Staying positive doesn’t mean you have to be happy all the time. It means that even on the hard days you know better ones are coming.', 'The less you respond to negative people, the more positive your life will become.', 'The question isn’t who’s going to let me; it’s who is going to stop me.', 'Little minds are tamed and subdued by misfortune; but great minds rise above them.', 'There are far, far better things ahead than anything we leave behind.', 'We must embrace pain and burn it as fuel for our journey.', 'Think big thoughts but relish small pleasures.', 'It doesn’t matter how slow you go, as long as you don’t stop.', 'Change your thoughts and you change your world.', 'Choose to be optimistic, it feels better.', 'If you focus narrowly on the problem as you see it, you might well lose hope, but if you look at it from a wider perspective, it’s easier to be more positive.', 'The great majority of men are bundles of beginnings.', 'Even though you’re fed up, you gotta keep your head up.', 'Write it on your heart that every day is the best day in the year.', 'Remember: Every champion was once a contender that refused to give up.', 'Believe you can and you’re halfway there.', 'Believe you can and you’re halfway there.', 'That which doesn’t kill us makes us stronger.', 'Always turn a negative situation into a positive situation.', 'Always turn a negative situation into a positive situation.', 'The positive thinker sees the invisible, feels the intangible, and achieves the impossible.', 'Dwell on the beauty of life. Watch the stars, and see yourself running with them.', 'Negative results are just what I want. They’re just as valuable to me as positive results. I can never find the thing that does the job best until I find the ones that don’t.', 'Light tomorrow with today.', 'The future belongs to those who believe in the beauty of their dreams.', 'If you don’t like something change it. If you can’t change it, change your attitude about it. Don’t complain.', 'Believe that life is worth living and your belief will help create the fact.',
  'All you really need is love, but a little chocolate now and then doesn’t hurt.', 'If opportunity doesn’t knock, build a door.', 'The secret is contained in a three-part formula I learned in the gym: self-confidence, a positive mental attitude, and honest hard work.', 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.', 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.', 'The best is yet to be.', 'There is a sense that things, if you keep positive and optimistic about what can be done, do work out.', 'Optimism is the faith that leads to achievement. Nothing can be done without hope or confidence.', 'We are all in the gutter, but some of us are looking at the stars.', 'I will go anywhere as long as it’s forward.', 'I will go anywhere as long as it’s forward.', 'Life gets better when you care for the right things.', 'We are limited, but we can push back the borders of our limitations.'
  embed = discord.Embed(title = "```Quote```", description =f'```{(random.choice(nice_quotes))}```', color = (0x36393E), timestamp = datetime.utcnow())
  await ctx.send(embed = embed)

@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@client.command(help='Nice quote.')
async def pp(ctx, user : discord.Member):
  the = '8=D', '8==D','8===D', '8====D','8=====D','8======D','8=======D','8========D','8=========D','8==========D','8===========D','8============D','8==============D','8============================================D'
  embed = discord.Embed(title = "```Pp size calculator```", description = f'```{user} size \n \n {(random.choice(the))}```', color = (0x36393E), timestamp = datetime.utcnow())
  await ctx.send(embed = embed)

@client.command(help='8ball')
async def magicball(ctx, *, message):
    e = f'Yes you shall : {message}.', f'No you shall not : {message}.'
    embed = discord.Embed(title = '```8ball```', description = f'```{(random.choice(e))}```', color = (0x36393E), timestamp = datetime.utcnow())
    await ctx.send(embed=embed)


@client.listen('on_message')
async def A(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Greetings, how are you doing?')
        bot.process_commands(message)

@client.command(help='Basicallly an softban..')
@has_permissions(kick_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
  user = ctx.message.author
  await member.kick(reason=reason)
  channels = client.get_channel(882327599131541514)
  
  await ctx.send(f'User {member} has been softbanned by {user}.')
  await channels.send(f'User {member} has been softbanned by {user}.')

@client.command(name='eradicate', help='Eradicate people.')
@has_permissions(kick_members=True)
async def eradicate(ctx, member: discord.Member, *, reason=None):
  user = ctx.message.author
  await member.ban(reason=reason)
  channels = client.get_channel(882327599131541514)

  await ctx.send(f'User {member} has been eradicated from this guild by {user}.')
  await channels.send(f'User {member} has been eradicated from this guild by {user}.')

@client.listen('on_message')
async def B(message):
    embed = discord.Embed(title='```Prefix```', description="```The prefix for this server is '.' or else commands will not work for you.```", color = (0x36393E), timestamp = datetime.utcnow())
    if message.author == client.user:
        return
    if  message.content.startswith('prefix'):
        await message.channel.send(embed=embed)

@client.command(help='Delete messages.')
@has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
  user = ctx.message.author
  embed = discord.Embed(title='Purge Log', description=f'```{user} has just purged {amount} of messages.```', color = (0x36393E), timestamp = datetime.utcnow())
  channel = client.get_channel(882327599131541514)
  await ctx.channel.purge(limit=amount)
  await channel.send(embed=embed)
  await ctx.send(f'{amount} messages has been purged.')

@client.event
async def on_member_remove(member):
 guild = member.guild
 channel = client.get_channel(899266438521552937)
 await channel.edit(name = f'Member Count: {guild.member_count}')

@client.event
async def on_member_join(member):
  guild = client.get_guild(881874875155898438)
  members = sorted(guild.members, key=lambda m: m.joined_at)
  embed = discord.Embed(title="New Member",description=F"Welcome {member.name} to {guild}\nJoined place `{str(members.index(member)+1)}`",color =0x36393E,timestamp = datetime.utcnow())
  embed.set_thumbnail(url=member.avatar_url)
  guild = client.get_guild(881874875155898438)
  channel2 = client.get_channel(883083595391053880)
  channel = client.get_channel(899266438521552937)
  await channel.edit(name = f'Member Count: {guild.member_count}')
  await channel2.send(embed=embed)

@client.listen()
async def on_message(message):
    if ".confess " in message.content:
        await message.delete()


@client.listen()
@commands.has_role("Member")
async def on_message(message):
    guild = client.get_guild(881874875155898438)
    rolenam = "Member"
    role = discord.utils.get(guild.roles, name=rolenam)
    user = message.author
    if "https://" in message.content:
        if role in user.roles:
            return
        else:
            await message.delete()
            await message.channel.send(f'{user.mention} message has been removed as it contained a link.')
    
@tasks.loop(seconds=150)
@commands.has_role("Muted")
async def on_guild_role_update(member):
    before = "Member"
    after = "Muted"
    guild = client.get_guild(881874875155898438)
    rolenam = "Muted"
    role = discord.utils.get(guild.roles, name=rolenam)
    if "Muted" in member.roles:
       if role in member.roles:
         await member.add_role(rolenam)
       if role not in member.roles:
         return

@client.listen()
@commands.has_role("Member")
async def on_message(message):
    channel = client.get_channel(882327599131541514)
    guild = client.get_guild(881874875155898438)
    rolenam = "Member"
    role = discord.utils.get(guild.roles, name=rolenam)
    user = message.author
    embed = discord.Embed(title="Link deleted!", description = f"`{message.content}`", color=0x36393E,timestamp = datetime.utcnow())
    embed.set_footer(text=f'Message was by {user}.')
    guild = client.get_guild(881874875155898438)
    if "www.com" in message.content:
        if role in user.roles:
            return
        else:
            await message.delete()
            await message.send(f'{user.mention} message has been removed as it contained a link.')
            await channel.send(embed=embed)


@client.command(brief='lists the servers the bot is in')
@commands.is_owner()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in client.guilds))

@client.command()
async def mhelp(ctx):
    embed = discord.Embed(title="Music Help Commands", color = (0x36393E), timestamp = datetime.utcnow())
    embed.add_field(name="Commands",value="Play \n Stop \n Resume \n Loop \n List \n Queue")
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_guild=True)
async def giveaway(ctx, msg:int):
    guild = client.get_guild(881874875155898438)
    member = ctx.message.author
    await ctx.send("What do you want to giveaway?")
    def check(message):
                return message.author == ctx.author
    what = await client.wait_for('message', timeout=30,check=check)
    await asyncio.sleep(1.9)
    emo = '🎁'
    embed2=discord.Embed(title="Giveaway", description=f'🎊 Giveaway!! \n \n Prize is **{what.content}**! \n Ends in `{msg}` seconds \n  Host is {member.mention}', color=0x36393E, timestamp = datetime.utcnow())
    dude = await ctx.send(embed=embed2)
    await dude.add_reaction(emo)
    await asyncio.sleep(msg)
    ms = await ctx.channel.fetch_message(dude.id)
    cool = await ms.reactions[0].users().flatten()
    user = random.choice(cool)
    await ctx.send(f'{user.mention} Congratulations! You have won the giveaway for the item `{what.content}`!')
    await user.send(f"Congratulations! You have won the `{what.content}` hosted by `{member}` in `{guild}`!")
    await member.send(f"The giveaway you hosted in `{guild}` for `{what.content}` is now done! The winner is `{user}`")

@client.command()
async def timehelp(ctx):
    embed = discord.Embed(title = "Time", description = f"1 minute = 60 seconds \n 1 hour = 60 minutes | 3600 seconds \n 1 day = 24 hours | 86400 \n 1 week = 168 hours | 604800 \n 1 month = 730 hours | 2628288 \n 3 months = 2190 hours |  7776000 \n 1 year = 8760 | 31536000",color = 0x36393E)
    await ctx.send(embed=embed)

 
snipe_message_author = {}
snipe_message_content = {}
 
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Snipe", description = snipe_message_content[channel.id], color=0x36393E,timestamp = datetime.utcnow())
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"There are no deleted messages in #{channel.name}")

@client.event
async def on_message_delete(message):
    user = message.author
    channel = client.get_channel(882327599131541514)
    embed = discord.Embed(title="Message deleted!", description = f"`{message.content}`", color=0x36393E,timestamp = datetime.utcnow())
    embed.set_footer(text=f'Message was by {user}.')
    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx,role : discord.Role):
    lock = discord.PermissionOverwrite(send_messages=False)
    embed = discord.Embed(description=f"off**|** successfully locked {channel.mention}" ,color=0x36393E)
    await ctx.channel.set_permissions(role, overwrite=lock)
    await ctx.send(embed=embed)


@client.command()
async def serverinfo(ctx):
    member = ctx.message.author
    icon = str(ctx.guild.icon_url)
    id = str(ctx.guild.id)

    embed = discord.Embed(title="Server Information", color = 0x36393E,timestamp = datetime.utcnow())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Member Count",value = ctx.guild.member_count, inline=True)
    embed.add_field(name="Owner",value = ctx.guild.owner, inline=True)
    embed.add_field(name="Channels",value=len(ctx.message.guild.channels),inline=True)
    embed.add_field(name="Roles",value=len(ctx.message.guild.roles),inline=True)
    embed.add_field(name="Server ID",value=id,inline=True)
    embed.add_field(name="Server Region",value = len(ctx.guild.region),inline=True)


    await ctx.send(embed=embed)

@client.command(case_insensitive=True)
async def slowmode(ctx, time:int):
    channel2 = client.get_channel(882327599131541514)
    user = ctx.message.author
    embed = discord.Embed(title="Slowmode", description=f"Slowmode was put in place by user {user} for `{time}`!",color = 0x36393E)
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Cannot run command! Requires: ``Manage Messages``')
        return
    if time == 0:
        await ctx.send('Slowmode is currently set to `0`! :timer:')
        await ctx.channel.edit(slowmode_delay = 0)
    elif time > 21600:
        await ctx.send('You cannot keep the slowmode higher than 6 hours!')
        return
    else:
        await ctx.channel.edit(slowmode_delay = time)
        msg = await ctx.send(f":timer: | Slowmode has been set to `{time}` seconds!")
        await msg.add_reaction("✅")
    await channel2.send(embed=embed)


api_key = 'removed'


me212 = "https://images-ext-1.discordapp.net/external/Mtpk5n8WXZpkYZlaiSotclUDwpgzmfvOCFN1-mpZMkw/https/cdn.upload.systems/uploads/2EboKc45.png"

@client.command(aliases=["cmds","commands","command","help"])
async def melikeu214289423424324234(ctx):
 
  embed = discord.Embed(title="<:Tylo1:893183296463339520> | Commands",description="Pressing on these links will redirect you to a pastebin.",color = 0x36393E)
  embed.set_thumbnail(url=me212)
  embed.add_field(name="<:Tylo1:893183296463339520> | Fun ", value = "[Commands](https://pastebin.com/umKrURaw)",inline=True)
  embed.add_field(name="<:Tylo1:893183296463339520> | Economy ", value = "[Commands](https://pastebin.com/cbAxPMV3)",inline=True)
  embed.add_field(name=" <:Tylo1:893183296463339520> | Moderation ", value = "[Commands](https://pastebin.com/UZPnp21p)",inline=True)
  embed.add_field(name="<:Tylo1:893183296463339520> | General ", value = "[Commands](https://pastebin.com/YuDc1wd1)",inline=True)
  embed.add_field(name="<:Tylo1:893183296463339520> | Music ", value = "[Commands](https://pastebin.com/ADR5CgY7)",inline=True)
  embed.add_field(name=" <:Tylo1:893183296463339520> | Level ", value = "[Commands](https://pastebin.com/b4b2qdDa)",inline=True)
  embed.add_field(name=" <:Tylo1:893183296463339520> | Update logs ", value = "+ `Upgrade rob command` \n+ `Made Embeds look prettier`",inline=False)
  embed.add_field(name="End of commands",value="These are the current commands, more will be added eventually! \n  TYLO #1 <:Tylo1:893183296463339520> ")
  await ctx.send(embed=embed)

@client.command(aliases=["cembed","createbed"])
async def createembed(ctx):
  await ctx.send("What would you like the title to be?")
  def check(message):
                return message.author == ctx.author
  what = await client.wait_for("message",timeout=30,check=check)
  await ctx.send("Amount of lines for the description? 1-5 lines")
  what2 = await client.wait_for("message",timeout=30,check=check)
  if "1" in what2.content:
    await ctx.send("Description?")
    what3 = await client.wait_for("message",timeout=30,check=check)
    embed= discord.Embed(title=what.content,description=what3.content, color=0x36393E)
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}")
    await ctx.send(embed=embed)
  if "2" in what2.content:
    await ctx.send("Description?")
    what4 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("2nd line description?")
    what5 = await client.wait_for("message",timeout=30)
    embed= discord.Embed(title=what.content,description=f"{what4.content} \n {what5.content}",color = 0x36393E)
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}")
    await ctx.send(embed=embed)
  if "3" in what2.content:
    await ctx.send("1st line?")
    what6 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("2nd line?")
    what7 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("3rd line?")
    what8 = await client.wait_for("message",timeout=30,check=check)
    embed = discord.Embed(title=what.content,description=f"{what6.content} \n {what7.content} \n {what8.content}",color = 0x36393E)
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}")
    await ctx.send(embed=embed)
  if "4" in what2.content:
    await ctx.send("1st line?")
    what6 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("2nd line?")
    what7 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("3rd line?")
    what8 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("4th line?")
    what9 = await client.wait_for("message",timeout=30)
    embed = discord.Embed(title=what.content,description=f"{what6.content} \n {what7.content} \n {what8.content} \n {what9.content}", color=0x36393E)
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}")
    await ctx.send(embed=embed)
  if "5" in what2.content:
    await ctx.send("1st line?")
    what6 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("2nd line?")
    what7 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("3rd line?")
    what8 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("4th line?")
    what9 = await client.wait_for("message",timeout=30,check=check)
    await ctx.send("5th line?")
    what10 = await client.wait_for("message",timeout=30,check=check)
    embed = discord.Embed(title=what.content,description=f"{what6.content} \n {what7.content} \n {what8.content} \n {what9.content} \n {what10.content}",color = 0x36393E)
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}")
    await ctx.send(embed=embed)

@client.command()
async def verify2(ctx):
  user = ctx.author
  guild = client.get_guild(881874875155898438)
  rolenam = 'Member'
  thing = discord.utils.get(ctx.guild.roles, name=rolenam)
  channel = client.get_channel(894216511168872449)
  channel2 = client.get_channel(882327599131541514)
  await ctx.send("Are you sure that you want to verify? Reply with either Y/N in 40 seconds before you need to redo the command.")
  def check(message):
                return message.author == ctx.author
  me = await client.wait_for("message",timeout = 40,check=check)
  if "Y" in me.content:
    await ctx.send("Why would you like to be verified.? Respond in 300 seconds.")
    me2 = await client.wait_for("message",timeout = 300,check=check)
    await ctx.send("Application has been sent a Moderator will review it.")
    embed = discord.Embed(title="Verification",description =f"{me2.content}",color=0x36393E,timestamp = datetime.utcnow())
    embed.add_field(name="--------------------------------------------------------------------------",value="-------------------------------------------------------------------------")
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="`Name`",value=user.name,inline=False)
    embed.add_field(name="`Nickname`",value=user.nick, inline=True)
    embed.add_field(name="`Tag`",value=user, inline=True)
    embed.add_field(name="`Joined Date`",value=user.joined_at)
    embed.add_field(name="`Creation Date`",value=user.created_at)
    embed.add_field(name="`User ID`", value=user.id, inline=True)
    embed.add_field(name="`Status`", value=user.status, inline=True)
    await channel.send(embed=embed)
    await channel.send("Do you approve or decline? It is important to type it correctly without a capital letter.")
    me4 = await client.wait_for("message",timeout=400000000)
    if "approve" in me4.content:
      await channel.send("Application was successfully approved user has been roled.")
      await channel2.send("Application was successfully approved user has been roled.")
      await user.add_roles(thing)
      await user.send(f"The application in {guild} has been approved!")
    if "decline" in me4.content:
      await user.send("Application has been denied as a result you have been removed.")
      await channel2.send(f" The application has been declined for {user}!")
      await user.kick(reason="Declined application.")
  if "N" in me.content:
    await ctx.send("It has been cancelled!")

@client.command()
async def move(ctx,member : discord.Member,channel : discord.VoiceChannel):
  user = ctx.author
  await member.move_to(channel)
  await ctx.send(f"{member} has been moved to the voice {channel}! By {user}")

@client.command()
async def e(before,after):
  guild = client.get_guild(881874875155898438)
  channel = client.get_channel(882327599131541514)
  rol = ["Admin","kick","Member","Muted","professional","Verified","kick"]
  role = guild.roles
  newlist2 = [role.mention for role in before.roles]
  newlist1 = [role.mention for role in after.roles]
  role_string = ' '.join([r.mention for r in before.roles][1:])
  role_string2 = ' '.join([r.mention for r in after.roles][1:])


  embed = discord.Embed(title=before,description="Role update",color = 0x36393E,timestamp=datetime.utcnow())
  embed.add_field(name="\u200B Before",value=f"{role_string}",inline=True)
  embed.set_thumbnail(url=before.avatar_url)
  embed.add_field(name="\u200A After",value=f"{role_string2}",inline=True)  
  embed.set_footer(text="Role Updated Log")
  await channel.send(embed=embed)

@client.command(aliases=['youHaveBeenTerminated'])
@commands.is_owner()
async def terminate(ctx):
    user = ctx.author
    print(f"{user} has just terminated the bot!")
    await ctx.send("Terminating...")
    await client.close()

@client.command(aliases=['wikisearch', 'wa'])
async def swiki(ctx, *args):
    member = ctx.author
    """
    Answers questions and queries using WolframAlpha's Simple API
    """

    query = '+'.join(args)
    url = f"https://api.wolframalpha.com/v1/result?appid={('J6PQJQ-JTVRE58XG3')}&i={query}%3F"
    response = requests.get(url)
    embed = discord.Embed(title="Wikipedia Search",description=f"Search was done by {member.name} \n```{args}```\n```{response.text}```",color = 0x36393E,timestamp=datetime.utcnow())

    if response.status_code == 501:
        embed = discord.Embed(title="Error",description="Sorry an error occured try the command again with different arguments!")
        await ctx.send(embed=embed)
        return

    await ctx.send(embed=embed)

client.launch_time = datetime.utcnow()

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(title="Uptime",description=f"{days}d \n{hours}h \n{minutes}m \n{seconds}s",color = 0x36393E,timestamp = datetime.utcnow())
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def disable(ctx, command: client.get_command):
    user = ctx.author
    embed = discord.Embed(title=f"Command",description=f"Command {command.name} has been disabled.",color = 0x36393E,timestamp = datetime.utcnow())
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}",icon_url=ctx.message.author.avatar_url)
    """Disable a command in your code without a database.
    """
    if not command.enabled:
        return await ctx.send(f"This command is already disabled.")
    command.enabled = False
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def enable(ctx, command: client.get_command):
    user = ctx.author
    embed = discord.Embed(title=f"Command",description=f"Command {command.name} has been enabled.",color = 0x36393E,timestamp = datetime.utcnow())
    embed.set_footer(text=f"Invoked by {ctx.message.author.name}",icon_url=ctx.message.author.avatar_url)
    """Disable a command in your code without a database.
    """
    if  command.enabled:
        return await ctx.send(f"This command is already enabled.")
    command.enabled = True
    await ctx.send(embed=embed)

@client.command(aliases=["createmoji","emojic","ecreate"])
async def cemoji(ctx, Url: str, *, name):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		async with aiohttp.ClientSession() as ses:
			async with ses.get(Url) as r:
				
				try:
					img_or_gif = BytesIO(await r.read())
					b_value = img_or_gif.getvalue()
					if r.status in range(200, 299):
						emoji = await guild.create_custom_emoji(image=b_value, name=name)
						await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
						await ses.close()
					else:
						await ctx.send(f'Error when making request | {r.status} response.')
						await ses.close()
						
				except discord.HTTPException:
					await ctx.send('File size is too big!')

@client.command()
async def deleteemoji(ctx, Emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted (or not): {Emoji}')
		await Emoji.delete()

client.run('UR TOKEN!')
