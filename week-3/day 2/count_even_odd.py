a = [2, 5, 6, 9, 11]

count_odd = 0
count_even = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_odd)
print(count_even)
