# Incluya este módulo para poder manipular instancias de Item de su propiedad.

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Devuelve todas las instancias de Item que le pertenecen (es el propietario).
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Devuelve la instancia de Item de su propiedad correspondiente al número para la cantidad especificada.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Muestra el estado de las existencias de la instancia de artículo que posee en formato de tabla con las columnas ["Número", "Nombre de artículo", "Importe", "Cantidad"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["番号", "商品名", "金額", "数量"], tablefmt="grid"))    # Salida de resultados en formato tabla utilizando el módulo tabulate.

def _stock(self):   # Devuelve el estado de las existencias de la instancia del artículo que le pertenece.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):  # Clasificar por instancias de Item que devuelven el mismo valor en Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # items contiene instancias de Item clasificadas.
    return stock
