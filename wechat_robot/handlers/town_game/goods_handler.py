from collections import defaultdict
from wechat_robot.constants.const import DEFAULT_LEVEL, GET_MENU_TXT, NPC_GOODS_LEVEL, REMIND_TXT, STATE_MAPPING, TAB_MENU_TXT
from wechat_robot.handlers.base_handler import BaseHandler
from wechat_robot.lib.tools import to_int
from wechat_robot.model_managers.goods_manager import GoodsManager

class GoodsHandler(BaseHandler):
    """-"""

    def gen2txt(self, goods, infos):
        """-"""
        if not infos:
            return f"没有人物喜欢该物品：{goods}"
        data_dict = defaultdict(list)
        for info in infos:
            data_dict[info["level"]].append(info["name"])
        txt = f"{goods}\n"
        for level, level_id in NPC_GOODS_LEVEL.items():
            if level_id not in data_dict:
                continue
            data_txt = ",".join(data_dict[level_id])
            txt += f"{level}该物品的人物是：{data_txt}\n"

        return txt

    async def execute(self):
        """-"""
        # 从某个地方跳回页面
        if self.data == '' or self.data in GET_MENU_TXT:
            description, sub_name_list = await self.get_tab_txt_and_datas(GoodsManager)
            return None, TAB_MENU_TXT.format(description, sub_name_list)
        
        # 数据预处理，中文转数字(字符型)
        _, data = self.pretreatment()
        
       # 字符为数字时的处理，将数字转化为具体物品名字
        if to_int(data) > 0:
            result, data = await self.get_data_in_db(to_int(data), GoodsManager)
            if not result:
                return None, REMIND_TXT
        
        # 字符为数字时的处理，0退出、-1返回
        if isinstance(to_int(data, ''), int):
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

        # 处理非页面跳转申请
        if result:
            goods, level_str = new_data[0], new_data[1]
            level_ids = [NPC_GOODS_LEVEL[level_str]] if level_str in NPC_GOODS_LEVEL else DEFAULT_LEVEL
        else:
            goods, level_ids = data, DEFAULT_LEVEL

        infos = await GoodsManager().get_npc_goods_by_level(goods, level_ids)
        goods_infos = self.gen2txt(goods, infos)
        if result or goods_infos:
            return None, goods_infos
        
        return None, "goods"