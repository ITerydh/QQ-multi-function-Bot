# QQAIBot

这是一个QQ机器人功能合集。

目前实现了如下功能：

* [X] 点歌
* [X] 文生图-openai
* [X] 代码生成-openai
* [X] 美女图片-request
* [X] 单次聊天-openai
* [X] 天气预报-request
* [X] ip查询-高德
* [ ] 文生图 其他版本
* [ ] 多轮聊天

## How to start

1. 首先你要有go-cqhttp环境
2. 配置config.json
   你需要在config.py同级目录下新建一个config.json文件

   1) openai-key可以在[openai](https://beta.openai.com/)获取
   2) app_id和app_secret可以在[free-api](https://www.free-api.com/doc/577)
   3) gaode_key可以在[高德](https://console.amap.com/)获取

   ```json
   {
       "openai_key": "sk-xxxxxxxxxxxxxxxx",
       "app_id": "xxxxxxxxxxxxxxxxx",
       "app_secret": "xxxxxxxxxxx",
       "gaode_key": "xxxxxxxxxxxxxxxxx"
   }
   ```
3. 运行bot.py即可


## Copyright and License

**[QQ-multi-function-Bot](https://github.com/ITerydh/QQ-multi-function-Bot)** is provided under the [Apache-2.0 license](https://github.com/PaddlePaddle/Paddle/blob/develop/LICENSE).
