import discord
import os
from discord.ext import commands


intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True, presences=True
)
client = commands.Bot(command_prefix="t!", intents=intents)

B
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('your mom'))
    print("Sup fucker, im online")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")    
    await ctx.send(f"Unloaded cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Reloaded all cogs!")


@client.command()
async def test(ctx):
    async atx.send("test")


client.run("ODI3NDQ2ODUxMzE3MjY4NDgw.YGbJ7g.7DOF5Nf-AFCGLEh1eQ3vSekzuNk")
