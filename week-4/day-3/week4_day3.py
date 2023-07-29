# # Q1)
# n = int(input("enter a value :"))
# a = {}
# for i in range(1, n+1):
#     a[i] = i*i
# print(a)

# # Q2)
# a = {"name": "zaheer", "age": 22, "gender": "male"}
# if len(a.items()) > 0:
#     print("The list is not empty")
# else:
#     print("the list is empty")

# # Q3)
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {}
d3.update(d2)
d3.update(d1)
for i in d1:
    if i in d2.keys():
        d3[i] = d1[i]+d2[i]

print(d3)

# # Q4)
# a = {"name": "zaheer", "age": 22, "gender": "male"}
# print(f"the size of the dictionary is {len(a.items())}")

# Q5)
a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
b = {}
values = []
for k, v in a.items():
    if v not in values:
        values.append(v)
        b[k] = v
print(b)
