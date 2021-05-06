import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation commands loaded")

    @commands.command(aliases=["cls", "clear", "prg", "prge"])
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} messages deleted!")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked with the reason: ")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned with the reason: ")

    @commands.command(aliases=["pardon", "unbn"])
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guilds.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")


def setup(client):
    client.add_cog(moderation(client))