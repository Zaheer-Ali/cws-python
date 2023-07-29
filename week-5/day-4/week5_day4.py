# #Q1)
# a = input("enter a string : ")
# if len(a) > 0:
#     print("the string is not empty")
# else:
#     print("the string is empty")

# # Q2)
# a = input("enter a string : ")
# max_length = 0
# for i in a.split():
#     if len(i) > max_length:
#         max_length = len(i)
# print(f"the length of longest word is {max_length}")

# # Q3)
# a = input("enter a string : ")
# max_count = 0
# most_common_char = ""
# for i in a:
#     if a.count(i) > max_count:
#         max_count = a.count(i)
#         most_common_char = i
# print(f"the most common character is : {most_common_char}")

# # Q4)
# a = input("enter a word : ")
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# c = "".join(i for i in b)
# print(f"after removing duplicates : {c}")

# # Q5)
# a = input("enter a word : ").lower()
# max_count = 0
# for i in a:
#     if a.count(i) > max_count:
#         max_count = a.count(i)
# if max_count > 1:
#     print("no, the string is not an isogram")
# else:
#     print("yes, the string is an isogram")

# # Q6)
# a = input("enter a string : ").lower()
# max_count = 0
# max_Word = ""
# for i in a.split():
#     if a.split().count(i) > max_count:
#         max_count = a.split().count(i)
#         max_Word = i
# print(f"most frequent word is : {max_Word}")
