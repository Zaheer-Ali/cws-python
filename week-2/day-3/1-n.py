"""
ask num from user
print 1 to N

"""
num = int(input(f'Enter an integer for num: '))
count = 0
sum = 0
for i in range(1, num+1):
    if i % 8 == 0:
        count = count+1
        sum = sum+i
print(count)
print(sum)
