try:
    a = [54, 32, 21, 32, 43, 0]
    print(a[44])
    print(a[0]/a[-1])
except ZeroDivisionError:
    print("cannot divide by zero")
except IndexError:
    print("wrong index given")
except:
    print("some error occured")
