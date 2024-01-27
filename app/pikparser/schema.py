from pydantic import BaseModel
from datetime import date
from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    area: float
    floor: int
    price: int
    bulkName: str
    maxFloor: int
    settlementDate: date


class Data(BaseModel):
    items: List[Item]

class SPik(BaseModel):
    data: Data