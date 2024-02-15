from fastapi import FastAPI

from database import init_db
from routers import items

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    """Выполняется при запуске приложения.
    Инициализирует БД и запускает задачу обновления БД."""
    await init_db()

app.include_router(items.router)
