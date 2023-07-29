a = [45, 3, 65, 123, 65, 45, 321, 4, 65]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

# count the number of frequency of each number

for i in b:
    count = a.count(i)
    print(f"{i} occurs {count} times")
