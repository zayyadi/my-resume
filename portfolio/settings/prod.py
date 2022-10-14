from .base import *

SECRET_KEY = os.environ.get("PR_SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = [
    "135.181.88.125",
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
