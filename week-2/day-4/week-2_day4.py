# #Q1)
# #a)
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# b)
# for i in range(6, 1, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()

# # c)
# num = 1
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num += 1
#     print()

# d)
# num = 1
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num += 2
#     print()

# e)
num = 1
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:
            print("2", end=" ")
        else:
            print("1", end=" ")
    print()

# # f)
# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(" ", end=" ")
#     for k in range(1, i+1):
#         print('*', end=" ")
#     print()

# g)
for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(i, end=" ")
    print()
