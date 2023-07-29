a = [43, 54, 12, 43, 541, 12]
b = ["zaheer", "ali", "And", "Cat", "ball"]

# r = a.count(43)
# print(r)
# print(a.count(43))

# x = a.index(43)
# print(x)
# print(a.index(541))

for i in range(0, len(a)):
    if a[i] == 43:  # loop to print index numbers if number is repeated 2 or more times
        print(i)
