
# n = 5
# a = n-1


# for i in range(5, 0, -1):
#     for j in range(5-i):
#         print(end=" ")
#     # a = a-1
#     for k in range(2*i-1):
#         print("*", end=" ")
#     print()

r = 5
a = 2*r-2
for i in range(r, -1, -1):
    for j in range(a, 0, -1):
        print("", end=" ")
    a = a+1
    for k in range(0, i+1):
        print("*", end=" ")
    print()
