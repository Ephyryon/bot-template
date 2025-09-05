from bot_managment.bot_setup import bot
import discord

## Ping: Returns the latency of the bot.
async def ping(ctx, name: str = ""):
    if bot.user.name == name:
        latency = round(bot.latency * 1000) # Converts the latency to ms.
        embed = discord.Embed(leading="Pong!", description=f"Latency: {latency}ms", color=discord.Color.blurple())
        await ctx.send(embed=embed, ephemeral=True) # Sends the embed to the user who executed the command.
    else:
        None