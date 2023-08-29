from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa base", 28980, seller)
    Item("Unidad de fuente de alimentacion", 8980, seller)
    Item("Caja de PC", 8727, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("Tablero grafico", 23800, seller)

print("🤖 Nombre: ")
customer = Customer(input())

print("🏧 Monto a cargar: ")
customer.wallet.deposit(int(input()))

print("🛍️ Lista de productos")
end_shopping = False
while not end_shopping:
    print("📜 商品リスト")
    seller.show_items()

    print("️️⛏ Ingrese el numero de producto: ")
    number = int(input())

    print("⛏ Ingrese la cantidad del articulo: ")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito: ")
    customer.cart.show_items()
    print(f"🤑 Total: {customer.cart.total_amount()}")

    print("😭 Quieres terminar la compra? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Confirmar compra(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}Propiedad de ")
customer.show_items()
print(f"😱👛 {customer.name}Saldo del cliente: {customer.wallet.balance}")

print(f"📦 {seller.name}Estado de existencias de ")
seller.show_items()
print(f"😻👛 {seller.name}Saldo de billetera para: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Total: {customer.cart.total_amount()}")

print("🎉 FIN")
