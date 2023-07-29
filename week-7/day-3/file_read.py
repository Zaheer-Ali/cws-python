f = open("abc.txt", "r")  # default is read mode
# a = f.read()
# print(a)

# a = f.readline()
# print(a)

# b = f.readline()
# print(b)

c = f.readlines()
print(c)
f.close()
