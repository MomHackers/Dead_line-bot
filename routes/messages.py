from vkbottle.bot import Blueprint, Message
from vkbottle.keyboard import Keyboard, Text

# Blueprint init
bp = Blueprint(name="Работа с лисными сообщениями")

#
# Keyboards
menu = Keyboard(one_time=True)
menu.add_row()
menu.add_button(Text(label="Расписание"), color="primary")
menu.add_button(Text(label="Создать дедлайн"), color="primary")


# end of keyboards

@bp.on.message_handler(text="Меню")
async def wrapper(ans: Message):
    await ans("Расписание на ближайший день,\nменеджер дедлайнов и другое!", keyboard=menu.generate())


@bp.on.message_handler(text="Создать дедлайн")
async def wrapper(ans: Message):
    await ans("Расписание в разработке! =)")


@bp.on.message_handler(text="Создать дедлайн")
async def wrapper(ans: Message):
    await ans("Создание своих дедлайнов в разработке!")
