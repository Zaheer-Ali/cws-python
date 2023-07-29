class Product:

    def __init__(self):
        self.name = input("\nEnter the name of product : ")
        self.category = input("Enter the category the product belongs to : ")
        self.price = int(input("Enter the price of product : "))
        self.quantity = int(input("Enter the quantity of product in stock : "))

    def update_price(self):
        new_price = int(input("\nEnter the new price of the product : "))
        self.price = new_price

    def update_quantity(self):
        new_quantity = int(
            input("\nEnter the new quantity of product in stock : "))
        self.quantity = new_quantity

    def display_product(self):
        print("\n--------INFO-----------")
        print(f"Name of product : {self.name}")
        print(f"Category the product belongs to : {self.category}")
        print(f"price of the product : {self.price}")
        print(f"Quantity of product available : {self.quantity}\n")


items = []

while True:
    print("\n1. Add a product")
    print("2. View all the products")
    print("3. Search for a product")
    print("4. Update price")
    print("5. Update quantity")
    print("6. Remove a product")
    print("7. Exit")

    choice = int(input("\nChoose an option : "))
    if choice == 1:
        obj = Product()
        items.append(obj)
    elif choice == 2:
        if len(items) == 0:
            print("There are no products available\n")
        else:
            for i in items:
                i.display_product()
    elif choice == 3:
        name_prod = input("\nEnter name of the product : ")
        for i in items:
            if i.name == name_prod:
                i.display_product()
                break
        else:
            print("No products found\n")
    elif choice == 4:
        name_prod = input("\nEnter name of the product : ")
        for i in items:
            if i.name == name_prod:
                i.update_price()
                print("Price updated successfully\n")
                break
        else:
            print("No products found")
    elif choice == 5:
        name_prod = input("\nEnter name of the product : ")
        for i in items:
            if i.name == name_prod:
                i.update_quantity()
                print("Quantity updated successfully\n")
                break
        else:
            print("No products found\n")
    elif choice == 6:
        name_prod = input("\nEnter name of the product : ")
        for i in items:
            if i.name == name_prod:
                items.remove(i)
                print("Product removed successfully\n")
                break
        else:
            print("No products found\n")
    elif choice == 7:
        break
    else:
        print("\nChoose correct option.\n")
