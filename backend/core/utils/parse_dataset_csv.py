import csv

from database.crud.dataset import DatasetCRUD
from config import BASE_DIR


async def parse_dataset_csv():
    await DatasetCRUD.delete_all()
    file_path = BASE_DIR + "/config/dataset.csv"
    with open(file_path, 'r') as data:
        for line in csv.DictReader(data):
            line_model = DatasetCRUD.pydantic_model(**line)
            await DatasetCRUD.insert_one(line_model)
