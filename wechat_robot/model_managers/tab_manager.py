""" - """
from .base_manager import BaseManager
from wechat_robot.models import TabModel

class TabManager(BaseManager):
    """-"""
    model = TabModel
    
    def __init__(self):
        super().__init__(model=self.model)
        
    @classmethod
    async def get_sub_list_with_value(cls, tab_id, value):
        """-"""
        filter_params = {'pid': tab_id}
        return await cls.model.filter(**filter_params).order_by("sort").values_list(value, flat=True)
        
