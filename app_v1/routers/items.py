from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
from crud import crud_item
from database import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get('/',
            response_model=list[schemas.ItemOut],
            summary='Get all the items',
            description='You can look at the items',
            )
async def read_items(db: Session = Depends(get_db)) -> list[type[schemas.ItemOut]]:
    """Вызывает функцию получения всех items"""
    items = await crud_item.get_items(db)
    return items


@router.get('/{target_item_id}',
            response_model=schemas.ItemOut,
            summary='Get one item by id',
            description='You can look at the item'
            )
async def read_item(target_item_id: str, db: Session = Depends(get_db)) -> type[schemas.ItemOut]:
    """
    Вызывает функцию получения определенного item по id.
    При отсутствии item возвращает статус 404.
    """
    db_item = await crud_item.get_item(db, item_id=target_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail='item not found')
    return db_item


@router.post('/',
             response_model=schemas.ItemOut,
             status_code=status.HTTP_201_CREATED,
             summary='Create a item',
             description='Create a item with all the information',
             )
async def create_item(item: schemas.ItemBase, db: Session = Depends(get_db)) -> schemas.ItemOut:
    """Вызывает функцию создания item"""
    return await crud_item.create_item(db=db, item=item)


@router.patch('/{target_item_id}',
              response_model=schemas.ItemOut,
              summary='Get one item for update',
              description='You can update the item with all the information, title, description',
              )
async def update_item(
    target_item_id: str, item: schemas.ItemBase, db: Session = Depends(get_db)
) -> type[schemas.ItemOut]:
    """
    Вызывает функцию изменения определенного item по id.
    При отсутствии item возвращает статус 404.
    """
    db_item = await crud_item.get_item(db, item_id=target_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail='item not found')
    return await crud_item.update_item(db=db, item=item, item_id=target_item_id)


@router.delete(
    '/{target_item_id}',
    summary='Get one item for delete',
    description='You can delete the item',
)
async def delete_item(target_item_id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    """
    Вызывает функцию удаления определенного item по id.
    При отсутствии item возвращает статус 404.
    """
    db_item = await crud_item.get_item(db, item_id=target_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail='item not found')
    return await crud_item.delete_item(db=db, item_id=target_item_id)
#
#
# @router.get('/full/',
#             response_model=list[schemas.MenuReadFull],
#             summary='Get all the full menus',
#             description='You can look at the menus'
#             )
# async def get_full_base_menus(db: Session = Depends(get_db)): # -> list[Menu]:
#     """Получение всех меню c развернутым списком блюд и подменю."""
#     return await crud_menus.get_full_menus(db=db)