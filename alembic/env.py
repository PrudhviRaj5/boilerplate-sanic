from __future__ import with_statement

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# adding root folder as search path
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

# add your model's MetaData object here
# for 'autogenerate' support
# target_metadata = None
from b2b_app.database.psql.models import Base
target_metadata = Base.metadata

# loading .env file variables
from dotenv import load_dotenv
load_dotenv(dotenv_path=lib_path+'/.env')


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    alembic_config = config.get_section(
        config.config_ini_section,
        # prefix="sqlalchemy.", # not import from alembic.ini; assigning directly
    )
    url = os.getenv('PROD_PG_DB_URL') if os.getenv('B2B_PY_ENV') == 'production' else os.getenv('DEV_PG_DB_URL')
    alembic_config['sqlalchemy.url'] = url

    engine_conn = engine_from_config(alembic_config)

    with engine_conn.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
