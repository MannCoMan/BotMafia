import vk_api
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

'''
def write_msg(user_id, message):
    vk.method('message.send', {'user_id': user_id, 'message': message})
'''

# API-ключ созданный ранее
token = "26085dc482433a202c6b046fbd10fecc85e1b656bd2964d74d4c4a3e6dc7a479da4a8bb1499528e4dfe6c"

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
            print(f'For me by: {event.user_id}', end='')

            # Ответы в зависимости от сообщения пользователя
            bot = VkBot(event.user_id)
            '''
            write_msg(event.user_id, bot.new_message(event.text))
            '''
            vk.messages.send(user_id=event.user_id, message=bot.new_message(event.text), random_id=get_random_id(), keyboard=keyboard.get_keyboard())
            print('Text: ', event.text)
