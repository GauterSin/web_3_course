from fastapi import APIRouter
from app import handler_auth as handler
from app.api.schema.auth import SignIn, SignUp


router = APIRouter()


@router.post('/signup')
async def signup(
        arg: SignUp
        ):
    effect = await handler.signup(
            password=arg.password,
            login=arg.login,
            password_2=arg.password_2
            )
    return effect


@router.post('/signin')
async def signin(
        arg: SignIn
        ):
    effect = await handler.signin(
            password=arg.password,
            login=arg.login,
            )
    return effect
