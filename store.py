class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        for index in range(len(self.products) - 1):
            if self.products[index].uniqueID == id:
                print("Sold:")
                self.products[index].print_info()
                self.products.remove(self.products[index])
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.cat == category:
                product.update_price(percent_discount, False)