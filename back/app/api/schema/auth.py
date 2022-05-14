from pydantic import BaseModel


class SignUp(BaseModel):
    login: str
    password: str
    password_2: str


class SignIn(BaseModel):
    login: str
    password: str
