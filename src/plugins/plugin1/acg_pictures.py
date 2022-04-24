import json

import requests
from nonebot import on_keyword, on_regex
from nonebot.adapters.onebot.v11 import (
    Event,
    Message,
)

url = 'https://tenapi.cn/acg'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'}
acg = on_regex('acg',priority=11)
@acg.handle()
async def acg_(event:Event):
    data = {
        'return':True
    }
    html = requests.get(url,data=data).url
    print(html)
    await acg.send(Message(f"[CQ:image,file={html}]"))