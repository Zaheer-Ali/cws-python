a = {"name": "zaheer", "age": 22, "gender": "male"}

# a["name"] = "ali" #updates one at atime
a.update({"name": "ali", "phy": 55})  # updates multiple at a time
print(a)

# del a["name"]
a.pop("name")
print(a)

# ask key from user,if key exists then delete the key

keyname = input("enter key we want to delete :")
# if a.get(keyname) != None:
#     a.pop(keyname)
# else:
#     print("key does not exiists")

# or else

if keyname in a:
    a.pop(keyname)
    print(a)
