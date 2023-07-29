import random
order = {}
while True:
    print("~~~~~~~  WELCOME TO FOOD DELIVERY TRACKING SYSTEM  ~~~~~~~~~~\n")
    print("a. Place an Order")
    print("b. Track Delivery")
    print("c. Update Delivery Status")
    print("d. View Order History")
    print("e. Exit \n")

    choice = input("Choose an option : ").lower()
    if choice == "a":
        print("\n~~~~~~~~~~Place an Order~~~~~~~~~~\n")
        orderid = random.randint(1, 100000)
        name = input("\nEnter your name : ").lower()
        items = []
        while True:
            items.append(input("Enter an item to order : "))
            print("If you want to order anything else,enter yes else no")
            a = input("Enter [yes/no] : ").lower()
            if a == "no":
                break
            elif a != "no" and a != "yes":
                print("~~~~Enter Yes or no Correctly~~~~")
                c = input("Enter yes or no : ").lower()
                if c == "no":
                    break
        address = input("Enter your address : ")
        order = {"Order_id": orderid, "Customer_Name": name,
                 "Order_Items": items, "Delivery_Address": address, "Status": "Preparing"}
        print(order, "\n")
    elif choice == "b":
        print("\n~~~~~~~~~~Track Delivery~~~~~~~~~~\n")
        id = int(input("\nEnter your order id : "))
        print("\n")
        # order["Status"] = "Out for delivery"
        if id == order["Order_id"]:
            for k, v in order.items():
                if k == "Order_Items":
                    r = ", ".join(i for i in v)
                    print(f"Order Items : {r}")
                else:
                    print(f"{k} : {v}")
            print("\n")
        else:
            print("Enter correct order_id\n")
    elif choice == "c":
        print("\n~~~~~~~~~~Update Delivery Status~~~~~~~~~~\n")
        id = int(input("\nEnter your order id : "))
        print("\n")
        if id == order["Order_id"]:
            print(f"Current Status : {order['Status']}\n")
            print("Choose new status : \n1. Preparing\n2. Out for Delivery\n3. Delivered")
            option = int(input("Please Enter your choice in [1,2,3]: "))
            if option == 1:
                order["Status"] = "Preparing"
                print("\nDelivery status updated succesfully!\n")
            elif option == 2:
                order["Status"] = "Out for Delivery"
                print("\nDelivery status updated succesfully!\n")
            elif option == 3:
                order["Status"] = "Delivered"
                print("\nDelivery status updated succesfully!\n")
            else:
                print("Choose option correctly between 1,2 and 3 only")
        else:
            print("Enter correct order_id\n")
    elif choice == "d":
        print("\n~~~~~~~~~~View Order History~~~~~~~~~~\n")
        if len(order) != 0:
            cust_name = input("Enter customer name : ").lower()
            id = int(input("\nEnter your order id : "))
            if id == order["Order_id"] and cust_name == order["Customer_Name"]:
                print("\n")
                for k, v in order.items():
                    print(f"{k} : {v}")
                print("\n")
            elif id != order["Order_id"] and cust_name == order["Customer_Name"]:
                print("\nEnter correct order_id\n")
            elif id == order["Order_id"] and cust_name != order["Customer_Name"]:
                print("\nEnter correct Customer_name\n")
            else:
                print("\n Both customer_name and order_id are wrong.Enter correctly\n")
        else:
            print("Place an order first !! \n")
    elif choice == "e":
        print("\nThank you for using the Food Delivery Tracking System. Goodbye !\n")
        break
    else:
        print("\n~~Choose option correctly~~\n")
