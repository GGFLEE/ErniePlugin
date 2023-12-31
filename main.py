
from core import log, Message, Chain, Equal, AmiyaBotPluginInstance
from .Ernie import Ernie


import os


plugin_dir = os.path.dirname(__file__)
class ErniePlugin(AmiyaBotPluginInstance):
    def install(self):
        # 插件被安装时执行的操作        
        pass
    def uninstall(self):
        pass
bot = ErniePlugin(
    name='Ernie插件',
    version='1.0',
    plugin_id='ernie-plugin',
    description='文心一言web插件',
    plugin_type='GGF',
    document=f'{plugin_dir}/README.md',
    # channel_config_default=...,
    # channel_config_schema=...,
    global_config_default=f'{plugin_dir}/global_config_default.json',
    global_config_schema=f'{plugin_dir}/global_config_schema.json',
    # deprecated_config_delete_days=...,
)


def get_ernie():
    BAIDUID=bot.get_config('BAIDUID')
    BDUSS_BFESS=bot.get_config('BDUSS_BFESS')
    if not BAIDUID or not BDUSS_BFESS:
        raise Exception("ernie缺少配置")
    else:
        return Ernie(BAIDUID,BDUSS_BFESS)



@bot.on_message(keywords='文心')
async def _(data: Message):
    res=get_ernie().ask(data.text[4:])
    if res['imageurls']:
        return Chain(data).image(url=res['imageurls'][0]).text(res['answer'])
    return Chain(data).text(res['answer'])

# @bot.on_event('GUILD_CREATE')
# async def _(event: Event, instance: BotAdapterProtocol):
#     ...