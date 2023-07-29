a = {"phy": 52, "eng": 33, "mat": 78, "chem": 65, "comp": 80}

r = a.values()
total = 0
for i in r:
    if i % 2 == 0:
        total = total+i
print(total)
