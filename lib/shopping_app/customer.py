from user import User
from cart import Cart
from seller import Seller
class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # When a Customer instance is created it will have a cart owned by it.
