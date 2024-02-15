from uuid import uuid4

from sqlalchemy import String, Column, Integer

from database import Base


def generate_uuid() -> str:
    return str(uuid4())


class Item(Base):
    __tablename__ = 'item'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    value = Column(Integer)
