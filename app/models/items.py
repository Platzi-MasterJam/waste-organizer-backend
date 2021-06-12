from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum


class TrashType(str, Enum):
    organic = "organic"
    inorganic = "inorganic"

class ItemBase(BaseModel):
    name: str
    type: TrashType
    image: HttpUrl