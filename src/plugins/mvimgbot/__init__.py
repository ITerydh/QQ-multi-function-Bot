import requests
import json
from nonebot import on_command, on_message
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
import config

key, aid, asc, _ = config.getToken()


img = on_command("美女", aliases={"美女图片"}, priority=99)


@img.handle()
async def openai_img(event: MessageEvent):
    # 获取用户发送的消息
    msg = str(event.get_message()).strip()

    if msg == "美女" or msg == "美女图片":
        # 先回复一个正在生成的文本消息，再返回图片
        await img.send(MessageSegment.text("正在生成图片..."))
        try:
            imgGen_res = await imgGen()
            if imgGen_res == '返回接口出问题了':
                await img.send(MessageSegment.text("返回接口出问题了！"))
            else:
                # 返回图片
                await img.send(MessageSegment.image(imgGen_res))
        except Exception:
            await img.finish(MessageSegment.text("生成图片失败"))


async def imgGen():

    url = "https://www.mxnzp.com/api/image/girl/list/random"

    headers = {
        "app_id": aid,
        "app_secret": asc
    }

    mvimg = requests.get(url, headers=headers)

    mvimg = json.loads(mvimg.text)

    if mvimg['code'] != 1:
        return '返回接口出问题了'

    return mvimg['data'][0]['imageUrl']
