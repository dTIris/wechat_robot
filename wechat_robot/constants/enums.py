import enum


class CommonEnum(enum.Enum):
    @classmethod
    def get_members_values(cls):
        """ 获取所有的成员values """
        return [item.value for item in cls.__members__.values()]

    @classmethod
    def get_members_keys(cls):
        """ 获取所有的成员key """
        return [item for item in cls.__members__.keys()]

    @classmethod
    def get_value_by_key(cls, key):
        """根据key值获取value值，value不存时返回key值"""
        return cls.__members__.get(key).value if cls.__members__.get(key) else key

    @classmethod
    def get_members_items(cls):
        """
        获取所有的成员 items
        :return dict
        """
        return {item: getattr(cls, item).value for item in cls.__members__.keys()}


class IntEnum(int, CommonEnum):
    pass


class StringEnum(str, CommonEnum):
    pass


class Method(StringEnum):
    get = "get"
    post = "post"


class TabStatus(StringEnum):
    """-"""
    normal = "normal"  # 正常
    stop = "stop"      # 停用
