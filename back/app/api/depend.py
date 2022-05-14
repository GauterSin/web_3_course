from app import crud
from fastapi import Header
from app.pkg.exception.exception import UnauthorizedSignatureException


async def auth_validate(
        signature: str = Header(...)
        ):
    
    effect = await crud.signature.get(
            signature=signature
            )

    if effect is None:
        raise UnauthorizedSignatureException()

    return int(effect)
