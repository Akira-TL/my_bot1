from email import message
from nonebot import on_keyword, on_message
from pydantic import BaseSettings


# test = on_keyword("测试", priority=2)
# @test.handle()
# async def test_():
#     await test.send(
#         message = "成功"
#     )

class Config(BaseSettings):
    # Your Config Here
    # matcher = on_request()

    # @matcher.type_updater
    # async def update_type():
    # return "message"



    class Config:
        extra = "ignore"