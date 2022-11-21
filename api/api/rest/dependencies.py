"""Dependencies."""

from typing import Type
from pydantic import BaseModel

from ..db.database import Session


class DbConnection:
    def __init__(self, url: str, model: Type[BaseModel]):
        self.__url = url
        self.__model = model

    async def __call__(self):
        async with Session(self.__url, self.__model) as db:
            yield db
