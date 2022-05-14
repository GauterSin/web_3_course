from app.api.endpoint import (
        auth,
        comment
        )
from fastapi import APIRouter


api_router = APIRouter()


api_router.include_router(
        router=auth.router,
        prefix='/auth',
        tags=['auth']
        )

api_router.include_router(
        router=comment.router,
        prefix='/comment',
        tags=['comment'],
        )
