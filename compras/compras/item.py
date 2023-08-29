from ownable import set_owner

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Item, la instancia de Item (self) se almacena en una variable de clase llamada insntances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}
    def set_owner(self, owner):
        self.owner = owner
    @staticmethod
    def item_all():
        # Devuelve instancias ==> Esto significa que Item.item_all() devuelve todas las instancias de Item creadas hasta el momento.
        return Item.instances
