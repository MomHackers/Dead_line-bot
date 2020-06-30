import requests
import bs4


class VkBot:

    # TODO Интеграция с БД
    def __init__(self, user_id):
        self.USER_ID = user_id
        self.USERNAME = self._get_user_name_from_vk_id(user_id)
        self.COMMANDS = ["ПРИВЕТ", "РАСПИСАНИЕ", "ПОГОДА", "ПОКА"]  # TODO расширить

    def _get_user_name_from_vk_id(self, user_id):
        pass  # TODO Name from ID

    def new_message(self, message):

        # Привет
        if message.upper() == self.COMMANDS[0]:
            return f"Привет-привет, {self.USERNAME}!"  # Пример

        # Расписание
        elif message.upper() == self.COMMANDS[2]:
            return self.get_shedule()  # TODO Интеграция с расписанием

        # Погода
        elif message.upper() == self.COMMANDS[1]:
            return self.set_deadline()  # TODO Интеграция с базой данных дедлайнов
            # пользователей и из РУЗа

        # Пока
        elif message.upper() == self.COMMANDS[3]:
            return f"Пока-пока, {self.USERNAME}!"

        else:
            return "А вот тут я не поняла :/"
