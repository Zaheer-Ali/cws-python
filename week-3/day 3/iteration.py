a = [41, 74, 85, 89, 41, 52]

# for i in range(0, len(a)):  #iteration by position
#     print(a)

# for i in a:
#     print(i)

# total = 0
# for i in a:
#     total += i
# print(total)

for i in a:
    if i % 2 == 0:  # iteration by value
        print(i)
