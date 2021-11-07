from aiohttp import helpers
import discord
import random
import helpers 
import asyncio
import re
import io
import datetime
import aiohttp
import time
import urllib
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from PIL import Image,ImageFilter
from io import BytesIO

def setup(client):
    client.add_cog(Fun3(client))

class Fun3(commands.Cog):
    "<:soccer:899621880120639509> | Fun commands like meme, hug and more" 
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ship(self, ctx, member1 : discord.Member, member2 : discord.Member=None):
        if member2 is None:
            if ctx.message.reference:
                member2 = ctx.message.reference.resolved.author
            else:
                member2 = ctx.author
                
        number1 = random.randint(0, 100)
        
        number2 = int(str(number1)[:-1] + '0')
        
        if number2 == 10:
            text = "<:notlikethis:596577155169910784> Yikes.. That's bad."
        elif number2 == 20:
            text = "<:blobsweatsip:759934644807401512> Maybe?.. I doubt thought."
        elif number2 == 30:
            text = "<:blobpain:739614945045643447> Hey it's not terrible.. It could be worse."
        elif number2 == 40:
            text = "<:monkaS:596577132063490060> Not bad!"
        elif number2 == 50:
            text = "<:flooshed:814095751042039828> Damn!"
        elif number2 == 60:
            text = "<:pogu2:787676797184770060> AYOOO POG"
        elif number2 == 70:
            text = "<:rooAww:747680003021471825> That has to be a ship!"
        elif number2 == 80:
            text = "<a:rooClap:759933903959228446> That's a ship!"
        elif number2 == 90:
            text = ":flushed: Wow!"
        elif number2 == 100:
            text = "<:drakeYea:596577437182197791> That's a ship 100%"
        else:
            text = "<:thrinking:597590667669274651> I don't know man.."
            
        await ctx.send(f"{text}\n{member1.name} & {member2.name}\n{number1}%")

    
    
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def hug(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/hug') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} hugged {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def pat(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't pat yourself!")
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/pat') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} patted {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def kiss(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/kiss') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} kissed {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)

        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def lick(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/lick') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} licked {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def bonk(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/bonk') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} bonked {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def bully(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/bully') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} bullied {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def cuddle(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
            
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/cuddle') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} cuddled {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def slap(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/slap') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} slapped {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)   
                        
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def yeet(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/yeet') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} yeeted {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def highfive(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/highfive') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} highfived {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
            
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://meme-api.herokuapp.com/gimme/dankmemes') as r:
            data = await r.json()

            embed = discord.Embed(title=f"Meme", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                embed = discord.Embed(title="Woof")
                embed.set_image(url=data['url'])

                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def bite(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/bite') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} bit {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, BucketType.member)
    async def kill(self, ctx, member : discord.Member=None):
        if member is None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.pics/sfw/kill') as r:
            data = await r.json()

            embed = discord.Embed(title=f"{ctx.author.name} killed {member.name}", color=0x36393E)
            embed.set_image(url=data['url'])
        
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def ass(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/ass/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def ecchi(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/ecchi/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def ero(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/ero/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def hentai(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/hentai/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def maid(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/maid/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def milf(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/milf/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def oppai(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/oppai/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def oral(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/oral/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def paizuri(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/paizuri/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def selfies(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/selfies/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def uniform(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.waifu.im/nsfw/uniform/') as r:
            data = await r.json()			        
            url=data.get('tags')[0].get('images')[0].get('url')


            embed = discord.Embed(title=f"NSFW",color=0x36393E)
            embed.set_image(url=url)
        
            await ctx.send(embed=embed)
    @commands.command()
    async def rip(self,ctx,member: discord.Member):
       if not member:
           member = ctx.author

       wanted = Image.open('rip2.png')

       asset = member.avatar_url_as(size = 128)
       data = BytesIO(await asset.read())
       pfp = Image.open(data)

       pfp = pfp.resize((179,163))

       wanted.paste(pfp, (94,264))

       wanted.save('rip2.png')

       await ctx.send(file = discord.File("rip2.png"))
    @commands.command()
    async def delete(self,ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        wanted = Image.open('delete this meme.png')

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((346,351))

        wanted.paste(pfp, (213,239))

        wanted.save('delete this meme.png')

        await ctx.send(file = discord.File("delete this meme.png"))
    @commands.command()
    async def caution(self,ctx,message):
      url = f"https://api.popcat.xyz/caution?text={message}"
      embed = discord.Embed(description=f"```URL={url}\nInvoker {ctx.author.name}```",color = 0x36393E)
      embed.set_image(url=url)
      await ctx.send(embed=embed)
    @commands.command()
    async def sadcat(self,ctx,message):
      url = f"https://api.popcat.xyz/sadcat?text={message}"
      embed = discord.Embed(description=f"```URL={url}\nInvoker {ctx.author.name}```")
      embed.set_image(url=url)
      await ctx.send(embed=embed)

    @commands.command()
    async def pooh(self,ctx):
      await ctx.send("First?")
      me = await self.bot.wait_for("message",timeout=30)
      await ctx.send("Second?")
      me2 = await self.bot.wait_for("message",timeout=30)
      url = f"https://api.popcat.xyz/pooh?text1={me.content}&text2={me2.content}"
      embed = discord.Embed(description=f"```URL={url}\nInvoker: {ctx.author.name}```",color = 0x36393E)
      embed.set_image(url=url)
      await ctx.send(embed=embed)

    # @commands.command(
    #     help="<:oof:787677985468579880> OOF's the person you mentioned",
    #     aliases=['commitoof', 'commit_oof'])
    # async def oof(self, ctx, member : discord.Member=None):
    #     if member is None or member == ctx.author:
    #         responses = [f"{ctx.author.name} was killed in Electrical.",
    #         f"{ctx.author.name} failed math.",
    #         f"{ctx.author.name} rolled down a large hill.",
    #         f"{ctx.author.name} cried to death.",
    #         f"{ctx.author.name} smelt their own socks.",
    #         f"{ctx.author.name} forgot to stop texting while driving. Don't text and drive, kids.",
    #         f"{ctx.author.name} said Among Us in a public chat.",
    #         f"{ctx.author.name} stubbed their toe.",
    #         f"{ctx.author.name} forgot to grippen their shoes when walking down the stairs.",
    #         f"{ctx.author.name} wasn't paying attention and stepped on a mine.",
    #         f"{ctx.author.name} held a grenade for too long.",
    #         f"{ctx.author.name} got pwned by a sweaty tryhard.",
    #         f"{ctx.author.name} wore a black shirt in the summer.",
    #         f"{ctx.author.name} burned to a crisp.",
    #         f"{ctx.author.name} choked on a chicken nugget.",
    #         f"{ctx.author.name} forgot to look at the expiration date on the food.",
    #         f"{ctx.author.name} ran into a wall.",
    #         f"{ctx.author.name} shook a vending machine too hard.",
    #         f"{ctx.author.name} was struck by lightning.",
    #         f"{ctx.author.name} chewed 5 gum.",
    #         f"{ctx.author.name} ate too many vitamin gummy bears.",
    #         f"{ctx.author.name} tried to swim in lava. Why would you ever try to do that?"]
    #         return await ctx.send(f"{random.choice(responses)}")
        
    #     else:
    #         responses = [f"{ctx.author.name} exploded {member.name}.",
    #                     f"{ctx.author.name} shot {member.name}.",
    #                     f"{ctx.author.name} went ham on {member.name}.",
    #                     f"{ctx.author.name} betrayed and killed {member.name}.",
    #                     f"{ctx.author.name} sent {member.name} to Davy Jones' locker.",
    #                     f"{ctx.author.name} no scoped {member.name}.",
    #                     f"{ctx.author.name} said no u and killed {member.name}.",
    #                     f"{ctx.author.name} blew up {member.name} with a rocket.",
    #                     f"{ctx.author.name} pushed {member.name} off a cliff.",
    #                     f"{ctx.author.name} stabbed {member.name} to death.",
    #                     f"{ctx.author.name} slammed {member.name} with a chair.",
    #                     f"{ctx.author.name} recited a magic spell and killed {member.name}.",
    #                     f"{ctx.author.name} electrified {member.name}.",
    #                     f"{member.name} was slain by {ctx.author.name}.",
    #                     f"{ctx.author.name} burnt {member.name} alive.",
    #                     f"{ctx.author.name} buried {member.name}.",
    #                     f"{ctx.author.name} shoved {member.name}'s head underwater for too long.",
    #                     f"{ctx.author.name} slid a banana peel under {member.name}'s feet. They tripped and died...",
    #                     f"{ctx.author.name} got a headshot on {member.name}.",
    #                     f"{ctx.author.name} said a hilarious joke to {member.name} and died.",
    #                     f"{ctx.author.name} showed old Vicente0670 videos to {member.name} and died of cringe.",
    #                     f"{ctx.author.name} didn't buy Panda Express for {member.name} and exploded.",
    #                     f"{ctx.author.name} sent {member.name} to the Nether.",
    #                     f"{ctx.author.name} tossed {member.name} off an airplane.",
    #                     f"{ctx.author.name} broke {member.name}'s neck."]

    #         await ctx.send(f"{random.choice(responses)}")