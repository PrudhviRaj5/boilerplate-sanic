import os
from dotenv import load_dotenv

# loading .env file variables
root_lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
load_dotenv(dotenv_path=root_lib_path+'/.env')

# get all .env variables
# pg db conn variables
PY_ENV = os.getenv('PY_ENV')
DEV_PG_DB_URL = os.getenv('DEV_PG_DB_URL')
PROD_PG_DB_URL = os.getenv('PROD_PG_DB_URL')

CONFIG = {
    'PY_ENV': PY_ENV,
    # Postgres DEV & PROD connection urls
    'DEV_PG_DB_URL': DEV_PG_DB_URL,
    'PROD_PG_DB_URL': PROD_PG_DB_URL,
    # Postgres actual connection url
    'PG_DB_URL': PROD_PG_DB_URL if PY_ENV == 'production' else DEV_PG_DB_URL,
}
