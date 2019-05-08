""" Module represents App/Db Connections """

from sqlalchemy import (
    Column, ForeignKey,
    String, Integer,
    DateTime, Boolean,
    Index,
)
from sqlalchemy.orm import relationship
from app.database.psql.models import Base
from app.database.psql.utils import utcnow


class Users(Base):
    __tablename__ = 'users'

    # primary attributes
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    email_id = Column(String(64), nullable=False, index=True)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    # relationships
    role_id = relationship("Roles", uselist=False, back_populates='role_id') # one-to-one;
    org_id = relationship("Organizations", uselist=False, back_populates='org_id') # one-to-one;

    # common table attributes
    created_time = Column(DateTime(timezone=True), server_default=utcnow(), index=True)
    updated_time = Column(DateTime(timezone=True), server_default=utcnow(), server_onupdate=utcnow())
    is_deleted = Column(Boolean, default=False) # True for soft deletes

    # Methods
    def __repr__(self):
        return '<User: {}>'.format(self.id)


class Roles(Base):
    __tablename__ = 'roles'

    # primary attributes
    role_id = Column(Integer, autoincrement=True, primary_key=True)
    role_name = Column(String(16), nullable=False)
    # permissons = PgARRAY()

    # Methods
    def __repr__(self):
        return '<Role: {}>'.format(self.id)


class Organizations(Base):
    __tablename__ = 'organizations'

    # primary attributes
    org_id = Column(Integer, autoincrement=True, primary_key=True)
    org_name = Column(String(64), nullable=False)
    domain = Column(String(64), nullable=False, index=True)

    # Methods
    def __repr__(self):
        return '<Organization: {}>'.format(self.id)


class UserSessions(Base):
    __tablename__ = 'user_sessions'

    # primary attributes
    user_session_id = Column(String(16), primary_key=True)
    session_token = Column(String(256), index=True)
    expiry_time = Column(DateTime(timezone=True),
        server_default=utcnow()+20*24*60*60)
    is_expired = Column(Boolean, default=False)

    # relationships
    user_id = relationship("Users", uselist=False, back_populates='user_id') # one-to-one;

    # Methods
    def __repr__(self):
        return '<UserSession: {}>'.format(self.id)
