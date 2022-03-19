# -*- coding:utf-8 -*-

from datetime import date
import tornado.escape
import tornado.web
from wechat_sdk import WechatBasic

import re
import time
from observers import informer
import xml.etree.ElementTree as ET

import config as CONFIG

wechat = WechatBasic(conf=CONFIG.conf)

class WxSignatureHandler(tornado.web.RequestHandler):
    # 用来验证服务器有效性
    def get(self):
        signature = self.get_argument('signature', 'defatult')#微信加密签名
        timestamp = self.get_argument('timestamp', 'default')#时间戳
        nonce = self.get_argument('nonce', 'default')#随机数
        echostr = self.get_argument('echostr', 'default')#随机字符串

        if signature == 'defatult' or timestamp == 'defatult' or nonce == 'defatult' or echostr == 'defatult':
            self.write("")
        elif wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write("")

    # 接受用户数据
    def post(self):
        body = self.request.body.decode("utf-8")
        
        data = self.analysis(body)
        print('{}：{}'.format(data['UserName'], data['Content']))
        # 交由处理器处理s
        text = informer.categorize(data)
        print(text)
        answer = CONFIG.textTpl.format(data['UserName'], data['MyName'], int(time.time()), 'text', text)
        self.write(answer)
    
    # 解析xml数据
    def analysis(self, body):
        data = {}
        try:
            tree = ET.fromstring(body)
        except Exception as e:
            print(e)
            return 'error'

        data['MyName'] = tree.find('ToUserName').text
        data['UserName'] = tree.find('FromUserName').text
        data['CreateTime'] = tree.find('CreateTime').text
        data['MsgType'] = tree.find('MsgType').text
        data['MsgId'] = tree.find('MsgId').text
        
        # 分类处理
        # text时，提取内容即可
        if data['MsgType'] == 'text':
            data['Content'] = tree.find('Content').text

        # voice,使用正则过滤文本
        elif data['MsgType'] == 'voice':
            Recognition = tree.find('Recognition').text
            data['Content'] = re.match(r'[\u4E00-\u9FA5]+', Recognition)
        
        return data








