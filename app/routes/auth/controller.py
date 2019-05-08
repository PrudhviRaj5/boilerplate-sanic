import uuid
from sqlalchemy.sql import (
    select as sql_select,
    update as sql_update,
    delete as sql_delete,
    join as sql_join,
)
from sqlalchemy import func
from sanic.exceptions import ServerError

from app.database.psql.db import scoped_session, Session
from app.database.psql.models import (
    Users,
    Roles,
    Organizations,
    UserSessions,
)
from app.database.memcache.db import mem_client
from app.config.constants import (
    ERROR_MSG,
)

def login(u_name, u_pass):
    # create tokens
    with scoped_session() as session:
        stmt = sql_select([Users]).where(func.lower(Users.email_id)==func.lower(u_name)).limit(1) # for all cols
        users = session.execute(stmt).fetchall()
        if len(users) > 0:
            user = users[0]
            if user.password == u_pass:
                return create_user_session(user.user_id, user.role_id, user.org_id)
            else:
                raise ServerError('Password doesn\'t match', status_code=401)
            pass
        else:
            raise ServerError('No Registered Username', status_code=401)


def create_user(u_name, u_pass):
    session = Session()

    user_check_stmt = sql_select([Users.email_id]).where(
        func.lower(Users.email_id)==func.lower(u_name)).limit(1)
    users = session.execute(user_check_stmt).fetchall()
    if len(users) > 0:
        raise ServerError('User with email "{}" already exists, please try another name'.format(u_name), status_code=422)
    # adding user if doesn't exist
    user = Users(email_id=u_name, password=u_pass,
        is_admin=True, role_id=1, org_id=1)
    session.add(user)
    session.commit()
    session.refresh(user)

    if not user.id:
        raise ServerError('Db insertion failed for {}'.format(u_name), status_code=500)
    return user


def create_role(role_name):
    session = Session()

    role_check_stmt = sql_select([Roles.role_id]).where(
        func.lower(Roles.role_name)==func.lower(role_name)).limit(1)
    roles = session.execute(role_check_stmt).fetchall()
    if len(roles) > 0:
        raise ServerError('Role with name "{}" already exists'.format(role_name), status_code=422)
    # adding role if doesn't exist
    role = Roles(role_name=role_name)
    session.add(role)
    session.commit()
    session.refresh(role)

    if not role.id:
        raise ServerError('Db insertion failed for: {}'.format(role_name), status_code=500)
    return role


def create_organization(org_name, org_domain):
    session = Session()

    org_check_stmt = sql_select([Organizations.org_id]).where(
        func.lower(Organizations.domain)==func.lower(org_domain)).limit(1)
    roles = session.execute(role_check_stmt).fetchall()
    if len(roles) > 0:
        raise ServerError('Organization with domain "{}" already exists'.format(org_domain), status_code=422)
    # adding role if doesn't exist
    org = Organizations(org_name=org_name, org_domain=org_domain)
    session.add(org)
    session.commit()
    session.refresh(org)

    if not org.id:
        raise ServerError('Db insertion failed for: {}'.format(org_name), status_code=500)
    return org


def create_user_session(user_id, role_id, org_id):
    session = Session()

    uid = uuid.uuid4()
    u_s_id = '{}__{}__{}'.format(user_id, role_id, org_id)
    user_session = UserSessions(user_session_id=u_s_id, session_token=uid, user_id=user_id)
    session.add(user_session)
    session.commit()
    session.refresh(user_session)

    if not user_session.expiry_time:
        raise ServerError('Db insertion failed for UserSession Entry', status_code=500)
    return user_session


def verify_token(session_token):
    # verify session token
    session = Session()

    token_check_stmt = sql_select([UserSessions]).where(
        UserSessions.session_token==session_token).limit(1)
    user_sessions = session.execute(token_check_stmt).fetchall()
    if len(user_sessions) == 0:
        raise ServerError('Session token expired', status_code=401)
    else:
        if user_sessions[0].session_token == session_token:
            return True
        else:
            raise ServerError('Session token expired', status_code=401)


# def create_access_token_from_refresh():
#     pass
