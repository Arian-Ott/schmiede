import inspect
from collections.abc import Callable
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from schmiede.abstract import AbstractModule


class Schmiede:
    def __init__(self) -> None:
        self._modules: list[AbstractModule] = []
        self._startup: list[tuple[Callable, tuple, dict]] = []
        self._shutdown: list[tuple[Callable, tuple, dict]] = []
        self._middleware: list[tuple[type, dict]] = []
        self._app = FastAPI(summary="powered by Schmiede")
    def enable(self, module: AbstractModule) -> "Schmiede":
        """Enables a module in Schmiede.

        :param module: Module to be enabled.
        :type module: AbstractModule
        :raises ValueError: Module is already enabled.
        :return: Initialised object of Schmiede.
        :rtype: Schmiede
        """
        if module in self._modules:
            raise ValueError(
                f"Module {module.__class__.__qualname__} already registered."
            )
        self._modules.append(module)
        return self

    def on_startup(
        self, func: Callable[..., None], *args: Any, **kwargs: Any
    ) -> "Schmiede":
        """Adds startup behaviour.

        :param func: Generator to be called at startup.
        :type func: Callable[..., None]
        :return: Initialised object of Schmiede.
        :rtype: Schmiede
        """
        self._startup.append((func, args, kwargs))
        return self

    def on_shutdown(
        self, func: Callable[..., None], *args: Any, **kwargs: Any
    ) -> "Schmiede":
        """Adds shutdown behaviour.

        :param func:  Generator to be called at shutdown.
        :type func: Callable[..., None]
        :return: Initialised object of Schmiede.
        :rtype: Schmiede
        """
        self._shutdown.append((func, args, kwargs))
        return self

    def add_middleware(
        self, middleware_class: type, **options: Any
    ) -> "Schmiede":
        """Adds a middleware to Schmiede.

        :param middleware_class: A valid Middleware
        :type middleware_class: type
        :return: Initialised object of Schmiede.
        :rtype: Schmiede
        """
        self._middleware.append((middleware_class, options))
        return self

    def build(self) -> FastAPI:
        """Builds a FastAPI with all Schmiede initialisations.

        :return: FastAPI object.
        :rtype: FastAPI
        """

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            for func, args, kwargs in self._startup:
                await func(*args, **kwargs) if inspect.iscoroutinefunction(
                    func
                ) else func(*args, **kwargs)
            yield
            for func, args, kwargs in self._shutdown:
                await func(*args, **kwargs) if inspect.iscoroutinefunction(
                    func
                ) else func(*args, **kwargs)

        self._app.router.lifespan_context = lifespan

        for middleware_class, options in self._middleware:
            self._app.add_middleware(middleware_class, **options)

        for module in self._modules:
            module.settings_checker()
            module.register(self._app)

        return self._app

