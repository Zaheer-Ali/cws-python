# Q1)
# a = [12, 324, 45, 23, 556, 332, 656, 223]
# if a == a.sort():
#     print("The list is sorted in ascending order")
# else:
#     print("the list is not sorted in ascending order")

# # Q2)
# a = [10, 20, 30, 40, 50]
# b = [15, 25, 35, 45, 55]
# x = a+b
# c = []
# for i in range(0, len(x)):
#     c.append(min(x))
#     x.remove(min(x))
# print(c)

# # Q3)
# a = [1, 1, 1, 64, 23, 64, 22, 22, 22]

# for i in range(0, len(a)-2):
#     if a[i] == a[i+1] == a[i+2]:
#         print(a[i], end=" ")

# # Q4)
# a = [1, 2, 3, 4, 3, 2, 1]
# b = []
# for i in range(len(a)-1, -1, -1):
#     b.append(a[i])

# if a == b:
#     print("It is a palindrome")
# else:
#     print("it is not a palindrome")

# Q5)
a = [1, 3, 3, 6, 7, 1, 6, 6, 3, 7, 6]

element = 0
num = a[0]
for i in a:
    count = a.count(i)
    if count > element:
        element = count
        num = i
print(num)

# Q6)
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]

for i in a:
    if i not in b:
        print(i, end=" ")

# Q7)
a = [10, 12, 20, 34, 76, 47]
b = []
for i in range(0, len(a)):
    b.append(min(a))
    a.remove(min(a))
print(f"The second largest number in the list is {b[-2]}")

# # Q8)
# a = [1, 4, 0, 23, 0, 56, 74, 0]
# for i in range(0, len(a)):
#     if a[i] == 0:
#         a.remove(0)
#         a.append(0)
# print(a)
