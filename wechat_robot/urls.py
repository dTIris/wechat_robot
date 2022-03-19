from fastapi import APIRouter

from wechat_robot.views import wx_check_auth

api_router = APIRouter()

api_router.add_api_route(
    'message_send',
    wx_check_auth,
    methods=['get'],
    summary='接受信息'
)