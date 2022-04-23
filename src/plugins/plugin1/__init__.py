from pathlib import Path

import nonebot
from nonebot import get_driver, on_keyword, on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"


# @export.xxx
# def some_function():
#     pass

_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").
    resolve()))

