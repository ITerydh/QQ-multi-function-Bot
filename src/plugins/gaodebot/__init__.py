import requests
import json
from nonebot import on_command, on_message
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
import config
from nonebot.rule import to_me

# 只有艾特机器人才会触发
rule = to_me()

key, aid, asc, gdkey = config.getToken()


ip = on_command("ip", aliases={"IP查询", "ip查询", "ip定位"}, priority=99, rule=rule)


@ip.handle()
async def openai_img(event: MessageEvent):
    # 获取用户发送的消息
    msg = str(event.get_message()).strip()

    if msg == "":
        await ip.send(MessageSegment.text("请输入IP地址"))
    elif len(msg.split(' ')) != 2:
        await ip.send(MessageSegment.text("请输入IP地址\n例：ip 114.247.50.2"))
    else:
        # 获取参数
        flag = msg.split(' ')[0]
        prompt = msg.split(' ')[1]
        if flag == 'ip' or flag == 'IP' or flag == 'IP查询' or flag == 'ip查询' or flag == 'ip定位':
            try:
                res = await gdGen(prompt)
                if res == '返回接口出问题了':
                    await ip.send(MessageSegment.text("返回接口出问题了！"))
                else:
                    # 返回图片
                    await ip.send(MessageSegment.text(res))
            except Exception:
                await ip.finish(MessageSegment.text("生成失败,请检查参数是否正确"))


async def gdGen(parameters="114.247.50.2"):

    url = f"https://restapi.amap.com/v3/ip?ip={parameters}&output=json&key={gdkey}"

    ip = requests.get(url)

    ip = json.loads(ip.text)

    if ip['status'] != '1':
        return '返回接口出问题了'

    pro = ip['province']
    city = ip['city']
    adcode = ip['adcode']
    if pro == city:
        # 拼接省市和邮编
        msg = "您所在的地区为" + str(pro) + "，邮编为" + str(adcode)
    else:
        # 拼接省市和邮编
        msg = "您所在的地区为" + str(pro) + str(city) + "，邮编为" + str(adcode)

    return msg
