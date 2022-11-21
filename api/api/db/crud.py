"""CRUD operations."""

# pyright: reportUnknownMemberType=false

from psycopg import AsyncConnection, AsyncCursor

from . import schemas


async def read_hypertables(
    db: AsyncConnection[schemas.Hypertable],
) -> list[schemas.Hypertable]:
    cur: AsyncCursor[schemas.Hypertable] = await db.execute(
        query="SELECT * FROM timescaledb_information.hypertables",
    )
    return await cur.fetchall()


async def hypertable_detailed_size(
    db: AsyncConnection[schemas.HypertableDetailedSize],
    hypertable: str,
) -> schemas.HypertableDetailedSize:
    """Get detailed information about disk space used by a hypertable.

    Parameters
    ----------
    db
        Сессия БД
    hypertable: str
        гипертаблица для вывода размера

    Returns
    -------
    Инфо о размере таблицы

    Raises
    ------
    ValueError
        Таблица не найдена
    """
    cur = await db.execute(
        query="SELECT * FROM hypertable_detailed_size(%s)",
        params=(hypertable,),
    )
    size = await cur.fetchone()
    if size is None:
        raise ValueError("Unknown table {0}".format(hypertable))
    return size
