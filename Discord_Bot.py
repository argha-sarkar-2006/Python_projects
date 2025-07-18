app_id = "Your_Discord_app_id_here"  # Replace with your actual app ID
public_key = "Your_DDiscord_public_key_here"  # Replace with your actual public key
token  = "Your_token_here"  # Replace with your actual token
link = "Bot_channel_link"
import discord
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author == self.user:
            return 
        print(f"Message from {message.author}: {message.content}")
        channel = message.channel
        try:
            response = model.generate(
                prompt=message.content,
                max_tokens=1000,  # Adjust as needed
                temp = 1.2,  # Adjust temperature for creativity
            )
            reply = f"Hello I am Bot GPT, created by Argha Sarkar\n{response}"
        except Exception as e:
            reply = f"Error: {str(e)}"
        await channel.send(reply)
        print(f"Sent reply: {reply}")
        return 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)