from fastapi import APIRouter


router = APIRouter()


@router.post('/signup')
async def signup():
    ...


@router.post('/signup')
async def signin():
    ...
