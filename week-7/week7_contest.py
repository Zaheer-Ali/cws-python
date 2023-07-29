# # Q1)
# a = open("file.txt", "r")
# c = a.readlines()
# print(f"No of lines : {len(c)}")
# d = []
# for i in c:
#     d.append(i.split())
# total = 0
# for k in d:
#     total += len(k)
# print(f"No of words : {total}")
# count = 0
# for j in c:
#     count += len(j)
# print(f"No of characters : {count}")

# # Q2)
# a = open(input("enter file name : "), "r")
# b = a.readlines()
# for i in range(int(input("enter a number to print no of lines : "))):
#     print(b[i])

# # Q3)
# try:
#     a = open(input("enter file name : "), "r")
#     b = a.read()
#     print(b)
# except FileNotFoundError:
#     print("File not found")

# # Q4)
# try:
#     a = open(input("enter file name : "), "r")
#     word = input("Enter a word to search : ")
#     b = a.readlines()
#     exists = False
#     num = 0
#     for i in range(len(b)):
#         if word in b[i]:
#             exists = True
#             num = i+1
#             break
#     if exists:
#         print(f"The word {word} first appears on line {num}")
#     else:
#         print("The word doesnot exists in file")
# except FileNotFoundError:
#     print("File not found")

# Q5)
try:
    a = open(input("enter file name : "), "r")
    num = int(input("enter a positive integer : "))
    b = a.readlines()
    if num > len(b):
        print(
            f"The file has lesser lines than the entered value.It has only {len(b)} lines")
    else:
        print(b[num-1])

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Enter integer value")
