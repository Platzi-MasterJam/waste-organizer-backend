from pydantic import BaseModel
from typing import Optional 
from enum import Enum

class User(BaseModel):
    name: str

class UserResult(BaseModel):
    username: str
    date: str
    right_answers: int
    bad_answers: int