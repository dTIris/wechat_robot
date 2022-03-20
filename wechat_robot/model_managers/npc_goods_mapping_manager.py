""" - """
from wechat_robot.models import NpcGoodsMappingModel

class GoodsManager:
    """-"""
    model = NpcGoodsMappingModel
    
    @classmethod
    async def get_values_with_params(cls, filter_params, values_field=None):
        """-"""
        return await cls.model.filter(**filter_params).values(*values_field)
    
    @classmethod
    async def get_with_params(cls, filter_params):
        """ 普通查询 """
        return await cls.model.filter(**filter_params)
    
    @classmethod
    async def get_all_with_params(cls, filter_params):
        """ .all """
        return await cls.model.filter(**filter_params).all()
    
    @classmethod
    async def get_values_list_with_params(cls, filter_params, values_list_field=None, flat=True):
        """ .values_list """
        return await cls.model.filter(**filter_params).values_list(values_list_field, flat=flat)