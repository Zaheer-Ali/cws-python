a = {"phy": 52, "eng": 33, "mat": 78, "chem": 65, "comp": 80}

# l = a.values()
# print(max(l))

max = a["phy"]

for v in a.values():
    if v > max:
        max = v
# print(max)
sub = 0
for i in a:
    if a[i] == max:
        sub = i
print(f"maximum marks is {max} of {sub}")
