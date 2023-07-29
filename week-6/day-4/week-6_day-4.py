# #Q1)
# def sum_natural_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total


# print(sum_natural_numbers(int(input)))

# # Q2)
# def find_largest(lst):
#     return (max(lst))


# print(find_largest([10, 20, 40, 30]))

# # Q3)
# def find_smallest(lst):
#     return (min(lst))


# print(find_smallest([10, 20, 40, 4]))

# # Q4)
# def count_vowels(s):
#     total = 0
#     for i in s:
#         if i in 'aeiou':
#             total += 1
#     return (total)


# x = count_vowels(input("enter a string : "))
# print(f"vowels count in string is : {x}")

# # Q5)
# def is_prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count = count+1
#     if count == 2:
#         return True
#     else:
#         return False


# print(is_prime(int(input("enter a number : "))))

# # Q6)
# def find_common_elements(lst1, lst2):
#     lst3 = []
#     for i in lst1:
#         if i in lst2:
#             lst3.append(i)
#     return (lst3)


# x = find_common_elements([10, 20, 30], [40, 30, 10, 455])
# print(x)

# # Q7)
# def merge_dictionaries(dict1, dict2):
#     dict3 = dict1
#     dict3.update(dict2)
#     return (dict3)


# x = merge_dictionaries({'zaheer': 23, "ali": 123}, {
#                        'akash': 151, "zaheer": 147})
# print(x)
