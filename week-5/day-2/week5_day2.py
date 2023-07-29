# #Q1)
# a = input('Enter a string : ')
# string = False
# num = False
# for i in a:
#     if i in "abcdefghijklmnopqrstuvwxyz":
#         string = True
#     if i in "0123456789":
#         num = True
# if string == True and num == True:
#     print("yes")
# else:
#     print("no")

# # Q2)
# a = input('Enter a string : ')
# vowel_count = 0
# consonant_count = 0
# for i in a:
#     if i in 'aeiou':
#         vowel_count += 1
#     elif i in 'bcdfghjklmnpqrstvwxyz':
#         consonant_count += 1
# print(f"number of vowels in string is : {vowel_count}")
# print(f"number of consonants in string is : {consonant_count}")

# # Q3)
# a = input('Enter a string : ')
# b = list(a)
# c = []
# for i in b:
#     if i not in c:
#         c.append(i)
# d = "".join(i for i in c)
# print(f"the string after removing duplicates is {d}")

# # Q4)
# a = input('Enter a string : ')
# b = list(a)
# c = []
# c.append(b[0])
# c.append(b[1])
# c.append(b[-2])
# c.append(b[-1])
# d = "".join(i for i in c)
# print(d)

# Q5)
a = input('Enter a string : ')
b = list(a)
c = []
if len(b) % 2 != 0:
    for i in range(int(len(b)/2)+1, len(b)):
        c.append(b[i])
    d = "".join(i for i in c)
    print(d)
else:
    for i in range(int(len(b)/2), len(b)):
        c.append(b[i])
    d = "".join(i for i in c)
    print(d)
