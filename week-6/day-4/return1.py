"""
write a function which returns add of 2 values

check if sum is odd or even
"""


def addition(a, b):
    return a+b


def check(c):
    if c % 2 == 0:
        print("even")
    else:
        print("odd")


x = addition(10, 20)
check(x)
