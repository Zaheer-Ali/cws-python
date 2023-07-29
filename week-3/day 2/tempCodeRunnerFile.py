# Q5)
a = [12, 32, 4, 22, 4, 12, 54, 32, 12, 4, 54, 4, 32, 52, 43, 32]

b = []
for i in a:
    if i not in b:
        b.append(i)

for i in b:
    count = a.count(i)
    if count > 3:
        print(i)