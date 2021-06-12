from pydantic import BaseModel
from typing import Optional, 
from enum import Enum

class User(BaseModel):
    name: str
    email: str
    password: str

class GameResult(BaseModel):
    user: User
    # date: