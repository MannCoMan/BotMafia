import vk_api
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import sqlite3


# API-ключ созданный ранее
token = "645afc1133658c6516df7ad7930afcdeb1556cbc0f87fb8f3021ddb1b53c18c700d5eabcee0da76e4f4f4"

# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

keyboard = VkKeyboard()
keyboard.add_button('Привет', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('Погода', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Время', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Пока', color=VkKeyboardColor.PRIMARY)

# Основной цикл бота
print("Server started")
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня
        if event.to_me:
            # Сообщение от пользователя
            print('New message:')
            print(f'For me by: {event.user_id}')

            # Ответы в зависимости от сообщения пользователя
            bot = VkBot(event.user_id)
            vk.messages.send(
                user_id=event.user_id,
                message=event.user_id,
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard()
            )
            print('Text: ', event.text)
