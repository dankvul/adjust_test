import sqlalchemy

from database.init import db
from sqlalchemy.sql.selectable import Select
from pydantic import BaseModel


class BaseCRUD:
    model: sqlalchemy.Table = NotImplemented
    pydantic_model: BaseModel = NotImplemented

    @staticmethod
    async def get_pydantic_model(_object: dict) -> pydantic_model:
        pass

    @classmethod
    async def select_all(cls, select_query: Select) -> list:
        return await db.database.fetch_all(select_query)

    @classmethod
    async def select_one(cls, select_query: Select) -> dict:
        return await db.database.fetch_one(select_query)

    @classmethod
    async def insert_one(cls, model_to_insert: pydantic_model) -> dict:
        query = cls.model.insert().values(**model_to_insert.dict(exclude_none=True))
        last_record_id = await db.database.execute(query)
        return {**model_to_insert.dict(exclude_none=True), "id": last_record_id}

    @classmethod
    async def delete_all(cls):
        return await db.database.execute(cls.model.delete())
