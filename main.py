from store import Store
from product import Product

mart = Store('My Shop')
cheetos = Product("Flamin' Hot Cheetos", 2.99, 'Snacks')
lays = Product("Lay's Potato Chips", 2.99, 'Snacks')
milk = Product("Milk", 1.99, 'Milk')

mart.add_product(cheetos).add_product(lays).add_product(milk)

mart.sell_product(0)

mart.inflation(100)

mart.products[0].print_info()

mart.set_clearance('Snacks', 50)

mart.products[0].print_info()
mart.products[1].print_info()