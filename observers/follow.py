# -*- coding:utf-8 -*-

from observers.menus import Menus

import config as CONFIG

# 处理关注事件
class Follow(Menus):
    def __init__(self, function_) -> None:
        return function_(1, self)

    def handle(self, data, users):
        pass
