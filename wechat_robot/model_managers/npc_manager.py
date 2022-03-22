""" - """
from .base_manager import BaseManager
from wechat_robot.models import NpcModel

class NpcManager(BaseManager):
    """-"""
    model = NpcModel
