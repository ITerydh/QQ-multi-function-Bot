import config
import openai
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot.rule import to_me

# 只有艾特机器人才会触发
rule = to_me()

key, _, _,_ = config.getToken()


def getcode(prompt):

    openai.api_key = key

    # Set the model and prompt
    model_engine = "text-davinci-002"

    # Generate the code
    completion = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)

    code = completion.choices[0].text

    return code


code = on_command("code", aliases={"代码", "写代码", "代码生成"}, priority=99, rule=rule)


@code.handle()
async def wcode(event: MessageEvent):

    # 获取用户发送的消息
    msg = str(event.get_message()).strip()
    if len(msg.split(" ")) == 1:
        await code.finish(MessageSegment.text("请输入代码提示词"))
    if len(msg.split(" ")) > 1:
        flag = msg.split(" ")[0]
        prompt = msg.split(" ", 1)[1]

        if flag == "代码" or flag == "code" or flag == "写代码" or flag == "代码生成":
            await code.send(MessageSegment.text("正在生成代码..."))
            res_code = getcode(prompt)
            await code.finish(MessageSegment.text(res_code))
