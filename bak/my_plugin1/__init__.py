from email import message
from pathlib import Path
from loguru import Message

import nonebot
import json
import requests
from nonebot import get_driver, on_keyword, on_message

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)



# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

__cmd__ = """
@我 0
""".strip()

a = on_message("0")
@a.handle()
async def a_handle():
    Message("成功")



_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").
    resolve()))

