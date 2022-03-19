# -*- coding:utf-8 -*-

from observers.menus import Menus
from datetime import date, timedelta

import config as CONFIG

class Clock(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.clock_word, self)
        
    def handle(self, data, users):
        today = date.today()
        userid = data['UserName']
        cur = CONFIG.clock_table.find_one({'openid': userid})
        # users[userid] = -1
        
        # 判断是否是新用户,新用户则插入
        if not cur:
            cur = {
                'openid': userid, 
                'firstday': str(today), 
                'endday': str(today),
                'fate': 1,
                'persist':1
                }

            CONFIG.clock_table.insert_one(cur)
            query = {'$inc': CONFIG.clock_reward_map.get(1)}
            CONFIG.user_table.update_one({'openid': userid}, query)
            # print('新用户{}签到成功。'.format(userid))
            result = CONFIG.clock_result_map[1]
            result += "{}{}".format(CONFIG.reward_text, CONFIG.horline)
            clock_reward = CONFIG.clock_reward_map.get(1)
            for _ in clock_reward:
                result += '{}+{}\n'.format(CONFIG.attribute.get(_), clock_reward[_])

            return result
           
        endday = cur.get('endday', '')
        # 判断是否已经签到
        if str(today) == endday:
            return CONFIG.clock_result_map[0]
        
        # 判断是否连续签到
        if str(today - timedelta(days=1)) == endday:
            cur['fate'] = cur.get('fate', 0)+1
            cur['persist'] = cur.get('persist', 0)+1
            cur['endday'] = str(today)
        else:
            cur['fate'] = 1
            cur['firstday'] = str(today)
            cur['endday'] = str(today)
            cur['persist'] = cur.get('persist', 0)+1

        fate = cur['fate'] if cur['fate'] < 7 else 7
        query = {'$inc': CONFIG.clock_reward_map.get(fate)}
        update_result = CONFIG.clock_table.update({'openid': userid}, cur)
        # 签到成功则用户表新增数据
        if update_result.get('nModified', 0) == 1:
            CONFIG.user_table.update_one({'openid': userid}, query)
            result = CONFIG.clock_result_map[2]
            result += "{}{}".format(CONFIG.reward_text, CONFIG.horline)
            clock_reward = CONFIG.clock_reward_map.get(fate)
            for _ in clock_reward:
                result += '{}+{}\n'.format(CONFIG.attribute.get(_), clock_reward[_])
            return result
        else:
            return CONFIG.clock_result_map[-1]
