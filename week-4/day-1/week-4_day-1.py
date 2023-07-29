# # Q1)
# a = (12, 2, 45, 235, 765, 321, 52)
# print(a[len(a)-4])

# # Q2)
# a = (23, 35, 556, 23, 3, 84, 35, 742, 43)
# b = list(a)
# for i in b:
#     if b.count(i) > 1:
#         print(i, end=" ")
#         b.remove(i)

# # Q3)
# a = (12, 2, 45, 235, 765, 321, 52)
# num = int(input("Enter a number to check : "))
# exist = False
# for i in a:
#     if num == i:
#         exist = True
# if exist == True:
#     print("the element exists")
# else:
#     print("the element does not exists")

# # Q4)
# a = (12, 2, 45, 235, 765, 321, 52)
# num = int(input("Enter a number to remove : "))
# b = list(a)
# for i in b:
#     if num == i:
#         b.remove(i)
# a = tuple(b)
# print(a)

# # Q5)
# a = (12, 2, 45, 235, 765, 321, 52)
# b = list(a)
# b.reverse()
# a = tuple(b)
# print(a)

# # Q6)
# a = {10, 20, 30, 40, 50, 60}
# b = {40, 50, 60, 70, 80, 90}
# print("union a and b =", a.union(b))
# print("intesection a and b =", a.intersection(b))
