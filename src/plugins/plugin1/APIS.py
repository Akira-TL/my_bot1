#星座运势
import requests,json,re
from nonebot import on_keyword, on_regex
from nonebot.adapters.onebot.v11 import (
    Event,
    Message,
    MessageSegment,
)

meitu = on_regex('美女',priority=11)
# yunshi = on_regex('运势',priority=11)
# url = 'http://api.wpbom.com/api/conste.php'
# @yunshi.handle()
# async def yunshi_(event:Event):
#     message:str = str(event.get_message())
#     message = message.split('_')[0]
#     print(message)
#     data = {
#         'msg':message
#     }
#     html = requests.get(url,data=data).text
#     print(html)
#     # await acg.send(Message(f"[CQ:image,file={html}]"))

url2 = 'https://api.iyk0.com/mtyh/?return=json'
@meitu.handle()
async def meitu_(event:Event):
    data = {
        'return':'True'
    }
    html = requests.get(url2)
    html = json.loads(html.content)
    # html = str(html)
    # html = 'https://tva1.sinaimg.cn/large/dae614afly1fu89lrtp2hj212w0rgkjl.jpg'
    print(html['imgurl'])
    await meitu.send(message=MessageSegment.image('http://p.ananas.chaoxing.com/star3/origin/c3f116e787ad710171f12ffc37940d68.png'))

b404 = on_regex('404',priority=11)
url3 = 'https://api.iyk0.com/bili_chart'
@b404.handle()
async def b404_(event:Event):
    html = requests.get(url3)
    html = json.loads(html.content)
    print(html)
    print(html['img'])
    # html = str(html)
    # html = 'https://tva1.sinaimg.cn/large/dae614afly1fu89lrtp2hj212w0rgkjl.jpg'
    print(html)
    await b404.send(MessageSegment.image(html['img']))

# weather = on_regex('天气',priority=11)
# weather_url = 'https://api.iyk0.com/7rtq'
# @weather.handle()
# async def weather_(event:Event):
#     message = event.get_message()
#     result = re.findall('(.){2}(.){2}[.*]天气',message)
#     city = result.group(0)
#     data = {
#         'city':city
#     }
#     html = requests.get(weather_url,data=json.dump(data))
#     html = json.loads(html.content)
#     if result.group(1) == '天气':
#         # date = re.findall('(.){10}',html['update_time'])
#         date_num = 0
#     elif result.group(1) == '明天':
#         date_num = 1
#     elif result.group(1) == '后天':
#         date_num = 2
#     print(html)
#     print(html['img'][date_num])
#     # html = str(html)
#     # html = 'https://tva1.sinaimg.cn/large/dae614afly1fu89lrtp2hj212w0rgkjl.jpg'
#     print(html)
#     await weather.send(MessageSegment.image(html['img']))

# xxxxx = on_regex('404',priority=11)
# xxxxx_url = 'hurl'
# @xxxxx.handle()
# async def xxxxx_(event:Event):
#     html = requests.get(xxxxx_url)
#     html = json.loads(html.content)
#     print(html)
#     print(html['img'])
#     # html = str(html)
#     # html = 'https://tva1.sinaimg.cn/large/dae614afly1fu89lrtp2hj212w0rgkjl.jpg'
#     print(html)
#     await xxxxx.send(MessageSegment.image(html['img']))