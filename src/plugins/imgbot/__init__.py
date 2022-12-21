import openai
from nonebot import on_command, on_message
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot.rule import to_me
import config

key, _, _,_= config.getToken()

# 设置被艾特才调用
rule = to_me()

img = on_command("img", aliases={"图片", "图像生成", "画图", "绘画",
                 "图片生成", "画画"}, priority=50, rule=rule)


@img.handle()
async def openai_img(event: MessageEvent):
    # 获取用户发送的消息
    msg = str(event.get_message()).strip()
    if len(msg.split(" ")) == 1:
        await img.finish(MessageSegment.text("请输入图像提示词"))
    if len(msg.split(" ")) > 1:
        flag = msg.split(" ")[0]
        prompt = msg.split(" ", 1)[1]
        if flag == "img" or flag == "图片" or flag == "图像生成" or flag == "图片生成" or flag == "画图" or flag == "绘画" or flag == "画画":
            # 先回复一个正在生成的文本消息，再返回图片
            await img.send(MessageSegment.text("正在生成图片..."))
            # 调用openai生成图片
            try:
                imgGen_res = await imgGen(prompt)
                # 返回图片
                await img.send(MessageSegment.image(imgGen_res))
            except Exception:
                await img.send(MessageSegment.text("生成图片失败，请检查提示词是否违禁"))


async def imgGen(prompt):

    def is_contains_chinese(strs):
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False

    if is_contains_chinese(prompt):
        import paddlehub as hub

        model = hub.Module(name='transformer_zh-en', beam_size=5)
        src_texts = [prompt]

        n_best = 1  # 每个输入样本的输出候选句子数量
        trg_texts = model.predict(src_texts, n_best=n_best)
        for idx, st in enumerate(src_texts):
            for i in range(n_best):
                prompt = f'{trg_texts[idx*n_best+i]}'

    openai.api_key = key

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return image_url
