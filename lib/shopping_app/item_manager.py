# Including this module will allow you to manipulate your own Item instances

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Returns all Item instances owned by self (self owned).
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):  # Returns the specified quantity of Item instances owned by itself corresponding to number.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Output the inventory status of Item instances owned by itself in a table format with columns ["number", "product name", "price", "quantity"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["number", "product name", "price", "quantity"], tablefmt="grid"))    
    # output results in tabular format using tabulate module

def _stock(self):   # Returns the inventory status of Item instances owned by itself.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Classify by Item instances that return the same value in Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # Items contains categorized Item instances.
    return stock

