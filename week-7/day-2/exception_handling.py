try:
    a = int(input("enter a num : "))
    b = int(input("enter a num : "))
    print(a+b)
except:
    print("shome error occured")
else:  # the code will go into else when there is no error in try
    print("this is else statement")
finally:  # finally will execute everytime evn if there is an error or not
    print("this is a final statement")
