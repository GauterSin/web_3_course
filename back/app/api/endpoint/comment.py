from fastapi import APIRouter, Depends
from app import handler_comment as handler
from app.api.schema.comment import CreateComment
from app.api.depend import auth_validate


router = APIRouter()


@router.get('/get')
async def get(
        game_id: int,
        client_id: int = Depends(auth_validate)):
    effect = await handler.get(
            game_id=game_id
            )
    return effect


@router.post('/create')
async def create(
        arg: CreateComment,
        client_id: int = Depends(auth_validate)
        ):
    await handler.create(
            game_id=arg.game_id,
            client_id=client_id,
            content=arg.content
            )
