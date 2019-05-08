""" Module represents Module1 """

from sqlalchemy import (
    Column, ForeignKey,
    String, Integer,
    DateTime, Boolean,
    Index,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import (
    JSON as PgJSON,
    JSONB as PgJSONB,
    ARRAY as PgARRAY,
)
from app.database.psql.models import Base
from app.database.psql.utils import utcnow


class Module1(Base):
    __tablename__ = 'module_1'

    # primary attributes
    id = Column(Integer, autoincrement=True, primary_key=True)
    some_data = PgJSON() # app, database

    # common table attributes
    created_time = Column(DateTime(timezone=True), server_default=utcnow(), index=True)
    updated_time = Column(DateTime(timezone=True), server_default=utcnow(), server_onupdate=utcnow())
    is_deleted = Column(Boolean, default=False) # True for soft deletes

    # Methods
    def __repr__(self):
        """ Show module_1 object info. """
        return '<Module1: {}>'.format(self.id)
