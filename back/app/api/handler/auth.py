from app.crud import CrudCollector
import bcrypt
from app.pkg.exception.exception import (
        UnauthorizedException,
        UnauthorizedPassowrdCheckerException,
        UnauthorizedMoreSessionException
        )
from uuid import uuid4
import asyncio


class Handler:

    def __init__(
            self,
            crud: CrudCollector):
        
        self.__crud = crud 

    async def __delete_session(
            self,
            session_list: list):
        for s in session_list:
            yield s
    
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

        session_effect = await self.__crud.signature.get_list(
                client_id=effect.client_id
                )

        if len(session_effect) >= 5:
            await self.__crud.signature.delete(
                    key=str(effect.client_id)
                    )
            async for i in self.__delete_session(session_effect):
                await self.__crud.signature.delete(
                        key=i
                        )
            raise UnauthorizedMoreSessionException()

        # await asyncio.gather(
        #     self.__crud.signature.create(
        #         signature=signa,
        #         client_id=effect.client_id),
        #     self.__crud.signature.rpush(
        #         client_id=effect.client_id,
        #         value=signa)
        #         )

        await self.__crud.signature.create(
                signature=signa,
                client_id=effect.client_id)

        await self.__crud.signature.rpush(
                client_id=effect.client_id,
                value=signa
                )

        return signa

    async def signup(
            self,
            login: str,
            password: str,
            password_2: str):
        
        if password != password_2:
            raise UnauthorizedPassowrdCheckerException()

        hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
                )

        await self.__crud.client.create(
                login=login,
                password=hashed_password.decode('utf-8')
                )
