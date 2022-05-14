from app.crud.crud import CRUD
from app.pkg.database.postgresql import Postgresql
from app.model.client import Client
from app.pkg.exception.exception import UnauthorizedException


class CRUDclient(CRUD):

    def __init__(
            self,
            database: Postgresql) -> None:
        self.__postgres = database
    
    async def get(
            self,
            login: str) -> Client:
        
        query = """
            select
                id as "client_id",
                login,
                password
            from client.client
            where login = $1;
        """
        
        effect = await self.__postgres.fetchrow(
                query,
                login
                )
        if effect is None:
            raise UnauthorizedException()

        return Client(**effect)

    async def fetch(self):
        ...

    async def create(
            self,
            login: str,
            password: str):
        query = """
            insert into client.client(login, password)
            values($1, $2);
        """
        await self.__postgres.create(
                query,
                login,
                password
                )

    async def update(self):
        ...

    async def delete(self):
        ...
