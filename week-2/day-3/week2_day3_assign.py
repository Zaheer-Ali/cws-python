# start = int(input(f'Enter an integer for start: '))
# end = int(input(f'Enter an integer for end: '))

# for i in range(start, end+1):
#     print(i)

# # Q2)
# start = int(input(f'Enter an integer for start: '))
# end = int(input(f'Enter an integer for end: '))

# for i in range(start, end+1):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)

# # Q3)
# start = int(input(f'Enter an integer for start: '))
# end = int(input(f'Enter an integer for end: '))
# sum = 0
# for i in range(start, end+1):
#     if i % 4 == 0:
#         sum = sum+i
# print(f"Sum of numbers divisible by 4 in range {start} to {end} is {sum}")

# # Q5)
# table_number = int(input("enter a number to make multiplication table:"))

# for i in range(1, 11):
#     print(f"{table_number}*{i}=", table_number*i)

# # Q4)
# total = 1
# for i in range(1, 11):
#     total = total*i

# print(f"product of numbers from 1-10 is {total}")

# # Q6)
# count = 0
# for i in range(20, 71):
#     if i % 4 == 0:
#         count += 1
# print(f"count of numbers divisible by 4 between 20 and 70 are {count}")

#Q7)
num = int(input(f'Enter an integer for num: '))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count+1
if count == 2:
    print("it is a prime")
else:
    print("it is a composite")