# Q4)
try:
    num = int(input(f'Enter an integer for num: '))
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count+1
    if count == 2:
        print("it is a prime")
    else:
        raise Exception("the number is not prime")
except Exception as e:
    print(e)
except:
    print("some error occured")
