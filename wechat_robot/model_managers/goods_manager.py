""" - """
from tortoise import Tortoise

from .base_manager import BaseManager
from wechat_robot.models import GoodsModel

class GoodsManager(BaseManager):
    """-"""
    model = GoodsModel
