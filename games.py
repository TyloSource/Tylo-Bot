from __future__ import print_function
import discord
import aiohttp
from discord.ext import commands
import random
import time


def setup(client):
    client.add_cog(Moot(client))

class Moot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def typerace(self,ctx):
      sentences = "incredible insane godly like yes cool nice superior funny tree monkey discord sheep beep meep production development deploy deployed pictures nut children kids humans toys lego mini monster slave destroyer cut doctor literature marsh lot hate accident listen step wolf robot acute boast perfection grind badge flinch sound brainwash conquest cholera battery perception heroes disgusting grind die alive error command work help".split()

      me2 = random.sample(sentences,15)
      me = " ".join(me2)
      me3 =  "‏‏‎ ‎".join(me2)

      embed = discord.Embed(
      title="Type this following message",
      description=f"```{me3}```",
      color = 0x36393E
      )
      embed.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.message.author.avatar_url)
      start = time.time()
      d = await ctx.send(embed=embed)
      def check(message):
                return message.author == ctx.author
      ced = await self.client.wait_for("message",timeout=50,check=check)
      end = time.time()

      d = len(ced.content)

      e = end - start

      f = e / 60

      g = d / 5 / f
      embed2 = discord.Embed(title="Correct",description =f"```Speed: {round(e)}\nWPM: {round(g)}```")
      embed3 = discord.Embed(title="Incorrect",description =f"But what it would of been if correct:\n```Speed: {round(e)}\nWPM: {round(g)}```")

      if ced.content == me:
        te = await ctx.send(embed=embed)
        await te.edit(embed=embed2)
      else:
        ye = await ctx.send(embed=embed)
        await ye.edit(embed=embed3)
       
    @commands.command()
    async def trivia(self, ctx):
      yes = "easy","hard","medium"
      me = (random.choice(yes))
      if me == "easy":
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple') as r:
            data = await r.json()
            #print(data)
            #print(data["results"])
            #print(data["category"])
            url= data.get('results')[0].get('question')
            url2= data.get('results')[0].get('category')
            url3= data.get('results')[0].get('type')
            url4= data.get('results')[0].get('difficulty')
            url5= data.get('results')[0].get('incorrect_answers')
            url6= data.get('results')[0].get('correct_answer')

            url5.append(url6)


            random.shuffle(url5)

            me = url5

            string = ", ".join(me)

            embed = discord.Embed(title=f"Trivia",description=f"Trivia for {url2} mode {url4}!")
            embed.add_field(name="Question",value=url)
            embed.add_field(name="Answer",value=f"{string}",inline=False)
            embed.set_footer(text=f"Invoked by {ctx.author}")

            await ctx.send(embed=embed)
            await ctx.send("What is your answer?")
            def check(message):
                return message.author == ctx.author
            message = await self.client.wait_for("message",timeout=500,check=check)
            if url6 in message.content:
              await ctx.send("Good job!")
            else:
              await ctx.send("Atleast you tried!")
      if me == "medium":
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=multiple') as r:
            data = await r.json()
            #print(data)
            #print(data["results"])
            #print(data["category"])
            url= data.get('results')[0].get('question')
            url2= data.get('results')[0].get('category')
            url3= data.get('results')[0].get('type')
            url4= data.get('results')[0].get('difficulty')
            url5= data.get('results')[0].get('incorrect_answers')
            url6= data.get('results')[0].get('correct_answer')

            url5.append(url6)


            random.shuffle(url5)

            me = url5

            string = ", ".join(me)

            embed = discord.Embed(title=f"Trivia",description=f"Trivia for {url2} mode {url4}!")
            embed.add_field(name="Question",value=url)
            embed.add_field(name="Answer",value=f"{string}",inline=False)
            embed.set_footer(text=f"Invoked by {ctx.author}")

            await ctx.send(embed=embed)
            await ctx.send("What is your answer?")
            def check(message):
                return message.author == ctx.author
            message = await self.client.wait_for("message",timeout=500,check=check)
            if url6 in message.content:
              await ctx.send("Good job!")
            else:
              await ctx.send("Atleast you tried!")
      if me == "hard":
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://opentdb.com/api.php?amount=1&category=9&difficulty=hard&type=multiple') as r:
            data = await r.json()
            #print(data)
            #print(data["results"])
            #print(data["category"])
            url= data.get('results')[0].get('question')
            url2= data.get('results')[0].get('category')
            url3= data.get('results')[0].get('type')
            url4= data.get('results')[0].get('difficulty')
            url5= data.get('results')[0].get('incorrect_answers')
            url6= data.get('results')[0].get('correct_answer')

            url5.append(url6)


            random.shuffle(url5)

            me = url5

            string = ", ".join(me)

            embed = discord.Embed(title=f"Trivia",description=f"Trivia for {url2} mode {url4}!")
            embed.add_field(name="Question",value=url)
            embed.add_field(name="Answer",value=f"{string}",inline=False)
            embed.set_footer(text=f"Invoked by {ctx.author}")

            await ctx.send(embed=embed)
            await ctx.send("What is your answer?")
            def check(message):
                return message.author == ctx.author
            message = await self.client.wait_for("message",timeout=500,check=check)
            if url6 in message.content:
              await ctx.send("Good job!")
            else:
              await ctx.send("Atleast you tried!")
    