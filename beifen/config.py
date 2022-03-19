# -*- coding:utf-8 -*-

import os
from wechat_sdk import WechatConf
import pymongo
import json

port = 80
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['wechat']
db.authenticate('iris', '19970721')
clock_table = db['clock']
task_table = db['task']
user_table = db['user']
shop_table = db['shop']
special_shop_table = db['special_shop']

conf = WechatConf(
    token = "WeChatForTest",
    appid = "wx1f0043387c3de18d",
    appsecret = "7aee91fa5b6dd8b033ff24e873cfa426",
    encrypt_mode = "normal",
    encoding_aes_key = "vEVaV9GrsREFYOkbKwpHYOsRMGN2jcv2DeAqvQXToqu"
)
settings = {
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'template_path': os.path.join(os.path.dirname(__file__), 'view'),
        'cookie_secret': 'iris_cookie_secret',
        'login_url': '/login',
        'session_secret': "iris_session_secret",
        'session_timeout': 3600,
        'port': port,
        'wx_token':"WeChatForTest"
        }

# 返回模板
textTpl = """<xml> 
    <ToUserName><![CDATA[{}]]></ToUserName> 
    <FromUserName><![CDATA[{}]]></FromUserName> 
    <CreateTime>{}</CreateTime>
    <MsgType><![CDATA[{}]]></MsgType> 
    <Content><![CDATA[{}]]></Content>
</xml>"""

# 游戏参数

# 不明回复
err_text = "不好意思，不能理解您的回复\n您可以"
# 功能未完善
fail_text = "该功能待开发，请输入任意单词返回主菜单"
# 奖励语
reward_text = '奖励如下：\n'
# 分割线
horline = "-------------------\n"
# 选择语
select_text = "请输入序号或名称：\n"
# 查询语
find_text = '查询失败'

# 主菜单命名
main_word = "主菜单"
clock_word = "签到"
task_word = "任务"
record_word = "记录"
user_data_word = "积分"
rule_word = "规则"
shop_word = "商店"
configure_word = "设置"
attribute_word = "属性值"

mainmenu = [clock_word, task_word, record_word, user_data_word, rule_word, shop_word, configure_word]

# 主菜单介绍
menu_text = select_text + horline
for id, menu in enumerate(mainmenu):
    menu_text += '{}：【{}】\n'.format(id+1, menu)

# 属性值对应表
attribute = {
    'coins': '金币',
    'experience': '经验值',
    'charm': '魅力',
    'energy': '活力',
    'strength' : '体力',
    'patience': '耐力',
    'wisdom': '智力',
    }
# 背包对应表
package = {
    ""
    }

# 签到奖励表
clock_reward_map = {
    1:{"experience": 1},
    2:{"experience": 3},
    3:{"experience": 4},
    4:{"experience": 6},
    5:{"experience": 7},
    6:{"experience": 9},
    7:{"experience": 10, "coins": 5, "patience": 1}
    }
# 签到结果表
clock_result_map = {
    -1: '签到失败，请稍后重试',
    0: '您已签到，请勿重复签到',
    1: "恭喜你，首次签到成功。\n"+horline,
    2: "签到成功。\n"+horline
    }

# 任务菜单语
task_text = '您的{}菜单：\n'+horline
# 任务奖励语
task_reward_text = '{}任务'+reward_text+horline

# 积分查询语
user_text = '您的积分情况如下:\n'

# 规则
rule_text = '''亲爱的玩家，欢迎来到人生打卡通关系统~
这是一个让你记录待办事项的地方
我们希望您在体验的过程如玩游戏一样
你需要依靠完成任务来获得经验值和金币
同时也可以提高自己的属性和获取特殊奖品
你将拥有「魅力」、「体力」、「智力」、「耐力」、「活力」五个属性
是否查询详细规则
    1:【是的】\n\t
    '''
# 签到规则
clock_rule = '签到规则如下：\n'+horline
for key, value in clock_reward_map.items():
    for attr, num in value.items():
        clock_rule += '\t第{}天{}+{}\n'.format(key, attribute[attr], num)
# 属性值规则
attr_rule = '属性值规则如下：\n'+horline
for i, _ in enumerate(attribute):
    attr_rule += '{}:{}代表{}\n'.format(i+1, _, attribute[_])
# 商店规则
shop_rule = '商店规则如下：\n'+horline
# 规则二级菜单目录
rule_index_map = {
    1: clock_rule,
    2: attr_rule,
    3: shop_rule
    }
# 规则二级菜单内容
rule_text_map ={
    clock_word: clock_rule,
    attribute_word: attr_rule,
    shop_word: shop_rule,
    }





