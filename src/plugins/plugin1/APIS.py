#星座运势
import requests,json,re
from nonebot import on_keyword, on_regex
from nonebot.adapters.onebot.v11 import (
    Event,
    Message,
    MessageSegment,
)
from tomlkit import date

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

# weather = on_regex('天气',priority=11)
# @weather.handle()
# async def weather_(event:Event):
#     weather_url = 'https://api.iyk0.com/7rtq'
#     message = str(event.get_message())
#     print(message)
#     # print(type(event.get_message()))
#     result = re.findall('(.{2})(.天)|(.{2})(天气)',message)
#     print(result)
#     city = result[0][2]
#     date = result[0][3]
#     print(city)
#     data = {
#         'city':city
#     }
#     weather_url = weather_url + '/?city=' + city
#     print(weather_url)
#     html = requests.get(weather_url)
#     html = json.loads(html.content)
#     if date == '天气':
#         # date = re.findall('(.){10}',html['update_time'])
#         date_num = 0
#     elif date == '明天':
#         date_num = 1
#     elif date == '后天':
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