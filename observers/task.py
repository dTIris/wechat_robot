# -*- coding:utf-8 -*-

import config as CONFIG
from observers.menus import Menus

# 处理任务查询
class Task(Menus):
    def __init__(self, function_) -> None:
        return function_(CONFIG.task_word, self)

    def handle(self, data, users):
        # userid = data['UserName']
        userid = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
        result = ''
        id_ = users.get(data['UserName'], -1)
        content = data['Content']

        # 查询任务
        if id_ == 0:
            query = {'_id':0, 'id':1, 'classname':1}
            cursors = CONFIG.task_table.find({'openid': userid}, query).sort('id')
            if cursors.count() == 0:
                return CONFIG.find_text

            result += CONFIG.task_text.format(CONFIG.task_word)
            distinct = set()
            for cur in cursors:
                if cur['id'] not in distinct:
                    distinct.add(cur['id'])
                    result += '{}：【{}】\n'.format(cur['id'], cur['classname'])
            users[data['UserName']] = 1

        # 查询子任务
        elif id_ == 1:
            if content in [str(i) for i in range(10)]:
                query = {'openid': userid,'id': int(content)}
            else:
                query = {'openid': userid,'classname': content}

            myfilter = {'_id': 0, 'id':1, 'classname':1, 'sub_id':1, 'subclassname':1}
            cursors = CONFIG.task_table.find(query, myfilter)
            if cursors.count() == 0:
                return CONFIG.find_text

            result += CONFIG.task_text.format(cursors[0].get('classname'))
            for cur in cursors:
                result += '{}：【{}】\n'.format(cur.get('sub_id'), cur.get('subclassname'))
            users[data['UserName']] = cur.get('id')+10

        # 查询子任务奖励
        elif id_ <20 and id_ >10:
            id_ -= 10
            if content in [str(i) for i in range(10)]:
                query = {'openid': userid, 'id': id_, 'sub_id':int(content)}
            else:
                query = {'openid': userid, 'id': id_, 'subclassname':content}
            myfilter = {'_id':0, 'openid':0, 'id':0, 'classname':0, 'sub_id': 0}
            cursors = CONFIG.task_table.find_one(query, myfilter)
            if cursors.count() == 0:
                return CONFIG.find_text

            result += CONFIG.task_reward_text.format(cursors['subclassname'])
            for cur in cursors:
                if cursors[cur] == 0 or cur not in CONFIG.attribute:
                    continue
                result += '{}+{}\n'.format(CONFIG.attribute[cur], cursors[cur])
            result += CONFIG.horline
        
        else:
            return CONFIG.find_text

        result += '{}：【{}】'.format(0, '返回')
        return result
