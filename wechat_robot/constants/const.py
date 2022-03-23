DEFAULT = "default"

class ErrorCode:
    state_error = "用户状态错误"
    type_error = "暂时无法处理该类型的消息"
    tab_error = "用户tab错误"
    
SEPARATOR_LIST = ["-", "_", " ", "/", ",", "|", ":", "·", "\\"]

REMIND_TXT = "您好，请输入正确指令"
TAB_MENU_TXT = "你好，这里是{}: \n{}请输入选项或数字进行选择"

TXTMAPPING = {
    "退出": '0',
    "返回": '-1'
}

NUMBERS = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

GET_MENU_TXT = [
    "您好",
    "你好",
    "菜单",
    "页面",
    "蛋挞"
]

STATE_MAPPING = {
    "主菜单": 1,
    "游戏": 2,
    "game": 2,
    "人物": 3,
    "居民": 3,
    "npc": 3,
    "物品": 4,
    "商品": 4,
    "食物": 4,
}

NPC_GOODS_LEVEL = {
    "最喜欢": 1,
    "很喜欢": 2,
    "喜欢": 3,
    "普通": 4,
    "讨厌": 5,
    "很讨厌": 6,
    "不喜欢": 0
}

DEFAULT_LEVEL = [1,2,3]