import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN, GROUP_ID, Debug
from bot import VkBot

vk_session = vk_api.VkApi(token=TOKEN)

vk = vk_session.get_api()
mh_bot = VkBot
longpoll = VkLongPoll(vk_session, group_id=GROUP_ID)


def main():
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
                # vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=reply)
                user = vk.users.get(user_ids=event.user_id)[0]
                # ТЕСТОВЫЙ ВЫВОД В КОНСОЛЬ:
                if Debug:
                    print(str(event.text) + " FROM: " + user['first_name'] + ' ' + user['last_name'])
    except Exception as exc:
        print("EXCEPTION: " + str(exc))
        main()


if __name__ == '__main__':
    main()
