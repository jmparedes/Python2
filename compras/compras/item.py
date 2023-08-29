from ownable import set_owner

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        set_owner(self, owner)  # Llamada correcta a la función set_owner
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    
    def item_all():
        return Item.instances
