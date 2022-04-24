import requests
from nonebot import on_keyword, on_regex
from nonebot.adapters.onebot.v11 import (
    Event,
    Message,
    MessageSegment,
)

url = 'https://tenapi.cn/acg'
test = on_regex('test',priority=11)
@test.handle()
async def test_(event:Event):
    data = {
        'return':True
    }
    html = requests.get(url,data=data).url
    print(html)
    await test.send(MessageSegment.image('https://tva1.sinaimg.cn/large/dae614afly1fu89q0es5fj21op1c74qp.jpg'))