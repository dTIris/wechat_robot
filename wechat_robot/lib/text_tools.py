from collections import defaultdict
import cn2an
from wechat_robot.constants.const import NPC_GOODS_LEVEL, SEPARATOR_LIST, STATE_MAPPING, TXTMAPPING, NUMBERS

def str2list(data: str):
    """
    数据转列表，是则返回列表，否则返回False
    """
    for sep in SEPARATOR_LIST:
        if sep in data:
            return data.split(sep)
    return False

def str2num(data: str, default_num='-2'):
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

def gen_data_with_infos(name, infos, default_txt='', format_txt=''):
    """根据信息生成数据"""
    if not infos:
        return default_txt.format(name)
    data_dict = defaultdict(list)
    for info in infos:
        data_dict[info["level"]].append(info["name"])
    txt = f"{name}\n"
    for level, level_id in NPC_GOODS_LEVEL.items():
        if level_id not in data_dict:
            continue
        data_txt = ",".join(data_dict[level_id])
        txt += format_txt.format(level,data_txt)

    return txt