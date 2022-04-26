
from nonebot import on_command, on_keyword, on_message, on_regex, on_startswith
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.permission import SUPERUSER
from ..tools.my_way import way

name = 'switch_reply_car'

keyword:list = ['刀'] 

notice = on_regex('[\d]{9}(.*)刀(车?)',priority=12,block=False)
@notice.handle()
async def _(bot:Bot,event:Event):
    if way.switch(name,way.get_group_id(event.get_session_id())):
        global switch
        print(switch)
        if switch == True:
            await bot.call_api('send_msg',user_id = '2273076505',message = event.get_message())
        notice.stop_propagation(notice)



switch:bool
isopen = on_keyword(['上车','下车'],block=False)
@isopen.handle()
async def _(event:Event):
    print('jinru')
    if way.switch(name,way.get_group_id(event.get_session_id())):
        global switch
            # print('init2')
        if str(event.get_user_id()) == '2273076505':
            print(str(event.get_user_id()) == '2273076505')
            if str(event.get_message()) == '上车':
                switch = True
                print(switch)
            else:
                switch = False
        isopen.stop_propagation(isopen)
            # print(switch)
        # print(str(event.get_message()))



