import asyncio
import logging

from .api.api import server_task
from .shared.logger import logger_init
from .shared.settings import settings_store

settings = settings_store.settings

logger_init("test_reader_side")

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


async def _main1():

    from .db.database import test1

    await test1()

    await asyncio.sleep(0)


def main() -> None:
    """Entry point."""

    async def _main() -> None:
        done, _ = await asyncio.wait(
            [
                # asyncio.create_task(_main1()),
                asyncio.create_task(server_task(settings.API_PORT)),
                # asyncio.create_task(reader_side.task()),
                # asyncio.create_task(opcua.task()),
            ],
            return_when=asyncio.FIRST_COMPLETED,
        )
        try:
            _ = [done_task.result() for done_task in done]
        except BaseException:  # noqa: WPS424
            log.exception(
                "Необработанное исключение, программа заканчивает выполнение",
            )

    asyncio.run(_main())
