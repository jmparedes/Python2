
class Cart:
    from item_manager import show_items
    from ownable import set_owner
    def __init__(self, owner):
        self.set_owner(owner)
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
            print("You don't have money enough to buy these things.")
            pass
        if(len(self.items_list()) <= 0):
            print("The cart is empty.")
            pass
        print("The purchase has been complete.")
        return self.owner.wallet.withdraw(self.total_amount())
        
        # Remove the pass when coding the check_out method.
        # requirements
        # - The purchase price of all items in the cart (Cart#items) in the cart owner's wallet.
        # - Elementos del carrito de compras.
        # - Empty cart (Artículos del carrito).
        # Tips
        # - cart owner wallet ==> self.owner.wallet
        # - Item owner's wallet ==> item.propietario.billetera
        # - Money is transferred ==> Withdraw that amount from (?) wallet and deposit that amount to (?) wallet
        # - item ownership transferred to cart owner ==> rewrite owner (item.owner = ?)
