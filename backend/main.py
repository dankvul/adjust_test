from fastapi import FastAPI
from starlette.middleware import cors

from api.routes import api_router
from core.utils import exception_handlers
from database.db_events import close_db_connection, test_db_connection
from config import *

docs_config = (
    {
        "docs_url": "/api/docs/",
        "redoc_url": "/api/redocs/",
        "openapi_url": "/api/docs/openapi.json",
    }
    if not IS_PRODUCTION
    else {}
)

app = FastAPI(
    title="Adjust Test Task",
    exception_handlers=exception_handlers,
    on_startup=[test_db_connection],
    on_shutdown=[close_db_connection],
    **docs_config,
)

#########
# Routes
##########

app.include_router(api_router, prefix="/api")

##########
# Middlewares
##########

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

