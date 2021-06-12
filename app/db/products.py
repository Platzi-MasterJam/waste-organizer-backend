from models.products import ProductBase

class Product(ProductBase):
    class Config:
        orm_mode = True