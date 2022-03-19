# -*- coding:utf-8 -*-
from observers.configure import Configure
import config as CONFIG

class Informer(object):
    def __init__(self):
        self.menus = {}
        self.level = {}
        self.user = {}

    def register(self, key, class_):
        self.menus[key] = class_

    # 分类处理
    def categorize(self, data: dict):
        Content = data.get('Content', '')
        userid = data.get('UserName', '')
        print('用户等级为：', self.user.get(data['UserName'], '无'))

        id_ = self.user.get(userid, -1)
        if id_ == -1:
            Content = CONFIG.main_word
        # 当用户退出时
        if Content == '0' or Content == '返回':
            if id_ > 0 and id_ < 10:
                self.user[userid] = 0
            # 正处于子任务菜单页面中
            elif id_ >10 and id_ < 20:
                Content = CONFIG.task_word
                self.user[userid] = 0
            # 正处于子规则任务菜单中
            elif id_ == 20:
                self.user[userid] = 2
        id_ = self.user.get(userid, -1)
        # 当用户处于主菜单页面时,将序号替换为关键词
        if id_ == 0:
            if Content in [str(i) for i in range(1, len(CONFIG.mainmenu)+1)]:
                Content = CONFIG.mainmenu[int(Content)-1]
        # 当用户处于任务菜单页面时，直接调用任务管理器
        elif id_ == 1:
            Handle = self.menus[CONFIG.task_word]
            result = Handle.handle(data, self.user)
            return result
        elif id_ > 10 and id_ < 20:
            Handle = self.menus[CONFIG.task_word]
            result = Handle.handle(data, self.user)
            return result
        # 当用户处于规则菜单页面时，直接调用规则管理器
        elif id_ == 2 or id_ == 20:
            Handle = self.menus[CONFIG.rule_word]
            result = Handle.handle(data, self.user)
            return result   
        # 当用户处于商城菜单页面时，直接调用规则管理器
        elif id_ == 3:
            return CONFIG.fail_text
        elif id_ == 30:
            return CONFIG.fail_text
        elif id_ > 100 and id_ < 200:
            return CONFIG.fail_text

        # 根据关键词调用管理器
        if Content in self.menus:
            Handle = self.menus[Content]
            result = Handle.handle(data, self.user)
            return result

        # default处理器
        Handle = self.menus[CONFIG.main_word]
        result = Handle.handle(data, self.user)
        return result

