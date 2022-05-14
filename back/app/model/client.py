from pydantic import BaseModel


class Client(BaseModel):
    login: str
    password: str
    client_id: int
