import asyncio
import random

import nextcord
from nextcord.ext import commands

import logging

import config

logging.basicConfig(level=logging.INFO)

intents = nextcord.Intents.default()
intents.message_content = True

GUILD_IDS = config.GUILD_IDS
TOKEN = config.TOKEN

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="Selamün aleyküm dostlar!", guild_ids=GUILD_IDS)
async def sea(interaction: nextcord.Interaction):
    await interaction.send("AS")

@bot.slash_command(description="AS deyince ne olacak acaba?", guild_ids=GUILD_IDS)
async def ase(interaction: nextcord.Interaction):
    await interaction.send("SA demedim ki olm da neyse as")

@bot.slash_command(description="Fatih ay tam bir ...?", guild_ids=GUILD_IDS)
async def fatihay(interaction: nextcord.Interaction):
    await interaction.send("TAM BİR GAY")

@bot.command()
async def guess(ctx, guess: int = None):
    def is_correct(message):
        return message.author == ctx.author and message.content.isdigit()

    answer = random.randint(1, 10)

    if not guess:
        await ctx.send("Guess a number between 1 and 10.")
        try:
            guess = await bot.wait_for("message", check=is_correct, timeout=5.0)
            guess = guess.content
        except asyncio.TimeoutError:
            return await ctx.send(f"Sorry, you took so long! The answer was {answer}.")

    if int(guess) == answer:
        await ctx.send("You are right!")
    else:
        await ctx.send(f"Oops. It is actually {answer}.")

@bot.slash_command(guild_ids=GUILD_IDS, description="Guess a number between 1 and 10.")
async def guess(interaction: nextcord.Interaction, number: int = nextcord.SlashOption(description="Enter your guess", required=True)):
    answer = random.randint(1, 10)
    if answer != number:
        await interaction.response.send_message(f"Oops. It is actually {answer}.", ephemeral=True)
    else:
        await interaction.response.send_message("You are right!")

bot.run(TOKEN)
