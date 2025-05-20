from pydantic import BaseModel

class Product_1(BaseModel):
    name: str
    price: float
    order: bool
    quantity: int
    description: str  # fixed typo here
    category: str
    rating: float
    discount: float

gift = Product_1(
    name='flowers',
    price=100.0,
    order=True,
    quantity=10,
    description='gift for you',
    category='gift',
    rating=4.5,
    discount=10.0
)


print(gift.name)