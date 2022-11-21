"""Entry point."""

import asyncio
import logging

from .rest.rest import server_task
from .shared.logger import logger_init
from .shared.settings import settings_store

settings = settings_store.settings

logger_init("test_reader_side")

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


async def _main() -> None:
    done, _ = await asyncio.wait(
        [
            asyncio.create_task(server_task(settings.API_PORT)),
        ],
        return_when=asyncio.FIRST_COMPLETED,
    )
    try:
        _ = [done_task.result() for done_task in done]
    except BaseException:  # noqa: WPS424
        log.exception(
            "Необработанное исключение, программа заканчивает выполнение",
        )


def main() -> None:
    """Entry point."""
    asyncio.run(_main())


if __name__ == "__main__":
    main()
