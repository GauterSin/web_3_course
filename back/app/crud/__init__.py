from dataclasses import dataclass
from app.crud.site.comment import CRUDcomment
from app.crud.site.client import CRUDclient 
from app.crud.site.signature import CRUDsignature 


@dataclass(frozen=True)
class CrudCollector:
    comment: CRUDcomment
    client: CRUDclient
    signature: CRUDsignature
