"""API."""

import uvicorn
from fastapi import FastAPI

from .routers import info

api = FastAPI()

api.include_router(info.router)


async def server_task(port: int) -> None:
    """Задача для запуска сервера api.

    Parameters
    ----------
    port: int
        порт
    """
    config = uvicorn.Config(
        api,
        host="0.0.0.0",
        port=port,
        log_level="info",
        reload=True,
    )
    await uvicorn.Server(
        config,
    ).serve()
