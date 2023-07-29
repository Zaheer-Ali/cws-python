# s1 = input("Enter a letter : ")
# print(ord(s1))

s1 = input("enter a string :")
a = list(s1)
sum = 0
for i in a:
    sum += ord(i)
print(sum)
