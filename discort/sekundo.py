import discord
import requests
import asyncio

TOKEN = 'ODI0NTM3MTEwNDgwMjg5ODAz.YFw0Bg.fTt7clavVHEUtT54cCd1NL8i74w'


class DiscordBot(discord.Client):
    async def on_message(self, message):
        if self.user != message.author:
            message_text = message.content
            print(message_text)
            if message_text.startswith('set_timer'):
                hours, minutes = map(int, message_text.split()[2:5:2])
                seconds = minutes * 60 + hours * 3600
                await asyncio.sleep(seconds)
                await message.channel.send('Это волшебный подзатыльник, время и стекло!')


client =  DiscordBot()
client.run(TOKEN)