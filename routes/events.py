from vkbottle.bot import Blueprint
from vkbottle.types import GroupJoin, GroupLeave

bp = Blueprint(name="Работа с ивентами")


@bp.on.event.group_join()
async def group_join(event: GroupJoin):
    print(f"Новый пользователь: {event.user_id}")
