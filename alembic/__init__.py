import os
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))

# loading .env file variables
from dotenv import load_dotenv
load_dotenv(dotenv_path=lib_path+'/.env')
