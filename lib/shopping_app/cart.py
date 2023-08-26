# from ownable import Ownable

# class Cart(Ownable):

#     def __init__(self, owner):
#         super().__init__(owner)
#         self.items = []

#     def items_list(self):
#         return self.items

#     def add(self, item):
#         self.items.append(item)

#     def total_amount(self):
#         price_list = []
#         for item in self.items:
#             price_list.append(item.price)
#         return sum(price_list)

#     def check_out(self):
#         if self.owner.wallet.balance < self.total_amount():
#             return False

#         for item in self.items:
#             item.owner.wallet.withdraw(item.price)
#             self.owner.wallet.deposit(item.price)
#             item.set_owner(self.owner)

#         self.items = []
#         return True
from ownable import Ownable

class Cart(Ownable):

    def __init__(self, owner):
        super().__init__(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return False

        for item in self.items:
            item.owner.wallet.withdraw(item.price)
            self.owner.wallet.deposit(item.price)
            item.set_owner(self.owner)

        self.items = []
        return True
