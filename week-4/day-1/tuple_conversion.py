a = (12, 434, 5432, 234, 45)
print(a, type(a))
b = list(a)
print(b, type(b))
b.append(100)
a = tuple(b)
print(a, type(a))