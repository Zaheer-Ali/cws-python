"""
ask a num and print factors of that number

"""
num = int(input(f'Enter an integer for num: '))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        # print(count)
        count = count+1
print(count)
