# -*- coding:utf-8 -*-

from datetime import date, timedelta, datetime
import pymongo
import config as CONFIG

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['wechat']
db.authenticate('iris', '19970721')
task_table = db['task']
clock_table = db['clock']
user_table = db['user']

def a2():
    today = date.today()

    day = today - timedelta(days=1)

    # count = (today - datetime.datetime.strptime(day,"%Y-%m-%d")).days

    print(str(today), str(day))

def main():
    # today = date.today()
    aday = '2021-09-12'
    today = datetime.strptime(aday, '%Y-%m-%d')
    # print(str(date.today()))
    # print(str(today - timedelta(days=1)))
    print(str(today))

    # return ''
    userid = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
    cur = CONFIG.clock_table.find_one({'openid': userid})
    # 判断是否是新用户,新用户则插入
    if not cur:
        cur = {
            'openid': userid, 
            'firstday': str(today), 
            'endday': str(today),
            'fate': 1,
            'persist':1
            }
        s = CONFIG.clock_table.insert_one(cur)
        print (s)
        return ''
        query = CONFIG.clock_rule[1]
        CONFIG.user_table.update_one({'openid': userid}, query)
        return "签到成功。\n 奖励1经验值。"

    endday = cur.get('endday', '')
    # 判断是否已经签到
    if str(today) == endday:
        return '您已签到，请勿重复签到'
    
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
    query = CONFIG.clock_rule.get(fate)
    r1 = clock_table.update({'openid': userid}, cur)
    r2 = user_table.update_one({'openid': userid}, query)
    print(r1)
    print(r2)
    return '签到成功。'+ CONFIG.clock_text_rule.get(fate)

def tt():
    # print(CONFIG.menu_text)  
    userid = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
    # cursors = CONFIG.task_table.find({'openid': userid}, {'_id':0, 'classname':1}).sort('id')
    # cursors = CONFIG.task_table.find({'openid': userid}, {'_id':0, 'classname':1}).sort('id').distinct("classname")
    # print(cursors)
    # for cur in cursors:
    #     print(cur)
    cursors = CONFIG.task_table.find({'openid': userid, 'classname': '?'})
    print(cursors.count())
    # for cur in cursors:
    #     print(cur)

if __name__ == '__main__':
    tt()