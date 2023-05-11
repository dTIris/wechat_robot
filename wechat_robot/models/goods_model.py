""" - """
from email.policy import default
from tortoise import fields
from tortoise.models import Model

from wechat_robot.constants.enums import GoodsType


class GoodsModel(Model):
    """-"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=16, default='', description="物品名")
    category = fields.CharEnumField(enum_type=GoodsType, default='default', description="物品类别")
    price = fields.IntField(default=0, description='售价（卖出）')
    cost = fields.IntField(default=0, description='成本（买入）')
    description = fields.CharField(max_length=64, default='', description="描述")
    where_is = fields.CharField(max_length=32, default='', description="获取物品地点")
    when_get = fields.CharField(max_length=32, default='', description="解锁时间")
    
    class Meta:
        """Meta"""
        app = "wechat"
        table = "goods_table"
        
    def to_dict(self):
        """to dict"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "cost": self.cost,
            "category": self.category,
            "where_is": self.where_is,
            "when_get": self.when_get,
        }