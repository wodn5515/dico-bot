import discord
import os
import asyncio

from discord.ext import commands

from client.music import Music

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.event
async def on_ready():
    print(f"Login Bot: {bot.user}")

@bot.tree.command(name="재생", description="테스트")
@discord.app_commands.describe(text="url")
async def test(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f'{interaction.user.mention} : {text}', ephemeral=True)


async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.start(os.environ.get("BOT_TOKEN"))


asyncio.run(main())
