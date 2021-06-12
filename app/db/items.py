from models.items import ItemBase

class Item(ItemBase):
    class Config:
        orm_mode = True