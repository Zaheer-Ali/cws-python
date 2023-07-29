num1 = int(input(f'Enter an integer for num1: '))
num2 = int(input(f'Enter an integer for num2: '))
num3 = int(input(f'Enter an integer for num3: '))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is the largest number")
elif num3 > num2 and num3 > num1:
    print(f"{num3} is the largest number")
else:
    print("Enter valid input")