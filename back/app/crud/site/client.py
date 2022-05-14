from app.crud.crud import CRUD
from app.pkg.database.postgresql import Postgresql
from app.model.client import Client


class CRUDclient(CRUD):

    def __init__(
            self,
            database: Postgresql) -> None:
        self.__postgres = database
    
    async def get(
            self,
            login: str) -> Client:
        
        query = """
            select * from client.client
            where login = $1;
        """
        
        effect = await self.__postgres.fetchrow(
                query,
                login
                )
        return Client(**effect)

    async def fetch(self):
        ...

    async def create(
            self,
            login: str,
            password: str):
        query = """
            insert into game.comment(login, password)
            values($1, $2);
        """

    async def update(self):
        ...

    async def delete(self):
        ...
