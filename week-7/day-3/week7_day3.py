# #Q1)
# a = open("assgn.txt", "r")
# b = a.readlines()
# c = []
# for i in b:
#     c.append(int(i))
# print(sum(c))

# # Q2)
# a = open("assgn.txt", "r")
# b = a.readlines()
# c = []
# for i in b:
#     d = i.rstrip("\n")
#     c.append((d))
# word = input("enter a word : ").lower()
# if word in c:
#     print("YES")
# else:
#     print("NO")

# # Q3)
# a = open("assgn.txt", "r")
# b = a.readlines()
# c = []
# for i in b:
#     d = i.rstrip("\n")
#     c.append((d))
# word = input("enter a word : ").lower()
# print(f"{word} is repeating {c.count(word)} times")

# # Q4)
# a = open("assgn.txt", "r")
# b = a.readlines()
# c = []
# for i in b:
#     c = i.split()
#     for j in c:
#         print(j[::-1], end=" ")
#     print()

# # Q5)
# a = open("assgn.txt", "r")
# b = a.readlines()
# for i in b:
#     if "a" in i:
#         print(i, end="")
