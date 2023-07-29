a = {}
names = input("enter name:")
a["name"] = names

ages = input("enter age:")
a["age"] = ages
genders = input("enter gender:")
a["gender"] = genders

for i in range(0, 5):
    sub = input("Enter subject name:")
    marks = int(input("Enter marks:"))
    a[sub] = marks
print(a)
