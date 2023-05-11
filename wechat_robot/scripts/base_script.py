""" - """
from abc import abstractmethod
import argparse


class BaseScript:
    """-"""

    def __init__(self, script_name="脚本名"):
        self.parse_args(script_name)
        self.edit_parse()
        self.args = self.get_parse()

    def parse_args(self, script_name):
        """-"""
        self.parser = argparse.ArgumentParser(description=script_name)

    @abstractmethod
    def edit_parse(self):
        """
        编辑脚本参数
        parser.add_argument('--object-ids', dest='object_ids', nargs='+', type=int, help='非必须整型参数', required=False)
        group = parser.add_mutually_exclusive_group(required=True) 互斥参数组
        group.add_argument('--all', dest='is_all', action='store_true', help='互斥参数，加上后为真')
        group.add_argument('--not-all', dest='is_all', action='store_false', help='互斥参数，加上后为假')
        """
        pass

    def get_parse(self):
        """-"""
        return self.parser.parse_args()
