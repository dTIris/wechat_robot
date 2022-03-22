from wechat_robot.constants.const import REMIND_TXT, MAIN_TXT
from wechat_robot.handlers.base_handler import BaseHandler
from wechat_robot.lib.tools import to_int

class NpcHandler(BaseHandler):
    """-"""
    async def execute(self):
        """-"""
        # 从某个地方跳回页面
        if not self.data:
            return None, "npc"
        # 数据预处理，中文转数字(字符型)
        _, data = self.pretreatment()
        if to_int(data) > 0:
            return None, REMIND_TXT
        # 字符为数字时的处理
        if data.isdigit():
            tab = await self.get_next_tab(to_int(data))
            if not tab:
                await self.cache.set_with_cache_info(self.user_tab_key, self.tab)
                return None, REMIND_TXT
            await self.cache.set_with_cache_info(self.user_tab_key, tab)
            return None, MAIN_TXT
            
        return None, "npc"