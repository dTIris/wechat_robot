# -*- coding:utf-8 -*-

from observers.menus import Menus

import config as CONFIG

class Rule(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.rule_word, self)
    def handle(self, data, users):
        result = ''
        openid = data['UserName']
        content = data['Content']
        id_ = users.get(openid, -1)

         # 查询规则
        if id_ == 0:
            result += CONFIG.rule_text
            users[openid] = 2

        # 确认查询规则，展示规则菜单
        elif id_ == 2:
            if content != '1' or content != '是的':
                return CONFIG.find_text
            result += CONFIG.select_text
            for i, _ in enumerate(CONFIG.rule_text_map):
                result += '\t{}:【{}】\n'.format(i+1, _)
            users[openid] = 20
        
        # 根据用户输入序号展示详细规则
        elif id_ == 20:
            if content in [str(i) for i in range(len(CONFIG.rule_index_map))]:
                result += CONFIG.rule_index_map.get(int(content), '')
            elif content in CONFIG.rule_text_map:
                result += CONFIG.rule_text_map.get(content, '')
            else:
                return CONFIG.find_text
        
        result += '{}:【{}】'.format(0, '返回')
        return result
