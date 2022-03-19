# -*- coding:utf-8 -*-

from datetime import date, timedelta, datetime
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['wechat']
db.authenticate('iris', '19970721')
task_table = db['task']
clock_table = db['clock']
user_table = db['user']

def a3():
    data = {}
    # data['openid'] = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
    data['openid'] = 'oALMC6WYcP0UXNhEhuUxkrj_7-jc'
    data['coins'] = 0
    data['experience'] = 0
    data['strength'] = 0
    data['charm'] = 0
    data['energy'] = 0
    data['patience'] = 0
    data['wisdom'] = 0
    result = user_table.insert_one(data)
    # result = user_table.update({'openid': data['openid']}, {'$inc': {'coins': 4}})
    print(result)
    # cur = task_table.distinct('classname', {'openid':  'oALMC6XKieHpEqdBStP2EhzY5ALs'})
    # print(cur)

def a1():
    classname = ['学习', '猫咪', '护肤', '家政']
    subname1 = ['leetcode', '编程笔记', '阅读半小时', '日语学习']
    subname2 = ['铲屎', '喂猫', '剪指甲', '内外驱虫', '洗澡']
    subname3 = ['修复面膜', '美白面霜']
    subname4 = ['扫地拖地', '洗晾衣服', '做饭洗碗', '整理柜子']

    d = {}
    d[classname[0]] = subname1
    d[classname[1]] = subname2
    d[classname[2]] = subname3
    d[classname[3]] = subname4


    i = 0
    for d1 in d:
        i += 1
        j = 0
        for d2 in d[d1]:
            j += 1
            data = {}
            data['openid'] = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
            data['id'] = i
            data['classname'] = d1
            data['sub_id'] = j
            data['subclassname'] = d2
            data['coins'] = 1
            data['experience'] = 5
            data['strength'] = 0
            data['charm'] = 0
            data['energy'] = 0
            data['patience'] = 0
            data['wisdom'] = 0
            try:
                task_table.insert_one(data)
            except Exception as e:
                print(e)
                break

            print(data['classname'], data['subclassname'], '-插入成功')

def a2():
    today = datetime.date.today()

    day = today - datetime.timedelta(days=1)

    # count = (today - datetime.datetime.strptime(day,"%Y-%m-%d")).days

    print(str(today), str(day))

def a4():
    a = ['1', '2','3']
    for i, s in enumerate(a):
        print(i, s)

def main():
    userid = 'oALMC6XKieHpEqdBStP2EhzY5ALs'
    text = ''
    cursors = task_table.find({'openid': userid,'classname': '猫咪'}, {'_id': 0, 'sub_id':1, 'subclassname':1})
    for cur in cursors:
        text += '{}: 【{}】\n'.format(cur.get('sub_id', ''), cur.get('subclassname', ''))
    print(text)
if __name__ == '__main__':
    # main()
    a3()