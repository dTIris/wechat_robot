import cn2an
from wechat_robot.constants.const import TXTMAPPING, NUMBERS

def txt2num(data: str, default_num='-2'):
    """ 
    将中文转化为数字,包括
        中文大写数字: 一 -> 1, 十一 -> 11 
        特殊文本转数字: 退出 -> 0(即返回主菜单), 返回 -> -1(返回上一级)
    """
    if data in TXTMAPPING:
        return TXTMAPPING[data]
    if data[0] in NUMBERS:
        try: 
            num = cn2an.cn2an(data, "smart")
            return str(num)
        except:
            return default_num
    return default_num