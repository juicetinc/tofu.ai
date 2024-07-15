import discord
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# get the token from the environment variable
token = os.getenv('DISCORD_TOKEN')

# set up the necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if you need to read message content

# initializes the discord client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')



# run the client with the token
client.run(token)