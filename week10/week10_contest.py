# # Q1)
# def nonRepeat(word):
#     for i in word:
#         if word.count(i) == 1:
#             return i
#             break


# a = nonRepeat(input("Enter a string :"))
# print(f"The first non-repeating character in string is {a}")

# # Q2)
# def intersectionArrays(a, b):
#     c = []
#     for i in a:
#         if i in b:
#             c.append(i)
#     print(c)


# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7]
# intersectionArrays(a, b)

# #Q3)
# def commonPrefix(list):
#     result = ""
#     minimum = list[0]
#     for i in list:
#         if len(i) < len(minimum):
#             minimum = i
#     for i in range(len(minimum)):
#         count = 0
#         for j in list:
#             if minimum[i] == j[i]:
#                 count += 1
#             else:
#                 break
#     for _ in range(count):
#         result += list[0][_]

#     return result


# lst = ["flower", "flow", "flight"]
# y = commonPrefix(lst)
# print(y)

# # Q4)
# def missingNum(num):
#     minimum = min(num)
#     maximum = max(num)
#     x = []
#     for i in range(minimum, maximum+1):
#         x.append(i)
#     for _ in x:
#         if _ not in num:
#             return _


# numbers = [1,2,4,6,3,7,8]
# a = missingNum(numbers)
# print(f"The missing number is {a}")

# Q5)
def minimumCoins(deno, amt):
    deno.sort()
    count = 0
    for i in range(len(deno)-1, -1, -1):

        if deno[i] <= amt:
            amt = amt-deno[i]
            count += 1
    return count


denomination = [1, 5, 10, 25]
amount = 36
a = minimumCoins(denomination, amount)
print(
    f"The minimum number of coins required to make given amount are {a} coins")
