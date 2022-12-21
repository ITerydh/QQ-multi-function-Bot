from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape
from nonebot.rule import to_me

# 只有艾特机器人才会触发
rule = to_me()


wettr = on_command('天气', aliases={'wttr', 'weather', 'tianqi','天气预报'}, rule=rule, priority=99)


@wettr.handle()
async def _handle(matcher: Matcher, city: Message = CommandArg()):
    if city.extract_plain_text() and city.extract_plain_text()[0]!='_':
        matcher.set_arg('city', city)


@wettr.got('city', prompt='你想查询哪个城市的天气呢？')
async def _(city: str = ArgPlainText('city')):
    if city[0]!='_':
        await wettr.send('猛男夜观星象中...', at_sender=True)
        await wettr.send(MessageSegment.image(file=f'http://zh.wttr.in/{escape(city)}.png', cache=False), at_sender=True)
    else:
        await wettr.reject_arg('city',prompt='不能使用“_”作为查询前缀！请重新输入！')
