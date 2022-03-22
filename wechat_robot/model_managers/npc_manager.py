""" - """
from tortoise import Tortoise
from wechat_robot.constants.const import DEFAULT_LEVEL
from .base_manager import BaseManager
from wechat_robot.models import NpcModel

class NpcManager(BaseManager):
    """-"""
    model = NpcModel

    @classmethod
    async def get_npc_goods_by_level(cls, npc_name, level_ids=DEFAULT_LEVEL):
        """-"""
        level_str = ','.join([str(level) for level in level_ids])
        sql = f"""
        SELECT
            t3.name,
            t2.`level`
        FROM
            npc_table t1
            INNER JOIN npc_goods_mapping t2 ON t1.id = t2.npc_id
            INNER JOIN goods_table t3 ON t2.goods_id = t3.id
        WHERE
            t1.NAME = "{npc_name}"
            AND t2.`level` in ({level_str})
        """
        
        conn = Tortoise.get_connection('default')
        _, infos = await conn.execute_query(sql, [])
        return infos