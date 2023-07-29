a = {11: 43, 6: 32, 2: 57, 9: 78, 5: 78}
b = {}
r = list(a.keys())
r.sort()

for k in r:
    b[k] = a[k]
print(b)

# orelse

# a={11:43,6:32,2:57,9:78,5:78}
# c={}

# for k in sorted(list(a.keys())):
#   # c.update({k:a[k]})
#   c.update({k:a.get(k)})
#   # c[k]=a[k]

# print(c)
