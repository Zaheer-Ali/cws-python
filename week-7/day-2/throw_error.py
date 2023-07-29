try:
    name = input("enter name : ")
    password = input("enter password : ")
    if name == "admin" and password == "admin":
        print("successfully logged in")
    else:
        raise Exception("wrong password")
except Exception as e:
    print(e)
