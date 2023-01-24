from main import generate_email
import dotenv
import os
import discord

dotenv.load_dotenv(".env")
TOKEN = os.getenv("BOT_TOKEN")
API_TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    print(f'Successful Launch!!! {client.user}') 
    
@client.event
async def on_message(message):
    print("Message received")
    prompt: str = message.content

    print(message)

    if prompt.startswith("!formal"):
        prompt = prompt.replace("!formal", "")
        print(prompt)
        response: str = generate_email(prompt, API_TOKEN)
        print(response)
        await message.channel.send(response)

client.run(TOKEN)