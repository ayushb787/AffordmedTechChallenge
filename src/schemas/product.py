from pydantic import BaseModel


class ProductResponse(BaseModel):
    productName: str
    company: str
    price: float
    rating: float
    discount: int
    availability: str
