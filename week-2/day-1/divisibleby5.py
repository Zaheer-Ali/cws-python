"""
print all the numbers divisible by 5 from 1-100
"""
start = int(input(f'Enter an integer for start: '))
end = int(input(f'Enter an integer for end: '))

i = start
while i <= end:
    if i % 5 == 0:
        print(i)
    i = i+1
