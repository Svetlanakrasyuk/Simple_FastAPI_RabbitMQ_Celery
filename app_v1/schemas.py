from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    value: int


class ItemOut(ItemBase):
    id: str


class Message:
    message: str
