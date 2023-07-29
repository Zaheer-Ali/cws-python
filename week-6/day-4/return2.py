"""
sumList,check

sumlist(a)
"""


def sumList(a):
    return sum(a)


def check(c):
    if c % 2 == 0:
        print("even")
    else:
        print("odd")


x = sumList([10, 20, 30, 40])
check(x)
