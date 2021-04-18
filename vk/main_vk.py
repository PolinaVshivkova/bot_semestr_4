import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import requests
from bs4 import BeautifulSoup

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


def main():
    vk_session = vk_api.VkApi(
        token="7d3359a00a09fca1ad2da3ec46cb56a89b84ad26573381510da0a1cb4de640b6e4de4b43f1ddb010d5d60")
    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, '204057199')

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Мой гороскоп', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Мой знак зодиака', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Словари', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Больше гороскопа!', color=VkKeyboardColor.SECONDARY)
    key_clava = '453c553ee58dec67ee27b06174723bf3d6ff61d3'
    server_clava = 'https://lp.vk.com/wh202300325'
    ts_clava = '132'

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text_message = event.object.get('message').get('text')
            if event.from_user:
                if 'ку' in text_message.lower() or 'привет' in text_message.lower() or 'хай' in text_message.lower() \
                        or 'хелло' in text_message.lower() or 'хеллоу' in text_message.lower() or 'start' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='Привет! Чем я могу помочь?',
                                     random_id=get_random_id())
                elif 'спасибо' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='Не за что! Всегда рад помочь)',
                                     random_id=get_random_id())
                elif 'мой знак зодиака' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='Напиши свою дату рождения по образцу: \n'
                                             'Мой др 10 10',
                                     random_id=get_random_id())
                elif 'мой др' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message=get_zodiac_sign(text_message.split()[2], text_message.split()[3]),
                                     random_id=get_random_id())
                elif 'мой гороскоп' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='Напиши свой знак зодиака и день по образцу:\n'
                                             'Предсказание leo today\n'
                                             'P.S. Словарь дней и знаков зодиака можешь узнать по команде: '
                                             'Словари',
                                     random_id=get_random_id())
                elif 'предсказание' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message=horoscope(text_message.split()[1], text_message.split()[2]),
                                     random_id=get_random_id())
                elif 'словари' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='СЛОВАРЬ ЗНАКОВ:\n'
                                             'Овен - aries, \nТелец - taurus, \nБлизнецы - gemini, \n'
                                             'Рак - cancer, \nЛев - leo, \nДева - virgo, \n'
                                             'Весы - libra, \nСкорпион - scorpio, \nСтрелец - sagittarius, \n'
                                             'Козерог - capricorn, \nВодолей - aquarius, \nРыбы - pisces\n'
                                             '\nСЛОВАРЬ ДНЕЙ:\n'
                                             'Вчера - yesterday, \nСегодня - today, \n'
                                             'Завтра - tomorrow, \nПослезавтра - tomorrow02',
                                     random_id=get_random_id())
                elif 'больше гороскопа!' in text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message='Больше гороскопа ты можешь найти, перейдя по ссылке: https://ignio.com/',
                                     random_id=get_random_id())
                else:
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     random_id=get_random_id(),
                                     message='Я не знаю такую команду:(',
                                     chat_id=event.chat_id)


if __name__ == '__main__':
    main()
