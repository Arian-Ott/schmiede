from fastapi import FastAPI

from schmiede.abstract import AbstractModule


class FakeModuleEmpty(AbstractModule):
    def __init__(self):
        super().__init__(prefix="/fake", tags=["fake"])

    @property
    def required_infra(self):
        """We do not have any infra, since this module does not need any
        infra to work"""
        return

    def register(self, app: FastAPI):

        @self.router.get("/returns_true")
        async def returns_true():
            return True

        @self.router.post("/returns_what_came")
        async def what_came(data: dict):
            return data

        app.include_router(self.router)
