import aioredis

__all__ = ['Redis']


class Redis:

    __connection: aioredis.ConnectionPool | None = None

    def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
            db: str
    ) -> None:
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db = db
        self.__pool: aioredis.ConnectionPool | None = None

    def __create_dsn(self):
        return f"""redis://{self.__host}:{self.__port}/{self.__db}"""

    async def __create_connector(self) -> aioredis.Redis:
        if self.__pool is None:
            self.__pool = aioredis.ConnectionPool.from_url(
                    self.__create_dsn(),
                    max_connections=10
            )
        #return await aioredis.Redis(
        #        connection_pool=self.__pool,
        #        decode_responses=True)

        return await aioredis.from_url(
                self.__create_dsn(),
                decode_responses=True)

    async def get(self, key: str) -> str:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            return await conn.get(name=key)

    async def get_hash(self, key: str) -> dict:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            return await conn.hgetall(name=key)

    async def get_hash_row(self, key: str, sub_key: str) -> str:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            return await conn.hgetall(name=key)[sub_key]

    async def set(self, key: str, value: str, expire: int | None = None):
        redis = await self.__create_connector()
        async with redis.client() as conn:
            await conn.set(
                    name=key,
                    value=value,
                    ex=expire
            )

    async def set_hash(self, key: str, value: dict, expire: int | None = None):
        redis = await self.__create_connector()
        async with redis.client() as conn:
            await conn.hset(
                    name=key,
                    mapping=value
            )
            await conn.expire(name=key, time=expire)

    async def delete_hash(self, key: str) -> None:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            await conn.delete(key)

    async def delete(self, key: list) -> None:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            await conn.delete(*key)

    async def get_ttl(self, key: str) -> int:
        redis = await self.__create_connector()
        async with redis.client() as conn:
            return await conn.ttl(name=key)

    async def rpush_list(self, key: str, value: str):
        redis = await self.__create_connector()
        async with redis.client() as conn:
            await conn.rpush(
                    key,
                    value
                    )
    
    async def get_list(self, key: str, start: int, end: int):
        redis = await self.__create_connector()
        async with redis.client() as conn:
            return await conn.lrange(
                    name=key,
                    start=start,
                    end=end
                    )
        
