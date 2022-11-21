"""Подключение к БД."""

# pyright: reportUnknownMemberType=false

from types import TracebackType
from typing import Generic, Type, TypeVar

import psycopg
from psycopg.rows import class_row
from pydantic import BaseModel

from . import schemas
from ..shared.settings import settings_store

settings = settings_store.settings


T = TypeVar("T", bound=BaseModel)


class Session(Generic[T]):
    """Контекстный менеджер для подключения к БД."""

    __url: str

    def __init__(self, url: str, model: Type[T]) -> None:
        """Контекстный менеджер для подключения к БД.

        Parameters
        ----------
        url: str
            строка подключения к db_data
        model: BaseModel
            модель для получаемых данных
        """
        self.__conn: psycopg.AsyncConnection[T] | None = None
        self.__url = url
        self.__model: Type[T] = model

    async def __aenter__(self) -> psycopg.AsyncConnection[T]:
        """Enter the runtime context related to this object.

        Returns
        -------
        Объект подключения к БД
        """
        self.__conn = await psycopg.AsyncConnection.connect(
            conninfo=self.__url,
            row_factory=class_row(self.__model),
            autocommit=True,
        )
        return self.__conn

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the runtime context related to this object.

        Parameters
        ----------
        exc_type
            exc_type
        exc_value
            exc_value
        traceback
            traceback
        """
        if self.__conn is None:
            return
        await self.__conn.close()


async def test1():
    async with Session[schemas.Hypertable](
        settings.DATABASE_URL,
        schemas.Hypertable,
    ) as session:
        from .crud import read_hypertables

        print(await read_hypertables(session))
