# #Q1
# a = [10, 20, 30, 40]

# if len(a) == 0:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# # Q2)
# a = []
# for i in range(0, 10):
#     num = int(input(f'Enter an integer for index {i}: '))
#     a.append(num)
# print(a)

# b = []
# for _ in range(0, len(a)):
#     if a[_] % 2 != 0:
#         b.append(a[_])
# print(f"List after removing all even numbers : {b}")

# # Q3)
# a = [23, 345, 654, 43, 321, 34, 1, 45]
# a.sort()
# print(f"The second smaller number in the list is {a[1]}")

# # Q4)
# a = [23, 345, 654, 43, 321, 34, 1, 45]
# a.sort()
# print(f"The second largest number in the list is {a[-2]}")

# Q5)
a = [12, 32, 4, 22, 4, 12, 54, 32, 12, 4, 54, 4, 32, 52, 43, 32]

b = []
for i in a:
    if i not in b:
        b.append(i)

for i in b:
    count = a.count(i)
    if count > 3:
        print(i)


# # Q6)
# a = []
# for i in range(0, 10):
#     num = int(input(f'Enter an integer for index {i}: '))
#     a.append(num)
# print(a)

# b = []
# for i in range(len(a)-1, -1, -1):
#     b.append(a[i])
# print(b)

# Q7)
# text = [10, 20, 30, 40, 50, 60, 70, 80]
# avg = sum(text)/len(text)
# print("the average of all the values in the list is :", avg)

# Q8)
# a = [10, 20, 30]
# b = [40, 50, 60, 70]

# c = a+b
# c.sort(reverse=True)
# print(c)

# # Q9)
# a = [10, 20, 30, 40, 50, 60, 70]

# add = a[1]+a[-2]
# print(f"sum of second element from start and second element from end is {add} ")
