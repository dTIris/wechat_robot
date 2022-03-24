from wechat_robot.constants.const import ErrorCode
from wechat_robot.handlers.town_game.game_handler import GameHandler
from wechat_robot.handlers.town_game.goods_handler import GoodsHandler
from wechat_robot.handlers.town_game.npc_handler import NpcHandler
from .main_handler import MainHandler

class StateHandler:
    handlers = {}  # 状态对应处理模块的字典
    end_states = ['error', 'end']  # 最终状态集合
    def __init__(self, state=None, user=""):
        self.start_state = state
        self.user = user
    
    @classmethod
    def add_state(cls, state_name, handler):
        """-"""
        cls.handlers[state_name] = handler
    
    def set_state(self, state: dict):
        """-"""
        if state:
            self.start_state = state
    
    async def run(self, cargo):
        """-"""
        start_state = self.start_state
        handle_time = 0
        while handle_time < 4:
            print('run', start_state["name"], cargo)
            handler = self.handlers.get(start_state["name"] or "")
            if not handler:
                return False, ErrorCode.state_error
            try:
                handler_ = handler(tab=start_state, user=self.user, data=cargo)
                new_state, cargo = await handler_.execute()
                if not new_state:
                    return False, cargo
                if new_state in self.end_states:
                    return True, cargo
                start_state = new_state
            except Exception as e:
                return False, f"消息处理失败{e}"
            handle_time += 1
        return False, ErrorCode.type_error

StateHandler.add_state("main", MainHandler)
StateHandler.add_state("game", GameHandler)
StateHandler.add_state("npc", NpcHandler)
StateHandler.add_state("goods", GoodsHandler)