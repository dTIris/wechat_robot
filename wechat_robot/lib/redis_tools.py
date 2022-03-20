"""-"""
from aioredis import create_redis_pool, Redis

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