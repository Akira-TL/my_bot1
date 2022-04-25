import json
from nonebot import on_command, on_keyword, on_notice, on_regex
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import (
    NoticeEvent,
    MessageSegment,
    Message,
    Event,
    Bot,
    GROUP_ADMIN,GROUP_OWNER,
)

path = 'F:\document\OneDrive - 南京农业大学\My_codes\python\my_bot1\src\plugins\plugin1\db'#数据文件的存储位置
file = path + '\GroupInOrDecreaseNotice.json'
GroupMemNotice = on_notice(priority=5)
@GroupMemNotice.handle() # 进退群提醒
async def _(bot:Bot,event:NoticeEvent):
    group_id = str(event.get_session_id()).split('_')[1]
    user_id = event.get_user_id()
    user_info = await bot.get_stranger_info(user_id=int(user_id))
    head_url = f"https://q.qlogo.cn/g?b=qq&nk={user_id}&s=640"#QQ头像地址
    try:
        await create_document()
        f = open(file,'r')
        global switch
        print('<<<'+group_id+'>>>')
        switch = str(json.load(f)[group_id])
        print('<<<'+switch+'>>>')

        if switch == '1':
            description = json.loads(event.get_event_description().replace("'",'"'))
            if description['notice_type'] == 'group_increase':
                await GroupMemNotice.finish(
                    MessageSegment.at(user_id=user_id)+Message('欢迎新成员的加入!') + \
                    MessageSegment.image(head_url) + Message('既然来了就不要走了哦੭ ᐕ)੭*⁾⁾')
                )
            elif description['notice_type'] == 'group_decrease':
                if description['sub_type'] == 'leave':
                    await GroupMemNotice.finish(
                        MessageSegment.image(head_url) + Message('悄咪咪的离开了我们...')
                    )
                elif description['sub_type'] == 'kick':
                    op_user_id = description['operator_id']
                    await GroupMemNotice.finish(MessageSegment.image(head_url) +
                                            "发现超级可爱的 " + MessageSegment.at(op_user_id) + f"({op_user_id})"
                                            f" 面无表情地把 {user_info['nickname']}({user_id}) 踹了出去，当时害怕极了喵。。")
    except:
        pass




    pass


    # group_id = str(event.get_session_id).split(_)[1]
    # user_id = event.get_user_id()
    # # head_url = f"https://q.qlogo.cn/g?b=qq&nk={user_id}&s=640"#QQ头像地址
    # try:
    #     with open(file,'r') as a:
    #         notice = json.load(a)
    #     notice_content = notice[group_id]
    # except:
    #     notice_content = '欢迎新成员的加入!'

    # description = json.loads(event.get_event_description().replace("'",'"'))

    # if description['notice_type'] == 'group_increase':
    #     await GroupMemNotice.finish(
    #                                 MessageSegment.at(user_id) + f""
    #                                 )

GroupNoticeswitch = on_command('进退群提醒',priority=5,block=True,permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)
@GroupNoticeswitch.handle()
async def GroupNoticeswitch_(event:Event):
    group_id = str(event.get_session_id()).split('_')[1]
    print(group_id)
    try:
        with open(file,'r') as f:
            content = json.load(f)
    except FileNotFoundError:
        open(file,'w')
        content = {}
    f.close

    try:
        switch = content[group_id]
    except KeyError:
        switch = '0'
    
    if switch == '1':
        switch = '0'
    else:
        switch = '1'

    data = {group_id:switch}
    content.update(data)

    with open(file,'w') as f_new:
        json.dump(content,f_new)

    if switch == '1':
        await GroupNoticeswitch.finish('进退群提醒已开启')
    elif switch == '0':
        await GroupNoticeswitch.finish('进退群提醒已关闭')
    else:
        await GroupNoticeswitch.finish('进退群提醒错误,请检查日志!')


async def create_document():#检查有没有数据库,没有就创建,有就pass
    try:
        import os
        os.mkdir(path)
        print('<reate floder cuccesful>')
    except FileExistsError:
        pass
    try:
        f = open(path+'\\GroupInOrDecreaseNotice.json','r')
    except FileNotFoundError:
        f = open(path+'\\GroupInOrDecreaseNotice.json','w')
        f.close()
        print('<create documen cuccesful>')
    print('<create_document() handed>')


test = on_notice()
@test.handle()
async def _(event:NoticeEvent):
    print(event.get_event_description())
