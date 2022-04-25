import requests
from nonebot import on_keyword, on_regex
from nonebot.adapters.onebot.v11 import (
    Event,
    Message,
    MessageSegment,
)

def create_document():
    try:
        import os
        path = 'F:\document\OneDrive - 南京农业大学\My_codes\python\my_bot1\src\plugins\plugin1\db'
        os.mkdir(path)
    except FileExistsError:
        pass
    try:
        f = open(path+'\\GroupInOrDecreaseNotice.json','r')
    except FileNotFoundError:
        f = open(path+'\\GroupInOrDecreaseNotice.json','w')
        f.close()


# a = open('F:\document\OneDrive - 南京农业大学\My_codes\python\my_bot1\src\plugins\plugin1\db\\a.txt','r')

    
create_document()