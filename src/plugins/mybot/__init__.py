from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot import on_command
from nonebot.rule import to_me

# 只有艾特机器人才会触发
rule = to_me()

# 用户发送菜单 bot回复一个菜单列表
menu = on_command("菜单", aliases={"menu", "help", "功能"}, priority=99, rule=rule)


@menu.handle()
async def receive(event: MessageEvent):
    # 获取用户发送的消息
    msg = str(event.get_message()).strip()
    # 如果用户发送的消息是菜单，就回复一个菜单列表
    if msg == "菜单" or msg == "menu" or msg == "help" or msg == "功能":
        await menu.send(MessageSegment.text("菜单如下:\n1.点歌\n2.天气\n3.图片生成\n4.聊天\n5.代码生成\n6.ip查询"))
        await menu.send(MessageSegment.text("格式样例：点歌 你的歌名"))
        await menu.finish(MessageSegment.text("更多功能敬请期待..."))
