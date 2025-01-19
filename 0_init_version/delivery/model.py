import datetime

from pydantic import BaseModel


class Ticket(BaseModel):
    order_id: int
    status_id: str
    driver_username: str


class Driver(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str
    busy_now: bool
