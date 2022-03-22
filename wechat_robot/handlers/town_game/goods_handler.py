from wechat_robot.constants.const import REMIND_TXT, STATE_MAPPING
from wechat_robot.handlers.base_handler import BaseHandler
from wechat_robot.lib.tools import to_int
from wechat_robot.model_managers.goods_manager import GoodsManager

class GoodsHandler(BaseHandler):
    """-"""
    async def find_good_with_name(self, name):
        """-"""
        goods = GoodsManager.get_all_with_params
    
    async def execute(self):
        """-"""
        # 从某个地方跳回页面
        if not self.data:
            return None, "goods"
        
        # 数据预处理，中文转数字(字符型)
        _, data = self.pretreatment()
        
        # 物品页面没有下级页面，不进行处理
        if to_int(data) > 0:
            return None, REMIND_TXT
        
        # 字符为数字时的处理，0退出、-1返回
        if data.isdigit():
            tab = await self.get_next_tab(to_int(data))
            # 找不到跳转页面时，返回提醒
            if not tab:
                return None, REMIND_TXT
            # 跳转页面，并更改用户状态
            await self.cache.set_with_cache_info(self.user_tab_key, tab)
            return tab, ''
        
        # 解析字符串
        result, new_data = self.parse_data(data)
        # 根据字符串找出对应的页面id
        tab_id = STATE_MAPPING.get(new_data[0], -2) if result else STATE_MAPPING.get(data, -2)
        # 根据页面id找出页面
        tab = await self.get_tab_by_id(tab_id)
        # 找到对应页面则返回新页面并更新用户状态
        if tab:
            await self.cache.set_with_cache_info(self.user_tab_key, tab)
            return tab, new_data[1:] if result else ''
        
        
            
        return None, "goods"