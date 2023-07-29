# # q1)
# # a)
# for i in range(1, 201):
#     if i % 10 == 0:
#         print(i, end=" ")

# b)
# num = 1
# for i in range(0, 10):
#     print(num, end=" ")
#     num = num*10


# # c)
# num = 0
# for i in range(1, 11):
#     num = num*10+1
#     print(num, end=" ")

# # d)
num = 1
print(num, end=" ")
for i in range(1, 7):
    num = num+2
    print(num, end=" ")
    num = num+3
    print(num, end=" ")

# # e)
# num = 1

# for i in range(1, 13):
#     print(num, end=" ")
#     num = num*2

# # Q2)
# n = int(input(f'Enter an integer for n: '))
# sum = 1
# for i in range(1, n+1):
#     sum = sum+(1/(2**n))
# print(sum)

# # q3)
# sum = 0
# for i in range(1, 11):
#     sum = sum+(i**2)
# print(f"sum of first 10 natural numbers is {sum}")

# # q4)
# for i in range(1, 101):
#     # count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count = count+1
#     if count == 2:
#         print(i, end=" ")
