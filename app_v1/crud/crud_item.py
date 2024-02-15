from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

import schemas
from models import Item


async def get_items(db: Session) -> list[type[schemas.ItemOut]]:
    """Получает все items."""
    items = (await db.execute(select(Item))).scalars().fetchall()
    return items


async def get_item(db: Session, item_id: str) -> type[schemas.ItemOut]:
    """
    Получает конкретный item по id из БД."""
    item = (await db.execute(select(Item).where(Item.id == item_id))).scalar()
    return item


async def create_item(db: Session, item: schemas.ItemBase) -> schemas.ItemOut:
    """Создает item"""
    db_item = Item(name=item.name, value=item.value)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def update_item(db: Session, item: schemas.ItemBase, item_id: str) -> type[schemas.ItemOut]:
    """Изменяет item"""
    db_item = await get_item(db, item_id=item_id)
    db_item.name = item.name
    db_item.value = item.value
    await db.merge(db_item)
    await db.commit()
    await db.refresh(db_item)
    db_item = await get_item(db=db, item_id=item_id)
    return db_item


async def delete_item(db: Session, item_id: str) -> dict[str, object]:
    """Удаляет меню и вызывает функцию инвалидации кэша"""
    my_db = (await db.execute(select(Item).where(Item.id == item_id))).scalar()
    await db.delete(my_db)
    await db.commit()
    result = {'status': True, 'message': 'The item has been deleted'}
    return result
#
#
# async def get_full_menus(db: Session): # -> type[schemas.Menu]:
#     """Получает все меню из БД или из кэша, с подменю и блюдами."""
#     # from_cache = await redis_cache_get(menu_id)
#     # if from_cache:
#     #     return from_cache
#     full_menu = ((await db.execute(select(Menu)
#                              .options(selectinload(Menu.r_submenus)
#                                       .options(selectinload(Submenu.r_dishes)))))
#             .scalars().fetchall())
#     # await redis_cache_menu_set(menu, menu_id)
#     return full_menu
