
import nonebot,re
from ..tools.my_way import way
from nonebot import on, on_command, on_keyword, on_metaevent, on_notice
from nonebot.adapters.onebot.v11 import Bot, Event

a = on_keyword('时',priority=11)
@a.handle()
async def _(event:Event,bot:Bot):
    group_id = way.get_group_id(event.get_session_id())
    print(group_id)
    print('\n',
    event.get_session_id(),'\n',
    )
