"""Настройки приложения.

Для чтения настроек импортировать:

from src.shared.settings import SettingsSchema, settings_store
settings: SettingsSchema = settings_store.settings
"""

import logging

from pydantic import BaseSettings, Field, PostgresDsn

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.INFO)

ENV_FILE: str = ".env"
ENCODING: str = "utf-8"


class SettingsSchema(BaseSettings):
    """Модель для сохранения настроек."""

    class Config(BaseSettings.Config):
        """Настройки."""

        env_file: str = ENV_FILE
        env_file_encoding: str = ENCODING

    DATABASE_URL: PostgresDsn = Field(
        default="postgresql://user:password@host:port/database",
    )

    API_PORT: int = 8000


class SettingsStore(object):
    """Хранение настроек."""

    __settings: SettingsSchema | None

    def __init__(self) -> None:
        """Хранение настроек."""
        self.__settings = None

    @property
    def settings(self) -> SettingsSchema:
        """Получить настройки.

        Returns
        -------
        Настройки
        """
        if self.__settings is None:
            self.__settings = SettingsSchema()
            print("Settings:", self.__settings.json())  # noqa: WPS421
        return self.__settings


settings_store: SettingsStore = SettingsStore()
