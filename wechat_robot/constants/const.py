DEFAULT = "default"

class ErrorCode:
    state_error = "用户状态错误"
    type_error = "暂时无法处理该类型的消息"
    tab_error = "用户tab错误"
    
SEPARATOR_LIST = ["-", "_", " ", "/", ",", "|"]

REMIND_TXT = "您好，请输入正确指令"
MAIN_TXT = "你好，这里是主菜单页面：\n  1.游戏\n  2.其他（暂未开发）\n请输入选项或数字进行选择"
GAME_TXT = "你好，这里是游戏页面：\n  1.npc\n  2.物品\n  0.返回\n  -1.退出\n请输入选项或数字进行选择"
GOODS_TXT = "你好，这里是物品页面：\n  1.npc\n  2.物品\n  0.返回\n  -1.退出\n请输入选项或数字进行选择"

TXTMAPPING = {
    "退出": '0',
    "返回": '-1'
}

NUMBERS = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

STATE_MAPPING = {
    "主菜单": 1,
    "游戏": 2,
    "npc": 3,
    "物品": 4,
}