import pytest
from fastapi.testclient import TestClient

from schmiede.core import Schmiede
from tests.fakes.modules import FakeModuleEmpty


def test_enable_returns_schmiede(schmiede):
    assert isinstance(schmiede.enable(FakeModuleEmpty()), Schmiede)


def test_enable_duplicate_raises(schmiede):
    module = FakeModuleEmpty()
    schmiede.enable(module)
    with pytest.raises(ValueError):
        schmiede.enable(module)


def test_build_returns_fastapi(app):
    from fastapi import FastAPI

    assert isinstance(app, FastAPI)


def test_chaining(schmiede):
    from fastapi import FastAPI

    app = schmiede.enable(FakeModuleEmpty()).build()
    assert isinstance(app, FastAPI)


def test_startup_called(schmiede):
    called = []

    def on_start():
        called.append(True)

    app = schmiede.on_startup(on_start).build()

    with TestClient(app):
        pass  # lifespan läuft durch

    assert called == [True]


def test_async_startup_called(schmiede):

    called = []

    async def on_start():
        called.append(True)

    from fastapi.testclient import TestClient

    app = schmiede.on_startup(on_start).build()

    with TestClient(app):
        pass

    assert called == [True]
