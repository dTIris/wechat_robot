# -*- coding:utf-8 -*-

from observers.menus import Menus

import config as CONFIG

class Shop(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.shop_word, self)
    def handle(self, data, users):
        # find_and_modify 当用户金币数达到这个值时才可以购买
        return '暂时未开发该功能'
