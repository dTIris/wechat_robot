from wechat_robot.constants.const import DEFAULT_LEVEL, GET_MENU_TXT, NPC_GOODS_LEVEL, REMIND_TXT, TAB_MENU_TXT
from wechat_robot.handlers.base_handler import BaseHandler
from wechat_robot.lib.text_tools import gen_data_with_infos
from wechat_robot.lib.tools import to_int
from wechat_robot.model_managers.goods_manager import GoodsManager


class GoodsHandler(BaseHandler):
    """-"""

    def __init__(self, **kwargs):
        self.model_manager = GoodsManager
        super().__init__(model_manager=self.model_manager, **kwargs)

    async def is_show_menu(self):
        """
        是否显示菜单页, 返回
            是否结束, True即结束
            data数据
        get_tab_sub_list: 获取子项信息
        """
        if self.data == '' or self.data in GET_MENU_TXT:
            description, sub_name_list = await self.get_name_list()
            return True, TAB_MENU_TXT.format(description, sub_name_list)
        return False, self.data

    async def is_unrecognized(self):
        """
            goods没有下级页面, 无法处理数字(>0)跳转页面
            数字选项需转为文字, 若找不到文字，则返回提示
        """
        data = to_int(self.data)
        if data > 0:
            result, data = await self.get_name_by_id(to_int(data))
            return (False, data) if result else (True, REMIND_TXT)
        return False, self.data

    async def is_show_data(self):
        """ 
            npc处理非页面跳转信息, 返回
            是否有信息可展示
            展示信息
        """
        if self.is_list:
            npc, level_str = self.new_data[0], self.new_data[1]
            level_ids = [NPC_GOODS_LEVEL[level_str]] if level_str in NPC_GOODS_LEVEL else DEFAULT_LEVEL
        else:
            npc, level_ids = self.data, DEFAULT_LEVEL

        infos = await GoodsManager().get_npc_goods_by_level(npc, level_ids)
        format_txt = "{}该物品的人物是：{}\n"
        default_txt = "没有人物喜欢该物品：{}"
        goods_infos = gen_data_with_infos(npc, infos, default_txt, format_txt)
        if goods_infos:
            return True, goods_infos
        return False, self.data
