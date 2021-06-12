from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum


class TrashType(str, Enum):
    organic = "organic"
    inorganic = "inorganic"

class ProductBase(BaseModel):
    key: str
    name: str
    type: TrashType
    image: str