"""-"""
from aioredis import create_redis_pool, Redis
import ujson as json

from .tools import GetSetTer
import wechat_robot.config as CONFIG

r_pool = GetSetTer()


async def get_redis_pool(rdb_conf, **kwargs) -> Redis:
    """
    redis连接池
    :rdb_conf redis_config
    """
    return await get_redis_pool_with_kwargs(
        host=rdb_conf.host,
        port=rdb_conf.port,
        db=rdb_conf.db,
        password=rdb_conf.password,
        **kwargs
    )


async def get_redis_pool_with_kwargs(host, port, db, password, **kwargs) -> Redis:
    """redis连接池【显式传参】"""
    minsize = kwargs.get('minsize') or 1
    maxsize = kwargs.get('maxsize') or 3
    timeout = kwargs.get('timeout') or 3

    pool = await create_redis_pool(
        f"redis://:{password}@{host}:{port}/{db}?encoding=utf-8",
        minsize=minsize,
        maxsize=maxsize,
        timeout=timeout
    )
    return pool


async def setup_redis(name, conf):
    """
    初始化redis连接池
    name 连接名
    conf redis连接
    """
    redis_conn = await get_redis_pool_with_kwargs(**conf)
    setattr(r_pool, name, redis_conn)


async def get_redis_connection(name=None):
    """获取一个redis连接"""
    name = name or 'default'
    redis_setting = CONFIG.REDIS_SETTINGS.get(name)
    if not redis_setting:
        return None

    if hasattr(r_pool, name):
        return getattr(r_pool, name)

    redis_conn = await get_redis_pool_with_kwargs(**redis_setting)
    setattr(r_pool, name, redis_conn)
    return redis_conn


class CacheInfo:

    def __init__(self, key, timeout=600):
        self.key = key
        self.timeout = timeout


class Cache:
    redis_client = None

    def __init__(self, client=None):
        self.redis_client = client
        if not self.redis_client and hasattr(r_pool, 'default'):
            self.redis_client = getattr(r_pool, 'default')

    async def set(self, key: str, value, timeout=600):
        """设置缓存"""
        value = json.dumps(value)
        await self.redis_client.setex(key, timeout, value)

    async def get(self, key: str):
        """获取缓存"""
        value = await self.redis_client.get(key)
        if value is None:
            return None
        return json.loads(value)

    async def hgetall(self, key: str):
        """获取所有缓存"""
        value = await self.redis_client.hgetall(key)
        if value is None:
            return None
        return value

    async def hincrby(self, key: str, field: str, increment=1):
        """增量缓存"""
        await self.redis_client.hincrby(key, field, increment)

    async def hdel(self, key: str, field, *fields):
        """删除缓存"""
        await self.redis_client.hdel(key, field, *fields)

    async def delete(self, key: str):
        """清除缓存"""
        await self.redis_client.delete(key)

    async def set_with_cache_info(self, cache_info: CacheInfo, value):
        """通过 CacheInfo 设置缓存"""
        return await self.set(cache_info.key, value, cache_info.timeout)

    async def get_with_cache_info(self, cache_info: CacheInfo):
        """通过 CacheInfo 获取str缓存"""
        return await self.get(cache_info.key)

    async def delete_with_cache_info(self, cache_info: CacheInfo):
        """通过 CacheInfo 清除缓存"""
        return await self.delete(cache_info.key)

    async def hgetall_with_cache_info(self, cache_info: CacheInfo):
        """通过 CacheInfo 获取hash缓存"""
        return await self.hgetall(cache_info.key)
