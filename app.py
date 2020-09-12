import os
import discord
from discord import Embed
from discord.utils import get
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

command_list = {
    "_tag+_": "Add a tag to yourself. For example `!panda tag+ Learn_The_Dungeon`.",
    "_tag-_": "Remove a tag from yourself. For example `!panda tag- Push_The_Key`.",
    "_tags_": "List all assignable tags and which ones you have. For example `!panda tags`."
}

mythic_plus_tags = ["Hit_The_Timer", "Push_The_Key", "Learn_The_Dungeon", "Finsh_The_Run"]
role_tags = ["Healer", "Tank", "Dps"]
other_tags = ["Guild_Raid"]

valid_roles = mythic_plus_tags + role_tags + other_tags

@bot.command(pass_context=True)
async def panda(ctx):
    """
    Central controller for whatver commands are passed in after the keyword
    """
    line_split = ctx.message.content.split(" ")
    print(line_split)
    core_command = "list" if len(line_split) < 2 else line_split[1]
    command_list = {
        "list": panda_list,
        "tag+": panda_add_role,
        "tag-": panda_remove_role,
        "tags": panda_list_tags
    }
    await command_list[core_command](ctx)

async def finish_with(ctx):
    """
    Always finish a message with a nudge towards the help commands
    """
    await ctx.channel.send("_For a summary of what else I can do, just use `!panda`._")

async def panda_list_tags(ctx):
    str_roles = [x.name for x in ctx.message.author.roles]
    name = ctx.message.author.mention

    # TODO: waaaaay too much repetition here

    # Mythic plus
    embed = Embed(color=0x566de1, description="_These are the mythic+ tags you can assign and unassign via this bot._")
    for role in mythic_plus_tags:
        v = "```ARM\nNope\n```\n" if role not in str_roles else "```CSS\nGot it\n```\n" 
        embed.add_field(name=role, value=v, inline=True)
    await ctx.channel.send("hey {} :wave:".format(name), embed=embed)

    # Role
    embed = Embed(color=0x22a041, description="_These are the role based tags you can assign and unassign via this bot._")
    for role in role_tags:
        v = "```ARM\nNope\n```\n" if role not in str_roles else "```CSS\nGot it\n```\n" 
        embed.add_field(name=role, value=v, inline=True)
    await ctx.channel.send(embed=embed)

    # Other tags
    embed = Embed(color=0xfaef5c, description="_These are the other tags you can assign and unassign via this bot._")
    for role in other_tags:
        v = "```ARM\nNope\n```\n" if role not in str_roles else "```CSS\nGot it\n```\n" 
        embed.add_field(name=role, value=v, inline=True)
    await ctx.channel.send(embed=embed)

    await finish_with(ctx)

async def panda_list(ctx):
    embed = Embed(
        title="Panda Help",
        description="_The following is a high level summary of things I can do._"
        )
    for name, example in command_list.items():
        embed.add_field(name=name, value=example, inline=False)

    await ctx.channel.send(embed=embed)
    await finish_with(ctx)

async def panda_add_role(ctx):
    try:
        member = ctx.message.author
        split_the_line = ctx.message.content.split(" ")
        role_in_question = split_the_line[2]
        role = get(member.guild.roles, name=role_in_question)
        if role is None:
            await ctx.channel.send("The tag `{}` does not exist or isn't something you can change this way.".format(role_in_question))
        else:
            await member.add_roles(role)
            await ctx.channel.send("I've added the role `{}` for you. You'll now get a ping when anyone @'s this tag.".format(role_in_question))
    except Exception as e:
        raise e
    await finish_with(ctx)

async def panda_remove_role(ctx):
    try:
        member = ctx.message.author
        split_the_line = ctx.message.content.split(" ")
        role_in_question = split_the_line[2]
        role = get(member.guild.roles, name=role_in_question)
        if role is None:
            await ctx.channel.send("The tag `{}` does not exist or isn't something you can change this way.".format(role_in_question))
        else:
            await member.remove_roles(role)
            await ctx.channel.send("I've removed the role `{}` from you. You'll no longer get a ping when someone @'s this tag.".format(role_in_question))
    except Exception as e:
        raise e
    await finish_with(ctx)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
