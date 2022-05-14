from fastapi import FastAPI
from app.pkg.exception.base import BaseExceptionHandler
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app import config
import uvicorn


app = FastAPI()


@app.exception_handler(BaseExceptionHandler)
async def validation_exception_handler(request, exc):
    _ = request
    return JSONResponse(exc.detail, status_code=exc.status_code)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
        router=api_router
        )


if __name__ == '__main__':
    uvicorn.run(
            'main:app',
            host=config.HOST,
            port=config.PORT,
            workers=config.WORKER)
