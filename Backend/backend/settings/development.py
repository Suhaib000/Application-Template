from .base import *
from pathlib import Path
from dotenv import load_dotenv
import os



load_dotenv('.env')



dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), './.env.development')

load_dotenv(dotenv_path)

# Use environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

# print("*"*80)
# print("Development SECRET_KEY ==> ",SECRET_KEY)
# print("*"*80)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200'
]