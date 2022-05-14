from app.crud.crud import CRUD
from app.pkg.database.redis import Redis


class CRUDsignature(CRUD):

    def __init__(
            self,
            database: Redis) -> None:
        self.__redis = database
    
    async def get(
            self,
            signature: str):
        effect = await self.__redis.get(
                key=signature
                )
        return effect

    async def fetch(self):
        ...

    async def create(
            self,
            signature: str,
            client_id: int
            ):
        await self.__redis.set(
                key=signature,
                value=str(client_id),
                expire=18000)

    async def update(self):
        ...

    async def delete(self):
        ...
