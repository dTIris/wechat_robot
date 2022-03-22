""" - """
from .base_manager import BaseManager
from wechat_robot.models import NpcGoodsMappingModel

class GoodsManager(BaseManager):
    """-"""
    model = NpcGoodsMappingModel