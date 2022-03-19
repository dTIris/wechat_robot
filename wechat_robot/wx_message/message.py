""" 
    消息处理器
"""

class MessageHandler:
    def __init__(self, msg) -> None:
        self.msg = msg
        
    async def execute(self):
        """-"""
        msg = self.msg
        # print(msg.id, msg.source, msg.create_time, msg.type, msg.target, msg.time, msg.__dict__['_data'], '====')
        return "你好"
