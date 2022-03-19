from fastapi import FastAPI
from wechat_robot.urls import api_router

app = FastAPI(
    title="公众号自动回复系统",
    description=f"用于公众号“做一只蛋挞”自动回复信息"
)


@app.on_event('startup')
async def startup_event():
    app.include_router(api_router)