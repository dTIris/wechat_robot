""" - """
from tortoise import fields
from tortoise.models import Model


class NpcModel(Model):
    """-"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=16, default='', description="名字")
    sex = fields.IntField(default=0, description='性别(0：未知，1男，2女)')

    class Meta:
        """Meta"""
        app = "wechat"
        table = "npc_table"
        
    def to_dict(self):
        """to dict"""
        return {
            "id": self.id,
            "name": self.name,
            "sex": self.sex
        }