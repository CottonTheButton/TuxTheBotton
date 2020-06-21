import discord
import asyncio
import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='sudo ')


@bot.event
async def on_ready():

    channel = bot.get_channel(709669976390500422)
    print(f'bot is online!')
    await bot.change_presence(activity=discord.Game(name='You bitches best behave'))
    await channel.send("I'm online. You bitches best behave.")


@bot.command()
@commands.has_any_role('God', 'Jesus Christ', 'Big pp')
async def purge(ctx, *, amount):
    await ctx.channel.purge(limit=int(amount)+1)


@bot.command()
@commands.has_any_role('Cardinal', 'God', 'Pope', 'Jesus Christ', 'Big pp')
async def rm(ctx, flag, member: discord.Member, *, reason=None):

    if flag == str:

        if reason is None:
            await ctx.send(f'Kicked {member.mention} for being gay.')
            await member.kick(reason=reason)

        else:
            await ctx.send(f'Kicked {member.mention} because {reason}.')
            await member.kick(reason=reason)

    elif flag == "-f":

        if reason is None:
            await ctx.send(f'Banned {member.mention} for being gay.')
            await member.ban(reason=reason)

        else:
            await ctx.send(f'Banned {member.mention} because {reason}.')
            await member.ban(reason=reason)


@bot.command()
@commands.has_any_role('Big pp')
async def give_role(ctx, member: discord.Member, *, role_name):

    guild = discord.utils.get(bot.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name=role_name)

    await ctx.channel.purge(limit=2)
    await ctx.send(f"Gave {member} a {role_id} role!")
    await member.add_roles(role_id)


@bot.command(aliases=["allmightypush", "AllMightyPush"])
@commands.has_any_role('Big pp')
async def all_mighty_push(ctx):

    await ctx.channel.purge(limit=999999)

bot.run('NzE0NDUyODE3MDQ5NTUwOTY4.XtsnEg.usC4ux-vpGuGRdDEIBjO19GCHcg')

