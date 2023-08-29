from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa base", 28980, seller)
    Item("Fuente de alimentación", 8980, seller)
    Item("Caja PC", 8727, seller)
    Item("Disco duro de 3,5 pulgadas", 10980, seller)
    Item("SSD de 2,5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Enfriador CPU", 13400, seller)
    Item("Tarjeta gráfica", 23800, seller)

print("🤖 ¿Cómo te llamas?")
customer = Customer(input())

print("🏧 Por favor, introduzca el importe a cargar en el monedero.")
customer.wallet.deposit(int(input()))

print("🛍️ Empezar a comprar")
end_shopping = False

while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("Por favor, introduzca el number de artículo")
    number = int(input())

    print("⛏ Por favor, introduzca la quantity de mercancía")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carro")
    customer.cart.show_items()
    print(f"🤑 Importe total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar de comprar (yes/no)?")
    end_shopping = input() == "yes"

print("💸 ¿Desea confirmar su compra (yes/no)?")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}'s property")
customer.show_items()
print(f"😱👛 Saldo de cartera para {customer.name}: {customer.wallet.balance}")

print(f"📦 Estado de las existencias de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo del monedero de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carro")
customer.cart.show_items()
print(f"🌚 Importe total: {customer.cart.total_amount()}")

print("🎉 terminado")
