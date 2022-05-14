from app import crud
from fastapi import Header


async def auth_validate(
        signature: str = Header(...)
        ):
    
    effect = await crud.signature.get(
            signature=signature
            )

    return int(effect)
