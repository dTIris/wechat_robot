""" - """
from tortoise import fields
from tortoise.models import Model


class NpcGoodsMappingModel(Model):
    """-"""
    id = fields.IntField(pk=True)
    npc_id = fields.IntField(default=0, description='人物id')
    goods_id = fields.IntField(default=0, description='物品id')
    level = fields.IntField(default=0, description='关系程度1: 最喜欢，2: 很喜欢，3: 喜欢，4: 普通，5: 讨厌，6: 很讨厌，0：不喜欢')
    
    class Meta:
        """Meta"""
        app = "wechat"
        table = "npc_goods_mapping"
        
    def to_dict(self):
        """to dict"""
        return {
            "id": self.id,
            "npc_id": self.npc_id,
            "goods_id": self.goods_id,
            "level": self.level
        }