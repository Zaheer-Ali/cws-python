# def xyz(a):   #in list the changes are applicable outside function also
#     a.append(100)

# x=[10,20,30]
# print(f"list before calling function : {x}")
# xyz(x)
# print(f"list after calling function : {x}")


# def xyz(a):  # in dictionary the changes are applicable outside function also
#     a["afa"] = 129


# x = {"zaheer": 123, "ali": 472}
# print(f"list before calling function : {x}")
# xyz(x)
# print(f"list after calling function : {x}")

def xyz(a):  # in string and integer the changes are not applicable outside function also
    a = a+"1234"
    print(a)


x = "zaheer"
print(f"list before calling function : {x}")
xyz(x)
print(f"list after calling function : {x}")
