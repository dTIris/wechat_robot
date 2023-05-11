"""-"""

from wechat_robot.constants.const import GET_MENU_TXT, REMIND_TXT, STATE_MAPPING, TAB_MENU_TXT
from wechat_robot.constants.redis_keys import RedisKeys
from wechat_robot.lib.redis_tools import Cache
from wechat_robot.lib.text_tools import str2list, str2num
from wechat_robot.lib.tools import to_int
from wechat_robot.model_managers.tab_manager import TabManager


class BaseHandler:
    """-"""
    def __init__(self, **kwargs):
        self.tab = kwargs.get('tab')
        self.user = kwargs.get('user')
        self.data = kwargs.get('data')
        self.cache = Cache()
        self.user_tab_key = RedisKeys.user_tab(self.user)
        self.model_manager = kwargs.get('model_manager')
        self.is_list = False
        self.new_data = None
        
    def is_data_list(self, data:str):
        """
        数据预处理，转化列表，返回
            bool(是否转化列表成功),
            成功返回数字，否则返回原有data
        """
        if not data:
            return False, data
        result = str2list(data)
        if result:
            return True, result
        return False, data.strip()

    def is_data_num(self, data:str):
        """
        数据预处理,,转化数字,返回
            bool(是否转化数字成功), 
            成功返回数字, 否则返回原有data
        """
        if not data:
            return False, data
        num = str2num(data)
        if num == '-2':
            return False, data
        return True, num 

    async def is_show_menu(self):
        """
        是否显示菜单页, 返回
            是否结束, True即结束
            data数据
        默认使用get_tab_sub_list: 获取下一页信息
        """
        if self.data == '' or self.data in GET_MENU_TXT:
            description, sub_name_list = await self.get_tab_sub_list()
            return True, TAB_MENU_TXT.format(description, sub_name_list)
        return False, self.data

    async def get_tab_sub_list(self):
        """
        获取子页面列表, 返回
        页面详情信息，子页面名字列表
        """
        sub_name_list = await TabManager.get_sub_list_with_value(self.tab["id"], "alias") or []
        sub_name_txt = ''
        for i, j in enumerate(sub_name_list):
            sub_name_txt += f"  {i+1}:{j}\n"
        return self.tab["description"], sub_name_txt

    async def is_change_tab_with_txt(self, data):
        """
        是否跳转页面，只处理字符为中文的情况，根据中文找出对应数字跳转页面
        """
        num = STATE_MAPPING[data] if data in STATE_MAPPING else 0
        if num == 0:
            return False, data
        tab = await self.get_tab_by_id(num)
        # 找不到跳转页面时，返回提醒
        if not tab:
            return True, REMIND_TXT
        # 跳转页面，并更改用户状态
        await self.cache.set_with_cache_info(self.user_tab_key, tab)
        return True, tab
    
    async def get_tab_by_id(self, tab_id):
        """
        查询tab表信息: tab_id-主键id，返回匹配项的字典类型
        """
        if tab_id < 1:
            return {}
        tab = await TabManager.get_by_id(tab_id)
        print(f'{self.tab["description"]} get_tab_by_id {tab_id}', tab.to_dict())
        return tab.to_dict() if tab else {}
        
    async def is_unrecognized(self):
        """ 
        是否存在无法识别的信息，有需要则可重写
        """
        return False, self.data
           
    async def is_change_tab_with_num(self, data):
        """
        是否跳转页面, 只处理字符为数字的情况, 根据数字找出跳转页面
        """
        num = to_int(data, '')
        if isinstance(num, int):
            tab = await self.get_next_tab(num)
            # 找不到跳转页面时，返回提醒
            if not tab:
                return True, REMIND_TXT
            # 跳转页面，并更改用户状态
            await self.cache.set_with_cache_info(self.user_tab_key, tab)
            return True, tab
        return False, data
    
    async def get_next_tab(self, number: int):
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
        print(f'{self.tab["description"]} get_next_tab number {number}')
        return tab.to_dict() if tab else {}
    
    async def is_show_data(self):
        """
        是否有其他展示信息，有需要则可重写
        """
        return False, self.data
    
    async def execute(self):
        """-"""
        # 解析字符串,是否为字符串
        self.is_list, self.new_data = self.is_data_list(self.data)
        
        # 解析字符串,是否为数字
        data = self.new_data[0] if self.is_list else self.data
        self.is_num, self.data = self.is_data_num(data)
        
        # 是否显示菜单页
        result, self.data = await self.is_show_menu()
        if result:
            return None, self.data

        # 是否能够根据中文跳转页面
        data = self.new_data[0] if self.is_list else self.data
        result, tab = await self.is_change_tab_with_txt(data)
        if result:
            return tab, ','.join(self.new_data[1:]) if self.is_list else ''
        
        # 信息是否无法识别
        result, self.data = await self.is_unrecognized()
        if result:
            return None, self.data
        
        # 是否能够根据数字跳转页面
        data = self.new_data[0] if self.is_list else self.data
        result, tab = await self.is_change_tab_with_num(data)
        if result:
            return tab, ','.join(self.new_data[1:]) if self.is_list else ''
        
        # 是否有其他展示信息
        result, data = await self.is_show_data()
        if result:
            return None, data

        return None, REMIND_TXT
    
    async def get_name_list(self, offset=0, limit=8):
        """
        查询数据库信息: 返回匹配项的name列表
        过滤规则: offset 位移, limit 限制
        """
        sub_name_list = await self.model_manager.get_by_limit_and_value("name", offset, limit)
        sub_name_txt = ''
        for i, j in enumerate(sub_name_list):
            sub_name_txt += f"  {i+1}:{j}\n"
        return self.tab["description"], sub_name_txt
    
    async def get_name_by_id(self, number):
        """
        查询数据库信息：number-主键id，返回匹配项的name
        """
        obj = await self.model_manager.get_by_id(number)
        if not obj:
            return False, {}
        data = obj.to_dict()
        return True, data["name"]