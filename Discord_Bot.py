app_id = 1392020928585662504
public_key = "a475445277dc757dd3460a5f2661966b044cbd8dff3ae040813dc6ff74c19eb5"
token  = "MTM5MjAyMDkyODU4NTY2MjUwNA.GZR9QY.-l5Qdny-vR9R4YHJhwIicD8MeX0a4f6Us-otN4"
link = "https://discord.com/channels/1392019736761733232/1392019737676087309"
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