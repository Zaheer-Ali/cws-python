# a = []
# n = int(input(f'Enter an integer for n: '))

# for i in range(0, n):
#     num = int(input(f'Enter an integer for num: '))
#     a.insert(0, num)
# print(a)
a = [10, 54, 78, 74, 85, 74, 84, 114, 44, 55, 55, 55, 55]
count = 0
for _ in range(0, len(a)):
    if a[_] == 55:
        count += 1
print(count)
