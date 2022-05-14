from app.crud.crud import CRUD
from app.pkg.database.postgresql import Postgresql


class CRUDcomment(CRUD):

    def __init__(
            self,
            database: Postgresql) -> None:
        self.__postgres = database
    
    async def get(self):
        ...

    async def fetch(
            self,
            game_id: int):
        query = """
            select 
                gc.id as "id",
                gc.content as "content",
                gc.game_id as "game_id",
                gc.client_id as "client_id",
                cc.login as "username"
            from game.comment gc
            inner join client.client cc
            on gc.client_id = cc.id
            where game_id = $1;
        """

        effect = await self.__postgres.fetch(
                query,
                game_id
                )
        return effect

    async def create(
            self,
            content: str,
            game_id: int,
            client_id):
        query = """
            insert into game.comment(content, game_id, client_id)
            values($1, $2, $3);
        """
        
        await self.__postgres.create(
                query,
                content,
                game_id,
                client_id
                )

    async def update(self):
        ...

    async def delete(self):
        ...
