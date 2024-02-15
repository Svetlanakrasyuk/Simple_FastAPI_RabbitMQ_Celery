from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./sql_app.db'
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
Base = declarative_base()
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db() -> AsyncSession:
    """Возвращает соединение с базой данных."""
    async with AsyncSessionLocal() as async_session:
        yield async_session


async def init_db() -> None:
    """Создание таблиц."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
