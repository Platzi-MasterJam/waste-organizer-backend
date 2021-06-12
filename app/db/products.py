from models.products import ProductBase, TrashType

class Product(ProductBase):
    class Config:
        orm_mode = True
