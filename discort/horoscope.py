import discord
import requests
from bs4 import BeautifulSoup

TOKEN = 'ODI0NTM3MTEwNDgwMjg5ODAz.YFw0Bg.fTt7clavVHEUtT54cCd1NL8i74w'

sign_dates = (((20, 3), (19, 4)),
              ((20, 4), (20, 5)),
              ((21, 5), (20, 6)),
              ((21, 6), (22, 7)),
              ((23, 7), (22, 8)),
              ((23, 8), (22, 9)),
              ((23, 9), (22, 10)),
              ((23, 10), (21, 11)),
              ((22, 11), (21, 12)),
              ((22, 12), (19, 1)),
              ((20, 1), (17, 2)),
              ((18, 2), (19, 3)),)

ru_dict = {0: "Овен",
           1: "Телец",
           2: "Близнецы",
           3: "Рак",
           4: "Лев",
           5: "Дева",
           6: "Весы",
           7: "Скорпион",
           8: "Стрелец",
           9: "Козерог",
           10: "Водолей",
           11: "Рыбы"}


def get_zodiac_sign(day, month):
    for index, sign in enumerate(sign_dates):
        if (int(month) == sign[0][1] and int(day) >= sign[0][0]) or \
                (int(month) == sign[1][1] and int(day) <= sign[1][0]):
            return ru_dict[index]
    return


def horoscope(sign, dat):
    try:
        res = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        zodiac_sign = soup.findAll(f"{sign}")
        soup2 = BeautifulSoup(str(zodiac_sign), 'html.parser')
        dat = str(soup2.findAll(f"{dat}"))
        res = dat.split('\n')[1]
        return f"Твой гороскоп: {res}"
    except Exception:
        return f'неправильные данные('


class DiscordBot(discord.Client):
    async def on_message(self, message):
        if self.user != message.author:
            message_text = message.content
            if message_text.startswith('help_horoscope'):
                await message.channel.send('!horoscope <знак зодиака> <день> - узнать гороскоп\n'
                                           'Пример: !horoscope aries yesterday, \n '
                                           '!zodiac_sign_dict - словарь значений ЗЗ,\n '
                                           '!day_dict - словарь дней'
                                           '!my_zodiac <Число рождения> <месяц рождения числом> - '
                                           'узнать свой знак зодиака по дате рождения\n'
                                           'Пример: !my_zodiac 30 11')
            elif message_text.startswith('!horoscope'):
                await message.channel.send(horoscope(message_text.split()[1], message_text.split()[2]))
            elif message_text.startswith('!zodiac_sign_dict'):
                await message.channel.send('Овен - aries, \nТелец - taurus, \nБлизнецы - gemini, \n'
                                           'Рак - cancer, \nЛев - leo, \nДева - virgo, \n'
                                           'Весы - libra, \nСкорпион - scorpio, \nСтрелец - sagittarius, \n'
                                           'Козерог - capricorn, \nВодолей - aquarius, \nРыбы - pisces')
            elif message_text.startswith('!day_dict'):
                await message.channel.send('Вчера - yesterday, \nСегодня - today, \n'
                                           'Завтра - tomorrow, \nПослезавтра - tomorrow02')
            elif message_text.startswith('!my_zodiac'):
                await message.channel.send(get_zodiac_sign(message_text.split()[1], message_text.split()[2]))


client = DiscordBot()
client.run(TOKEN)