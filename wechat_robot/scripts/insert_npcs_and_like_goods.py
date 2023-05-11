""" 
游戏-居民以及商品映射入库脚本
执行命令: python -m wechat_robot.scripts.insert_npcs_and_like_goods -file npc_goods.txt --log
"""

import asyncio
import os
import logging
import re
from wechat_robot import app
from wechat_robot.model_managers.goods_manager import GoodsManager
from wechat_robot.model_managers.npc_goods_mapping_manager import NpcGoodsMappingManger
from wechat_robot.model_managers.npc_manager import NpcManager
from wechat_robot.models.goods_model import GoodsModel
from wechat_robot.models.npc_goods_mapping_mpdel import NpcGoodsMappingModel
from wechat_robot.scripts.app_ctx import app_context
from wechat_robot.scripts.base_script import BaseScript

logger = logging.getLogger("NpcAddByFile")


class NpcAddByFile(BaseScript):
    """-"""

    def edit_parse(self):
        """-"""
        self.parser.add_argument('-file', dest='file_list', required=True, nargs='+', help="读取文件名")
        self.parser.add_argument('--log', dest='need_log', default=False, action="store_true", help="是否需要日志输出")

    def get_data(self, file_name, need_log=False):
        """-"""
        cur_path = os.getcwd()
        file_path = os.path.join(cur_path, 'wechat_robot/scripts/datas/' + file_name)
        npc_datas = []
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                data = line.split('：')
                name = (data[0] or "").strip()
                description = ''
                match = re.findall("(.+)\((.+)\)", name)
                if match and match[0]:
                    match = match[0]
                    name, description = match
                birthday, goods = (data[1] or "").split(" ")
                npc_datas.append({
                    "name": name,
                    "description": description,
                    "birthday": birthday,
                    "goods": goods.strip().split('、') or []
                })
        print(npc_datas)
        return npc_datas

    async def insert_datas(self, datas):
        """-"""
        for data in datas:
            goods = data.pop("goods")
            _, npc = await NpcManager.update_or_create(data)
            filter_params = {
                "name__in": goods
            }
            good_ids = await GoodsManager.get_values_list_with_params(
                filter_params=filter_params,
                values_list_field='id'
            )
            mapping_datas = [
                {'npc_id': npc['id'], 'goods_id': good_id, "level": 3}
                for good_id in good_ids
            ]
            print('npc', npc["name"], 'goods', goods)
            print('mapping_datas', mapping_datas)
            # if mapping_datas:
            #     await NpcGoodsMappingManger().bulk_create(mapping_datas)

    async def run(self):
        """-"""
        async with app_context(app):
            file_list = self.args.file_list
            need_log = self.args.need_log
            for file_name in file_list:
                npc_datas = self.get_data(file_name)
                if need_log:
                    logger.info(f"insert npc_datas {npc_datas}")
                await self.insert_datas(npc_datas)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(NpcAddByFile("NpcAddByFile").run())
    loop.run_until_complete(task)
