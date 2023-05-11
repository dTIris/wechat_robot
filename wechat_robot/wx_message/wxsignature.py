import logging
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

import wechat_robot.config as CONFIG

logger = logging.getLogger("WxSignatureHandler")


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
            check_signature(CONFIG.TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException as e:
            logger.error(e)
            return False, "错误的请求"

        return True, ""
