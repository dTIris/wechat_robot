from wechat_robot.lib.redis_tools import CacheInfo


class RedisKeys:
    """缓存key"""

    @staticmethod
    def user_tab(user_name):
        """用户所在tab"""
        return CacheInfo(f"wx_{user_name}", 3600)
