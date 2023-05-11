from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from wechat_robot.config import DB_CONFIG, REDIS_SETTINGS
from wechat_robot.constants.const import DEFAULT
from wechat_robot.urls import api_router
from wechat_robot.lib.redis_tools import setup_redis

app = FastAPI(
    title="公众号自动回复系统",
    description=f"用于公众号“做一只蛋挞”自动回复信息"
)


@app.on_event('startup')
async def startup_event():
    app.include_router(api_router)
    register_tortoise(
        app,
        config=DB_CONFIG,
        generate_schemas=False,
        add_exception_handlers=False,
    )
    await setup_redis(DEFAULT, REDIS_SETTINGS[DEFAULT])
