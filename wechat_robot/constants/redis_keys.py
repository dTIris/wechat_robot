from wechat_robot.lib.redis_tools import CacheInfo

class RedisKeys:
    """-"""
    @staticmethod
    def user_tab(user_name):
        """-"""
        return CacheInfo(f"wx_{user_name}", 3600)