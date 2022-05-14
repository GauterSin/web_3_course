from app.crud import CrudCollector
import bcrypt
import base64
import hashlib
from app.pkg.exception.exception import (
        UnauthorizedException,
        UnauthorizedPassowrdCheckerException
        )
from uuid import uuid4


class Handler:

    def __init__(
            self,
            crud: CrudCollector):
        
        self.__crud = crud 
    
    async def signin(
            self,
            login: str,
            password: str) -> str:
        
        effect = await self.__crud.client.get(
                login=login
                )
        
        if not bcrypt.checkpw(
                password=password.encode('utf-8'),
                hashed_password=effect.password.encode('utf-8')):
            raise UnauthorizedException()

        signa = uuid4().__str__()
        
        await self.__crud.signature.create(
                signature=signa,
                client_id=effect.client_id)

        return signa

    async def signup(
            self,
            login: str,
            password: str,
            password_2: str):
        
        if password != password_2:
            raise UnauthorizedPassowrdCheckerException()

        hashed_password = bcrypt.hashpw(
                base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()),
                bcrypt.gensalt()
                )

        await self.__crud.client.create(
                login=login,
                password=hashed_password.decode('utf-8')
                )
