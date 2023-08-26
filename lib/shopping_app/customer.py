# from user import User
# from cart import Cart
# from ownable import Ownable

# class Customer(User):

#     def __init__(self, name):
#         super().__init__(name)
#         self.cart = Cart(self)  # Customerインスタンスは生成されると、自身をオーナーとするカートを持ちます。
# from user import User
# from cart import Cart

# class Customer(User):

#     def __init__(self, name):
#         super().__init__(name)
#         self.cart = Cart(self)

#     def check_out(self):
#         success = self.cart.check_out()
#         if success:
#             self.cart = Cart(self)
#         return success
from user import User
from cart import Cart

class Customer(User):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)

    def check_out(self):
        success = self.cart.check_out()
        if success:
            self.cart = Cart(self)
        return success
