n = int(input("Enter a number 1 : "))

a = [i for i in range(1, n+1) if n % i == 0]
print("prime"if len(a) == 2 else "notprime")
