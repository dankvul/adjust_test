from os import getenv, path

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
ENV = getenv("ENV", None)


HOST_URL = getenv("HOST_URL")

SECRET = getenv("SECRET", "87de177d-0add-4783-80e1-171dd133a035")
API_HOST = getenv("API_HOST", "0.0.0.0")
API_PORT = getenv("API_PORT", 4000)
DEBUG = getenv("DEBUG", "") == "True"

IS_PRODUCTION = ENV == "production"

ALLOWED_ORIGINS = ["*"]
