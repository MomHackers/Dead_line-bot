import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from settings import TOKEN

reply = "Я не понимаю, что ты там написал"  # TODO reply - Функция распознования текста сообщения


def main():
    try:
        vk_session = vk_api.VkApi(token=TOKEN)
        vk = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=reply)
                user = vk.users.get(user_ids=event.user_id)[0]
                # ТЕСТОВЫЙ ВЫВОД В КОНСОЛЬ:
                print(str(event.text) + " FROM: " + user['first_name'] + ' ' + user['last_name'])
    except Exception as e:
        print("EXCEPTION: " + str(e))
        main()


if __name__ == '__main__':
    main()
