import datetime
from typing import Optional, List, Literal

import pydantic.schema
from sqlalchemy import Table, Integer, Date, String, Column, Float

from pydantic import BaseModel, Field, validator

from .base import BaseCRUD
from database.init import db


__all__ = ["DatasetCRUD", "DatasetPydanticField", "DatasetSummableFields"]


dataset = Table(
    "dataset",
    db.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("date", Date),
    Column("channel", String),
    Column("country", String),
    Column("os", String),
    Column("impressions", Integer),
    Column("clicks", Integer),
    Column("installs", Integer),
    Column("spend", Float),
    Column("revenue", Float),
)


class DatasetSummableFields:
    IMPRESSIONS = "dataset.impressions"
    CLICKS = "dataset.clicks"
    INSTALLS = "dataset.installs"
    SPEND = "dataset.spend"
    REVENUE = "dataset.revenue"

    ALL = (IMPRESSIONS, CLICKS, INSTALLS, SPEND, REVENUE)


class DatasetPydanticModel(BaseModel):
    date: datetime.date = Field(default=None)
    channel: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    os: Optional[str] = Field(default=None)
    cpi: Optional[float] = Field(default=None)
    impressions: Optional[int] = Field(default=None)
    clicks: Optional[int] = Field(default=None)
    installs: Optional[int] = Field(default=None)
    spend: Optional[float] = Field(default=None)
    revenue: Optional[float] = Field(default=None)


class DatasetCRUD(BaseCRUD):
    pydantic_model = DatasetPydanticModel
    model = dataset

    @classmethod
    def columns(cls) -> List[str]:
        columns: List[str] = DatasetCRUD.model.columns # noqa
        result = []
        for column in columns:
            if str(column) != "dataset.id":
                result.append(str(column).replace("dataset.", ""))
        return result


class DatasetPydanticField(BaseModel):
    field: str = Field(...)

    @validator("field")
    def is_in_dataset(cls, v):
        if v not in DatasetCRUD.columns():
            raise ValueError("Wrong column name")
        return f"dataset.{v}"
