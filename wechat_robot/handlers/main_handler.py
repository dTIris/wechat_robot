"""-"""
from wechat_robot.constants.const import GET_MENU_TXT, REMIND_TXT, TAB_MENU_TXT, STATE_MAPPING
from wechat_robot.lib.tools import to_int
from wechat_robot.model_managers.tab_manager import TabManager
from .base_handler import BaseHandler


class MainHandler(BaseHandler):
    """-"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    async def is_unrecognized(self):
        """主菜单页面,无法识别0, -1"""
        if self.data in ['0', '-1']:
            return True, REMIND_TXT
        return False, self.data
