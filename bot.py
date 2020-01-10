import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('message.send', {'user_id': user_id, 'message': message})

# API-ключ созданный ранее
token = "26085dc482433a202c6b046fbd10fecc85e1b656bd2964d74d4c4a3e6dc7a479da4a8bb1499528e4dfe6c"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл бота
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Ответы в зависимости от сообщения пользователя
            if request == "привет":
                write_msg(event.user_id, "Здарова!")
            elif request == "Пока":
                write_msg(event.user_id, "До свидули(")
            else:
                write_msg(event.user_id, "Блет, Кряжин не прописал, что в таких случаях отвечать")


