# # Q1)
# word = input('Enter a string : ').lower()
# count = 0
# for i in word:
#     if i in "abcdefghijklmnopqrstuvwxyz":
#         count += 1
# print(f"the number of alphabets in string are {count}")

# # Q2)
# user_string = input("Enter a sentence = ")
# user_string = "aerOPLAne is a good transport"

# words = user_string.split()

# for i in words:
#     if len(i) == 1:
#         print(i.upper(), end=" ")
#     else:
#         print(i[0].upper() + i[1 : len(i) - 1] + i[-1].upper(), end=" ")


# # Q3)
# a = input('Enter a string : ')
# b = list(a)
# c = []
# result = []
# for i in b:
#     if i not in c:
#         c.append(i)
# for i in c:
#     if b.count(i) % 2 != 0:
#         result.append(i)
# print(result)

# # Q4)
# a = input("enter a string in snake case : ")
# b = a.title()
# c = b.replace("_", "")
# print(f"pascal case of sentence is : {c}")

# Q5)

a = input("Enter a string: ")

vowels = ["a", "e", "i", "o", "u"]
result = []
words = ""

for i in a:
    if i.lower() in vowels:
        if words:
            result.append(words)
            words = ""
    else:
        words = words + i

if words:
    result.append(words)

print("Split string on vowels:", result)
