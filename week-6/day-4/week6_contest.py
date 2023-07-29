# # Q1)
# def list_average(lst):
#     avg = sum(lst)/len(lst)
#     return avg


# numbers = [10, 20, 30, 40, 50, 60]
# average = list_average(numbers)
# print(average)

# # Q2)
# def dictionary_value_sum(d):
#     total = 0
#     for v in d.values():
#         total += v
#     return total


# dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# sum = dictionary_value_sum(dict)
# print(sum)


# # Q3)
# def filter_even_numbers(lst):
#     new_list = []
#     for i in lst:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = filter_even_numbers(a)
# print(even_list)

# # Q4)
# def union_of_sets(set_a, set_b):
#     return set_a.union(set_b)


# new_set = union_of_sets({1, 2, 3}, {3, 4, 5})
# print(new_set)

# # Q5)
# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False


# word = is_palindrome("racecar")
# print(word)

# Q6)
def get_factors(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    return factors


fact = get_factors(20)
print(fact)
