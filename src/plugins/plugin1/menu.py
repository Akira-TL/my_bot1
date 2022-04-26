from email import message
import json
from tokenize import group
from nonebot import on_command, on_message,on_notice
from nonebot.adapters.onebot.v11 import (
    MessageSegment,
    NoticeEvent,
    Event,
    Bot,

)


#进群和退群时发送消息
# 回复help、帮助、菜单等消息时发送目录和使用方法
help = on_command('help',aliases={'菜单','帮助','Help'},priority=5,block=True)
@help.handle()
async def help_list(event:Event):
    await help.send(message=
        '''
    ====功能菜单表====
     智能秘书|群管系统
     签到系统|金币中心
     娱乐系统|游戏系统
     群管理员|自动改名
     聊天系统|禁止文件
     翻译系统|便民查询
     猜拳游戏|接龙游戏
     黑白名单|抽签游戏
     看图系统|点歌系统
     冒泡系统|问答系统
     邀请统计|基本设置
     更多功能|群内监控
    ====功能菜单表====
    Ps:回复内容进入选项！
    Ps:以上啥都没做

    现在可公开情报:
    美图/acg/404
    其中运势需要带操作符(cmd)例: /运势
    cmd列表:["/","!","！",">"]
    cmd指令:进退群提醒/查询进退群提醒/运势
    更多功能待补充

        '''
        )

