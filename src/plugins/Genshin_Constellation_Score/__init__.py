from nonebot.plugin import on_regex
from nonebot.typing import T_State
from nonebot.params import State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment

# from .utils import score


# score_constellation = on_regex(r"^/?圣遗物评分$", priority=50)

# @score_constellation.got("constellation_pic", prompt="请发送圣遗物的图片！")
# async def main(bot: Bot, event: MessageEvent, state: T_State = State()):
#     pic_cqcode = str(state["constellation_pic"])
#     user_id = event.get_user_id()
#     if "CQ:image" in pic_cqcode:
#         is_main_attr_valid, val = await score(score_constellation, pic_cqcode, user_id)

#         if val != 0:
#             await score_constellation.finish(MessageSegment.at(user_id) +
#                                              "\n主词条是否为暴击/暴伤：" + is_main_attr_valid +
#                                              "\n圣遗物双暴评分：" + str(val))
#         else:
#             await score_constellation.finish(MessageSegment.at(user_id) + "圣遗物评分为0...\n"
#                                                                           "也有可能是输入了错误的图片或图片不清晰！")
#     else:
#         await score_constellation.finish(MessageSegment.at(user_id) + "输入格式有误，请重新触发指令！")
