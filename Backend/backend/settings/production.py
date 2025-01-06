from .base import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), './.env.production')

load_dotenv(dotenv_path)

# Use environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

print("*"*80)
print("Production SECRET_KEY ==> ",SECRET_KEY)
print("*"*80)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = [
    'your-production'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200'
]
ALLOWED_HOSTS = ['*']