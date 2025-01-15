from Models import Company, Product, Basket


c1 = Company("apple", 1990, "stiv")
pr1 = Product("15 pro", 800, 10, c1)
pr2 = Product("15 pro", 800, 5, c1)

b = Basket()
b.add_product(pr1)
b.add_product(pr2)
b.view()