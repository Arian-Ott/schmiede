from abc import ABC, abstractmethod
from enum import StrEnum

from fastapi import APIRouter, FastAPI


class Infrastructure(StrEnum):
    SQL = "SQL"
    REDIS = "REDIS"
    OTEL = "OTEL"


class AbstractModule(ABC):
    def __init__(self, prefix: str = "", tags: list[str] | None = None):
        self.router = APIRouter(prefix=prefix, tags=tags or [])

    @property
    @abstractmethod
    def required_infra(self) -> list[Infrastructure] | None: ...

    @abstractmethod
    def register(self, app: FastAPI) -> None: ...
