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

    async def fetch(
            self,
            client_id: int):
        
        return await self.__redis.get_hash(
                key=str(client_id)
                )

    async def get_list(self, client_id: int):
        
        return await self.__redis.get_list(
                key=str(client_id),
                start=0,
                end=5)

    async def rpush(self, client_id: int, value: str):
        
        await self.__redis.rpush_list(
                key=str(client_id),
                value=value
                )

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

    async def delete(
            self,
            key: str):
        
        await self.__redis.delete_hash(
                key=key
                )
        
