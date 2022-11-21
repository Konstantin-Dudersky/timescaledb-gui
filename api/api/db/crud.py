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
