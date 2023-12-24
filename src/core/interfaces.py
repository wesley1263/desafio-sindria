from abc import ABC, abstractmethod


class IBaseRepository(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass


class ICreateRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        pass


class IRetrieveOneByRepository(ABC):
    @abstractmethod
    async def get_one_by(self, **kwargs):
        pass


class IRetrieveAllRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass


class IDeleteRepository(ABC):
    @abstractmethod
    async def delete(self, **kwargs):
        pass
