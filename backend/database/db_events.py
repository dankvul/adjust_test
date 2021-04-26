import logging

from database.init import db
from sqlalchemy import create_engine

from config import DATABASE_URL
from database.crud.dataset import DatasetCRUD


__all__ = ["test_db_connection", "close_db_connection"]


async def test_db_connection():
    logging.info("Testing db connection")
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
    db.metadata.create_all(engine, tables=[DatasetCRUD.model])
    await db.database.connect()


async def close_db_connection():
    logging.info("Shutting down db connection")
    await db.database.disconnect()
