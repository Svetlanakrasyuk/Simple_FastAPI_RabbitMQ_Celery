import requests


def post_item(target_item_id: str, item: dict[str, int]) -> None:
    """Запостить новое меню в базу."""
    url = f'http://127.0.0.1:8000/items/{target_item_id}'
    data = {
        'name': item['name'],
        'value': item['value'],
    }
    requests.patch(url, json=data)
