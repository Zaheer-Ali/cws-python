# #Q1)
# def maximum(a, b, c):
#     print(max(a, b, c))

# maximum(10, 20, 30)

# # Q2)
# def multiply(a):
#     total = 1
#     for i in a:
#         total *= i
#     print(total)


# multiply([1, 2, 3, 4])

# # Q3)
# def prime(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count = count+1
#     if count == 2:
#         print("it is a prime")
#     else:
#         print("it is not a prime")


# prime(int(input("enter a number")))

# # Q4)
# def reverse_str(a: str):
#     print(a[::-1])


# reverse_str("aeroplane")

# # Q5)
# def palindrome(a):
#     if a == a[::-1]:
#         print("yes it is a palindrome")
#     else:
#         print("no it is not a palindrome")


# palindrome('noon')

# # Q6)
# def squareList():
#     a = []
#     for i in range(1, 31):
#         a.append(i*i)
#     print(a)


# squareList()


# # Q7)
# def multiplicationTable(num):
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num*i}")


# multiplicationTable(int(input("enter a number : ")))

# Q8)
def prodDigits(num):
    total = 1
    while num != 0:
        total *= (num % 10)
        num = num//10
    print(total)


prodDigits(int(input("Enter a number : ")))
