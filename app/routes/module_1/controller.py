from sqlalchemy.sql import (
    select as sql_select,
    update as sql_update,
    delete as sql_delete,
    join as sql_join,
)
from sanic.exceptions import ServerError
from app.database.psql.db import scoped_session, Session
from app.database.psql.models import (
    Module1,
)
from app.database.memcache.db import mem_client

async def get_mem():
    result = mem_client.get('some_key')
    # pd.read_msgpack(mem_client.get("key"))
    return result

async def put_mem(val):
    mem_client.set('some_key', val)
    # mem_client.set("key", df.to_msgpack(compress='zlib'))
    return True

async def get_data(id):
    with scoped_session() as session:
        stmt = sql_select([Module1]).where(Module1.id==id).limit(1) # for all cols
        data_set = session.execute(stmt).fetchall()
        if len(data_set) > 0:
            return data_set[0]
        else:
            ServerError('Data Not Found!', status_code=404)
