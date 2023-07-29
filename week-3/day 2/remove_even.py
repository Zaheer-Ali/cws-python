a = [54, 74, 85, 41, 52, 89, 41]

even = []
odd = []

for i in range(0, len(a)):
    if a[i] % 2 != 0:
        odd.append(a[i])
    else:
        even.append(a[i])
print(odd)
print(even)
