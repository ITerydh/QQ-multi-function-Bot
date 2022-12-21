import config
import openai
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot.rule import to_me

# 只有艾特机器人才会触发
rule = to_me()

key, _, _ ,_= config.getToken()

chat = on_command("gpt", aliases={"对话", "聊天"}, priority=99, rule=rule)


@chat.handle()
async def gpt3chat(event: MessageEvent):

    # 获取用户发送的消息
    msg = str(event.get_message()).strip()
    if len(msg.split(" ")) == 1:
        await chat.send(MessageSegment.text("请输入对话提示（或检查格式）"))
        await chat.send(MessageSegment.text("格式：聊天 你吃饭了吗？"))
    if len(msg.split(" ")) > 1:
        flag = msg.split(" ")[0]
        prompt = msg.split(" ", 1)[1]

        if flag == "对话" or flag == "gpt" or flag == "聊天":
            res = await getres(prompt)
            await chat.finish(MessageSegment.text(res))


async def getres(prompt):

    openai.api_key = key

    # Set the model and prompt
    model_engine = "text-davinci-003"

    # Generate the code
    completion = openai.Completion.create(
        engine=model_engine, prompt=prompt)

    print(completion)

    res = completion.choices[0].text

    return res.strip()
