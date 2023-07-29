a = [45, 3, 65, 123, 65, 45, 321, 4, 65]
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
