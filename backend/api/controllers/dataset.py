from datetime import date
from typing import List
from fastapi import APIRouter, Body, Query
from sqlalchemy.sql import func, select, desc, asc, text, label

from database.crud.dataset import DatasetCRUD, DatasetPydanticField, DatasetSummableFields


__all__ = ["router"]

router = APIRouter()


@router.get("/", response_model=List[DatasetCRUD.pydantic_model], response_model_exclude_unset=True)
async def get_dataset(
        select_by: List[str] = Query(default=[*DatasetCRUD.columns()], alias="select"),
        group_by: List[str] = Query(default=[]),
        date_from: date = Query(default=None, description="date in ISO format"),
        date_to: date = Query(default=None, description="date in ISO format"),
        channel: str = Query(default=None),
        country: str = Query(default=None),
        os: str = Query(default=None),
        sort: str = Query(default=None),
        order: int = Query(default=0, ge=0, le=1, description="0 - asc, 1 - desc"),
        count_cpi: bool = Query(default=None, description="true - show cpi"),
):

    dataset = DatasetCRUD.model

    # Validation section

    if select_by:
        for item in range(len(select_by)):
            select_by[item] = DatasetPydanticField(field=select_by[item]).field
    if group_by:
        for item in range(len(group_by)):
            group_by[item] = DatasetPydanticField(field=group_by[item]).field

    order_field = None

    if sort:
        if sort != 'cpi' and count_cpi is True:
            _ = DatasetPydanticField(field=sort)
        if order:
            order_field = desc(sort) if order else asc(sort)
        else:
            order_field = asc(sort)

    # Proceeding select fields...

    select_fields = []

    for select_field in select_by:
        if select_field in DatasetSummableFields.ALL and group_by:
            select_fields.append(
                func.sum(text(select_field)).label(select_field.replace('dataset.', ''))
            )
        else:
            select_fields.append(text(select_field))

    if count_cpi is True:
        if group_by:
            select_fields.append(
                label(
                    'cpi',
                    func.sum(dataset.c.spend) / func.sum(dataset.c.installs)
                )
            )
        else:
            select_fields.append(
                label('cpi', dataset.c.spend / dataset.c.installs)
            )

    query = select([*select_fields])

    # Proceeding group by fields...

    group_by_fields = [text(group_by_field) for group_by_field in group_by]
    for group_by_field in group_by_fields:
        query = query.group_by(group_by_field)

    # Proceeding where fields...

    if channel:
        query = query.where(dataset.c.channel == channel)
    if country:
        query = query.where(dataset.c.country == country)
    if os:
        query = query.where(dataset.c.os == os)
    if date_from:
        query = query.where(dataset.c.date >= date_from)
    if date_to:
        query = query.where(dataset.c.date < date_to)

    # Proceeding order clause...

    if order_field is not None:
        query = query.order_by(order_field)

    # Fix bug with selects without from field...

    if not len(query.froms):
        query = query.select_from(text("dataset"))

    return await DatasetCRUD.select_all(query)


@router.post("/", response_model=DatasetCRUD.pydantic_model)
async def insert_dataset_row(
        data: DatasetCRUD.pydantic_model = Body(...)
):
    return await DatasetCRUD.insert_one(data)
