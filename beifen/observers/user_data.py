# -*- coding:utf-8 -*-

from observers.menus import Menus

import config as CONFIG

class UserData(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.user_data_word, self)

    def handle(self, data, users):
        result = CONFIG.user_text
        cursors = CONFIG.user_table.find_one({'openid': data['UserName']})
        if not cursors:
            return CONFIG.find_text
        for cur in cursors:
            if cur not in CONFIG.attribute:
                continue
            result += '{}：{}\n'.format(CONFIG.attribute[cur], cursors[cur])

        return result
