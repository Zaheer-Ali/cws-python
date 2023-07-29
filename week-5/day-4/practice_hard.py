# Q1)
# a = input("enter a string : ")
# print(f"number of words in the string : {len(a.split())}")

# # Q2)
# sentence = input("enter a string : ").lower()
# total_count = 0
# for i in sentence:
#     if i in "aeiou":
#         total_count += 1
# print(total_count)

# # Q3)
# a = input("enter a string : ")
# max_length = 0
# long_word = ""
# for i in a.split():
#     if len(i) > max_length:
#         max_length = len(i)
#         long_word = i
# print(f"the longest word is {long_word}")

# # Q4)
# a = input("enter a string : ")
# min_length = len(a.split()[0])
# short_word = a.split()[0]
# for i in a.split():
#     if len(i) < min_length:
#         min_length = len(i)
#         short_word = i
# print(f"the shortest word : {short_word}")

# # Q5)
# a = input("enter a string : ")
# b = list(a)
# temp = b[0]
# b[0] = b[-1]
# b[-1] = temp
# print("".join(i for i in b))

# # Q6)
# a = input("enter a string : ")
# b = a.split()
# print("".join(i for i in b))

# Q7)
a = input("enter a string : ")
b = input("enter another string : ")
c = " ".join(i for i in a.split())
c = " ".join(j for j in b.split())
