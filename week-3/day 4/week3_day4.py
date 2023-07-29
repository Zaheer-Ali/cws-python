# # Q1)
a = [12, 324, 45, 23, 556, 332, 656, 223]
start = int(input(f'Enter an number for start index: '))
end = int(input(f'Enter an number for ending index: '))
print(a[start:end+1])

# Q2)
a = [12, 324, 45, 23, 556, 332, 656, 223]
start = int(input(f'Enter an number for start index: '))
end = int(input(f'Enter an number for ending index: '))
result = a[start:end+1]
print(result)

# # Q3)
# a = [12, 324, 45, 23, 556, 332, 656, 223]
# n = int(input("enter the last number of elements:"))
# b = a[len(a)-n:]
# print(b)

# # Q4)
# a = [12, 324, 45, 23, 556, 332, 656, 223]
# n = int(input("enter the last number of elements:"))
# b = a[-1:len(a)-(n+1):-1]
# print(b)

# #Q5)
a = [12, 324, 45, 23, 556, 332, 656, 223]
print("Before interchanging elements : ", a)
b = a.copy()
a[0] = b[-1]
a[-1] = b[0]
print("After interchanging elements : ", a)

# Q6)
a = [12, 324, 45, 23, 556, 332, 656, 223]
print(a)
x = int(len(a)/2)

b = a[0:x]
c = a[x:len(a)]
print("first half of list a is:", b)
print("second half of list a is:", c)
