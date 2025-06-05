from pydantic import BaseModel, HttpUrl
from typing import Optional
from models import CategoryEnum, UOMEnum

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[HttpUrl]
    sku: Optional[str]
    unit_of_measure: UOMEnum
    lead_time: Optional[int]

class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    product_id: int
    created_date: Optional[str]
    updated_date: Optional[str]

    class Config:
        orm_mode = True
