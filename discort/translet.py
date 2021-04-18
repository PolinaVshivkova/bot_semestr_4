import discord
import requests
import asyncio
from translate import Translator

TOKEN = 'ODI0NTM3MTEwNDgwMjg5ODAz.YFw0Bg.fTt7clavVHEUtT54cCd1NL8i74w'

scr = 'english'
dst = 'ru'


class DiscordBot(discord.Client):
    async def on_message(self, message):
        global scr, dst
        if self.user != message.author:
            message_text = message.content
            if message_text.startswith('help_text'):
                await message.channel.send('!reverse - перевернет твое сообщение\n'
                                           '!text - переведет твое сообщение\n'
                                           '!set_lang - поменяет языки. какие ты попросишь,\n '
                                           'пример: "!set_lang ru-korean"')
            if message_text.startswith('!reverse'):
                await message.channel.send(message_text[:7:-1])
            if message_text.startswith('!text'):
                translator = Translator(from_lang=dst, to_lang=scr)
                await message.channel.send(translator.translate(message_text[5::]))
            if message_text.startswith('!set_lang'):
                dst, scr = message_text[10:].split('-')


client = DiscordBot()
client.run(TOKEN)
