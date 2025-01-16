from Models import Company, Product, Basket


menu = ("1.Add\n"
        "2.View\n"
        "3.Remove\n"
        "4.Total\n"
        "5.Exit\n")

basket = Basket()
while True:
    print(menu)
    choice = input(">> ")
    if choice == "1":
        name = input("name>")
        price = int(input("price>"))
        amount = int(input("amount>"))
        company = Company("Company", 2000, "Company")
        product = Product(name, price, amount, company)
        basket.add_product(product)
    elif choice == "2":
        basket.view()
    elif choice == "3":
        name = input("O'chiriladigan name>")
        basket.remove(name)
    elif choice == "4":
        print(basket.total())
