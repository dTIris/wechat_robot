"""-"""

from wechat_robot.constants.const import SEPARATOR_LIST
from wechat_robot.constants.redis_keys import RedisKeys
from wechat_robot.lib.redis_tools import Cache
from wechat_robot.lib.text_tools import txt2num
from wechat_robot.model_managers.tab_manager import TabManager


class BaseHandler:
    """-"""
    def __init__(self, tab: dict, user: str, data: str):
        self.tab = tab
        self.user = user
        self.data = data
        self.cache = Cache()
        self.user_tab_key = RedisKeys.user_tab(user)

    def parse_data(self, data: str):
        """
        解析数据，返回：
            是否为列表，是则返回列表，否则返回数据本身
        """
        for sep in SEPARATOR_LIST:
            if sep in data:
                return True, data.split(sep)
        return False, data
    
    def pretreatment(self):
        """
        预处理, 返回
            bool(是否转化数字成功), 
            成功返回数字, 不成功返回原有data
        """
        data = self.data.strip()
        num = txt2num(data)
        if num == '-2':
            return False, data
        return True, num 
        
    async def get_next_tab(self, number):
        """ 
            根据数字返回tab页的上下级
            -1为返回上一级
            0为返回主菜单 
        """
        if number == -1:
            tab = await TabManager().get_by_id(self.tab["pid"])
        elif number == 0:
            tab = await TabManager().get_by_id(1)
        else:
            filter_params = {
                "pid": self.tab["id"],
                "sort": number - 1 if number > 0 else number
            }
            tab = await TabManager().get_with_params_first(filter_params)
        return tab.to_dict() if tab else {}
    
    async def get_tab_by_id(self, tab_id):
        """-"""
        if tab_id < 1:
            return {}
        tab = await TabManager.get_by_id(tab_id)
        return tab.to_dict() if tab else {}