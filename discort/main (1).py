import discord
import requests

TOKEN = 'TOKEN'
client = discord.Client()


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})'
            )

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author != self.user:
            if "кот" in message.content.lower():
                result = requests.get("https://api.thecatapi.com/v1/images/search")
                link = result.json()[0]['url']
                await message.channel.send(link)
                await message.channel.send("Вот тебе котеЧЕЧКА")
            elif 'соба' in message.content.lower():
                result = requests.get("https://dog.ceo/api/breeds/image/random")
                link = result.json()['message']
                await message.channel.send(link)
                await message.channel.send("Ну вот тебе собаЧЕЧКА")
            elif "привет" in message.content.lower():
                await message.channel.send("И тебе привет")


client = YLBotClient()
client.run(TOKEN)
