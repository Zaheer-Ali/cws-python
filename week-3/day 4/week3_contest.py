# Q1)
# a = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0, len(a)):
#     a[i] = a[i]**2
# print(a)

# # Q2)
# a = [10, 20, 30, 40]
# b = [100, 200, 300, 400]
# for i in range(0, len(a)):
#     print(a[i], b[-(i+1)])

# Q3)
# a = [70, 20, 15, 70, 25, 50, 20]

# for i in a:
#     if i == 70:
#         a.remove(70)
# print(a)

# # Q4)
# a = [10, 20, -7, 25, -5, -10, 12]
# sum = 0
# product = 1
# for i in a:
#     if i > 0:
#         sum += i
#     elif i < 0:
#         product = product*i
# print(f"The sum of all positive numbers is {sum}")
# print(f"The product of all negative numbers is {product}")

# # Q5)
# a = [2, 4, 5, 7, 9, 15, 17]

# for i in range(0, len(a)):
#     factors = 0
#     for j in range(1, a[i]+1):
#         if a[i] % j == 0:
#             factors += 1
#     if factors == 2:
#         print(a[i])

# Q6)
a = [10, 20, 'xyz', 12, 'apple', 'python', 1272, '1234']

str_count = 0
int_count = 0

for i in a:
    if type(i) == int:
        int_count += 1
    elif type(i) == str:
        str_count += 1
print(f"The number of strings present in the list is {str_count}")
print(f"The number of integers present in the list is {int_count}")
