# # Q1)
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for k, v in a.items():
#     b[v] = k
# print(b, type(b))

# # Q2)
# a = {'a': 10, 'b': 2, 'c': 23, 'd': 61, 'e': 12}
# b = {}
# r = list(a.values())
# r.sort()
# print(r)
# for i in r:
#     for k, v in a.items():
#         if i == v:
#             b[k] = i
# print(b)

# # Q3)
# a = {'a': 10, 'b': 2, 'c': 23, 'd': 61, 'e': 12}
# num = int(input(f'Enter a number: '))
# b = {}
# for k, v in a.items():
#     if v > num:
#         b[k] = v
# print(b)

# # Q4)
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'e': 24}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# result = {}
# for k in dict1.keys():
#     if k not in dict2.keys():
#         result[k] = dict1[k]
# print(result)
