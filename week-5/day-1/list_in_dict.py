a = {"sagar": [67, 74, 35, 12, 94],
     "sanjay": [78, 32, 2, 34, 33],
     "akul": [76, 88, 31, 4, 56]}
# print(a.values())
# print student name along with their total marks

# for k, v in a.items():
#     print(f"{k} has score {sum(v)}")

"""
output - 
sagar
44
12
32
74
67
"""
# for k, v in a.items():
#     print(k)
#     for i in range(len(v)-1, -1, -1):
#         print(v[i])

"""
sanjay -> max mark
"""
# with max
# for k, v in a.items():
#     print(f"{k} -> {max(v)}")

# without max
# for k, v in a.items():
#     max = 0
#     for i in v:
#         if i > max:
#             max = i
#     print(f"{k} -> {max}")

"""
print only max mark of all
"""
# max = 0
# for k, v in a.items():
#     for i in v:
#         if i > max:
#             max = i
# print(max)

# orelse

# result = []
# for k, v in a.items():
#     max_marks = 0
#     for i in v:
#         if i > max_marks:
#             max_marks = i
#     result.append(max_marks)
# print(max(result))

# orelse

# result = []
# for k, v in a.items():
#     result.extend(v)
# print(max(result))

"""
88 (maxmarks)-> akul(name)
 """
# result = []
# for k, v in a.items():
#     result.extend(v)
# for k, v in a.items():
#     if max(result) in v:
#         print(f"{k} -> {max(result)}")
