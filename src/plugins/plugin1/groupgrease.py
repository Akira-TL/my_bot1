import json
from tokenize import group
from nonebot import on_command, on_keyword, on_notice,message
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import (
    NoticeEvent,
    MessageSegment,
    Event,
    Bot,
    GROUP_ADMIN,GROUP_OWNER,
)

adress = 'F:\document\OneDrive - 南京农业大学\My_codes\python\my_bot1\src\plugins\plugin1\db\GroupInOrDecreaseNotice.json'

GroupMenNotice = on_notice(priority=5)
@GroupMenNotice.handle() # 进退群提醒
async def _(bot:Bot,event:NoticeEvent):
    group_id = str(event.get_session_id).split(_)[1]
    user_id = event.get_user_id()
    # head_url = f"https://q.qlogo.cn/g?b=qq&nk={user_id}&s=640"#头像
    try:
        with open(adress,'r') as a:
            notice = json.load(a)
        notice_content = notice[group_id]
    except:
        notice_content = '欢迎新成员的加入!'

    describtion = json.loads(event.get_event_description().replace("'",'"'))

    if describtion['notice_type'] == 'group_increase':
        await GroupMenNotice.finish(
                                    MessageSegment.at(user_id) + f""
                                    )

GroupNoticeswitch = on_command('进退群提醒',priority=5,block=True,permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)
@GroupNoticeswitch.handle()
async def GroupNoticeswitch_(event:Event):
    group_id = str(event.get_session_id()).split('_')[1]
    print(group_id)
    try:
        with open(adress,'r') as f:
            content = json.load(f)
    except FileNotFoundError:
        open(adress,'w')
        content = {}
    f.close

    try:
        switch = content[group_id]
    except KeyError:
        switch = False
    
    if switch:
        switch = False
    else:
        switch = True

    data = {group_id:switch}
    content.update(data)

    with open(adress,'w') as f_new:
        json.dump(content,f_new)

    if switch:
        await GroupNoticeswitch.finish('进退群提醒已开启')
    elif not switch:
        await GroupNoticeswitch.finish('进退群提醒已关闭')
    else:
        await GroupNoticeswitch.finish('进退群提醒错误,请检查日志!')


test = on_notice()
@test.handle()
async def _(event:NoticeEvent):
    print(event.get_event_description())