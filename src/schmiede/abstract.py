from abc import ABC, abstractmethod
from enum import StrEnum


class Infrastructure(StrEnum):
    SQL = "SQL"
    REDIS = "REDIS"
    OTEL = "OTEL"


class AbstractModule(ABC):
    @property
    @abstractmethod
    def required_infra(self) -> list[Infrastructure] | None: ...

    @abstractmethod
    def register(self) -> None: ...
