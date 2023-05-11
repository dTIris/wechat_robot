""" - """
from .base_manager import BaseManager
from wechat_robot.models import NpcGoodsMappingModel

class NpcGoodsMappingManger(BaseManager):
    """-"""
    model = NpcGoodsMappingModel
    
    def __init__(self):
        super().__init__(model=self.model)
        
    @classmethod
    async def update_or_create(cls, data):
        """新增或者更新记录"""
        params = {
            "npc_id": data['npc_id'],
            "goods_id": data['goods_id']
        }
        _data = await cls.model.filter(**params).first()
        is_created = 0
        if _data:
            _data = await _data.update_from_dict(data)
            await _data.save()
        else:
            _data = await cls.create(data)
            is_created = 1
        return is_created, _data.to_dict()