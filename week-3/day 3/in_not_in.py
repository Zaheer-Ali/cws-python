a = [45, 3, 65, 123, 65, 45, 321, 4, 65]

num = int(input(f'Enter an integer for num: '))

# if a.count(num) >= 1:
#     print("yes")
# else:
#     print("no")


# if num in a:
#     print("yes")
# else:
#     print("no")

if num not in a:
    print("it doesnot exist")
else:
    print("it exist")
