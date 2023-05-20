from dotenv import load_dotenv
import discord
import os
import responses

load_dotenv()

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, message.author.id)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e: 
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!');
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        usermame = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        
        print(f'{usermame} said: "{userMessage}" ({channel})')
        
        if userMessage[0] == '?':
            userMessage = userMessage[1:]
            await send_message(message, userMessage, is_private=True)
        else:
            await send_message(message, userMessage, is_private=False)
    print(os.getenv('KEY'))
    client.run(os.getenv('TOKEN'))