from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("memory", 13880, seller)
    Item("motherboard", 28980, seller)
    Item("Power supply unit", 8980, seller)
    Item("computer case", 8727, seller)
    Item("3.5 inch HDD", 10980, seller)
    Item("2.5 inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU cooler", 13400, seller)
    Item("graphic board", 23800, seller)

print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Please enter the amount to charge the wallet")
customer.wallet.deposit(int(input()))

print("🛍️ start shopping")
end_shopping = False
while not end_shopping:
    print("📜 Product List")
    seller.show_items()

    print("️️⛏ Please enter the product number")
    number = int(input())

    print("⛏ Please enter the product quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    print(items)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart contents:")

    print(f"🤑 total amount: {customer.cart.total_amount()}")

    print("😭 finish shopping？(yes/no)")
    if(input() == "yes"):
        end_shopping = True
        for item in items:
            Item(item.name,item.price, customer)

print("💸 Confirm purchase？(yes/no)")
if input() == "yes":
    seller.wallet.deposit(customer.cart.check_out())

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈result┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name} property of:")
customer.show_items()
print(f"😱👛 {customer.name} wallet balance of: {customer.wallet.balance}")

print(f"📦 {seller.name} stock status of:")
seller.show_items()
print(f"😻👛 {seller.name}wallet balance of: {seller.wallet.balance}")

print("🛒 Cart contents")
customer.cart.show_items()
print(f"🌚 total amount: {customer.cart.total_amount()}")

print("🎉 end")

