import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='sudo ')



@client.event
async def on_ready():
    # something like the terminal
    print('bot is online!')


@client.command()
@commands.has_any_role('God','Jesus Christ', 'Big pp')
async def purge(ctx, *, amount):
    await ctx.channel.purge(limit=int(amount)+1)


@client.command()
@commands.has_any_role('Cardinal', 'God','Pope', 'Jesus Christ', 'Big pp')
async def rm(ctx, flag, member : discord.Member, *, reason=None):

    if flag == str:
        if reason == None:
            await ctx.send(f'Kicked {member.mention} for being gay.')
            await member.kick(reason=reason)
        else:
            await ctx.send(f'Kicked {member.mention} because {reason}.')
            await member.kick(reason=reason)
    elif flag == "-f":
        if reason == None:
            await ctx.send(f'Banned {member.mention} for being gay.')
            await member.ban(reason=reason)
        else:
            await ctx.send(f'Banned {member.mention} because {reason}.')
            await member.ban(reason=reason)


client.run('NzE0NDUyODE3MDQ5NTUwOTY4.Xsu5RA.KyzUwrrCqXcvHB39KH7WS5SQp-Q')

