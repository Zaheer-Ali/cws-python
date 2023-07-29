# a = [2, 5, 6, 9, 11]

# count = 0
# for i in range(0, len(a)):
#     factors = 0
#     for j in range(1, a[i] + 1):
#         if a[i] % j == 0:
#             factors += 1
#     if factors == 2:
#         count += 1

# print(count)

a = [2, 5, 6, 9, 11]

count = 0
for position in range(0, len(a)):
    factors = 0
    for number in range(1, a[position] + 1):
        if a[position] % number == 0:
            factors += 1
    if factors == 2:
        count += 1

print(count)
