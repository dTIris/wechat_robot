# -*- coding:utf-8 -*-

import config as CONFIG
from observers.menus import Menus

# 处理任务查询
class Record(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.record_word, self)

    def handle(self, data, users):
        pass