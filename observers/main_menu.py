# -*- coding:utf-8 -*-

import config as CONFIG
from observers.menus import Menus

# 显示主菜单
class MainMenu(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.main_word, self)

    def handle(self, data, users):
        userid = data['UserName']
        result = ''
        if userid not in users:
            result += CONFIG.err_text
        else:
            result += CONFIG.main_word+','

        result += CONFIG.menu_text
        users[userid] = 0
        return result

