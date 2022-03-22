""" 
    消息处理器
"""

from wechat_robot.constants.const import ErrorCode
from wechat_robot.constants.enums import TabScene, TabStatus
from wechat_robot.constants.redis_keys import RedisKeys
from wechat_robot.handlers.state_handler import StateHandler
from wechat_robot.lib.redis_tools import Cache
from wechat_robot.model_managers.tab_manager import TabManager

class MessageHandler:
    """-"""
    def __init__(self, msg) -> None:
        # self.msg_id = msg.id
        # self.source = msg.source
        # self.create_time = msg.create_time
        # self.msg_type = msg.type
        # self.target = msg.target
        # self.msg_ts = msg.time
        self.msg_data = msg.__dict__['_data']
        self.cache = Cache()
    
    async def get_tab_list(self):
        """-"""
        filter_params = {
            "status": TabStatus.normal.value,
            "scene": TabScene.menu.value
        }
        menu_tab_list = await TabManager().get_values_with_params(filter_params, "name") or []
        return menu_tab_list
        
    async def get_user_tab(self):
        """-"""
        user_name = self.msg_data.get("FromUserName")
        if not user_name:
            return None
        user_tab_key = RedisKeys.user_tab(user_name)
        user_tab = await self.cache.get_with_cache_info(user_tab_key)
        if not user_tab:
            user_tab_obj = await TabManager.get_by_id(1)
            if not user_tab_obj:
                return None
            user_tab = user_tab_obj.to_dict()
        await self.cache.set_with_cache_info(user_tab_key, user_tab)
        return user_tab
        
    async def execute(self):
        """-"""
        msg_type = self.msg_data.get("MsgType") or ""
        if msg_type != "text":
            return ErrorCode.type_error

        tab = await self.get_user_tab()
        if not tab:
            return ErrorCode.tab_error
        state_handler = StateHandler(tab, self.msg_data.get("FromUserName"))
        _, result = await state_handler.run(self.msg_data.get("Content", ""))
        return result or "你好"
