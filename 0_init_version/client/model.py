import datetime

from pydantic import BaseModel


class Client(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str


class ClientAddresses(BaseModel):
    client_username: str
    address: str
    last_using: datetime.date
