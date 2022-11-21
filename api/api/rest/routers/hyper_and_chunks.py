"""Hypertables & chunks.

https://docs.timescale.com/api/latest/hypertable/
"""

import logging

from fastapi import APIRouter, Depends, Query
from psycopg import AsyncConnection

from api.db import crud, schemas
from api.shared.settings import settings_store

from ..dependencies import DbConnection

settings = settings_store.settings

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.INFO)

router: APIRouter = APIRouter(
    prefix="/hyper_and_chunks",
    tags=["hyper_and_chunks"],
)


TSchema = schemas.HypertableDetailedSize


@router.get(
    "/hypertable_detailed_size",
    response_model=TSchema,
)
async def hypertables(
    db: AsyncConnection[TSchema] = Depends(
        DbConnection(url=settings.DATABASE_URL, model=TSchema),
    ),
    hypertable: str = Query(),
) -> TSchema:
    """Get detailed information about disk space used by a hypertable.

    Parameters
    ----------
    db
        Сессия для подключения к БД
    hypertable: str
        гипертаблица для вывода размера

    Returns
    -------
    List of hypertables
    """
    return await crud.hypertable_detailed_size(db, hypertable)
