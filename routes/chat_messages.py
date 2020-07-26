from vkbottle.bot import Blueprint
from vkbottle.rule import ChatActionRule

bp = Blueprint(name="Работа с чатами групп")


async def check(ans, id: int) -> bool:
    items = (await bp.api.messages.get_conversations_by_id(peer_ids=ans.peer_id)).items
    if not items:
        return False
    chat_settings = items[0].chat_settings
    admins = []
    admins.extend(chat_settings.admin_ids)
    admins.append(chat_settings.owner_id)
    return id in admins


async def getid(pattern: str) -> int:
    if pattern.isdigit():
        return pattern
    elif "vk.com/" in pattern:
        uid = (await bp.api.users.get(user_ids=pattern.split("/")[-1]))[0]
        return uid.id
    elif "[id" in pattern:
        uid = pattern.split("|")[0]
        return uid.replace("[id", "")


@bp.on.chat_invite()
async def chatstart(_):
    return "Салам алейкум, хацкеры"


@bp.on.chat_message(ChatActionRule(["chat_invite_user", "chat_invite_user_by_link"]))
async def invite(_):
    return "В рядах хацкеров пополнение -.-"
