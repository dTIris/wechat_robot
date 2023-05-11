from fastapi import Depends, Body
from fastapi.responses import HTMLResponse, Response
from wechatpy import parse_message, create_reply
from wechat_robot.wx_message.message import MessageHandler

from wechat_robot.wx_message.wxsignature import WxSignatureHandler
from wechat_robot.request_model import WxCheckAuth


async def wx_check_auth(item: WxCheckAuth = Depends(WxCheckAuth)):
    """-"""
    signature = item.signature or ""
    timestamp = item.timestamp or ""
    nonce = item.nonce or ""

    auth, result = await WxSignatureHandler().auth_service(signature, timestamp, nonce)
    if auth:
        result = item.echostr or ""
    return HTMLResponse(content=result)


async def wk_message_handle(body: str = Body(...)):
    """-"""
    msg = parse_message(body)
    if not msg:
        return Response(content="", media_type="application/xml")

    msg_handle = MessageHandler(msg=msg)
    result = await msg_handle.execute()
    reply = create_reply(result, msg)
    return Response(reply.render(), media_type="application/xml")
