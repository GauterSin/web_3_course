from fastapi import APIRouter, Header
from app import handler_comment as handler
from app.api.schema.comment import CreateComment


router = APIRouter()


@router.get('/get')
async def get(game_id: int):
    effect = await handler.get(
            game_id=game_id
            )
    return effect


@router.post('/create')
async def create(
        arg: CreateComment,
        client_id: int = Header(...)
        ):
    await handler.create(
            game_id=arg.game_id,
            client_id=client_id,
            content=arg.content
            )
