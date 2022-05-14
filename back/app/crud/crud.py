from abc import ABC, abstractmethod


class CRUD(ABC):

    @abstractmethod
    async def create(self):
        ...

    @abstractmethod
    async def get(self):
        ...

    @abstractmethod
    async def fetch(self):
        ...

    @abstractmethod
    async def update(self):
        ...

    @abstractmethod
    async def delete(self):
        ...
