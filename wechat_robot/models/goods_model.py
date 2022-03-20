""" - """
from tortoise import fields
from tortoise.models import Model


class GoodsModel(Model):
    """-"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=16, default='', description="tab名")
    price = fields.IntField(default=0, description='售价（卖出）')
    cost = fields.IntField(default=0, description='成本（买入）')
    description = fields.CharField(max_length=64, default='', description="描述")
    
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
            "cost": self.cost
        }