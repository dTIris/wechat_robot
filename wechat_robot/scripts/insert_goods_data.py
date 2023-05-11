""" 
游戏-商品入库脚本
执行命令: python -m wechat_robot.scripts.insert_goods_data -file goods.txt --log
"""

import asyncio
import os
import logging
from wechat_robot import app
from wechat_robot.model_managers.goods_manager import GoodsManager
from wechat_robot.lib.tools import to_int
from wechat_robot.scripts.app_ctx import app_context
from wechat_robot.scripts.base_script import BaseScript

logger = logging.getLogger("GoodsAddByFile")


class GoodsAddByFile(BaseScript):
    """-"""

    def edit_parse(self):
        """-"""
        self.parser.add_argument('-file', dest='file_list', required=True, nargs='+', help="读取文件名")
        self.parser.add_argument('--log', dest='need_log', default=False, action="store_true", help="是否需要日志输出")

    def get_data(self, file_name, need_log=False):
        """-"""
        cur_path = os.getcwd()
        file_path = os.path.join(cur_path, 'wechat_robot/scripts/datas/' + file_name)
        goods_datas = []
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if not line or '——' not in line:
                    continue
                data = line.split('——')
                name = (data[0] or "").strip()
                price = to_int((data[1] or "").replace("G", ""))
                goods_datas.append({
                    "name": name,
                    "price": price,
                    "category": "default"
                })
        return goods_datas

    async def run(self):
        """-"""
        async with app_context(app):
            file_list = self.args.file_list
            need_log = self.args.need_log
            for file_name in file_list:
                goods_datas = self.get_data(file_name)
                if need_log:
                    print('goods_datas', goods_datas)
                    logger.info(f"insert goods_datas {goods_datas}")
                await GoodsManager().bulk_create(goods_datas)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(GoodsAddByFile("GoodsAddByFile").run())
    loop.run_until_complete(task)
