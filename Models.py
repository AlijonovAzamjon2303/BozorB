class Company:
    def __init__(self, name, yil, founder):
        self.name = name
        self.yil = yil
        self.founder = founder

    def info(self):
        return f"{self.founder}|{self.name} -- {self.yil}yy"

class Product:
    def __init__(self, name, price, amount, company):
        self.name = name
        self.price = price
        self.amount = amount
        self.company = company

    def info(self):
        return f"{self.name} -- {self.price}x{self.amount}"

class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for i in self.products:
            if i.name == product.name:
                i.amount += product.amount
                return
        self.products.append(product)

    def view(self):
        for i in self.products:
            print(i.info())