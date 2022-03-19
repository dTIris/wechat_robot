# -*- coding:utf-8 -*-

import json

def dict_to_text(**d):
    text = ''
    for key, value in d.items():
        text = '{}: {}'.format(key, value)
    return text

with open("config/classify.json", 'r') as f:
    data = json.load(f)
s = data.get('签到', '')
print(type(s))
print(s.format(3))

a = dict_to_text(**s)
print(a)
