__version__ = '0.1.0'

from app.config.config import get_settings
from app.api.handler import (
        comment,
        auth)
from app.pkg.database.postgresql import Postgresql
from app.pkg.database.redis import Redis
from app.crud import CrudCollector
from app.crud.site.comment import CRUDcomment
from app.crud.site.client import CRUDclient
from app.crud.site.signature import CRUDsignature


config = get_settings()


postgres = Postgresql(
        db=config.DB_DATABASE,
        host=config.DB_HOST,
        port=config.DB_PORT,
        password=config.DB_PASSWORD,
        user=config.DB_USERNAME)

redis = Redis(
        db=config.REDIS_DATABASE,
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        password=config.REDIS_PASSWORD,
        user=config.REDIS_USERNAME)


crud = CrudCollector(
        comment=CRUDcomment(postgres),
        client=CRUDclient(postgres),
        signature=CRUDsignature(redis)
        )


handler_comment = comment.Handler(
        crud=crud
        )

handler_auth = auth.Handler(
        crud=crud
        )
