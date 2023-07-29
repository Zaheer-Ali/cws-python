a = {"phy": 52, "eng": 32, "mat": 78, "chem": 25, "comp": 80}

b = a.copy()

# for i in a:
#     b[i] = b[i]+5
# print(b)

for v in a:
    if a[v] > 33:
        b[v] = "pass"
    else:
        b[v] = "fail"
print(b)

# orelse

# a = {"physics": 69, "chemistry": 25, "maths": 18, "english": 80, "cs": 89}
# b = {}

# for k, v in a.items():
#     if v > 33:
#         b[k] = "pass"
#     else:
#         b[k] = "fail"

# print(b)
