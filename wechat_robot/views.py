from fastapi import Depends

from wechat_robot.handlers.wxsignature import WxSignatureHandler
from wechat_robot.request_model import WxCheckAuth


async def wx_check_auth(item: WxCheckAuth = Depends(WxCheckAuth)):
    signature = item.signature or ""
    timestamp = item.timestamp or ""
    nonce = item.nonce or ""
    
    auth, result = await WxSignatureHandler.auth_service(signature, timestamp, nonce)
    if auth:
        return ""
    return item.echostr or ""