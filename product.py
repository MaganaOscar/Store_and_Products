class Product:
    id = 0
    def __init__(self, name, price, cat):
        self.name = name
        self.price = price
        self.cat = cat
        self.uniqueID = Product.id
        Product.id += 1

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * (percent_change / 100)
        else:
            self.price -= self.price * (percent_change / 100)
        return self
    def print_info(self):
        print(f"{self.name}: \nCategory: {self.cat}\nPrice: {self.price}")