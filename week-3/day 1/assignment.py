# # Q1)
# num = int(input(f'Enter an integer for num: '))
# exist = False
# for i in range(1, num+1):
#     i**2
#     if i**2 == num:
#         exist = True
# if exist == True:
#     print("it is a perfect square")
# else:
#     print("it is not a perfect square")

# # Q2)
# n = int(input("Enter a number = "))
# total = 0
# while n > 0:
#     total = total + (n % 10)
#     n = n // 10

# print(total)

# # Q3)
# num = int(input(f'Enter an integer for num: '))

# while num > 0:
#     print(num % 10, end="")
#     num = num//10

# # Q4)
# num = int(input(f'Enter an integer for num: '))
# total = 0
# for i in range(1, num+1):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count = count+1
#     if count == 2:
#         total += 1

# print(f"No of primbers betweeen 1 and {num} is {total}")

#  # Q5
# text = [10, 20, 30, 40, 50, 60, 70, 80]
# # print("the maximum value in the list is :", max(text))
# # print("the minimum value in the list is :",min(text))
# max = 0
# min = text[0]
# for i in range(0, len(text)):
#     if text[i] > max:
#         max = text[i]
#     if text[i] < min:
#         min = text[i]
# print(f"the maximum value in the list is {max}")
# print(f"the minimum value in the list is {min}")

# q6)
# text = [10, 20, 30, 40, 50, 60, 70, 80]
# avg = sum(text)/len(text)
# print("the average of all the values in the list is :", avg)
num = [10, 20, 30, 40, 50, 60, 70, 80]
sum = 0
count = 0
for i in range(0, len(num)):
    sum += num[i]
    count += 1
avg = sum/count
print(f"the average of the given list is {avg}")
