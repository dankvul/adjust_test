from os import getenv

DATABASE_URL = getenv("DATABASE_URL") or "sqlite:///./test.db"
