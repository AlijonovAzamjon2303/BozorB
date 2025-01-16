from Models import Company, Product, Basket


c1 = Company("apple", 1990, "stiv")
c2 = Company("Dehqon", 2015, "siz")
pr1 = Product("15 pro", 800, 10, c1)
pr2 = Product("14 pro", 500, 5, c1)
pr3 = Product("olma", 10, 100, c2)

b = Basket()
b.add_product(pr1)
b.add_product(pr2)
b.add_product(pr3)
b.view()
print("\n\n")
b.remove("olma")
b.view()