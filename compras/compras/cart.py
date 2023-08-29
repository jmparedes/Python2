class Cart:
    
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def set_owner(self, owner):
        self.owner = owner

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
            total_price = self.total_amount()
            if total_price > 0:
                cart_owner = self.items[0].owner  # Propietario del carrito (asumiendo que todos los artículos tienen el mismo propietario)
                for item in self.items:
                    item.owner.wallet.withdraw(item.price)  # Retirar el precio del artículo del monedero del propietario del artículo
                    item.owner = cart_owner  # Transferir la propiedad al propietario del carrito
                self.items = []  # Vaciar el carrito después de la compra
    def show_items(self):
        for item in self.items:
            print(item.label())  
                