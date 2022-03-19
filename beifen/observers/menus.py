# -*- coding:utf-8 -*-

# 处理基类
class Menus(object):  
    def __init__(self) -> None:
        super().__init__()
    def handle(self):
        raise Exception('handle not implemented')