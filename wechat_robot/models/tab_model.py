""" - """
from tortoise import fields
from tortoise.models import Model

from wechat_robot.constants.enums import TabScene, TabStatus

class TabModel(Model):
    """-"""
    id = fields.IntField(pk=True)
    level = fields.IntField(default=0, description='tab所处于层级')
    sort = fields.IntField(default=0, description='排序')
    name = fields.CharField(max_length=16, default='', description="tab名")
    description = fields.CharField(max_length=64, default='', description="描述")
    status = fields.CharEnumField(enum_type=TabStatus, default=TabStatus.normal.value, description="状态")
    code = fields.CharField(max_length=16, default='', description="识别码")
    pid = fields.IntField(default=0, description='父级id')
    scene = fields.CharEnumField(enum_type=TabScene, default='', description="场景")
    
    class Meta:
        """Meta"""
        app = "wechat"
        table = "tab_table"
        
    def to_dict(self):
        """to dict"""
        return {
            "id": self.id,
            "level": self.level,
            "sort": self.sort,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "code": self.code,
            "pid": self.pid,
            "scene": self.scene
        }
    