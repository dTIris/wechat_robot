from fastapi import APIRouter

from wechat_robot.views import wx_check_auth, wk_message_handle

api_router = APIRouter()

api_router.add_api_route(
    '/message_send',
    wx_check_auth,
    methods=['get'],
    summary='微信Token值校验'
)

api_router.add_api_route(
    '/message_send',
    wk_message_handle,
    methods=['post'],
    summary='接受信息并进行处理'
)
