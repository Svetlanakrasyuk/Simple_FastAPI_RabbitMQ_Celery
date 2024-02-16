from typing import Type

from celery_main import app_celery
from openpyxl.reader.excel import load_workbook

from updater import post_item


@app_celery.task
def parse_item(row: int = 1): # -> Type[ItemOut]:
    """Собрать данные о блюде из файла."""
    sheet = load_workbook(filename='./admin/Menu.xlsx').active
    item: dict[str, int] = {}
    cells = sheet[f'A{row}':f'C{row}'][0]  # type: ignore
    target_item_id: str = cells[0].value
    item['name'] = cells[1].value
    item['value'] = cells[2].value
    print(item['value'])
    post_item(target_item_id=target_item_id, item=item)
#
# @app_celery.task(name='tasks.task_name', queue='queue_name')
# def task_name(row: int = 1):
#     asyncio.run(async_function(param1, param2))

#
# @app_celery.task
# def add():
#     print('add work +++++++++++++++++++++++++++++++++++++++++')
#     return True

