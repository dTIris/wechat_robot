# -*- coding:utf-8 -*-

import json

data1 = {"签到", "任务", "记录", "积分", "规则"，"商店"}

data2 = {"学习","猫咪","家政","护肤"}

data3 = {
        "leetcode": [{"" : 5,}
        ]
    }

text1 = '玩家您好，欢迎来到人生打卡通关系统...\n请输入以下选项进行选择：\n'
text2 = '亲爱的玩家 {}，您已签到{}天\n生活奇奇怪怪，万物可可爱爱，元气满满，新的一天正式开启。'
text3 = '请按照分类表的详细行为记录\n如：喂猫'
text4 = '玩家 {}，截止到{}\n您的游戏数据如下所示：\n{}'
text5 = '人生打卡通关系统的规则如下：\n玩家每日通过签到和完成任务等获取金币和积分，得到一定的金币后可去商店兑换奖品'

data = {
    "初始化1": text1,
    "初始化2": data11,
    "签到": text2,
    "分类": data2,
    "记录": text3,
    "积分": text4,
    "规则": text5
}

with open('config/classify.json', 'w') as f:
    json.dump(data, f)

