import datetime

from pydantic import BaseModel, Date


class Payment(BaseModel):
    order_id: int
    client_username: str
    amount: int
    paid: bool


class Order(BaseModel):
    order_id: int
    client_username: str
    point: str
    cart: dict
    created_at: datetime = datetime.datetime.now()
    updated_at: datetime = datetime.datetime.now()
    status: str
