from fastapi import HTTPException
from typing import Any

class BaseExceptionHandler(HTTPException):
    status_code: Any = ...
    detail: Any = ...
    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)
