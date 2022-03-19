from fastapi.responses import JSONResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

import wechat_robot.config as CONFIG

class WxSignatureHandler:
    async def auth_service(self, signature, timestamp, nonce):
        """ 
        验证服务器有效性
        signature : 微信加密签名
        timestamp : 时间戳
        nonce     : 随机数
        echostr   : 随机字符串
        """
        
        try:
            check_signature(CONFIG.Token, signature, timestamp, nonce)
        except InvalidSignatureException:
            return JSONResponse('错误的请求')

