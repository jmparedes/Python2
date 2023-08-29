from ownable import set_owner
class Cart:
    from item_manager import show_items

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
    def set_owner(self, owner):
        self.owner = owner
    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            raise ValueError("Saldo insuficiente en la billetera del propietario para el pago.")

        for item in self.items:
            # Transferir el precio del artículo desde la billetera del propietario del carrito a la billetera del propietario del artículo.
            self.owner.wallet.balance -= item.price
            item.owner.wallet.balance += item.price

            # Transferir la propiedad del artículo al propietario del carrito.
            item.owner = self.owner

        # Vaciar el carrito al borrar la lista de artículos.
        self.items = []
            

        # Al codificar el método check_out, se debe eliminar PASS.
        # Requisito.
        # - el precio de compra de todos los artículos del contenido del carrito (Cart#items) se transfiere del monedero del propietario del carrito al monedero del propietario del artículo.
        # - Los derechos de propiedad de todos los artículos del contenido del carrito (Cart#items) se transferirán al propietario del carrito.
        # - El contenido del carrito (Cart#items) debe estar vacío.
        # Consejo.
        # - Cartera del propietario del carrito ==> self.owner.wallet
        # - Cartera del propietario del artículo ==> item.owner.wallet
        # - Que el dinero sea transferido ==> (?) retirando esa cantidad del monedero del (?).), lo que significa depositar esa cantidad en el monedero del
        # - Los derechos de propietario del artículo se transfieren al propietario del carrito ==> Reescritura de propietario (item.owner = ?)
