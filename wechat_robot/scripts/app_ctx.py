from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def app_context(app):
    """
    app上下文
    >>>
        async with app_context(app):
            pass
    """
    assert isinstance(app, FastAPI), '参数app必须是一个FastAPI类型'
    for func in app.router.on_startup:
        await func()

    try:
        yield app
    finally:
        for func in app.router.on_shutdown:
            await func()
