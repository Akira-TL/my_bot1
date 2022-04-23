switch_reply_car = ['562294259']

def switch(text:str,group_id:str) -> bool:
    if group_id in eval(text):
        return True
    return False