from app.crud import CrudCollector


class Handler:

    def __init__(
            self,
            crud: CrudCollector):
        
        self.__crud = crud 

    async def get(
            self,
            game_id: int):
        
        effect = await self.__crud.comment.fetch(
                game_id=game_id
                )

        return effect

    async def create(
            self,
            game_id: int,
            content: str,
            client_id: int):
        
        await self.__crud.comment.create(
                game_id=game_id,
                client_id=client_id,
                content=content
                )
