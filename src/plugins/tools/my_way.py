import imp
import re,os
from .switch import *

####################
switch_reply_car = ['562294259']
####################


class way:
    def get_group_id(text:str):
        ids = (re.findall('\d{1,11}',text))[::-1]
        print(ids)
        try:
            ids[1]
            print(ids[1])
        except:
            return None
        return ids[1]
    
    def switch(text:str,group_id:str) -> bool:
        if group_id in eval(text):
            return True
        return False

