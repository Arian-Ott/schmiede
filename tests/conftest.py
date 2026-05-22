import pytest
from fastapi.testclient import TestClient

from schmiede.core import Schmiede
from tests.fakes.modules import FakeModuleEmpty


@pytest.fixture
def schmiede():
    return Schmiede()


@pytest.fixture
def app(schmiede):
    return schmiede.enable(FakeModuleEmpty()).build()


@pytest.fixture
def client(app):
    return TestClient(app)
