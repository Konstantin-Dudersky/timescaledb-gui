"""Informational views.

https://docs.timescale.com/api/latest/informational-views/
"""

import logging

from fastapi import APIRouter, Depends
from psycopg import AsyncConnection

from api.db import crud, schemas
from api.shared.settings import settings_store

from ..dependencies import DbConnection

settings = settings_store.settings

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.INFO)

router: APIRouter = APIRouter(
    prefix="/info",
    tags=["info"],
)


@router.get("/hypertables", response_model=list[schemas.Hypertable])
async def hypertables(
    db: AsyncConnection[schemas.Hypertable] = Depends(
        DbConnection(url=settings.DATABASE_URL, model=schemas.Hypertable),
    ),
) -> list[schemas.Hypertable]:
    """List of hypertables.

    Parameters
    ----------
    db
        Сессия для подключения к БД

    Returns
    -------
    List of hypertables
    """
    return await crud.read_hypertables(db)
